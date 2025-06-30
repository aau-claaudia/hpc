# Set up Open OnDemand, Slurm and Singularity on an Ubuntu 24.04 server.

## Install Open OnDemand 
https://osc.github.io/ood-documentation/latest/installation/install-software.html

### 1. Install Dependencies
```
sudo apt install apt-transport-https ca-certificates
wget -O /tmp/ondemand-release-web_4.0.0-noble_all.deb https://apt.osc.edu/ondemand/4.0/ondemand-release-web_4.0.0-noble_all.deb
sudo apt install /tmp/ondemand-release-web_4.0.0-noble_all.deb
sudo apt update
sudo apt install ondemand
sudo systemctl start apache2
sudo systemctl enable apache2
```

Verify that you see the default Apache page on the servers IP address in a browser

### 2. Add servername

```
sudo nano /etc/apache2/conf-available/servername.conf
```

Add:

```bash title="servername.conf"
ServerName http://10.92.0.250/
```

Replace `10.92.0.250` with the servers IP

```
sudo a2enconf servername
sudo systemctl restart apache2
sudo systemctl reload apache2
```
	
### 3. Edit Open OnDemand configurations:

```
sudo nano /etc/ood/config/ood_portal.yml
```

Add:

```bash title="servername.conf"
servername: 10.92.0.250
auth:
  - 'AuthType Basic'
  - 'AuthName "Open OnDemand"'
  - 'AuthUserFile /etc/ood/passwd'
  - 'Require valid-user'
```

Place it under the `---` and Replace `10.92.0.250` with the servers public IP or URL.

### 4. Set up testuser
```
sudo htpasswd -c /etc/ood/passwd ubuntu
sudo /opt/ood/ood-portal-generator/sbin/update_ood_portal
sudo systemctl restart apache2
```

Now you should be able to open Open OnDemand interface and login with the user you created.

## Install Slurm
### 1. Install Dependencies
```
sudo apt update
sudo apt install -y build-essential munge libmunge-dev libmunge2 libhwloc-dev libhdf5-dev libopenmpi-dev libpam0g-dev libcurl4-openssl-dev libjson-c-dev man2html mariadb-server mariadb-client python3-pip git libdbus-1-dev libsystemd-dev
```

### 2. Set up MUNGE Authentication
```
sudo apt install -y munge	
sudo dd if=/dev/urandom bs=1 count=1024 | sudo tee /etc/munge/munge.key > /dev/null
sudo chown munge: /etc/munge/munge.key
sudo chmod 400 /etc/munge/munge.key	
sudo systemctl enable --now munge
```

Verify that you see `STATUS: Success (0)` when running `munge -n | unmunge`

### 3. Create Slurm User and Directories
```
sudo useradd -m slurm
sudo mkdir -p /etc/slurm /var/spool/slurmd /var/log/slurm
sudo chown slurm: /var/spool/slurmd /var/log/slurm	
```

### 4. Download Slurm and Build Slurm from Source
```
cd /usr/local/src
sudo git clone https://github.com/SchedMD/slurm.git
cd slurm
sudo git checkout slurm-23.11
sudo ./configure
sudo make -j$(nproc)
sudo make install
```
	
### 5. Create Slurm Config File
Replace `open-ondemand-v2` in `SlurmctldHost`, `NodeName`, and `PartitionName` with your hostname (type `hostname` to check). Also replace `NodeAddr=10.92.0.134` with the IP of your server

```
sudo tee /etc/slurm/slurm.conf > /dev/null <<EOF
TaskPlugin=task/none
ClusterName=singlecluster
SlurmctldHost=open-ondemand-v2
SlurmUser=slurm
SlurmdUser=root
StateSaveLocation=/var/spool/slurmd
SlurmdSpoolDir=/var/spool/slurmd
SlurmctldPidFile=/var/run/slurmctld.pid
SlurmdPidFile=/var/run/slurmd.pid
ProctrackType=proctrack/pgid
ReturnToService=1
SlurmctldPort=6817
SlurmdPort=6818
AuthType=auth/munge
CryptoType=crypto/munge
SchedulerType=sched/backfill
SelectType=select/linear
NodeName=open-ondemand-v2 NodeAddr=10.92.0.134 CPUs=8 State=UNKNOWN
PartitionName=debug Nodes=open-ondemand-v2 Default=YES MaxTime=INFINITE State=UP
EOF
```

