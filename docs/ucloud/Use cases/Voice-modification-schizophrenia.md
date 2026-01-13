# Use case: How UCloud supports research in voice modification for virtual reality therapy for people with schizophrenia

*How does research create impact in the real world?* *In this use case, we explore how research into voice-modification algorithms can make a positive difference for people with schizophrenia — and how the High Performance Computing platform UCloud helps support this research.*

<div style="display: flex; flex-direction: column; align-items: center;">
  <img src="/assets/img/UCloud/Use_case_voice-modification-schizophrenia.png" alt="Heka VR virtual reality therapy session environment" class="standard_image_width centered_image"/>
  <span class="image-caption" style="margin-top: 0.5em;">Photo: <a href="https://hekavr.com/" target="_blank">Heka VR</a></span>
</div>
<br>

Anders R. Bargum is a PhD student at CREATE – the Institute of Architecture and Media Technology at Aalborg University, where he is currently completing an industrial PhD in collaboration with the company [Heka VR](https://hekavr.com/). His project focuses on the development of an AI-based audio plugin for virtual reality–based therapy for people with schizophrenia. Through an exposure-therapy approach, the solution helps patients better manage the voices they experience in their everyday lives by gradually exposing them to these voices in controlled settings.

The software platform, Heka, creates a virtual reality environment in which the patient interacts with a therapist. During therapy, an avatar is used that can be designed to match the voice and character experienced by the patient. The voice's characteristics, including timbre, tone, expression, and visual appearance, are adjusted collaboratively by the therapist and the patient and form part of the exposure-therapy process.

A key feature of the platform is the ability to modify the therapist's voice in real time while the conversation is taking place. The therapist speaks into a microphone, after which the voice is processed and transformed by the system and perceived by the patient as the voice and character used in the therapy. This real-time voice-modification algorithm constitutes the core of Anders' research project.

## The technology

In his research, Anders works with AI and deep learning, developing his own models and algorithms for voice transformation. While several existing technologies are capable of producing realistic synthetic voices, they are typically unable to adapt dynamically in real time. Anders' research addresses this limitation by developing models that can continuously modify voices during live interaction.

The neural networks used in the project are trained over extended periods on large volumes of voice data, based on specific voice parameters and auditory attributes. The models learn to analyse and reconstruct voices so they can subsequently be used to create smooth and controlled voice transformations in real time. At present, the project has reached a stage where voices can be controlled and generated in real time with low latency, resulting in a concrete and usable product. At the same time, the therapy approach behind Heka is increasingly being implemented in practice and is now used in both public and private treatment contexts.

## UCloud provides access to the necessary computing power

The development and training of the AI and deep learning models place significant demands on computing power and access to GPU resources. The neural networks are trained over several days and require substantial memory and computational capacity—requirements that cannot realistically be met using local computers alone.

Here, the High Performance Computing platform UCloud plays a central role in Anders' research process. Through UCloud, he gains access to powerful GPUs, large memory capacity, and a scalable development environment, enabling him to train and test advanced voice models much more efficiently.

> "Access to powerful GPUs means that I can speed up training and scale my experiments much faster than would be possible with the limited and relatively modest graphics cards typically available locally at the university."  
> — Anders R. Bargum, PhD student, Aalborg University

In practice, Anders works via virtual machines (VMs) on UCloud. A virtual machine is a flexible, cloud-based computing environment where the exact amount of computing power, memory, and GPU resources required for a given project can be configured. This approach allows computations to be scaled up and down quickly, ensuring optimal support for both development and training processes.

## Get started with UCloud
To begin using UCloud and access scalable high-performance computing resources for your research, simply log in to [UCloud](https://cloud.sdu.dk/). If you are planning a larger project or have advanced requirements, visit the [How to access](/ucloud/how-to-access/) page for detailed instructions on applying for additional resources and setting up your environment. If you are in doubt UCloud can also support your research, feel free to reach out to us on the [serviceportal](https://aau.service-now.com/serviceportal?id=emp_taxonomy_topic&topic_id=82a253e8838fc21053711d447daad328) to learn more about your options and the support available.
