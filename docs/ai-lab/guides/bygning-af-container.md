---
hide:
    - navigation
    - toc
    - path
search:
    exclude: true
---

## Bygning af container 1:

Lad os sige, du har et Python-script:

```python
import pandas as pd
import numpy as np

data = pd.DataFrame({
    "temperature": [18, 20, 21, 19, 23],
    "sales": [100, 120, 130, 115, 160]
})

print(data)

print("\nAverage sales:")
print(data["sales"].mean())
```

Det vil du gerne have kørt på AI-LAB.

1. Lav et Python-script på AI-LAB med ovenstående kode.
2. Prøv at køre det som et job med Slurm.
3. Kan du se, hvilken fejlbesked den giver? Hvorfor giver den det?

## Bygning af container 2:

Du vil nu gerne have hentet de pakker, som skal bruges til at kunne køre dit Python-script. På AI-LAB gør vi det via en container. Altså: Vi vil gerne bygge et miljø, hvor både Python indgår samt de pakker, der er krævet for at køre scriptet. Specifikt til AI-LAB/AI Cloud bruger vi det, der hedder Singularity som container-software. En sådan container ender altid på `.sif`.

Når man skal bygge en container, har du brug for 2 elementer:

1. En definitionsfil (opskrift), som fortæller hvad der skal være i containeren (`.def`)
2. Et bash-script (`.sh`), som blot er en fil, der indeholder kommandoer, som bliver kørt i terminalen en linje ad gangen. Det er denne Slurm sætter i gang med `sbatch` (batchjob/baggrundsjob)

Lad os lave definitionsfilen først. Den kunne se sådan ud:

```bash title="torch.def"
Bootstrap: docker
From: ubuntu:22.04

%post
    # This section is where you install software packages

    # Update the package manager (apt)
    apt update

    # install the latest Python and pip version
    apt install -y python3-pip python3-dev

    # use pip to install torch
    pip3 install torch torchvision torchaudio
```

Lad os gå igennem, hvad det betyder. Det første:

`Bootstrap: docker`  
`From: ubuntu:22.04`

Betyder, at vi vil gå ud fra en anden container som udgangspunkt, hvor `ubuntu:22.04` blot er en standard Linux-container i version 22.04. Så får vi de fleste standardpakker, som er påkrævet. Det kunne også være en PyTorch-container, som vi kunne gå ud fra, men vores Python-script er ret simpelt, så vi har ikke brug for mere end Python + nogle enkle pakker.

Dernæst angiver vi i `%post`-sektionen direkte, hvilke installationer der skal køres i containeren. Det kan være mange forskellige typer software, der installeres her. I eksemplet opdaterer vi først systemet, hvilket er god praksis. Dernæst sørger vi for, at Python er installeret samt pip, som er det management-værktøj, der bruges til at installere Python-pakker. Det kan være, det allerede er i den basale Ubuntu-container, men vi installerer alligevel for at sikre, at det er der.

Herefter bruger vi så pip til at installere de Python-pakker, vi gerne vil have - her i eksemplet PyTorch-pakker.

Så opgaven er nu, at du skal lave din egen definitionsfil, hvor du skal installere de pakker, der kræves for at køre dit Python-script.  
Prøv dig ad.

## Bygning af container 3:

Nu skal vi så i gang med at bygge containeren ud fra denne opskriftsfil, du lige har lavet. Det gør vi stadig igennem et Slurm-job, så bygningsprocessen sker på de kraftige compute-nodes og ikke frontend-noden.

Du kan vælge at køre med `srun`, men bygningen kan godt tage lang tid, så vi anbefaler at køre i baggrunden, altså med `sbatch`. Det betyder, at vi skal have lavet et bash-script (`.sh`).

Vi har allerede et standardscript, vi anbefaler at bruge:

```bash title="build_torch.sh"
#!/usr/bin/env bash

#SBATCH --job-name=build_torch
#SBATCH --output=build_torch.out
#SBATCH --error=build_torch.err
#SBATCH --cpus-per-task=32
#SBATCH --mem=80G

export SINGULARITY_TMPDIR=$HOME/.singularity/tmp
export SINGULARITY_CACHEDIR=$HOME/.singularity/cache
mkdir -p $SINGULARITY_CACHEDIR $SINGULARITY_TMPDIR

# The path to the definition file
input_def="torch.def"

# The resulting container image
output_sif="torch.sif"

singularity build --fakeroot $output_sif $input_def
```

De vigtigste pointer:

- Vi sætter en del memory til jobbet (`80G`), da det godt kan bruge meget memory at bygge en container.
- Linjerne med `export` fortæller Singularity, hvor den skal gemme midlertidige filer under byggeprocessen. Når en container bygges, downloader og udpakker Singularity mange filer, som kan fylde flere gigabyte. Derfor er det en god idé at bruge mapper i brugerens home-directory i stedet for systemets standard `/tmp`, som har begrænset plads på HPC-systemer. Det ses ofte, at brugere glemmer dette, og så kan de få fejl relateret til manglende ressourcer under bygningen.
- `singularity build --fakeroot $output_sif $input_def` er kommandoen, der fortæller Singularity, at den skal bygge containeren ud fra input-`.def`-filen.

Så nu skal du lave scriptet som vist, og huske selv at definere `input_def` (din definitionsfil) og `output_sif` (hvad du synes, containeren skal hedde).  
Til sidst er det blot at køre det med:

```bash title="run-build.sh"
sbatch build.sh
```

## Bygning af container 4:

Når du er færdig med bygningen, skulle du gerne have en `.sif`-fil i din mappe.

Prøv nu at køre dit Python-script med den container, du lige har bygget, og se om det ikke virker.