```
sudo mkdir -p /usr/local/etc
sudo ln -s /etc/slurm/slurm.conf /usr/local/etc/slurm.conf
```

### 6. Start Slurm as a services

```
sudo nano /etc/systemd/system/slurmctld.service
```

Add:

```bash title="slurmctld.service"
[Unit]
Description=Slurm controller daemon
After=munge.service network.target
Requires=munge.service

[Service]
Type=simple
User=slurm
Group=slurm
ExecStart=/usr/local/sbin/slurmctld -D
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```
sudo nano /etc/systemd/system/slurmd.service
```

Add:

```bash title="slurmd.service"
[Unit]
Description=Slurm node daemon
After=munge.service network.target
Requires=munge.service

[Service]
Type=simple
User=root
Group=root
ExecStart=/usr/local/sbin/slurmd -D
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl daemon-reload
sudo systemctl restart slurmctld slurmd
sudo systemctl status slurmctld
sudo systemctl status slurmd
```

Then verify that everything is working with `sinfo` and `srun hostname`

## Install Singularity
https://github.com/sylabs/singularity/blob/main/INSTALL.md

### 1. Install Dependencies
```
sudo apt-get update
sudo apt-get install -y autoconf automake cryptsetup fuse2fs git fuse3 libfuse3-dev libseccomp-dev libtool pkg-config runc squashfs-tools squashfs-tools-ng uidmap wget zlib1g-dev
sudo apt-get install -y libsubid-dev
```

### 2. Install Go
```
cd ~
export VERSION=1.24.4 OS=linux ARCH=amd64
wget -O /tmp/go${VERSION}.${OS}-${ARCH}.tar.gz https://dl.google.com/go/go${VERSION}.${OS}-${ARCH}.tar.gz
sudo tar -C /usr/local -xzf /tmp/go${VERSION}.${OS}-${ARCH}.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc	
source ~/.bashrc
```

### 3. Clone the repo
```
sudo git clone --recurse-submodules https://github.com/sylabs/singularity.git
cd singularity
git submodule update –init
git config --global --add safe.directory /home/ubuntu/singularity
sudo chown -R ubuntu:ubuntu /home/ubuntu/singularity
git submodule update --init
git checkout --recurse-submodules v4.3.2
./mconfig
make -C builddir
sudo make -C builddir install
```

Verify installation with `singularity --version`



## Enable developer mode for user on Open OnDemand
If you would like developer capabilities for creating apps or tools like restarting the web server, then follow this guide:


```
sudo mkdir -p /var/www/ood/apps/dev/ubuntu
cd /var/www/ood/apps/dev/ubuntu
sudo ln -s /home/ubuntu/ondemand/dev gateway
sudo systemctl restart apache2
```

Replace `ubuntu` with the username.

Now you are able to restart Open OnDemand service directly on the website by clicking `Develop` then `Restart Web Server`.


## Setup Slurm integration with Open OnDemand

```
sudo mkdir -p /etc/ood/config/clusters.d
```

```
sudo nano /etc/ood/config/clusters.d/singlecluster.yml
```

Add:

```bash title="singlecluster.yml"
---
v2:
  metadata:
    title: "AI-LAB Cluster"
    url: "https://hpc.aau.dk/ai-lab/"
    hidden: false

  login:
    host: "open-ondemand-v2"

  job:
    adapter: "slurm"
    bin: "/usr/local/bin"
    conf: "/etc/slurm/slurm.conf"
    copy_environment: false

  batch_connect:
    basic:
      script_wrapper: |
        export SLURM_EXPORT_ENV=ALL
        %s
    vnc:
      script_wrapper: |
        export SLURM_EXPORT_ENV=ALL
        module load ondemand-vnc
        %s
    ssh_allow: true
