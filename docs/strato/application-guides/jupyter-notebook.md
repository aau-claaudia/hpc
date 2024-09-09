In the following we will be guiding you throught the process of setting up Jupyter Notebooks on a Strato Instance.

!!! info
    Jupyter Notebookes are also available on [DeiC Interactive HPC]("https://cloud.sdu.dk/") (also known as UCloud). This requires no setup and ships with a GUI out of the box. Read more about this possibility in [the official platform documentation]("https://docs.cloud.sdu.dk/Apps/jupyter-lab.html").

## Installing Jupyter

Jupyter can be installed either using Pip or Conda (also known as Anaconda). You will find instructions for both, but it is wise to only chose one of these methods.

### Using Conda

We recommend following the official installation instructions for installing [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/#quick-command-line-install) (a lightweight Conda distribution).

!!! info
    It's also possible to launch an instance that has Miniconda preinstalled. You can find this image in the list of source images (look for *Miniconda Ubuntu 22.04*) - refer back to the section [Launch Instance](/strato/getting-started/launch-instance/) to learn about this list. 


Install Jupyter with conda
```
conda install -c conda-forge jupyter
```

### Using Pip

Update the apt package index:
```
sudo apt update
```

Then install Pip:
```
sudo apt install python3-pip python3-dev
```

Jupyter Notebook can now be installed with Pip:
```
pip3 install jupyter
```

Finally set Jupyter to the path where pip installed it:
```
export PATH="$PATH:$HOME/.local/bin/"
```

## Launch Jupyter Notebook

By adding a few details to our initial SSH-command, you can launch a Jupyter Notebook on your Strato instance and access it in a web browser running on your local computer.
``` 
ssh -i ~/.ssh/my_ssh_key -L 8888:localhost:8888 <user>@<instance_ip>
```

This establishes port-forwarding from your instance to the localhost of your computer. If you did not do this when you logged in to your instance, simply log out and log back in with these details added.

Launch the Jupyter Notebook from your instance with:
```
jupyter notebook --port=8888
```

This will generate a substantial number of lines. Find the line that has a link that looks something like this:
```
http://localhost:8888/tree?token=b9fc44a51db685da273a2cd2kl25ac299f346ce8445bfa262382c
```

Now copy this link and paste it in to your web browser of choice. 

This should land you inside the notebook and everything should feel familiar.
