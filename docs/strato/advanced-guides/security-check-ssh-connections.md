# Security check you public IP server


**Summarise SSH activity on a virtual machine**

This page is to help understand why you need to be careful what ports you expose when running a virtual machine with a public IP address.

This guide describes how to use a Bash script to summarise SSH activity on a Strato virtual machine. The script can help you identify successful logins, automated login attempts, commonly attempted usernames, and the most active source IP addresses.

!!! warning "Public SSH services attract automated scanning"

    A virtual machine with a public IP address and SSH port 22 open to the Internet will normally receive automated connection attempts. Invalid usernames and connections ending with `[preauth]` do not by themselves mean that the virtual machine has been compromised.

## What the script reports

The script reports:

- successful SSH logins;
- source IP addresses used for successful logins;
- failed password attempts;
- attempts to log in as `root`;
- invalid usernames attempted;
- the most commonly attempted usernames;
- the most active invalid-user scanner IP addresses;
- the most active root-login attempt sources;
- the first and last time each source IP was observed;
- successful-login IP addresses that also generated suspicious entries; and
- a simple assessment of the observed activity.

## Create the script

Connect to the virtual machine with SSH and create a file named `ssh_activity_summary.sh`:

```bash
nano ssh_activity_summary.sh
```

??? info "Copy and paste this text in the nano editor for `ssh_activity_summary.sh`"

    ```bash
    #!/usr/bin/env bash

    set -euo pipefail

    SINCE="${1:-today}"
    TOP_LIMIT="${TOP_LIMIT:-20}"

    TMP=$(mktemp)
    trap 'rm -f "$TMP"' EXIT

    line() {
        printf '%100s\n' '' | tr ' ' '='
    }

    section() {
        echo
        line
        echo "$1"
        line
    }

    extract_ips() {
        grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' || true
    }

    if ! command -v journalctl >/dev/null 2>&1; then
        echo "Error: journalctl is not available on this system." >&2
        exit 1
    fi

    # On Ubuntu, the OpenSSH service is normally named ssh.service.
    # If the current user cannot read all journal entries, run the script with sudo.
    journalctl -u ssh.service --since "$SINCE" --no-pager -o short-iso 2>/dev/null > "$TMP"

    if [[ ! -s "$TMP" ]]; then
        echo "No SSH journal entries were found since: $SINCE"
        echo "Try running the script with sudo or specify a wider time range."
        exit 0
    fi

    SUCCESS_COUNT=$(grep -cE 'Accepted (publickey|password|keyboard-interactive)' "$TMP" || true)
    INVALID_COUNT=$(grep -c 'Invalid user' "$TMP" || true)
    ROOT_COUNT=$(grep -cE '(authenticating user root|Failed password for root|Failed publickey for root)' "$TMP" || true)
    FAILED_PASSWORD_COUNT=$(grep -c 'Failed password' "$TMP" || true)
    FAILED_PUBLICKEY_COUNT=$(grep -c 'Failed publickey' "$TMP" || true)
    UNIQUE_SOURCE_COUNT=$(
        grep 'sshd\[' "$TMP" \
            | extract_ips \
            | sort -u \
            | wc -l \
            | tr -d ' '
    )

    SUCCESSFUL_IPS=$(
        grep -E 'Accepted (publickey|password|keyboard-interactive)' "$TMP" \
            | sed -nE 's/.* from ([0-9.]+) port.*/\1/p' \
            | sort -u
    )

    section "SSH Activity Report"

    echo "Host      : $(hostname)"
    echo "Since     : $SINCE"
    echo "Generated : $(date --iso-8601=seconds)"
    echo "Journal   : ssh.service"

    section "Statistics"

    printf '%-42s %8s\n' "Successful logins" "$SUCCESS_COUNT"
    printf '%-42s %8s\n' "Invalid-user attempts" "$INVALID_COUNT"
    printf '%-42s %8s\n' "Root authentication attempts" "$ROOT_COUNT"
    printf '%-42s %8s\n' "Failed password attempts" "$FAILED_PASSWORD_COUNT"
    printf '%-42s %8s\n' "Failed public-key attempts" "$FAILED_PUBLICKEY_COUNT"
    printf '%-42s %8s\n' "Unique source IP addresses" "$UNIQUE_SOURCE_COUNT"

    section "Successful Logins"

    if ! grep -E 'Accepted (publickey|password|keyboard-interactive)' "$TMP"; then
        echo "None"
    fi

    section "Successful Login Source IPs"

    if [[ -n "$SUCCESSFUL_IPS" ]]; then
        while read -r IP; do
            [[ -n "$IP" ]] || continue
            COUNT=$(
                grep -E 'Accepted (publickey|password|keyboard-interactive)' "$TMP" \
                    | grep -F -c "from $IP " || true
            )
            printf '%8s  %s\n' "$COUNT" "$IP"
        done <<< "$SUCCESSFUL_IPS" | sort -rn
    else
        echo "None"
    fi

    section "Top SSH Source IPs"

    if ! grep 'sshd\[' "$TMP" \
        | extract_ips \
        | sort \
        | uniq -c \
        | sort -rn \
        | head -n "$TOP_LIMIT"; then
        echo "None"
    fi

    section "Most Common Usernames Attempted"

    {
        sed -nE 's/.*Invalid user ([^ ]+) from.*/\1/p' "$TMP"
        sed -nE 's/.*Failed password for (invalid user )?([^ ]+) from.*/\2/p' "$TMP"
        sed -nE 's/.*Failed publickey for (invalid user )?([^ ]+) from.*/\2/p' "$TMP"
    } \
        | sort \
        | uniq -c \
        | sort -rn \
        | head -n "$TOP_LIMIT" \
        | awk '{printf "%8s  %s\n", $1, $2}' \
        || true

    section "Top Invalid-User Scanner Sources"

    if ! grep 'Invalid user' "$TMP" \
        | sed -nE 's/.* from ([0-9.]+) port.*/\1/p' \
        | sort \
        | uniq -c \
        | sort -rn \
        | head -n "$TOP_LIMIT"; then
        echo "None"
    fi

    section "Top Root Login Attempt Sources"

    if ! grep -E '(authenticating user root|Failed password for root|Failed publickey for root)' "$TMP" \
        | extract_ips \
        | sort \
        | uniq -c \
        | sort -rn \
        | head -n "$TOP_LIMIT"; then
        echo "None"
    fi

    section "Source IP Timeline"

    printf '%-20s %8s  %-25s  %-25s\n' \
        "IP" "EVENTS" "FIRST SEEN" "LAST SEEN"

    awk '
    {
        timestamp = $1
        ip = ""

        for (i = 1; i <= NF; i++) {
            if ($i ~ /^[0-9]{1,3}(\.[0-9]{1,3}){3}$/) {
                ip = $i
                break
            }
        }

        if (ip != "") {
            if (!(ip in first)) {
                first[ip] = timestamp
            }
            last[ip] = timestamp
            count[ip]++
        }
    }
    END {
        for (ip in count) {
            printf "%-20s %8d  %-25s  %-25s\n", \
                ip, count[ip], first[ip], last[ip]
        }
    }
    ' "$TMP" | sort -k2,2nr | head -n "$TOP_LIMIT"

    section "Successful IPs Also Showing Suspicious Activity"

    MIXED_BEHAVIOUR=0

    if [[ -n "$SUCCESSFUL_IPS" ]]; then
        while read -r IP; do
            [[ -n "$IP" ]] || continue

            SUSPICIOUS_COUNT=$(
                grep -F "$IP" "$TMP" \
                    | grep -E -c '(Invalid user|Failed password|Failed publickey|authenticating user root)' \
                    || true
            )

            if (( SUSPICIOUS_COUNT > 0 )); then
                MIXED_BEHAVIOUR=1
                printf '%s  %s suspicious entries\n' "$IP" "$SUSPICIOUS_COUNT"
            fi
        done <<< "$SUCCESSFUL_IPS"
    fi

    if (( MIXED_BEHAVIOUR == 0 )); then
        echo "None detected"
    fi

    section "Recent Successful Logins"

    grep -E 'Accepted (publickey|password|keyboard-interactive)' "$TMP" \
        | tail -n "$TOP_LIMIT" \
        || true

    section "Recent Root Login Attempts"

    grep -E '(authenticating user root|Failed password for root|Failed publickey for root)' "$TMP" \
        | tail -n "$TOP_LIMIT" \
        || true

    section "Recent Invalid Users"

    grep 'Invalid user' "$TMP" \
        | tail -n "$TOP_LIMIT" \
        || true

    section "Assessment"

    if (( SUCCESS_COUNT == 0 )); then
        echo "[INFO] No successful SSH logins were observed in the selected period."
    else
        echo "[INFO] Successful SSH logins were observed. Verify that the users, source IPs and authentication methods are expected."
    fi

    if (( INVALID_COUNT > 0 )); then
        echo "[INFO] Invalid-user attempts were observed. This is common when SSH is publicly accessible."
    fi

    if (( INVALID_COUNT > 50 )); then
        echo "[INFO] A high volume of automated username scanning was observed."
    fi

    if (( ROOT_COUNT > 0 )); then
        echo "[INFO] Root-login probing was observed."
    fi

    if (( FAILED_PASSWORD_COUNT > 0 )); then
        echo "[WARNING] Failed password attempts were observed."
    fi

    if (( FAILED_PUBLICKEY_COUNT > 0 )); then
        echo "[INFO] Failed public-key attempts were observed."
    fi

    if (( MIXED_BEHAVIOUR > 0 )); then
        echo "[WARNING] At least one successful-login IP also generated suspicious SSH entries. Review those events manually."
    fi

    echo
    echo "Report complete."
    ```

