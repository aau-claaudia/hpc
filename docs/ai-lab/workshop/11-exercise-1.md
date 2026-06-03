# Exercise 1: Run a simple job with srun



<div class="workshop-internal-break" role="separator"></div>


1. Download workshop files by running this command:

      ```bash
      ailab --workshop
      ```

2. Change directory (`cd`) to `workshop`

    ??? info "Hint"
        ```bash
        cd ~/workshop
        ```

3. Run the script `simple_script.py` with `python3` using `srun -u`

    ??? info "Hint"
        ```bash
        srun -u python3 simple_script.py
        ```

4. ...and you should get:

```
...
Second 29...
Second 30...
Done after 30 seconds!
```



<div class="workshop-internal-break" role="separator"></div>


**Next:** [Creating an sbatch Script →](12-creating-a-sbatch-script.md)

