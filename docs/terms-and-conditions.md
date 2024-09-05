##### High-Performance Computing systems at AAU are subjects limited by the ever-changing availability of the resources, dependant on the users. Thus, having resources granted does not consequently mean that it is possible to use them right away. Learn about the guidelines and rules to ensure a smooth and efficient computing experience.

!!! info "General principles and definitions of terms"
    As a general principle, the HPC resources are intended to provide additional computational power to AAU researchers, staff and students.

    * _We_ refers to CLAAUDIA and or any other part of the Information Technology Services (ITS) department that is responsible for the provision, maintenance or support of HPC RESOURCES at Aalborg University.
    * _You_ refers to you the user, which may be an individual or other legal person.
    * _HPC_ refers to High Performance Computing resources

!!! info "What are the systems not intended for?"
    * They are not designed for long term storage of research data.
    * They are not designed for production.
    * They are not intended to host long term shared research projects.
  
    **We offer custom solutions**
    If you are in need of larger research project solutions, production virtual machines, or long term storage, please submit a request [CLAAUDIA support team](https://serviceportal.aau.dk/serviceportal?id=emp_taxonomy_topic&topic_id=82a253e8838fc21053711d447daad328).

## 1. Access and Responsibility
The use of HPC RESOURCES requires that you are either a student at, or employed at AAU. You are responsible for any actions taken on these systems including the responsibility for ensuring that access is restricted to the appropriate individuals. Users are responsible for ensuring that their activities align with the guidelines and best practices outlined in the respective documentation of each platform.

Only users authorized via the CLAAUDIA application form may have administrative access to the applied resources.

---

## 2. Fair and Sustainable Use of Platforms
!!! info "Responsibility for following guidelines"
    It is imperative to follow the guidelines for virtual machine usage and resource allocation in AI Cloud, and to always prioritize consideration for fellow researchers when using these resources.

#### 2.1. Strato

Active virtual machines prevent other users from accessing those resources. A virtual machine should only be kept running while it is in current and active use. Active use requires that the machine will be used for research purposes within the coming 48 hours. The setup of each virtual machine is stored on a block device volume, which can be used to new virtual machines “from volumes” at a later stage. All virtual machines that are not in use must be deleted. 
    
[See this guide](/strato/best-practice-guides/delete-and-restart-an-instance-from-the-volume/)

#### 2.2. AI Cloud

Users should be considerate of fellow researchers when allocating jobs in AI Cloud. Jobs should only run if they are actively utilising the computation resources that have been allocated to them. I.e. Interactive jobs should only be used very briefly for development purposes, and no job should allocate any GPU resources that are not used by the job. Users should test their applications for effective utilisation of GPU resources before starting any resource-heavy jobs.

---

## 3. GDPR Compliance and Data Responsibility
!!! info "Adherence to GDPR"
    You must adhere to the General Data Protection Act (GDPR) regulations, e.g. gain consent when needed - links are available below in sections _3.1._ and _3.2._. You are personally responsible for any data stored on any of the HPC RESOURCES.

#### 3.1. GDPR compliance for AAU employees

If you are interested in using HPC RESOURCES in your research work as an AAU employee, you need to go to the GDPR website and [complete and submit a notification of your data collection](https://aaudk.sharepoint.com/sites/persondata-ressourcer/SitePages/Registrations%20og%20reports%20(Online%20forms).aspx?xsdata=MDV8MDF8fDIyNzg2NjJhZjRlNDRmZjFjNmI5MDhkYjc2ZTdmZjdhfGY1ZGJiYTQ5Y2UwNjQ5NmZhYzNlMGNmMTQzNjFkOTM0fDB8MHw2MzgyMzQ1MTA5OTg4MTY0NDF8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxMMk5vWVhSekx6RTVPbUkxTURVMllqYzFNekV3TVRSa09HUmlOVGN3TlRZMlptWXdNRFl3Wm1ZMFFIUm9jbVZoWkM1Mk1pOXRaWE56WVdkbGN5OHhOamczT0RVME1qazROemMxfGNlZTJjNTc4ZGVjZTQ0YzBjNmI5MDhkYjc2ZTdmZjdhfDAxNDc2MWQwZjcxOTQyNGZiMGM1ZmMyOWZiMzY3ZTM2&sdata=cDZlMG5SdmFkUmx3bG9LOTRpYXFjMERiRFpCUmpaSk84WTBGQTBNN2Q5Yz0%3D&ovuser=f5dbba49-ce06-496f-ac3e-0cf14361d934%2CLL08CG%40its.aau.dk&OR=Teams-HL&CT=1687854545431&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMzA1MDEwMDQyMiIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D).

You can find more information at [AAU's website for GDPR related info for employees](https://aaudk.sharepoint.com/sites/gdpr-for-researchers).

#### 3.2. GDPR compliance for AAU students

As a student you are data controller for the personal data or information that you process while using the HPC RESOURCES, and you have an independent responsibility to comply with the GDPR regulations.

Please visit [AAU's website for GDPR related info for students](https://aaudk.sharepoint.com/sites/GDPR-for-students) and read it carefully. 

---

## 4. Confidentiality and Sensitivity of Data

AI Cloud and virtual machines on Strato or UCloud must not be used to store confidential and/or sensitive data.

!!! info "UCloud projects with sensitive data"
    Please read the [procedure for working with sensitive data on UCloud](/ucloud/how-to-access/) that has been agreed upon with the Department of Grants and Contracts. 

---

## 5. Deletion of Accounts and Data
With regards to data stored on any of the HPC RESOURCES, it will automatically be deleted if the user is no longer registered as an active student or staff member.

#### 5.1. Deletion of Strato and AI Cloud Student Accounts and Data Extraction Responsibilities

All Strato and AI Cloud student accounts will be deleted at the end of each semester (01 February, and 01 August). Students are responsible for the extraction or saving of all data that is of value to them prior to these dates.

---

## 6. Prohibited Usage and Consequences
HPC RESOURCES may not, under any circumstances, be used for any purpose outside the scope of student or staff research, teaching or administrative functions. Any misuse of the HPC RESOURCES will result in an immediate and permanent ban of the use of any HPC RESOURCES. Criminal or unlawful activity will be reported to the appropriate authorities.

---

## 7. Service Windows

!!! info "What is a service window?"
    A service window is a scheduled time when maintenance work is done on AAU's HPC systems that disrupt normal use. This maintenance can make the system temporarily unavailable or some resources unusable. AAU informs users in advance so they can plan their work around it. Once it's done, the system returns to normal and users can resume their work.

    * **Scheduled service windows:** Four entire days each year are reserved for security updates. 
    * **Planned service windows:** Occur when sub-system maintenance is required between the existing scheduled service windows.
    * **Emergency service windows:** All systems may be subject to emergency service windows. In the case of an accute emergency, all users will be informed of the nature and expected duration of the window.

#### 7.1. Scheduled service windows for Strato and AI Cloud

Four entire days each year are reserved for security updates. This may require that all hosts are restarted. Users should expect that all virtual machines will be shut off during this service window and the job queue will be cleared.

**Proposed schedule of service windows (these dates are subjects to change):**

**2024** 17/09, 03/12

**2025** 11/02, 13/05, 16/09, 02/12

**2026** 10/02, 12/05, 15/09, 01/12

**2027** 09/02, 11/05, 14/09, 30/11

**2028** 08/02, 09/05, 12/09, 28/11

Check [ServiceInfo.dk](https://serviceinfo.dk/login.php) to learn more about current service windows

#### 7.2. Right to maintenance and modification of systems

We reserve the right to periodically shut off entire systems for maintenance or security purposes. These systems require maintenance and updates at regular intervals, and we commit, where possible, to provide **a minimum of two calendar weeks** warning before any shut down period commences.

We reserve the right to modify, redesign, disable or remove any of the existing services. Where possible, users will be notified of major modifications to the existing systems **a minimum of three calendar months** before these changes are implemented. Updates, upgrades and shutdown periods are not considered major modifications.

#### 7.3. Communication policy around service windows

=== "Scheduled IT disruptions"

    1.  **Service window date reminder email**
        *   Sent to all users of Strato, AI Cloud
        *   Dispatched 6-8 weeks before service window
    
    2.  **Orientation email about service window**
        *   Sent to the internal CLAAUDIA and ITS management list
        *   Dispatched 2 weeks before service window

    3.  **Notice of service window pre arranged on [ServiceInfo.dk](https://serviceinfo.dk/login.php)**
        *   Put on 1 week before the service window.

    4.  **Orientation email to system owner forum, key stakeholders or research group leaders**
        *   Dispatched 2 weeks before service window.

    5.  **Orientation email to all users**
        *   Dispatched 1 week before service window.

    6.  **Completion of planned work changed on [ServiceInfo.dk](https://serviceinfo.dk/login.php)**
        *   Changed on first working day after the service window.

=== "Planned IT disruptions"

    7.  **Service window date reminder email**
        *   Sent to all users of Strato, AI Cloud
        *   Dispatched 6-8 weeks before service window

    8.  **Orientation email about service window**
        *   Sent to the internal CLAAUDIA and ITS management list
        *   Dispatched 4 weeks before service window

    9.  **Notice of service window pre arranged on [ServiceInfo.dk](https://serviceinfo.dk/login.php)**
        *   Put on 2-3 weeks before the service window

    10. **Orientation email to system owner forum, key stakeholders or research group leaders**
        *   Dispatched 3 weeks before service window.

    11. **Orientation email to all users**
        *   Dispatched 2 weeks before service window.

    12. **Completion of planned work changed on [ServiceInfo.dk](https://serviceinfo.dk/login.php)**
        *   Changed on first working day after the service window.

=== "Emergency communication timeframes"

    13. **After 1st hour**
        *   Out of order notice posted on [ServiceInfo.dk](https://serviceinfo.dk/login.php).

    14. **Unresolved problems at end of day**
        *   Update on status - even if no change has occurred.

    15. **After problem resolution**
        *   The issue will be marked as resolved on [ServiceInfo.dk](https://serviceinfo.dk/login.php)

---

## 8. Loan of physical equipment

#### 8.1. Responsibility and Liability for Physical Equipment Loaned by AAU

With regards to physical equipment, you are solely responsible for damage to or loss of the equipment during the loan period. In the event of damage, AAU determines whether the equipment shall be repaired or replaced. If AAU determines that it is not viable to repair the equipment or if the equipment is lost, you shall compensate AAU for the value of the equipment.

If AAU determines that the equipment can be repaired, you shall pay for the repair.

#### 8.2. Ethical Use and Legal Responsibility for Physical Kits with Cameras

Physical kits are delivered with a camera. Please act ethically and refrain from using them in places where other people may consider it unpleasant or annoying. You are responsible for acting according to the legislation of the country in which you use the equipment and the Danish legal and ethical rules.

---

## 9. Updates to Terms and Conditions
We reserve the right to make periodic changes to these terms and conditions, and commit to inform users of the changes made.