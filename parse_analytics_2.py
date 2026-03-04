# -*- coding: utf-8 -*-
"""Parse second analytics format: views, change+path, title per entry."""

data = """449
–28%	/ai-lab
About AI-LAB - AAU HPC
13
421
–3%	/
Home - AAU HPC
407
+7%	/ucloud
About UCloud - AAU HPC
326
–54%	/ucloud/guides/application-guides/transcriber
Transcriber - AAU HPC
264
+8%	/ucloud/how-to-access
How to access - AAU HPC
214
–35%	/ai-lab/guides/login
2. Login - AAU HPC
213
–9%	/ai-cloud
About AI Cloud - AAU HPC
203
+24%	/strato
About Strato - AAU HPC
194
–11%	/ai-lab/how-to-access
How to access - AAU HPC
167
–26%	/ai-lab/guides
Index - AAU HPC
130
–55%	/ai-lab/guides/file-handling
3. File Handling - AAU HPC
13
122
+270%	/taaurus
About TAAURUS - AAU HPC
#12
116
+61%	/strato/how-to-access
How to access - AAU HPC
#13
108
–41%	/ai-lab/guides/running-jobs
4. Running Jobs - AAU HPC
#14
106
–31%	/ai-lab/guides/getting-containers
5. Getting Containers - AAU HPC
#15
91
–39%	/ai-lab/guides/using-containers
6. Using Containers - AAU HPC
#16
85
–25%	/ai-lab/system-overview
System overview - AAU HPC
#17
76
+15%	/ucloud/guides/sensitive-data-on-ucloud
Guidelines for handling sensitive data - AAU HPC
#18
69
–20%	/ai-lab/guides/prerequisites
1. Prerequisites - AAU HPC
#19
66
+14%	/ucloud/guides/getting-started/before-you-begin
Before you begin - AAU HPC
#20
65
–24%	/ai-cloud/how-to-access
How to access - AAU HPC
13
63
–9%	/ai-cloud/system-overview
System overview - AAU HPC
#22
61
–20%	/ai-lab/guides/batch-llm-inference
Batch LLM Inference - AAU HPC
#23
56
–50%	/ai-lab/guides/monitoring
7. Monitoring - AAU HPC
#24
56
–8%	/strato/getting-started/access-instance
Access instance - AAU HPC
#25
55
+17%	/service-windows
Service windows - AAU HPC
#26
54
+10%	/strato/getting-started/launch-instance
Launch instance - AAU HPC
#27
54
+32%	/strato/getting-started
Before you begin - AAU HPC
#28
50
+6%	/ai-cloud/getting-started/file-management
File transfer - AAU HPC
#29
42
+27%	/external-hpc
External HPC facilities - AAU HPC
#30
41
+64%	/ucloud/guides/application-guides/ChatUI
ChatUI - AAU HPC
13
39
1%	/ai-cloud/getting-started
Before you begin - AAU HPC
#32
38
–16%	/ucloud/guides/getting-started/transfer-files
File transfer - AAU HPC
#33
37
+28%	/external-hpc/deic-resources
DeiC HPC resources - AAU HPC
#34
36
+33%	/ai-lab/additional-guides/checking-gpu-usage
Checking GPU usage - AAU HPC
#35
35
–43%	/ai-lab/guides/video-onboarding-guide
Video Onboarding Guide - AAU HPC
#36
34
+70%	/ai-lab/additional-guides/building-your-own-container-image-locally
Building your own container image locally - AAU HPC
#37
33
–31%	/ai-cloud/getting-started/login
Log in - AAU HPC
#38
32
+23%	/ai-cloud/getting-started/run-jobs
Run jobs - AAU HPC
#39
31
+107%	/taaurus/guides/applying-for-a-taaurus-project
Applying for a TAAURUS project - AAU HPC
#40
31
–30%	/ai-lab/troubleshooting
Troubleshooting - AAU HPC
13
31
+41%	/ai-cloud/additional-guides/cancelling-jobs
Cancelling jobs - AAU HPC
#42
28
–13%	/ai-cloud/getting-started/container-images
Container images - AAU HPC
#43
27
+125%	/ucloud/guides/application-guides/Voyant-Tools
Voyant Tools - AAU HPC
#44
27
–7%	/ucloud/terms-and-conditions
Terms and Conditions - AAU HPC
#45
26
+30%	/hpc-decision-tree
HPC Decision Tree - AAU HPC
#46
25
–14%	/ucloud/guides/application-guides/Dictaphone
Dictaphone - AAU HPC
#47
25
+213%	/ai-lab/workshop/12-creating-a-sbatch-script
12. Creating a job script - AAU HPC
#48
24
+85%	/ai-lab/workshop/11-exercise-1
11. Exercise 1 - AAU HPC
#49
24
–11%	/external-hpc/lumi
LUMI - AAU HPC
#50
24
–27%	/strato/getting-started/transfer-files
Transfer files - AAU HPC
13
22
+83%	/ai-lab/workshop/13-exercise-2
13. Exercise 2 - AAU HPC
#52
21
+75%	/hpc-cost-estimator
HPC Cost Estimator - AAU HPC - AAU HPC
#53
21
+17%	/ai-lab/additional-guides/running-a-container-in-interactive-mode
Running a container in interactive mode - AAU HPC
#54
20
–38%	/taaurus/guides/login
How to log in - AAU HPC
#55
20
+150%	/ai-lab/workshop/1-Introduction-to-ai-lab
1. Introduction to AI-LAB - AAU HPC
#56
20
+5%	/ai-cloud/additional-guides/batch-llm-inference
AAU HPC
#57
20
–26%	/ai-cloud/fair-usage
Fair usage - AAU HPC
#58
19
(new)	/ucloud/use-cases/voice-modification-schizophrenia
Voice modification for schizophrenia therapy - AAU HPC
#59
19
+36%	/hpc-comparison-table
HPC Comparison Tree - AAU HPC
#60
19
–64%	/ai-lab/fair-usage
AAU HPC
13
19
+46%	/ai-cloud/terms-and-conditions
Terms and Conditions - AAU HPC
#62
19
+12%	/strato/application-guides/strato-applications
Strato applications - AAU HPC
#63
18
+500%	/ai-lab/workshop/18-exercise-3
18. Exercise 3 - AAU HPC
#64
18
+125%	/ai-lab/workshop/17-using-containers
17. Using Containers - AAU HPC
#65
18
–14%	/strato/usage-management
Usage Management - AAU HPC
#66
18
+50%	/strato/getting-started/before-you-begin
AAU HPC
#67
17
(new)	/ai-cloud/additional-guides/additional-resources
Additional resources - AAU HPC
#68
17
+143%	/taaurus/guides/navigating-taaurus
Navigating TAAURUS - AAU HPC
#69
17
+467%	/taaurus/how-to-access
AAU HPC
#70
17
+325%	/ai-lab/workshop/10-two-ways-of-running-jobs
10. Two Ways of Running Jobs - AAU HPC
13
17
+42%	/ucloud/guides/advanced-guides/connect-neo4j-to-vscode
Connect Neo4j to VS Code - AAU HPC
#72
17
+240%	/strato/application-guides/matlab
Matlab - AAU HPC
#73
17
+13%	/ai-lab/additional-guides/multiple-gpus-with-pytorch
Multiple GPUs with PyTorch - AAU HPC
#74
17
–19%	/ai-cloud/additional-guides/building-your-own-container-image
Building your own container image - AAU HPC
#75
16
(new)	/ucloud/Use%20cases/Voice-modification-schizophrenia
Voice modification for schizophrenia therapy - AAU HPC
#76
16
+220%	/taaurus/system-overview
System overview - AAU HPC
#77
16
+220%	/ai-lab/workshop/7-essential-linux-commands
7. Essential Linux Commands - AAU HPC
#78
16
+100%	/ai-lab/workshop/16-getting-containers
16. Getting Containers - AAU HPC
#79
16
+78%	/ai-lab/workshop/15-containers
15. Containers - AAU HPC
#80
16
+14%	/ai-cloud/additional-guides/directories-overview
Overview of directories - AAU HPC
13
16
+23%	/strato/terms-and-conditions
Terms and Conditions - AAU HPC
#82
16
–53%	/ucloud/guides/application-guides/transcriber/transcriber-video
Transcriber guide videos - AAU HPC
#83
15
1%	/ai-cloud/additional-guides/checking-gpu-utilisation
Checking GPU utilisation - AAU HPC
#84
15
+25%	/ai-lab/workshop/9-slurm
9. Slurm - AAU HPC
#85
15
–29%	/ai-lab/workshop/5-logging-into-ai-lab
5. Logging into AI-LAB - AAU HPC
#86
15
+36%	/ucloud/providers
Providers - AAU HPC
#87
15
+15%	/ai-cloud/additional-guides/checking-the-queue
Checking the queue - AAU HPC
#88
14
+600%	/ai-lab/workshop/19-final-pointers
19. Final pointers - AAU HPC
#89
14
+75%	/ai-lab/workshop/8-transferring-files
8. Transferring Files - AAU HPC
#90
14
1%	/ai-lab/workshop/6-file-handling-on-ai-lab
6. File Handling on AI-LAB - AAU HPC
13
14
+17%	/external-hpc/eurohpc-resources
EuroHPC resources - AAU HPC
#92
14
–7%	/ucloud/guides/getting-started/Licens
License Management - AAU HPC
#93
14
+17%	/ai-lab/additional-guides/cpu-gpu-and-memory-allocation
CPU, GPU, and memory allocation - AAU HPC
#94
13
+225%	/ai-lab/workshop/14-allocating-resources
14. Allocating Resources - AAU HPC
#95
13
+30%	/ai-cloud/additional-guides/creating-a-virtual-environment
Creating a virtual environment - AAU HPC
#96
13
–7%	/ai-lab/guides/ci-cd-with-github-actions
CI/CD with GitHub Actions - AAU HPC
#97
13
–38%	/ai-cloud/additional-guides/multiple-gpus-with-pytorch
Multiple GPUs with PyTorch - AAU HPC
#98
12
–33%	/ai-cloud/getting-started/look-around
Look around - AAU HPC
#99
12
+300%	/strato/advanced-guides/persistent-terminal-sessions
Persistent terminal sessions - AAU HPC
#100
12
1%	/strato/advanced-guides/attaching-a-volume-for-additional-storage
Attaching a volume for additional storage - AAU HPC
13
12
+9%	/strato/application-guides/jupyter-notebook
Jupyter Notebook - AAU HPC
#102
12
+20%	/strato/advanced-guides/command-line-interface-access
Command line interface access - AAU HPC
#103
12
–25%	/ai-cloud/additional-guides/download-container-images
Pulling container images from the internet - AAU HPC
#104
11
(new)	/ai-cloud/resource-quotas
Resource quotas - AAU HPC
#105
11
+38%	/ai-lab/workshop/4-the-ai-lab-workflow
4. The AI-LAB Workflow - AAU HPC
#106
11
+38%	/ai-lab/workshop/3-ai-lab-under-the-hood
3. AI-LAB Under the Hood - AAU HPC
#107
11
+38%	/ai-lab/workshop/2-what-is-ai-lab
2. What is AI-LAB? - AAU HPC
#108
11
–62%	/ai-lab/guides/checkpointing
Checkpointing - AAU HPC
#109
11
–39%	/ai-cloud/additional-guides/cpu-gpu-and-memory-allocation
CPU, GPU, and memory allocation - AAU HPC
#110
"""

