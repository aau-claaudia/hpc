1. **Go to Strato web interface:** Strato servers are managed via the Strato web interface, to log go to the [Strato web interface](https://strato-new.claaudia.aau.dk/auth/login/?next=/project/){target="_blank} go to with your favourite browser.
2. **Authenticate:** Ensure the Authenticate Using is set to WAYF and click Connect. You will be redirected to signon.aau.dk/... 
3. **Log in:** You must login with your Aalborg University credentials, click LOGIN and now you should be redirected to the cloud dashboard.
4. **SSH key:** To access your server you will need to use an SSH key, and you can follow the step-by-step instructions in the [Getting started](/strato/getting-started/before-you-begin/) guide.

## Strato Projects: Apply for additional quota
Strato Projects allow users to apply for additional quota to access additional processing capacity. 

GPU resources are limited and users are expected to follow a strict policy of deleting all GPU instances when not actively using the GPU. New instances can be very quickly created from existing volumes (boot disks). 

<!-- Strato Projects are available primarily to all researchers, and - if there are sufficient resources available - to students that are supporting researchers, and, finally, to student research projects. Each project requires the completion of a project request form.
 -->

Strato Projects are only available to all researchers. Each project requires the completion of a project request form.


## Important Information

!!! info "Not for confidential or sensitive data"
    With Strato you are only allowed to work with public or internal information according to [AAU’s data classification model](https://www.security.aau.dk/data-classification){target="_blank} (classified as levels 0 and 1, respectively).

    If you would like to work with confidential or sensitive data (classified as levels 2 and 3), then we support another HPC platform called [UCloud](/ucloud/).

!!! info "There are no back-ups"
    It is important that you keep your data backed-up outside of the platform. Data is not backed up on any of our HPC platforms, while the data is kept safe through security copies, all copies are simultaneously updated when you make changes, and all changes are permanent.

<!-- !!! info "Student GPU access is limited to 1 NVIDIA T4 instance"
    Interactive use of larger GPU resources is limited to the [UCloud](/ucloud/) platform for Students. -->

!!! info "Review the terms and conditions"
    Before getting started, take a few moments to review the [terms and conditions](/strato/terms-and-conditions) of using Strato, and don't hesitate to [reach out](https://serviceportal.aau.dk/serviceportal?id=emp_taxonomy_topic&topic_id=82a253e8838fc21053711d447daad328){target="_blank} to our support team if you have any questions or concerns.

!!! info "GPU Limitations - Multi-GPU instances must be benchmarked"
    The GPU cards on Strato are not connected with high-speed interconnects. This means that unless you know exactly how to separate your processes across the GPU cards, there is no performance benefit to launching virtual machines with multiple GPU cards.
    
    If you are going to use a machine with multiple GPUs you must benchmark the performance of your code by resizing between single and multiple GPU flavours and comparing the performance.


[Access and complete the project request form for Strato Projects](https://forms.office.com/pages/responsepage.aspx/?id=Sbrb9QbOb0msPgzxQ2HZNEdKMbCNz_9Lom8_yaZURCNUNkE1NEYxMkw4UllRVllZTkFLVjRNUzJUTCQlQCN0PWcu){target="_blank}