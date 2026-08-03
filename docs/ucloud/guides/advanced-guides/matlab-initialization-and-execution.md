
This guide provides a portable and reproducible workflow for installing required MATLAB products and running long, unattended MATLAB calculations on UCloud. It separates environment preparation from execution, allowing calculations to continue independently of the interactive terminal session. Project files, data, outputs, and logs are kept together under /work, making jobs easier to manage, reproduce, and troubleshoot.

* Automatically detects the MATLAB release provided by UCloud.
* Installs the MATLAB products required by the project.
* Launches unattended calculations with a simple runjob command.
* Keeps scripts, data, outputs, and persistent logs together in the mounted project directory.
* Records job status information and terminates remaining user-owned processes after MATLAB finishes.

!!! warning "Use with dedicated UCloud jobs"

    This workflow is intended for dedicated UCloud MATLAB jobs. After the MATLAB calculation finishes, the execution script terminates processes owned by the current user so that the UCloud job can shut down automatically.


## Prepare the MATLAB project directory

Create a folder for the MATLAB project and mount it under `/work` when starting the UCloud job. The name of the folder is arbitrary.

For example:

```text
/work/MyMatlabProject/
├── initialization.sh
├── execute_matlab_job.sh
├── matlab-products.txt
├── main.m
├── Data/
└── Output/
```

The scripts determine the project directory automatically, so MyMatlabProject can be replaced by any folder name.

Place input data files in `Data/`. MATLAB results should be written to `Output/`.

??? info "MATLAB products - save to a file called `matlab-products.txt`"

    List the MATLAB products required by the project, using one MATLAB Package Manager product identifier per line.

    Blank lines and lines beginning with `#` are ignored.

    ```text
    # Comment out or remove products that are not needed.

    Datafeed_Toolbox
    Deep_Learning_Toolbox
    Econometrics_Toolbox
    Financial_Instruments_Toolbox
    Financial_Toolbox
    Global_Optimization_Toolbox
    Mapping_Toolbox
    Optimization_Toolbox
    Parallel_Computing_Toolbox
    Reinforcement_Learning_Toolbox
    Risk_Management_Toolbox
    Statistics_and_Machine_Learning_Toolbox
    Text_Analytics_Toolbox
    ```