Save the file in the Nano editor

```bash
CTRL + o

Enter
```

Exit the Nano editor

```bash
CTRL + x
```

## Prepare the script to run

Save the file and exit the editor.

Make the script executable:

```bash
chmod +x ssh_activity_summary.sh
```

## Run the script

Run the script as a user that can read the system journal:

```bash
sudo ./ssh_activity_summary.sh
```

With no argument, the script reports SSH activity since the beginning of the current day.

### Run the script with specific parameters

1. To report activity from the last 24 hours:

```bash
sudo ./ssh_activity_summary.sh "24 hours ago"
```

2. To report activity from the last six hours:

```bash
sudo ./ssh_activity_summary.sh "6 hours ago"
```

3. To report activity from a specific date and time:

```bash
sudo ./ssh_activity_summary.sh "2026-08-19 00:00:00"
```

The time expression is passed directly to `journalctl --since`. Use a date and time format accepted by `journalctl`.

### Change the number of displayed results

By default, the script displays up to 20 results in ranked and recent-event sections. Set `TOP_LIMIT` to change this value:

```bash
sudo TOP_LIMIT=50 ./ssh_activity_summary.sh "24 hours ago"
```

## Understand the report

### Statistics

The **Statistics** section provides counts of successful logins, invalid-user attempts, root authentication attempts, failed password attempts, failed public-key attempts, and unique source IP addresses.

