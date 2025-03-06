
After implementing checkpointing in your script, you have the option to set up automatic job requeuing in case your job gets cancelled. This is done by modifying a [bash script](/ai-lab/guides/running-jobs/#using-sbatch/) that will automatically requeue the job if it's terminated due to exceeding the time limit. You can find an example script, `requeue.sh`, on AI-LAB at `/ceph/course/claaudia/docs/requeue.sh`.


!!! info "Disclaimer"
    Using requeuing is done at your own risk. This guide is intended as a reference, but requeuing your jobs is entirely the responsibility of the user. There may be errors or inaccuracies within this guide. If you encounter any issues or discover mistakes, we encourage you to provide feedback so we can improve. You can submit your feedback [here](https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad001310e).


```bash title="requeue.sh"
#!/bin/bash

#SBATCH --job-name=requeue_example
#SBATCH --time=00:01:00
#SBATCH --signal=B:SIGTERM@30
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=15
#SBATCH --mem=24G

#####################################################################################

# tweak this to fit your needs
max_restarts=4

# Fetch the current restarts value from the job context
scontext=$(scontrol show job ${SLURM_JOB_ID})
restarts=$(echo ${scontext} | grep -o 'Restarts=[0-9]*' | cut -d= -f2)

# If no restarts found, it's the first run, so set restarts to 0
iteration=${restarts:-0}

# Dynamically set output and error filenames using job ID and iteration
outfile="${SLURM_JOB_ID}_${iteration}.out"
errfile="${SLURM_JOB_ID}_${iteration}.err"

# Print the filenames for debugging
echo "Output file: ${outfile}"
echo "Error file: ${errfile}"

##  Define a term-handler function to be executed           ##
##  when the job gets the SIGTERM (before timeout)          ##

term_handler()
{
    echo "Executing term handler at $(date)"
    if [[ $restarts -lt $max_restarts ]]; then
        # Requeue the job, allowing it to restart with incremented iteration
        scontrol requeue ${SLURM_JOB_ID}
        exit 0
    else
        echo "Maximum restarts reached, exiting."
        exit 1
    fi
}

# Trap SIGTERM to execute the term_handler when the job gets terminated
trap 'term_handler' SIGTERM

#######################################################################################

# Use srun to dynamically specify the output and error files
srun --output="${outfile}" --error="${errfile}" singularity exec --nv /ceph/container/pytorch/pytorch_24.09.sif python torch_bm.py
```

In this script, we will run a PyTorch script (located at `/ceph/course/claaudia/docs/torch_bm.py`) using the PyTorch container `/ceph/container/pytorch/pytorch_24.09.sif`. You can modify this to run any script or container you need. Key parameters to pay attention to are:

* `#SBATCH --time=00:01:00`: This sets the time limit for your job. If your job exceeds this limit, it will be cancelled. If not specified, the default time limit is 12 hours.
* `#SBATCH --signal=B:SIGTERM@30`: This tells Slurm to send a SIGTERM signal 30 seconds before the job reaches the time limit, giving the job time to handle termination gracefully.
* `max_restarts=4`: This defines the maximum number of times your job will be automatically requeued if it gets cancelled. In this example, the job will be requeued up to four times before it is finally terminated.