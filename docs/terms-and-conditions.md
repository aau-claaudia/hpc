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
    Please read the [procedure for working with sensitive data on UCloud](/ucloud/terms-and-conditions/#procedure-for-working-with-sensitive-data-on-ucloud-projects) that has been agreed upon with the Department of Grants and Contracts. 

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


## Appendix
### *Procedure for working with sensitive data on UCloud projects*

CLAAUDIA, Aalborg University

2023-10-10

v1.0

As a user on the UCloud platform you have a workspace called "My workspace".

It is also possible to apply for a separate "Project" workspace on the
UCloud platform. Projects on UCloud allow for collaboration with
separate storage, compute resources and management of user rights and
responsibilities on the UCloud platform.

**The project environment is required for the following types of work on
UCloud:**

1.  For employed researchers at AAU (VIP)

    a.  Sensitive data: All work on the UCloud platform that involves
        research data in classification levels 2 or 3.
a
2.  All users

    a.  GPU access on UCloud: All access to GPU resources on UCloud
        require a project. (Only data classification levels 0 and 1)

    b.  Additional compute resources that are allocated out of the AAU
        pool of UCloud resources.

UCloud users at AAU must be familiar with the details of
the following codes of conduct and policies:

1.  [The Danish Code of Conduct for Research
    Integrity](https://ufm.dk/en/publications/2014/the-danish-code-of-conduct-for-research-integrity)

2.  [The AAU Policy for Research Data
    Management](https://www.ansatte.aau.dk/regler/forskning/politik-for-handtering-af-forskningsdata)

3.  [The AAU policies with regards to
    GDPR](https://aaudk.sharepoint.com/sites/persondata/SitePages/In%20English.aspx)
    (Available in English for
    [researchers](https://aaudk.sharepoint.com/sites/gdpr-for-researchers)
    (VIP),
    [teachers](https://aaudk.sharepoint.com/sites/gdpr-for-teachers)
    (VIP) and
    [students](https://aaudk.sharepoint.com/sites/GDPR-for-students);
    Only in Danish for [administration (TAP)
    employees](https://aaudk.sharepoint.com/sites/persondata-administration))

4.  [The AAU data management
    recommendations](https://www.researcher.aau.dk/guides/research-data/data-management)

These policies cover the general rules all researchers (and students and
TAP staff for point 3.) should abide by with regards to what kind of
data may be kept, for how long, whether data can be re-used or recycled,
and how long it should be archived for, etc.

**Sensitive data: Registration of research projects at Grants and
Contracts (Excludes students)**

For researchers at AAU, working with sensitive personal data requires
that you register your research project with "Grants and Contracts" by
completing the [digital form that matches your role in relation to the
data, for example Data Controller or Data
processor](https://aaudk.sharepoint.com/sites/persondata-ressourcer/SitePages/Registrations%20og%20reports%20(Online%20forms).aspx).

**Data processing agreement between AAU and the EScience center at SDU**

> For AAU users, data analysis and processing may then take place on the
> UCloud platform according to the data
> processing agreement between AAU and EScience center at SDU.

**Steps required to working with projects on the UCloud platform**

1.  Identify the data classification of your data by reviewing the [AAU
    data classification
    model.](https://aaudk.sharepoint.com/sites/ForskIT/Delte%20dokumenter/General/01%20-%20Administration/03%20-%20Policies%20and%20procedures/DeiC%20Interactive%20HPC/i.%09https:/www.security.aau.dk/dataclassification/model)
    ([Classify your data at Aalborg University - Aalborg University
    (aau.dk)](https://www.security.aau.dk/data-classification))

2.  If you are a researcher, and working with data classifications 2 or
    3, you must register a research project with Grants and Contracts
    using [the relevant registration
    form.](https://aaudk.sharepoint.com/sites/persondata-ressourcer/SitePages/Registrations%20og%20reports%20(Online%20forms).aspx)

    a.  Once you have registered your research activity at Grants and
        Contracts, you will get a receipt that contains a "WorkZone case
        number" (To be included in your UCloud project application).

3.  Students cannot register projects with Grants and Contracts. As a
    student you are personally responsible for any data you collect. You
    must ensure that you comply with [GDPR regulations for
    students](https://aaudk.sharepoint.com/sites/GDPR-for-students).

    
4.  All applicants for projects on UCloud must complete the [CLAAUDIA
    application form for DeiC Interactive HPC resources](https://forms.office.com/e/8Khbr1TJGC).

5.  Once approved, you will receive a UCloud project
    number, and you must [apply for a project in the UCloud
    Interface](https://docs.cloud.sdu.dk/tutorials/tutorial3.html#create-a-project),
    including the resources that you had approved in the CLAAUDIA
    application. (You can apply for additional resources later if
    needed.)

    a.  As project applicant you will be the Principal Investigator for
        the project, and you should be aware of your [roles and
        responsibilities.](https://docs.cloud.sdu.dk/guide/project-overview.html#member-roles)

    b.  If the user is a student, then their supervisor for the student
        project must apply for the project, and so must assume the role
        of Principal Investigator.

    c.  The project must include both the **DeiC project number**, and
        the **Grants and Contracts** reference number in the "Comments"
        field of the UCloud project application.

    d.  Once your project is approved, you will get access to project
        storage (Drive(s)) on UCloud that is separate from your "My
        Workspace" storage. No sensitive data may be stored in the "My
        workspace" drives.

6.  Adding data to the UCloud platform:

    a.  Any data added to the project should be in a project folder and
        this must be marked according to the level of data sensitivity,
        as described in the [AAU data classification
        model](https://aaudk.sharepoint.com/sites/ForskIT/Delte%20dokumenter/General/01%20-%20Administration/03%20-%20Policies%20and%20procedures/DeiC%20Interactive%20HPC/i.%09https:/www.security.aau.dk/dataclassification/model).

        i.  On the UCloud platform the corresponding classifications are
            as follows: 

            1.  **AAU Level 0:** Public information = **UCloud:**
                Inherit.

            2.  **AAU Level 1:** Internal information = **UCloud:**
                Private.

            3.  **AAU Level 2:** Confidential information - **UCloud:**
                Confidential.

            4.  **AAU Level 3:** Sensitive information - **UCloud:**
                Sensitive. (Only permitted to be added to your
                registered and approved project folder.) Sensitive data
                may **NOT** be added to My Workspace.

7.  **Collaboration on UCloud within projects:** Fellow AAU persons

    a.  Only persons named in the project registered with Grants and
        Contracts may be added to the UCloud project.

8.  **Collaboration on UCloud within projects:** Persons from outside
    AAU

    a.  The collaborator's employer must have a Data Processing
        agreement with SDU (SDU are hosting UCloud), or

        i.  Where there is an agreement of shared data responsibility
            (Agreement on Joint data controlling), that states that it
            is agreed to use DeiC/SDU as the data processor, then it is
            sufficient that AAU has an existing data processing
            agreement with DeiC/SDU. In these cases AAU will be
            responsible for the data processing agreement with DeiC/SDU.

    b.  If this is not the case, you cannot invite the collaborator
        inside the project folder in UCloud.

    c.  No person(s) that are not included in the data processing
        agreement or the agreement on joint data controlling may be
        invited to the project.

9.  UCloud project members and roles should be set appropriately.

    a.  Project "admins" can see all member files by activating the
        "show member files" option. The Principal Investigator is
        responsible for ensuring that all [roles and
        responsibilities](https://docs.cloud.sdu.dk/guide/project-overview.html#member-roles)
        are properly assigned.

10. Read and write privileges on UCloud

    a.  If collaborators are only allowed read or write to specific
        parts of the data / dataset, you will need to follow the
        following steps:

        i.  Within the project, you will need to create a new "Drive".
            (As drives are the only level to which you can specify read
            and write permissions.)

            1.  Only project "admins" can create new drives within a
                project.

        ii. Name the drive and then click the "..." button to modify the
            permissions. Then choose the permissions (None / Read /
            Write).

11. Permitted applications and uses

    a.  All applications except those labeled as "Virtual Machines" may
        be used for work on all data.

    b.  Virtual Machine applications may only be used for data
        classified as level 0 and 1.

12. On completion the project 

    a.  All data on the UCloud platform should be deleted.

    b.  The project should then be archived with a final date that
        corresponds with the GDPR notification with 'Grants and
        Contracts'.

    c.  All files in trash folders should be permanently deleted.

    d.  All complete data sets and metadata should be stored in a data
        repository in accordance with [The AAU Policy for Research Data
        Management](https://www.handbook.aau.dk/document/?contentId=402570).
        As of 2023-January, AAU
        [DataDeposit](https://www.researcher.aau.dk/guides/research-data/data-management/data-publishing)
        as a local archiving solution, while a national solution is
        under development.
