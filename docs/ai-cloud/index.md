# AI Cloud

##### AI Cloud is Aalborg University's primary GPU resource, tailored for machine learning and parallel processing tasks. It leverages containers for flexibility, providing an efficient platform for research using GPU acceleration.

!!! info "What is AI Cloud?"

    AI Cloud consists of a powerful cluster of GPU servers, designed for running jobs that require containers. This approach offers significant flexibility, allowing users to tailor their environment based on their specific project needs.

    To access AI Cloud, users connect through a terminal on their local machine, logging into a front-end node. From there, files are managed, and jobs are submitted to a queueing system, which assigns tasks to available GPU nodes. Since the platform is shared among multiple users, software isn't installed directly on the system. Instead, containers with all required libraries are used to ensure smooth execution.

    [Apply for resources](/ai-cloud/how-to-access/){ .md-button .md-button--primary .not-max-width}

## Introduction to AI Cloud

##### Basic information and instructions for first-time users of AI Cloud.

<div class="grid cards grid-three grid-button-bottom" markdown>

<!--
Icons can be searched and found here:
https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/ (best, is to use the ones starting with material)
-->

- :material-key-outline: __How to access__ 

    ---

    Learn how to access AI Cloud.
  
    [How to access](/ai-cloud/how-to-access/){ .md-button .md-button--primary }

- :material-clipboard-check-multiple-outline: __Guides for AI Cloud__ 

    ---

    Learn the basics on how to use AI Cloud.

    [Guides for AI Cloud](/ai-cloud/getting-started/){ .md-button .md-button--primary }

- :material-lan: __System Overview__ 

    ---

    Get an overview of AI Cloud's capabilities.

    [System Overview](/ai-cloud/system-overview/){ .md-button .md-button--primary }

</div>


<br> <!-- Just a little break -->

<div class="grid" markdown>

=== "Common use"
    * Training deep learning models for image classification and recognition tasks.
    * Accelerating natural language processing with large-scale language models.
    * Running high-resolution visual simulations with GPU-powered parallel computing.
    * Performing video analysis for object detection and motion tracking in real-time.

=== "Recommended skills & knowledge"

    Operating the AI Cloud involves learning how to use the queueing mechanism and understanding the containerisation concept. It's also useful to be able to navigate a Linux terminal environment.


![Image title](/assets/img/ai-cloud/ai-cloud-hero.webp)

</div>

## Learn the Key Features

##### Discover the essential features of AI Cloud.


<div class="grid cards grid-three" markdown>

<!--
Icons can be searched and found here:
https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/ (best, is to use the ones starting with material)
-->


-   :material-speedometer:{ .lg .middle } __High-Performance GPU Cluster__

    ---
    
    AI Cloud provides access to a cluster of powerful NVIDIA GPUs, enabling the efficient processing of large datasets and complex models.

-   :material-package-variant-closed:{ .lg .middle } __Containerization for Flexibility__

    ---
    
    Users operate within containerized environments, ensuring that software dependencies are consistently maintained across different computational nodes.

-   :material-human-queue:{ .lg .middle } __Workload Management__

    ---
    
    Jobs are managed via a queueing mechanism (Slurm), allowing for effective distribution across the available GPU resources.

-   :material-server:{ .lg .middle } __Optimized for Parallel Processing__

    ---
    
    AI Cloud is specifically designed to handle large-scale, parallelized tasks, making it ideal for simulations, deep learning, and other high-throughput applications.

-   :material-file-document-multiple-outline:{ .lg .middle } __Comprehensive Documentation__

    ---
    
    Extensive resources are available to guide users through the setup and usage of AI Cloud, with a focus on accessibility for beginners.

-   :material-account-group-outline:{ .lg .middle } __Collaboration-Friendly Environment__

    ---
    
    AI Cloud supports file sharing and collaborative work among multiple users, facilitating teamwork on complex projects and enabling seamless integration of contributions from different researchers.

</div>

<br> <!-- Just a little break -->

<!--
## Use cases

##### Find out how AI Cloud can be effectively utilized in certain computing practices.

<div class="grid cards grid-three" markdown>

-   __Transformer methods with large amount of data__

    ---

    AI Cloud might be a relevant choice when working with transformer methods in deep learning, and when the analysis involves a great amount of data– particularly image or video data. In this scenario, a good practice would be to test your jobs locally on a smaller scale, and involve the HPC afterwards, as it might take a long time to finish – depending how large is the data set you are working on.

-   __Electricity price forecasting__

    ---

    Integrate machine learning in your project to identify patterns in electricity price forecasting and develop large models with the use of AI Cloud's access to a powerful GPU, which provides processing power capable of dealing with large and complex datasets.

-   __Training large language models__

    ---

    Train large language models thanks to the powerful GPU which AI Cloud provides. You can accelerate various cloud workloads in parallel data processing and develop models for human-robot interaction or image classification. Integrate large datasets in your projects and train your models on HPC servers.

-   __Object recognition__

    ---

    Consider involving AI Cloud for training large neural networks for object recognition. The powerful GPU allows for achieving high-performance processing by integrating parallel computing into your project, which will also make the training process faster. With AI Cloud, you can integrate large data sets into your analysis and run short sampling tests to make sure the further processes are correct, fast, and convenient.

-   __Running atomistic simulations__

    ---

    Consider involving AI Cloud if in your project you are planning to run atomistic simulations. Powerful GPU processing is relevant when applying various methods for simulating materials and minerals on an atomic level, which might require running parallel simulations or many related scientific computing applications - which are supported by AI Cloud.

</div>
-->

<!-- <br> --> <!-- Just a little break -->

## Important Information

!!! info "Not for confidential or sensitive data"
    With AI Cloud you are only allowed to work with public or internal information according to [AAU’s data classification model](https://www.security.aau.dk/data-classification){target="_blank} (classified as levels 0 and 1, respectively).

    If you would like to work with confidential or sensitive data (classified as levels 2 and 3), then we support another HPC platform called [UCloud](/ucloud/).

!!! info "Not suitable for CPU-only computational tasks"
    The powerful GPU processors allow users to process large datasets much more efficiently than would be the case with pure CPU processing - given that your application can be parallelised in a GPU compatible manner. At the same time, the AI Cloud platform is not designed for CPU-only computational tasks, and we have alternative recommended platforms, such as [UCloud](/ucloud/) or [Strato](/strato/) for those needs.

!!! info "Review the terms and conditions"
    Before getting started, take a few moments to review the [terms and conditions](/ai-cloud/terms-and-conditions/) of using AI Cloud, and don't hesitate to [reach out](https://serviceportal.aau.dk/serviceportal?id=emp_taxonomy_topic&topic_id=82a253e8838fc21053711d447daad328){target="_blank} to our support team if you have any questions or concerns.