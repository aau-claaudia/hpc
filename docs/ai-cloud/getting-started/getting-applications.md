To run applications on AI Cloud, you must use container images. On AI Cloud we use the container software, [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html).

!!! info "What is a container image?"
    A container image is a static, portable file that contains all the components needed to run a piece of software, including the code, runtime, system tools, libraries, and settings.

## Download container images
You can access a wide array of container images by visiting [NVIDIA GPU Cloud (NGC)](https://catalog.ngc.nvidia.com/) and exploring whether NVIDIA provides a container image for the application you require. Refer to our guide [here](../additional-guides/download-container-images.md) for detailed instructions.

<hr>

## Build your own container images
You also have the flexibility to create your own container images tailored to your specific environment requirements. Refer to our guide on [building your own container image](../additional-guides/building-your-own-container-image.md).

<br>

Now that you know how to obtain applications, let's delve into [**running jobs :octicons-arrow-right-24:**](running-jobs.md)