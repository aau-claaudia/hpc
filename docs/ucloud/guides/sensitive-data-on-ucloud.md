## Guidelines for handling Sensitive data on UCloud

### Data classification on UCloud
- On Ucloud you can work with all categories of data form AAUs data classification model.
- Store all project data in a designated project folder labeled according to its data sensitivity, following the AAU Data Classification Model. This folder must be labeled according to its data sensitivity, following the [AAU Data Classification Model](https://www.security.aau.dk/data-classification). The equivalent UCloud classifications are:
    - **AAU Level 0**: Public Information → **UCloud: Inherit**
    - **AAU Level 1**: Internal Information → **UCloud: Private**
    - **AAU Level 2**: Confidential Information → **UCloud: Confidential**
    - **AAU Level 3**: Sensitive Information → **UCloud: Sensitive**  
    *(Sensitive data can only be added to registered and approved project folders and must **NOT** be placed in My Workspace.)*


### Before uploading data on UCloud
- If you are a researcher, and working with data classifications 2 or 3, you must register the research project with Grants and Contracts using  [the relevant registration form](https://aaudk.sharepoint.com/sites/persondata-ressourcer/SitePages/Registrations%20og%20reports%20(Online%20forms).aspx).
- If you are a student your supervisor must approve the application. 
- Before you can create a project on UCloud for sensitive data, you must fill out this form [this form](https://forms.office.com/pages/responsepage.aspx?id=Sbrb9QbOb0msPgzxQ2HZNEdKMbCNz_9Lom8_yaZURCNUQVZUQVRXSFVYODBZQkNZWVRYM1lEUEFYTSQlQCN0PWcu&route=shorturl).
- When the application is approved you receive an email with details om what to do and information on which resources you have allocated. 
- If the application is rejected, you will be informed what you need to change in the application.  


- Once approved, you will receive a UCloud project number, and you must apply for a project in the UCloud Interface, for the resources that you had approved in the CLAAUDIA application. (You can apply for additional resources later if needed.)

  > **Note**:  As project applicant you will be the Principal Investigator for the project, and you should be aware of your roles and responsibilities.

  > **Note**:  If the user is a student, then their supervisor for the student project must apply for the project and so must assume the role of Principal Investigator.

<br>

### Be aware when working with sensitive data
**Researcher:**
For any research data, or any data owned or acquired by AAU, only participants approved by the department of Grants and Contracts may be included in this project. It is the responsibility of the principal investigator to ensure that this is the case.
If you don't have a WorkZone case number you can apply Grants and Contracts using [the  registration form](https://aaudk.sharepoint.com/sites/persondata-ressourcer/SitePages/Registrations%20og%20reports%20(Online%20forms).aspx). 

**Student:**
You cannot register projects with Grants and Contracts. As a student you are personally responsible for any data you collect. You must ensure that you comply with [GDPR regulations for students](https://aaudk.sharepoint.com/sites/GDPR-for-students).


<br>

### Creating a sensitive project folder on UCloud

- Log into the [UCloud platform](https://cloud.sdu.dk/) by using WAYF login. 
- Go to the navigation bar to the left side of the screen and go to “Project” 

<br>

   ![SensitiveGuide](/assets/img/UCloud/SensitiveGuide/Billede1.png)

<br>

- Click on “Apply for resources” 

<br>

   ![SensitiveGuide](/assets/img/UCloud/SensitiveGuide/Billede2.png)

<br>

- You must name the project the same name as in the application form. You can find it in the email. 

<br>

   ![SensitiveGuide](/assets/img/UCloud/SensitiveGuide/Billede3.png)

<br>

- When you click on Type one, more fields will appear and can fill out the information on what you need, the information should be the same as in the email. 

<br>

   ![SensitiveGuide](/assets/img/UCloud/SensitiveGuide/Billede4.png)

<br>

- If you are working with sensitive data it is important to reference your WorkZone number. 

<br>

   ![SensitiveGuide](/assets/img/UCloud/SensitiveGuide/Billede5.png)

<br>

- Once your project is approved, you will need to add all relevant team members to the project using either their UCloud user names, or the “create link” option. (Not relevant for existing projects). 

<br>

### Collaboration within UCloud projects (AAU Members)
- Only individuals registered with the department of Grants and Contracts or those included via an approved data 

processing agreement may be added to UCloud projects.

### Collaboration with external partners (Non-AAU Members)
- The external collaborator’s employer must have a Data Processing Agreement with SDU (who hosts UCloud through DeiC Interactive HPC), or there must be an Agreement on Joint Data Controlling. In such cases, AAU will be responsible for the data processing agreement with SDU/DeiC.  
- If no such agreement exists, the collaborator cannot be invited to the UCloud project folder.
- No individual who is not covered by the relevant agreements may be added to the project.

### Setting UCloud project roles and permissions
- **Project Admins** can view all member files by enabling the “show member files” option.
- The **Principal Investigator** is responsible for ensuring all roles and responsibilities are correctly assigned. Detailed guidance on roles can be found [here](https://docs.cloud.sdu.dk/guide/project-overview.html#member-roles).

### Managing read and write access
- To assign specific read or write permissions:
  1. Create a new "Drive" within the project (as drives are the only entities where you can assign specific permissions).
  2. Only **Project Admins** can create new drives.
  3. Name the drive, then modify its permissions by clicking the “…” button. Set permissions as either **None / Read / Write**.

### Applications  
-  It is **not allowed** to add a public link when running applications. 

### Guides 
- When using our guides, please check the "Approved Data Classification Level" icons at the top of each guide to ensure it is approved for sensitive data.

### Completing a Project
- Upon project completion:
  - Delete all data from the UCloud platform.
<!-- - Archive the project, ensuring that the final archiving date matches the GDPR notification with Grants and Contracts. -->
  - Permanently delete any files in trash folders.
  - Store all completed datasets and metadata in a data repository according to [AAU's Research Data Management Policy](https://www.ansatte.aau.dk/regler/forskning/politik-for-handtering-af-forskningsdata). You can find more information about out local archiving solution: [DataDeposit](https://www.researcher.aau.dk/guides/research-data-and-software/software-and-tools/datadeposit) 