??? info "Initialization script - save to a file called `initialization.sh`"

    The initialization script detects the MATLAB release provided by UCloud, installs the products listed in `matlab-products.txt`, and creates the `runjob` command.

    MATLAB is not started by this script because the network-license environment is made available after initialization.

    ```bash
    #!/usr/bin/env bash

    set -Eeuo pipefail

    ###############################################################################
    # Generic UCloud MATLAB initialization
    #
    # Place this file in the root of the mounted MATLAB project folder:
    #
    #   /work/<project-name>/initialization.sh
    #
    # The script:
    #   1. Detects its own project directory.
    #   2. Detects the UCloud MATLAB root and release.
    #   3. Reads requested products from matlab-products.txt.
    #   4. Installs/checks those products using MPM.
    #   5. Creates the global command:
    #
    #          runjob
    #
    # MATLAB is not launched during initialization because the MATLAB license
    # environment may only be available after UCloud startup has completed.
    ###############################################################################

    PROJECT_DIR="$(
        cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1
        pwd
    )"

    EXECUTION_SCRIPT="${PROJECT_DIR}/execute_matlab_job.sh"
    PRODUCT_FILE="${PROJECT_DIR}/matlab-products.txt"

    RUNTIME_DIR="${PROJECT_DIR}/.ucloud-matlab"
    MPM="${RUNTIME_DIR}/mpm"

    LOG_DIR="${PROJECT_DIR}/logs"
    LOG_FILE="${LOG_DIR}/initialization.log"

    MPM_URL="https://www.mathworks.com/mpm/glnxa64/mpm"

    RUNJOB_COMMAND="/usr/local/bin/runjob"

    mkdir -p "${RUNTIME_DIR}" "${LOG_DIR}"

    exec > >(tee -a "${LOG_FILE}") 2>&1

    echo "============================================================"
    echo "Generic UCloud MATLAB initialization"
    echo "Started:       $(date --iso-8601=seconds)"
    echo "Project dir:   ${PROJECT_DIR}"
    echo "Product file:  ${PRODUCT_FILE}"
    echo "Log file:      ${LOG_FILE}"
    echo "============================================================"

    ###############################################################################
    # Validate project files
    ###############################################################################

    if [[ ! -f "${EXECUTION_SCRIPT}" ]]; then
        echo "ERROR: Execution script was not found:"
        echo "  ${EXECUTION_SCRIPT}"
        exit 1
    fi

    chmod +x "${EXECUTION_SCRIPT}"

    ###############################################################################
    # Locate the MATLAB installation without starting MATLAB
    ###############################################################################

    MATLAB_LAUNCHER="$(command -v matlab || true)"

    if [[ -z "${MATLAB_LAUNCHER}" ]]; then
        echo "ERROR: MATLAB was not found in PATH."
        exit 1
    fi

    MATLAB_EXECUTABLE="$(readlink -f "${MATLAB_LAUNCHER}")"
    MATLAB_ROOT="$(dirname "$(dirname "${MATLAB_EXECUTABLE}")")"
    MATLAB_RELEASE="$(basename "${MATLAB_ROOT}")"

    if [[ ! "${MATLAB_RELEASE}" =~ ^R[0-9]{4}[ab]$ ]]; then
        echo "ERROR: Could not determine the MATLAB release from:"
        echo "  ${MATLAB_EXECUTABLE}"
        exit 1
    fi

    echo
    echo "MATLAB launcher:   ${MATLAB_LAUNCHER}"
    echo "MATLAB executable: ${MATLAB_EXECUTABLE}"
    echo "MATLAB root:       ${MATLAB_ROOT}"
    echo "MATLAB release:    ${MATLAB_RELEASE}"

    ###############################################################################
    # Read requested products
    ###############################################################################

    PRODUCTS=()

    if [[ -f "${PRODUCT_FILE}" ]]; then
        while IFS= read -r line || [[ -n "${line}" ]]; do
            # Remove carriage returns from Windows-edited files.
            line="${line//$'\r'/}"

            # Remove leading and trailing whitespace.
            line="$(sed 's/^[[:space:]]*//;s/[[:space:]]*$//' <<< "${line}")"

            # Ignore comments and blank lines.
            [[ -z "${line}" ]] && continue
            [[ "${line}" == \#* ]] && continue

            PRODUCTS+=("${line}")
        done < "${PRODUCT_FILE}"
    else
        echo
        echo "No matlab-products.txt file was found."
        echo "Toolbox installation will be skipped."
    fi

    ###############################################################################
    # Install requested products
    ###############################################################################

    if [[ ${#PRODUCTS[@]} -gt 0 ]]; then
        echo
        echo "Requested MATLAB products:"

        printf '  - %s\n' "${PRODUCTS[@]}"

        if ! sudo -n true; then
            echo "ERROR: Non-interactive sudo is unavailable."
            exit 1
        fi

        if [[ ! -x "${MPM}" ]]; then
            echo
            echo "Downloading MATLAB Package Manager..."

            if command -v curl >/dev/null 2>&1; then
                curl \
                    --fail \
                    --location \
                    --retry 3 \
                    --output "${MPM}.download" \
                    "${MPM_URL}"
            elif command -v wget >/dev/null 2>&1; then
                wget \
                    --tries=3 \
                    --output-document="${MPM}.download" \
                    "${MPM_URL}"
            else
                echo "ERROR: Neither curl nor wget is available."
                exit 1
            fi

            mv "${MPM}.download" "${MPM}"
            chmod 0755 "${MPM}"
        fi

        echo
        echo "Installing/checking MATLAB products..."

        sudo -n "${MPM}" install \
            --release="${MATLAB_RELEASE}" \
            --destination="${MATLAB_ROOT}" \
            --products "${PRODUCTS[@]}"
    else
        echo
        echo "No MATLAB products were requested."
    fi

    ###############################################################################
    # Create the global runjob command
    #
    # The project path is embedded in this command. The user runs it later from a
    # ready UCloud terminal, allowing the job to inherit MLM_LICENSE_FILE.
    ###############################################################################

    echo
    echo "Creating command:"
    echo "  ${RUNJOB_COMMAND}"

    sudo -n tee "${RUNJOB_COMMAND}" >/dev/null <<EOF
    #!/usr/bin/env bash

    set -e

    PROJECT_DIR="${PROJECT_DIR}"
    EXECUTION_SCRIPT="\${PROJECT_DIR}/execute_matlab_job.sh"
    LOG_DIR="\${PROJECT_DIR}/logs"
    LAUNCH_LOG="\${LOG_DIR}/execute-launcher.log"

    mkdir -p "\${LOG_DIR}"

    if [[ ! -x "\${EXECUTION_SCRIPT}" ]]; then
        echo "ERROR: Execution script is missing or not executable:"
        echo "  \${EXECUTION_SCRIPT}"
        exit 1
    fi

    if [[ -z "\${MLM_LICENSE_FILE:-}" &&
        -z "\${LM_LICENSE_FILE:-}" ]]; then
        echo "ERROR: MATLAB network-license environment is unavailable."
        echo "Wait until the UCloud terminal is fully ready, then run:"
        echo
        echo "  runjob"
        exit 1
    fi

    nohup "\${EXECUTION_SCRIPT}" \
        >> "\${LAUNCH_LOG}" \
        2>&1 \
        < /dev/null &

    echo "MATLAB job started."
    echo "PID:    \$!"
    echo "Log:    \${PROJECT_DIR}/logs/matlab-job.log"
    echo "Output: \${PROJECT_DIR}/Output"
    EOF

    sudo -n chmod 0755 "${RUNJOB_COMMAND}"

    echo
    echo "============================================================"
    echo "Initialization completed successfully"
    echo "Finished: $(date --iso-8601=seconds)"
    echo
    echo "After the UCloud terminal is ready, start the job with:"
    echo
    echo "  runjob"
    echo "============================================================"
    ```

