When you need to run the same computation multiple times with different inputs, parameters, or datasets, Slurm job arrays provide an efficient solution.
Instead of submitting many individual jobs, you can submit a single job script and let Slurm create multiple tasks automatically.

Typical use cases include:

- Machine learning hyperparameter tuning
- Processing many files
- Running simulations with different random seeds
- Batch data analysis

## What is a Job Array?
Normally, an sbatch job runs once. If you need to run the same script 100 times with different inputs, creating 100 separate job scripts quickly becomes cumbersome.

A job array allows Slurm to create multiple copies of the same job automatically.

```bash
#SBATCH --array=1-100
```
This tells Slurm to run the job 100 times and assign each task a unique number from 1 to 100. 

Every task receives its own identifier through the environment variable:
```bash
$SLURM_ARRAY_TASK_ID
```

##Making an array job
Create a file:
```bash
nano array_test.sh
```
and insert following content:
```bash
#!/usr/bin/env bash
#SBATCH --job-name=array_test
#SBATCH --array=1-5
#SBATCH --output=result_%A_%a.out
#SBATCH --time=00:10:00

echo "This is a array task:"
echo $SLURM_ARRAY_TASK_ID
``
```

Submit the job:
```bash
sbatch array_test.sh
```

You should now see something similar to:
```bash
Submitted batch job 123456
```

Although only one job was submitted, Slurm will internally create:
```bash
123456_1
123456_2
123456_3
123456_4
123456_5
```
Each task will execute independently.

## Understanding %A and %a
When using job arrays, it is often useful to create separate output files for each task.
```bash
#SBATCH --output=result_%A_%a.out
```
Where:

|Variables | Meaning     |
| ---      | ---         |
|%A        |Array Job ID |
|%a        |Task ID      |

Example outputs:
```bash
result_123456_1.out
result_123456_2.out
result_123456_3.out
```

##Using the array Index
The most powerful feature of job arrays is the ability to make each task process different data.

**Example:**
```bash
#!/usr/bin/env bash
#SBATCH --array=1-5

echo "Processing file_$SLURM_ARRAY_TASK_ID.csv"
```
This creates:
```bash
file_1.csv
file_2.csv
file_3.csv
file_4.csv
file_5.csv
```
without writing five separate scripts.

## Processing Multiple Files
Assuming you have following files:
```bash
patient_1.csv
patient_2.csv
patient_3.csv
patient_4.csv
patient_5.csv
```
Create the following batch script:
```bash
#!/usr/bin/env bash

#SBATCH --job-name=process-data
#SBATCH --array=1-5
#SBATCH --time=00:10:00

python analyse.py patient_${SLURM_ARRAY_TASK_ID}.csv
```
Submit the job:
```bash
sbatch process_data.sh
```
Slurm now launches automatically following:
```bash
python analyse.py patient_1.csv
python analyse.py patient_2.csv
python analyse.py patient_3.csv
python analyse.py patient_4.csv
python analyse.py patient_5.csv
```

## Limit The Number of Concurrent Tasks
Submitting 1000 jobs simultaneously may overwhelm the scheduler or consume unnecessary resources.

Slurm allows you to limit how many tasks run at the same time:
```bash
#SBATCH --array=1-1000%10
```
This means:
- Create 1000 tasks
- Only run 10 tasks concurrently

This is highly recommended for large arrays.

**Good practice:** If your tasks are short, independent, and require the same resources, a job array is almost always preferable to submitting hundreds of individual jobs.