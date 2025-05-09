# Installation guide for Isaac-sim on Strato

### General: 
* Software for mechanical simulation
* Recommended to use GPU virtual machines and docker
* It is a software package that requires docker and is currently tested for the "CUDA Ubuntu 22.04" image.

### Notes

* The NVIDIA driver installation requires a specific Linux kernel, which is available on the "CUDA Ubuntu 22.04" image.
* Isaac-Sim is compatible with a specific NVIDIA installation, which is not part of the standard Strato image set, so it requires removing the existing NVIDIA installation from the "CUDA Ubuntu 22.04" image.
* On UCloud, the product is called Virtual Machine "CUDA 22.04"
* X-forwarding (particularly the activation of a display) has been affected by which network a virtual machine is started on - i.e. a public or local network in the Strato platform. I can't explain why, but there are several items that must be modified in the `/etc/ssh/sshd_config` file location if starting from a "campus network" IP address, which are not necessary when launching from a public IP.

##  Create an instance on Strato (or on UCloud, if you have access to virtual machine resources)

For both Strato and UCloud you will need to prepare an SSH key. You can follow [the getting started guide for Strato](https://hpc.aau.dk/strato/getting-started/launch-instance/) to create an SSH key, and to ensure that you also enable access to the instance via SSH port 22.

On both platforms there is an option to enter the public part of you SSH key when launching an instance (on Strato) or job (on UCloud).

### Connect to your instance from the terminal (powershell for Windows) using SSH

It is a good idea include the X11 forwarding flag `-X` in your connection command.

Isaac-sim also allows traffic for different services via certain ports, and you might want to include port forwarding for some of those services from the beginning.

According to ChatGPT, Isaac Sim typically runs Omniverse Kit-based applications with a WebSocket or HTTP server. The default Ports for Isaac Sim are:
* Default WebSocket ports: 3000, 8211
* Default Streaming (WebRTC) port: 3000
* Default HTTP-based UI port: 8080
* If using Jupyter Lab: 8888

Some examples of the connection command for your virtual machine are as follows, you can leave out port exposures that you don't need by removing, for example, `-L 8888:localhost:8888` if you do not need Jupyter Lab notebook exposure.

#### UCloud connection command
```bash
ssh -i ~/.ssh/ucloud_key ucloud@130.225.38.??? -L 3000:localhost:3000 -L 8080:localhost:8080 -L 8888:localhost:8888 -X
```
#### Strato connection command
```bash
ssh -i ~/.ssh/strato_key ubuntu@130.225.37.??? -L 3000:localhost:3000 -L 8080:localhost:8080 -L 8888:localhost:8888 -X
```


### Update apt before purging the NVIDIA drivers
Begin by updating the APT packaging index, so that you have an updated list of sources to download applications from.

> It is very important that you do not `sudo apt upgrade`, as this will alter the kernel.

```bash
sudo apt update
```

## Purge the server for any NVIDIA drivers

The NVIDIA drivers pre-installed on the image will be incompatible with the installation you need for Isaac Sim. These need to be removed before continuing.

```bash
sudo apt-get remove --purge nvidia-* -y
```

```bash
sudo apt autoremove && sudo apt autoclean
```


## Install x server

To ensure that X11 works properly for forwarding the visual interface you will need to install a few additional packages.

```bash
sudo apt install -y \
    xserver-xorg x11-utils x11-xserver-utils xinit\
    pkg-config vulkan-tools build-essential\
    xdg-utils mesa-utils xvfb
```

## Install the NVIDIA drivers for running the docker container

It is possible to try to run either one of two sets of drivers, 550.127.05 is the latest driver available from XFree86, but if you want to install the one recommended on NVIDIA's website you can install 535.129.03. Both are compatible with the kernel of the "CUDA Ubuntu 22.04" image.

#### 550.127.05 driver (Latest)

```bash
wget https://us.download.nvidia.com/XFree86/Linux-x86_64/550.127.05/NVIDIA-Linux-x86_64-550.127.05.run
chmod +x NVIDIA-Linux-x86_64-550.127.05.run
sudo ./NVIDIA-Linux-x86_64-550.127.05.run
```

#### 535.129.03 driver

```bash
# wget https://us.download.nvidia.com/XFree86/Linux-x86_64/535.129.03/NVIDIA-Linux-x86_64-535.129.03.run
# chmod +x NVIDIA-Linux-x86_64-535.129.03.run
# sudo ./NVIDIA-Linux-x86_64-535.129.03.run

```
You will be presented with a few options during the installation, where I have had success by just selecting [YES] in each case.

- Install 32 bit components [YES]
- Build DKMS tarball [YES]
- Rebuild intraframs [YES]

## Install docker

You then need to install docker - there are some additional docker instructions if you launch this virtual machine on a "Campus Network"

```bash
# Docker installation using the convenience script
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
Allow the installation to complete, adn then run the post installation commands:

```bash
# Post-install steps for Docker
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```
Once complete, your user will be able to run docker without a `sudo` pre-text. Now run a `hello world` to test your installation.

```bash
# Verify Docker
docker run hello-world
```

## Install the NVIDIA Container Toolkit

Next you will need to install the NVIDIA container toolkit. 

It is important that this is run after purging nad reinstalling the NVIDIA drivers, as a compatible container toolkit will be automatically installed.

```bash
# Configure the repository
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
    && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
    && \
    sudo apt-get update

# Install the NVIDIA Container Toolkit packages
sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```

Configure the NVIDIA runtime to docker.

```bash
# Configure the container runtime
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

```

Run `nvidia-smi` from within docker to see that all GPUs are visible from within the docker environment.

```bash
# Verify NVIDIA Container Toolkit
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

## Fetch and run the Isaac-Sim container in Docker

Starting by the following lines to start the container from the link

#### Running Isaac-sim headless on Strato:

You will need to allow TCP and UDP traffic by modifying the security groups on Strato

```bash
docker run --name isaac-sim --entrypoint bash -it --runtime=nvidia --gpus all -e "ACCEPT_EULA=Y" --rm --network=host \
    -e "PRIVACY_CONSENT=Y" \
    -v ~/docker/isaac-sim/cache/kit:/isaac-sim/kit/cache:rw \
    -v ~/docker/isaac-sim/cache/ov:/root/.cache/ov:rw \
    -v ~/docker/isaac-sim/cache/pip:/root/.cache/pip:rw \
    -v ~/docker/isaac-sim/cache/glcache:/root/.cache/nvidia/GLCache:rw \
    -v ~/docker/isaac-sim/cache/computecache:/root/.nv/ComputeCache:rw \
    -v ~/docker/isaac-sim/logs:/root/.nvidia-omniverse/logs:rw \
    -v ~/docker/isaac-sim/data:/root/.local/share/ov/data:rw \
    -v ~/docker/isaac-sim/documents:/root/Documents:rw \
    nvcr.io/nvidia/isaac-sim:4.5.0
```

Then run Isaac Sim headless and wait for the terminal to show "Isaac Sim Full Streaming App is loaded"

```bash
./runheadless.sh -v
```


## Install the WebRTC Streaming Client on your local machine

Now open a new terminal on your local machine
(SKIP if you have downloaded the Isaac Sim WebRTC Streaming Client) if not, this is how to do it

Go to this link: https://docs.isaacsim.omniverse.nvidia.com/latest/installation/download.html#isaac-sim-latest-release


Download the Isaac Sim WebRTC Streaming Client for linux, and put it in a folder called ""IsaacSim" on your local machine home directory

Now start Isaac Sim WebRTC Streaming Client in the directory where you downloaded it.

```bash
./IsaacSim/isaacsim-webrtc-streaming-client-1.0.6-linux-x64.AppImage
```

Insert the ip addresse of the openstack instance and open the GUI

Now you should have Isaac Sim up and running



## Strato Campus Network Additional instructions

#### Strato Campus Network virtual machines: Docker port modifications to ensure that the ip ranges needed for docker are modified.

As per the AAU docker guidelines in [Danish](https://www.its.aau.dk/vejledninger/docker), or [English](https://www.en.its.aau.dk/instructions/docker)

Edit `/etc/docker/daemon.json` to include

```json
{
"bip": "10.14.0.1/16",
"ipv6": false
}
```

```bash
# reboot the virtual machine
sudo reboot
```



##### Modify some lines in the sshd_config file

If you are launching the instance on the Strato platform, and use the one of the local "Campus" network options. You will need to check that on the server the following is included in `/etc/ssh/sshd_config`:

```bash
AllowTcpForwarding yes
X11Forwarding yes
X11DisplayOffset 10
X11UseLocalhost yes
```

It is then a good idea to restart the SSH server service.
```bash
sudo systemctl restart sshd
```

Thereafter you should be able to activate a display point.

```bash
xauth generate $DISPLAY . trusted

export XAUTHORITY=$HOME/.Xauthority
```

## Alternate running options


```bash
sudo nvidia-xconfig
sudo reboot

sudo systemctl restart docker

docker run --privileged --gpus=all -e ACCEPT_EULA=Y   -e DISPLAY=$DISPLAY   -v /tmp/.X11-unix:/tmp/.X11-unix   -p 3000:3000 -p 8080:8080 -p 8888:8888   --network=host   --name isaac-sim   -it nvcr.io/nvidia/isaac-sim:4.5.0
```

```bash
docker run --name isaac-sim --entrypoint bash -it --runtime=nvidia --gpus all -e "ACCEPT_EULA=Y" --rm --network=host \
    -e "PRIVACY_CONSENT=Y" \
    -p 3000:3000 -p 8080:8080 -p 8888:8888 \
    -e "HEADLESS=1" \
    -v ~/docker/isaac-sim/cache/kit:/isaac-sim/kit/cache:rw \
    -v ~/docker/isaac-sim/cache/ov:/root/.cache/ov:rw \
    -v ~/docker/isaac-sim/cache/pip:/root/.cache/pip:rw \
    -v ~/docker/isaac-sim/cache/glcache:/root/.cache/nvidia/GLCache:rw \
    -v ~/docker/isaac-sim/cache/computecache:/root/.nv/ComputeCache:rw \
    -v ~/docker/isaac-sim/logs:/root/.nvidia-omniverse/logs:rw \
    -v ~/docker/isaac-sim/data:/root/.local/share/ov/data:rw \
    -v ~/docker/isaac-sim/documents:/root/Documents:rw \
    nvcr.io/nvidia/isaac-sim:4.5.0
```



## Reboot instance

Run a reboot to ensure that the X forwarding features are available.

```bash
sudo reboot
```

## Reconnect to your server after reboot

From the terminal either run the UCloud or Ubuntu (for Strato) connection command.

#### UCloud
```bash
ssh -i ~/.ssh/ucloud_key ucloud@130.225.38.??? -L 3000:localhost:3000 -L 8080:localhost:8080 -L 8888:localhost:8888 -X
```
#### Strato
```bash
ssh -i ~/.ssh/strato_key ubuntu@130.225.37.??? -L 3000:localhost:3000 -L 8080:localhost:8080 -L 8888:localhost:8888 -X
```