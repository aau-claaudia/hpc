When we want to launch jobs in a multi-user environment like AI Cloud, we can not install software directly on to the platform, since every project has different requirements. Instead we must bundle the software into container images, which are stand-alone files into which contain all the dependencies. On AI Cloud we use the container framework [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html) for this purpose.

## How to get containers

We recommend one of three different approaches to the software environment:

### Use a pre-built container image

A handful of ready-to-launch container images have been made available in: `/home/container`. If there's a container image you would like us to make available per default - [reach out to us](https://serviceportal.aau.dk/serviceportal?id=sc_cat_item&sys_id=a05e2fb4c3434610f0f3041ad001310e).

### Pull container images from the internet

Head over to our section [Additional guides > Pull containers from the internet](/ai-cloud/additional-guides/download-container-images/).

### Build your own container images

Head over to our section [Additional guides > Building your own container image](/ai-cloud/additional-guides/building-your-own-container-image/).

<hr>

Now that you've learned how to obtain containers, you are ready to learn how to [**run jobs :octicons-arrow-right-24:**](ai-cloud/getting-started/file-management)
