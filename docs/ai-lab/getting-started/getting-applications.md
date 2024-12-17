To run applications on AI-LAB, you need to use container images in most instances. On AI-LAB we use the container software, [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html).

!!! info "What is a container image?"
    A container image is a static, portable file that contains all the components needed to run a piece of software, including the code, runtime, system tools, libraries, and settings.

In general, there are 3 ways to get containers:

## 1. Pre-downloaded container images
The most straightforward method to acquire container images on AI-LAB is by accessing pre-downloaded container images stored in the `/ceph/container` directory. We aim to consistently update these container images to the latest versions. Some of the containers includes `Python`, `PyTorch`, and `TensorFlow` containers.

You can check which container images exist in the `/ceph/container` directory on AI-LAB with `ls`:

```console
ls /ceph/container
```

To use the container images, you can use them straight from the `/ceph/container` directory by referencing the absolute path, e.g.:

```
/ceph/container/pytorch/pytorch_24.09.sif
```

<hr>

## 2. Download container images
Alternatively, you can download a wide range of pre-built container images by visiting websites such as:

* [https://catalog.ngc.nvidia.com/](https://catalog.ngc.nvidia.com/)
* [https://hub.docker.com/](https://hub.docker.com/)

Refer to our guide [here](../additional-guides/download-container-images.md) for detailed instructions on how to download the container images.

<hr>

## 3. Build your own container images
You also have the flexibility to create your own container images tailored to your specific environment requirements. Refer to our guide on [building your own container image](../additional-guides/building-your-own-container-image.md).

<hr>

!!! info "Extending container images with Python packages"
    In many cases, you will need to add additional Python packages or packages to an existing container image. The easiest way to do this, is using a virtual environment. [This guide](https://hpc.aau.dk/ai-lab/additional-guides/adding-python-packages-via-virtual-environment/) outlines the steps to create and utilize a virtual environment within your directory on AI-LAB.

<br>

Now that you know how to obtain applications, let's delve into [**running jobs :octicons-arrow-right-24:**](running-jobs.md)