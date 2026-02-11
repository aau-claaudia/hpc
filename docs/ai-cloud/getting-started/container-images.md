When we want to launch jobs in a multi-user environment like AI Cloud, we can not install software directly on to the platform, as each project may have different requirements. Instead we must bundle the software into container images, which are stand-alone files into which we can bundle operating system, programs and dependencies. On AI Cloud we use [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html) for this purpose.

We recommend one of three different approaches to the software environment:

## Pre-built container images

A handful of ready-to-launch container images have been made available in: `/home/container`. If there's a container image, you would like us to make available per default - [reach out to us](https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad001310e).

<hr>

## Pull container images from the internet

Head over to our section [Additional guides > Pull containers from the internet](/ai-cloud/additional-guides/download-container-images/).

<hr>

## Build your own container images

Head over to our section [Additional guides > Building your own container image](/ai-cloud/additional-guides/building-your-own-container-image/).

<hr>

Now that you've learned how to obtain containers, you are ready to learn how to [**run jobs :octicons-arrow-right-24:**](ai-cloud/getting-started/file-management)
