
## Who can access?
All Aalborg University users automatically have access to UCloud and can simply log in using their WAYF credentials (university logon credentials). This gives you access to a fairly substantial starting quota that can be used in the standard web app environment. This is also the quickest and most user-friendly way to access HPC as a first-time user.

[Log in to UCloud](https://cloud.sdu.dk/app/dashboard){target="_blank}


!!! info "UCloud users at AAU must be familiar with the details of the following codes of conduct and policies:"
    * [The Danish Code of Conduct for Research Integrity](https://ufm.dk/en/publications/2014/the-danish-code-of-conduct-for-research-integrity)
    * [AAU Policy for Research Data Management](https://www.ansatte.aau.dk/regler/forskning/politik-for-handtering-af-forskningsdata)
    * [AAU policies for GDPR](https://aaudk.sharepoint.com/sites/persondata/SitePages/In%20English.aspx)
    * [AAU data management recommendations](https://www.researcher.aau.dk/guides/research-data/data-management)

    These policies cover the general rules all researchers (and students and TAP staff for GDPR) should abide by with regards to what kind of data may be kept, for how long, whether data can be re-used or recycled, and how long it should be archived for, etc.

## UCloud Projects: Apply for additional quota
It is also possible to apply for a separate **Project** workspace or environment on the UCloud platform.
The project environment allows collaboration with separate storage, computer resources, and management of user rights and responsibilities on the UCloud platform.

!!! info "The project environment is required for the following types of work on UCloud"

    **For researchers employed at AAU (VIP):**
    
    Sensitive data: All work on the UCloud platform that involves research [data in classification levels 2 or 3](https://www.security.aau.dk/data-classification).
    
    **For all users:**
    GPU access on UCloud: All access to GPU resources on UCloud require a project (Only [data classification levels 0 and 1](https://www.security.aau.dk/data-classification)). Additional computer resources that are allocated out of the AAU pool of UCloud resources.


#### How to get access to a UCloud Project?
Creating a project requires you to the follow these steps:

1.  **Identify the data classification** of your data by reviewing the [AAU data classification model](https://www.security.aau.dk/data-classification).
2.  **If you are a researcher**, and working with data classifications 2 or 3, you must register a research project with Grants and Contracts using the relevant [registration form](https://aaudk.sharepoint.com/sites/persondata-ressourcer/SitePages/Registrations%20og%20reports%20(Online%20forms).aspx).
    *   Once you have registered your research activity at Grants and Contracts, you will get a receipt that contains a WorkZone case number. This case number should be included in your UCloud project application.
    *   If your research is governed by separate data processing or subordinate data processing agreement, the WorkZone case number containing the contract details should be recorded in the UCloud platform. There is a standard data processing agreement between AAU and the EScience centre at SDU. This point is only applicable if the standard agreement is not applicable.
3.  **If you are a student**, you cannot register projects with Grants and Contracts. As a student you are personally responsible for any data you collect. You must ensure that you comply with [GDPR regulations for students](https://aaudk.sharepoint.com/sites/GDPR-for-students).
    *   To assist with GDPR compliance we recommend that students follow the same procedures as researchers.

4.  **All applicants for projects on UCloud** must complete the [CLAAUDIA application form for DeiC Interactive HPC resources](https://forms.office.com/pages/responsepage.aspx?id=Sbrb9QbOb0msPgzxQ2HZNEdKMbCNz_9Lom8_yaZURCNUQVZUQVRXSFVYODBZQkNZWVRYM1lEUEFYTSQlQCN0PWcu).
5.  **Once approved**, you will receive a DeiC Interactive HPC project number, and you must [apply for a project in the UCloud Interface](https://docs.cloud.sdu.dk/tutorials/tutorial3.html#create-a-project), including the resources that you had approved in the CLAAUDIA application. (You can apply for additional resources later if needed.)
    *   As project applicant you will be the Principal Investigator for the project, and you should be aware of your [roles and responsibilities](https://docs.cloud.sdu.dk/guide/project-overview.html#member-roles).
    *   If the user is a student, then their supervisor for the student project must apply for the project, and so must assume the role of Principal Investigator.
    *   The project must include both the DeiC Interactive HPC project number, and the relevant WorkZone case number in the correct fields in the UCloud application.
    *   Once your project is approved, you will get access to project storage (Drive(s)) on UCloud that is separate from your “My Workspace” storage. No sensitive data may be stored in the “My workspace” drives.
6.  **Adding data to the UCloud platform:** Any data added to the project should be in a project folder and this must be marked according to the level of data sensitivity, as described in the [AAU data classification model](https://www.security.aau.dk/data-classification). On the UCloud platform the corresponding classifications are as follows:  
    *   AAU Level 0: Public information = UCloud: Inherit.
    *   AAU Level 1: Internal information = UCloud: Private.
    *   AAU Level 2: Confidential information - UCloud: Confidential.
    *   AAU Level 3: Sensitive information - UCloud: Sensitive. (Only permitted to be added to your registered and approved project folder.) Sensitive data may **NOT** be added to My Workspace.
7.  **Collaboration on UCloud within projects: Fellow AAU persons.** 
    *   Only persons registered in the project with the department of Grants and Contracts, or registered according to an alternative data processing agreement may be added to the UCloud project.
8.  **Collaboration on UCloud within projects: Persons from outside AAU.**
    *   The collaborator’s employer must have a Data Processing agreement with SDU (SDU are hosts of the UCloud platform, DeiC Interactive HPC), or there must be an agreement of shared data responsibility (Agreement on Joint data controlling), that states that it is agreed to use DeiC/SDU as the data processor. Then it is sufficient that AAU has an existing data processing agreement with DeiC/SDU. In these cases AAU will be responsible for the data processing agreement with DeiC/SDU.
    *   If this is not the case, you cannot invite the collaborator inside the project folder in UCloud.
    *   No person(s) that are not included in the relevant data processing agreement or the agreement on joint data controlling may be invited to the project.
9.  **UCloud project members and roles should be set appropriately.**
    *   Project “admins” can see all member files by activating the “show member files” option. The Principal Investigator is responsible for ensuring that all [roles and responsibilities](https://docs.cloud.sdu.dk/guide/project-overview.html#member-roles) are properly assigned.
10.  **Read and write privileges on UCloud.**
     *   If collaborators are only allowed read or write to specific parts of the data / dataset, you will need to follow the following steps:
     *   Within the project, you will need to create a new “Drive”. (As drives are the only level to which you can specify read and write permissions.)
     *   Only project “admins” can create new drives within a project.
     *   Name the drive and then click the “…” button to modify the permissions.  Then choose the permissions (None / Read / Write).
11.  **Permitted applications and uses:**
     *   Only the SDU compute resources (DeiC Interactive HPC (SDU)) may be used to work with sensitive data.
     *   All applications except those labeled as “Virtual Machines” may be used for work on all data.
     *   Virtual Machine applications may only be used for data classified as level 0 and 1.
12.  **On completion of the project:**
     *  All data on the UCloud platform should be deleted.
     *  The project should then be archived with a final date that corresponds with the GDPR notification with ‘Grants and Contracts’.
     *  All files in trash folders should be permanently deleted.
     *  All complete data sets and metadata should be stored in a data repository in accordance with [The AAU Policy for Research Data Management](https://www.ansatte.aau.dk/regler/forskning/politik-for-handtering-af-forskningsdata). As of 2023-January, AAU DataDeposit as a local archiving solution, while a national solution is under development.
  