### Successful Logins

A successful public-key login resembles:

```text
Accepted publickey for ubuntu from 192.0.2.10 port 52311 ssh2
```

Verify that the username, source IP address and authentication method are expected.

!!! important "Only Accepted entries show successful authentication"

    Messages containing `Invalid user`, `Failed password`, `Connection closed` or `[preauth]` do not show a successful login. A successful SSH authentication normally contains `Accepted publickey`, `Accepted password` or `Accepted keyboard-interactive`.

### Successful Login Source IPs

This section lists IP addresses associated with successful SSH authentication and the number of successful logins from each address.

Known addresses may include:

- your administration workstation;
- an AAU or VPN address;
- a bastion host; or
- another authorised administration endpoint.

Investigate any successful-login source IP address you do not recognise.

### Top SSH Source IPs

This section counts all SSH log entries containing an IP address. A single connection can generate multiple log entries, so the number is an event count rather than an exact connection count.

### Most Common Usernames Attempted

This section combines usernames found in invalid-user, failed-password and failed-public-key entries. Common automated targets include `root`, `admin`, `test`, `oracle`, `deploy`, `pi` and `ubuntu`.

Repeated attempts against generic usernames usually indicate automated scanning. Attempts against a real account require closer attention, particularly when password authentication is enabled.

### Top Invalid-User Scanner Sources

This section identifies IP addresses generating the most `Invalid user` entries. These entries indicate attempts to authenticate with usernames that do not exist on the virtual machine.

### Top Root Login Attempt Sources

This section identifies IP addresses associated with attempts to authenticate as `root`.

A line ending in `[preauth]` means the connection ended before authentication completed. It does not indicate that the login succeeded.

### Source IP Timeline

This section displays the number of SSH log events associated with each IP address, together with the first and last timestamp observed in the selected period.

Use the timeline to distinguish a short scanning burst from activity continuing throughout the selected period.

### Successful IPs Also Showing Suspicious Activity

This section compares successful-login source IPs with entries containing:

- `Invalid user`;
- `Failed password`;
- `Failed publickey`; or
- `authenticating user root`.

An overlap is not proof of compromise. For example, an administrator may mistype a username. Review the related log entries and confirm that the activity is expected.

### Assessment

The final section provides a basic interpretation based on the entries found. It is intended as a prompt for further review and is not a security verdict.

## Recommended security checks

If SSH is reachable through a public IP address, review the following controls.

### Restrict the Strato security group

If possible, restrict inbound TCP port 22 to trusted source networks, such as the address range used by your organisation or VPN. Avoid allowing SSH from `0.0.0.0/0` unless public access is required.

### Use only SSH keys

Check the effective SSH server configuration:

```bash
sudo sshd -T | grep -Ei 'passwordauthentication|pubkeyauthentication|permitrootlogin'
```

A key-only configuration will normally include:

```text
passwordauthentication no
pubkeyauthentication yes
permitrootlogin no
```

!!! caution "Test configuration changes before ending your current session"

    Keep an existing administrative SSH session open while testing changes. An incorrect SSH configuration or firewall rule can lock you out of the virtual machine.

After changing the SSH server configuration, validate it before reloading the service:

```bash
sudo sshd -t
```

If the validation returns no errors, reload the service:

```bash
sudo systemctl reload ssh.service
```

### Review successful logins separately

To display successful SSH authentications from the current day:

```bash
sudo journalctl -u ssh.service --since today --no-pager \
    | grep -E 'Accepted (publickey|password|keyboard-interactive)'
```

To display SSH sessions opened for local users:

```bash
sudo journalctl -u ssh.service --since today --no-pager \
    | grep 'pam_unix(sshd:session): session opened'
```

## Limitations

The script summarises entries available in the `ssh.service` system journal. Keep the following limitations in mind:

- journal retention settings determine how far back the script can report;
- a source IP may represent a VPN, proxy, NAT gateway or bastion host rather than an individual device;
- one SSH connection can create several journal entries;
- the script does not determine the owner, location or reputation of an IP address;
- the script does not prove that a host is secure or compromised; and
- if OpenSSH uses a different systemd unit name, the `journalctl` command in the script must be adjusted.
