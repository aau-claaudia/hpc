In the following we will be guiding you throught the process of installing [Docker](https://www.docker.com/) on a Strato Instance.

## Installing Docker
Begin by fetching the appropriate GPG key. This is used by the APT package manager to verify the integrity of the software we want to install.
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

Add the Docker repository to the list of sources in the APT packaging index.
```
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

After this has been done, we will update the APT packaging index.
```
sudo apt update
```

Install Docker CE (Community Edition), Docker CE CLI (Command Line Interface) and containerd.io (a container runtime dependency).
```
sudo apt install docker-ce docker-ce-cli containerd.io
```
If this went well, we should now have installed Docker successfully. Let's verify that, by checking if Docker is running:
```
sudo systemctl --no-pager status docker
```

## Change the privileges
By default the `docker` commands can only be run by the root user, and we will thus need to take two steps to allow the current user to execute `docker` commands. 

Create a new group called `docker`
```
newgrp docker
```

Add the current user to the appropriate Linux group "Docker".
```
sudo usermod -aG docker $USER 
```

Optionally you can run a Docker command (eg. `docker ps`) to verify that all the steps were completed correctly.