lines = [ln.strip() for ln in data.strip().splitlines()]
rows = []
i = 0
while i < len(lines):
    if not lines[i]:
        i += 1
        continue
    # Line 1: views (number)
    views = lines[i]
    if not views.isdigit():
        i += 1
        continue
    i += 1
    if i >= len(lines):
        break
    # Line 2: change \t path
    part = lines[i]
    i += 1
    if "\t" in part:
        change_path = part.split("\t", 1)
        change = change_path[0].replace("\u2013", "-").strip()
        path = change_path[1].strip() if len(change_path) > 1 else ""
    else:
        change = part.replace("\u2013", "-").strip()
        path = lines[i].strip() if i < len(lines) else ""
        if path.startswith("/"):
            i += 1
        else:
            path = ""
    if i >= len(lines):
        break
    # Line 3: title
    title = lines[i].strip()
    i += 1
    # Optional line 4: #n (rank) or "13" (page number, skip)
    rank = len(rows) + 1
    if i < len(lines) and lines[i]:
        if lines[i].startswith("#"):
            rank = lines[i]
            i += 1
        elif lines[i] == "13":
            i += 1
    # Trim " - AAU HPC" from title for display (repeat for double suffix)
    while title.endswith(" - AAU HPC"):
        title = title[:-10].strip()
    if path.startswith("/"):
        rows.append((rank, views, change, path, title))

out = "| # | Views | Change | Path | Page |\n"
out += "|---|-------|--------|------|------|\n"
for r in rows:
    rank, views, change, path, title = r
    title_esc = title.replace("|", "\\|")
    out += "| {} | {} | {} | {} | {} |\n".format(rank, views, change, path, title_esc)

with open("docs/page-views-table-2.md", "w", encoding="utf-8") as f:
    f.write("# Page views (HPC site) — recent\n\n")
    f.write(out)
print(out)
