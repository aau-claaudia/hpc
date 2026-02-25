# Exercise 2: Create and submit a batch script

Practice creating and submitting batch scripts.

---


1. Use `micro` text editor (or any other if you're an experienced Linux user) to open the script `run.sh` that already exist in the workshop directory.

    ??? info "Hint"
        ```bash
        micro run.sh
        ```

2. In the bottom of the script, add:
   
      ```
      python3 simple_script.py
      ```
   
3. Save it by hitting `CTRL + S` and then `CTRL + Q` to exit nano.


4. Submit the job using `sbatch`

    ??? info "Hint"
        ```bash
        sbatch run.sh
        ```

5. Check the job status using `squeue --me`

    ??? info "Hint: Make it update every second"
        ```bash
        watch -n1 squeue --me
        ```

6. Once completed, check the results by printing out the output file using `cat` command
   
    ??? info "Hint"
        ```bash
        cat myjob.log
        ```

---

**Next:** [Allocating Resources →](14-allocating-resources.md)

