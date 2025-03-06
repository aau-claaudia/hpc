Below is a step-by-step guide on how to set up a self-hosted GitHub Actions runner on AI-LAB. This allows you to run CI/CD jobs directly from GitHub on AI-LAB.

### 1. Create a self-hosted runner in GitHub

1. Go to the repository in GitHub where you want to use the runner.
2. Click “Settings” (at the top, depending on GitHub’s UI).
3. Select “Actions” in the left menu, then choose “Runners.”
4. Click “New self-hosted runner.”
5. Choose Linux as the OS and X64 for the architecture.
6. GitHub will display commands you need to run on AI-LAB. 
7. Press "Enter" to all settings, to get the default setup.
8. Once you run `./run.sh`, the runner will stay in the foreground and listen for new GitHub jobs. Stop it with Ctrl+C when you’re done testing.

### 2. Create a GitHub Actions workflow
1.  Create or edit a file called .github/workflows/ci.yaml in your repository with a minimal workflow:

    ```yaml
    name: AI-LAB test job
    on:
        push:
        branches:
            - main
    jobs:
        test-hpc:
        runs-on: self-hosted
        steps:
            - name: Check out repo
            uses: actions/checkout@v3
            - name: AI-LAB hostname info
            run: |
                sbatch --output=hostname_output.txt --wrap="hostname"
    ```

2. With the runner, running on AI-LAB, the job should start immediately. Once complete, you can check the output file using: 

    ```
    cat actions-runner/_work/ai-lab-data/ai-lab-data/hostname_output.txt
    ```