```

```
sudo systemctl restart apache2
```

And `Restart Web Server` in the browser (remember to enable developer mode first). 
You can check if Slurm is configured correctly by submitting `salloc` and then refreshing `Jobs` -> `Active Jobs` to see your job running.



## Create an app

### Batch PyTorch app example

```
sudo mkdir -p /var/www/ood/apps/sys/pytorch
sudo chown -R $USER: /var/www/ood/apps/sys/pytorch
```

```
sudo nano /var/www/ood/apps/sys/pytorch/manifest.yml
```

Add:

```bash title="manifest.yml"
---
name: "pytorch"
category: "Batch Apps"
role: "batch_connect"
description: "Run PyTorch scripts inside a Singularity container."
```

```
sudo nano /var/www/ood/apps/sys/pytorch/form.yml
```

Add:

```bash title="form.yml"
---
cluster: "singlecluster"

form:
  - python_script

attributes:
  python_script:
    label: "Python script to run"
    help: "Relative path under your $HOME (e.g. 'myscript.py') or absolute path (e.g. '/home/ubuntu/script.py')"
    required: true
    widget: text_field
```

```
sudo nano /var/www/ood/apps/sys/pytorch/submit.yml.erb
```

Add:

```bash title="submit.yml.erb"
---
batch_connect:
  template: "basic"

script:
  wall_time: 3600
  copy_environment: true

```

```
sudo mkdir /var/www/ood/apps/sys/pytorch/template
```

```
sudo nano /var/www/ood/apps/sys/pytorch/template/script.sh.erb
```

Add:

```bash title="script.sh.erb"
#!/bin/bash
set -e

# Path to the Singularity image
SINGULARITY_IMAGE="/home/ubuntu/containers/pytorch_25.04.sif"

# Path to the user Python script (expanded from form attribute)
SCRIPT_PATH="$HOME/<%= context.python_script %>"

echo "Running Python script inside Singularity container: $SCRIPT_PATH"

singularity exec "$SINGULARITY_IMAGE" python3 "$SCRIPT_PATH"
```

Add a simple python script in your own directory:

```
nano script.py
```

Add:

```bash title="script.py"
print("Hello from PyTorch Container!")
```

Now go to Open OnDemand dashboard -> `HPC Apps` -> `pytorch`. Then enter `script.py` and hit `Launch`.

Your job should now start and when completet, click on the `Session ID` and click on `output.log`. You should see `Hello from PyTorch Container!`.

### Pin the app to the dashboard
[https://osc.github.io/ood-documentation/latest/customizations.html#pinning-applications-to-the-dashboard](https://osc.github.io/ood-documentation/latest/customizations.html#pinning-applications-to-the-dashboard)
```
sudo nano /etc/ood/config/ondemand.d/ondemand.yml
```

```bash title="ondemand.yml"
pinned_apps:
  - sys/pytorch
```

### Choose an image and shown title for the application
First create this directory to store images in, if not already there:

```
sudo mkdir /var/www/ood/public/images
```

Then move some image in this folder, in this example a PyTorch logo `pytorch.png`

Then modify the apps manifest file:

```
sudo nano /var/www/ood/apps/sys/pytorch/manifest.yml
```

Add the following:

```bash title="manifest.yml"
tile:
  title: "PyTorch"
  icon: "/public/images/pytorch.png"
```

Reload the server with `sudo systemctl restart apache2` and restart OOD in the browser to see the changes.


## Change configurations and design of OOD:

### Override CSS styling:

```
sudo nano /var/www/ood/public/styles.css
```

```css title="styles.css"
.navbar-dark {
    background-color: #211A52;
}
```

Create a new configuration file:

```
sudo nano /etc/ood/config/ondemand.d/customizations.yml
```

```bash title="customizations.yml"
custom_css_files: ["/styles.css"]
```

Reload the server with `sudo systemctl restart apache2` and restart OOD in the browser to see the changes.

### Change footer

```
sudo mkdir -p /etc/ood/config/apps/dashboard/views/layouts
```

```
sudo nano /etc/ood/config/apps/dashboard/views/layouts/_footer.html.erb
```

```html title="_footer.html.erb"
<div>
  My custom footer
<div>
```

### Hide/show items in navigation

```
sudo nano /etc/ood/config/ondemand.d/customizations.yml
```

Add the following somewhere:

```bash title="customizations.yml"
nav_categories: ['Apps', 'Files', 'Jobs']
```