??? info "MATLAB execution script - save to a file called `execute_matlab_job.sh`"

    The execution script starts MATLAB, writes persistent logs, records whether the calculation completed successfully, and terminates the processes associated with the UCloud job after MATLAB finishes.

    ```bash
    #!/usr/bin/env bash

    set -uo pipefail

    ###############################################################################
    # Generic UCloud MATLAB execution script
    #
    # Expected project structure:
    #
    #   project/
    #   ├── execute_matlab_job.sh
    #   ├── main.m
    #   ├── Data/
    #   └── Output/
    #
    # main.m should contain the user's MATLAB calculation.
    ###############################################################################

    PROJECT_DIR="$(
        cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1
        pwd
    )"

    MATLAB_SCRIPT="${MATLAB_SCRIPT:-main.m}"
    MATLAB_SCRIPT_PATH="${PROJECT_DIR}/${MATLAB_SCRIPT}"

    DATA_DIR="${PROJECT_DIR}/Data"
    OUTPUT_DIR="${PROJECT_DIR}/Output"
    LOG_DIR="${PROJECT_DIR}/logs"
    STATUS_DIR="${PROJECT_DIR}/job-status"

    LOG_FILE="${LOG_DIR}/matlab-job.log"
    SUCCESS_FILE="${STATUS_DIR}/matlab-job.success"
    FAILURE_FILE="${STATUS_DIR}/matlab-job.failed"
    SHUTDOWN_LOG="${LOG_DIR}/shutdown.log"

    mkdir -p "${DATA_DIR}" "${OUTPUT_DIR}" "${LOG_DIR}" "${STATUS_DIR}"

    rm -f "${SUCCESS_FILE}" "${FAILURE_FILE}"

    cd "${PROJECT_DIR}" || exit 1

    exec > >(tee -a "${LOG_FILE}") 2>&1

    ###############################################################################
    # Shutdown helper
    #
    # This reproduces the earlier process-kill approach using the current UID,
    # rather than hard-coding a username.
    #
    # WARNING:
    # This is intended for a dedicated UCloud job pod. It kills all processes
    # belonging to the current user after the MATLAB job finishes.
    ###############################################################################

    shutdown_pod() {
        echo
        echo "Scheduling shutdown of user-owned processes in 10 seconds..."

        (
            sleep 10

            {
                echo "============================================================"
                echo "Shutdown started: $(date --iso-8601=seconds)"
                echo "UID: $(id -u)"
                echo
                echo "Processes before shutdown:"
                ps -eo user=,uid=,pid=,ppid=,stat=,comm=,args= || true
                echo
                echo "Executing:"
                echo "  pkill -9 -u $(id -u)"
                echo "============================================================"
            } >> "${SHUTDOWN_LOG}" 2>&1

            pkill -9 -u "$(id -u)"

        ) >/dev/null 2>&1 &

        disown 2>/dev/null || true
    }

    ###############################################################################
    # Startup information
    ###############################################################################

    echo "============================================================"
    echo "Generic UCloud MATLAB job"
    echo "Started:       $(date --iso-8601=seconds)"
    echo "Project dir:   ${PROJECT_DIR}"
    echo "MATLAB script: ${MATLAB_SCRIPT_PATH}"
    echo "Data dir:      ${DATA_DIR}"
    echo "Output dir:    ${OUTPUT_DIR}"
    echo "Log file:      ${LOG_FILE}"
    echo "============================================================"

    ###############################################################################
    # Validate environment
    ###############################################################################

    if [[ ! -f "${MATLAB_SCRIPT_PATH}" ]]; then
        echo "ERROR: MATLAB script was not found:"
        echo "  ${MATLAB_SCRIPT_PATH}"

        {
            echo "status=failed"
            echo "exit_code=1"
            echo "reason=MATLAB script not found"
            echo "finished=$(date --iso-8601=seconds)"
        } > "${FAILURE_FILE}"

        sync
        shutdown_pod
        exit 1
    fi

    if ! command -v matlab >/dev/null 2>&1; then
        echo "ERROR: MATLAB was not found in PATH."

        {
            echo "status=failed"
            echo "exit_code=127"
            echo "reason=MATLAB executable not found"
            echo "finished=$(date --iso-8601=seconds)"
        } > "${FAILURE_FILE}"

        sync
        shutdown_pod
        exit 127
    fi

    if [[ -z "${MLM_LICENSE_FILE:-}" &&
        -z "${LM_LICENSE_FILE:-}" ]]; then
        echo "ERROR: MATLAB network-license environment is unavailable."

        {
            echo "status=failed"
            echo "exit_code=1"
            echo "reason=MATLAB license environment unavailable"
            echo "finished=$(date --iso-8601=seconds)"
        } > "${FAILURE_FILE}"

        sync
        shutdown_pod
        exit 1
    fi

    echo
    echo "MATLAB executable: $(command -v matlab)"
    echo "License environment: available"
    echo
    echo "Starting MATLAB..."

    ###############################################################################
    # Execute the MATLAB script
    #
    # Keep this invocation on one physical line.
    ###############################################################################

    matlab -batch "cd('${PROJECT_DIR}');run('${MATLAB_SCRIPT_PATH}');"

    MATLAB_EXIT_CODE=$?

    ###############################################################################
    # Record completion
    ###############################################################################

    echo
    echo "============================================================"
    echo "MATLAB process finished"
    echo "Finished:  $(date --iso-8601=seconds)"
    echo "Exit code: ${MATLAB_EXIT_CODE}"
    echo "============================================================"

    if [[ ${MATLAB_EXIT_CODE} -eq 0 ]]; then
        {
            echo "status=success"
            echo "exit_code=0"
            echo "finished=$(date --iso-8601=seconds)"
            echo "project_dir=${PROJECT_DIR}"
            echo "matlab_script=${MATLAB_SCRIPT_PATH}"
            echo "output_dir=${OUTPUT_DIR}"
            echo "log_file=${LOG_FILE}"
        } > "${SUCCESS_FILE}"

        rm -f "${FAILURE_FILE}"

        echo
        echo "MATLAB job completed successfully."
    else
        {
            echo "status=failed"
            echo "exit_code=${MATLAB_EXIT_CODE}"
            echo "reason=MATLAB returned a nonzero exit code"
            echo "finished=$(date --iso-8601=seconds)"
            echo "project_dir=${PROJECT_DIR}"
            echo "matlab_script=${MATLAB_SCRIPT_PATH}"
            echo "log_file=${LOG_FILE}"
        } > "${FAILURE_FILE}"

        rm -f "${SUCCESS_FILE}"

        echo
        echo "MATLAB job failed."
    fi

    echo
    echo "Output files:"

    find "${OUTPUT_DIR}" \
        -type f \
        -printf '  %p (%s bytes)\n' \
        2>/dev/null || true

    sync

    shutdown_pod

    echo
    echo "Execution wrapper finished."
    echo "The shutdown helper will run shortly."

    exit "${MATLAB_EXIT_CODE}"
    ```


