To run applications on AI-LAB, you must use container images. On AI-LAB we use the container software, [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html).

!!! info "What is a container image?"
    A container image is a static, portable file that contains all the components needed to run a piece of software, including the code, runtime, system tools, libraries, and settings.

## Pre-downloaded container images
The most straightforward method to acquire container images on AI-LAB is by accessing pre-downloaded container images stored in the `/ceph/container` directory. We aim to consistently update these container images to the latest versions.

You can check which container images exist in the `/ceph/container` directory on AI-LAB with `ls`:

```console
ls /ceph/container
```

To use the container images, you can use them straight from the `/ceph/container` directory by referencing the absolute path, e.g.:

```
/ceph/container/pytorch/pytorch_24.09.sif
```


<hr>

## Download container images
Alternatively, you can access a wide array of container images by visiting [NVIDIA GPU Cloud (NGC)](https://catalog.ngc.nvidia.com/) and exploring whether NVIDIA provides a container image for the application you require. Refer to our guide [here](../additional-guides/download-container-images.md) for detailed instructions.

<hr>

## Build your own container images
You also have the flexibility to create your own container images tailored to your specific environment requirements. Refer to our guide on [building your own container image](../additional-guides/building-your-own-container-image.md).

<br>

Now that you know how to obtain applications, let's delve into [**running jobs :octicons-arrow-right-24:**](running-jobs.md)