!!! important "Write outputs under `Output/`"

    Files stored elsewhere in the container may be lost when the UCloud job terminates. Write results that should persist after the job finishes to the `Output/` directory inside the mounted project folder.

??? info "MATLAB entry-point script - save to a file called `main.m`"

    Place the MATLAB commands that perform the calculation in `main.m`.

    The example below determines the project directory automatically and defines standard locations for input data and output files.

    ```matlab
    %% Project MATLAB entry point

    projectDir = fileparts(mfilename('fullpath'));
    dataDir = fullfile(projectDir, 'Data');
    outputDir = fullfile(projectDir, 'Output');

    if ~isfolder(outputDir)
        mkdir(outputDir);
    end

    fprintf('Project directory: %s\n', projectDir);
    fprintf('Data directory:    %s\n', dataDir);
    fprintf('Output directory:  %s\n', outputDir);

    %% Load data

    % Example:
    % inputFile = fullfile(dataDir, 'my-data.mat');
    % load(inputFile);

    %% Run analysis

    % Add project-specific MATLAB code here.

    %% Save output

    % Example:
    % save(fullfile(outputDir, 'results.mat'), 'results', '-v7.3');
    ```

## Run the MATLAB job

When starting the MATLAB application on UCloud:

1. Mount the MATLAB project folder under `/work`.
2. Select `initialization.sh` as the initialization script.
3. Select the required MATLAB network license.
4. Start the job and wait until the MATLAB application is fully ready.
5. Open a terminal and run:

```bash
runjob
```

The `runjob` command starts `execute_matlab_job.sh` in the background and redirects its output to persistent log files inside the mounted project directory. The terminal can therefore be closed without stopping the MATLAB calculation.

!!! note

    Do not run `runjob` until the UCloud application is fully ready. The MATLAB network-license environment required by the execution script may not be available during initialization.

To follow the MATLAB calculation while it is running, use:

```bash
tail -f /work/<project-name>/logs/matlab-job.log
```

After MATLAB finishes, inspect:

```text
Output/                     MATLAB output files
logs/initialization.log     Initialization and toolbox installation log
logs/matlab-job.log         MATLAB execution log
logs/execute-launcher.log   Background launcher log
logs/shutdown.log           Process shutdown log
job-status/                 Success or failure status files
```

A successful calculation creates `job-status/matlab-job.success`. If MATLAB exits with an error, the execution script instead creates `job-status/matlab-job.failed`.

To follow the MATLAB calculation while it is running, use:

```bash
tail -f /work/<project-name>/logs/matlab-job.log
```