# Guidelines for handling Sensitive data on UCloud

### Procedure sensitive UCloud projects
  <!-- Mermaid Diagram -->
  <div style="flex: 1; min-width: 300px; text-align: left;">
    <div class="mermaid">
    ```mermaid
    graph TD
        A[<a href="https://forms.office.com/e/8Khbr1TJGC" target="_blank">Register your project with Grants and Contracts</a>] --> B[📝 <a href="https://forms.office.com/e/8Khbr1TJGC" target="_blank">Complete the application form</a>]; 
        B --> C[✅ CLAAUDIA approval];
        C --> D[💻 <a href="https://cloud.sdu.dk/app/dashboard" target="_blank">Enter the approved resources in UCloud</a>];
        D --> E[✅ CLAAUDIA approval];
        E --> F[⭐ The project is now available];
        
    ```
    </div>
  </div>

  > **Note**:  As project applicant you will be the Principal Investigator for the project, and you should be aware of your roles and responsibilities.


### Data classification on UCloud
- On Ucloud you can work with all categories of data form AAUs data classification model.
- Store all project data in a designated project folder labeled according to its data sensitivity, following the AAU Data Classification Model. This folder must be labeled according to its data sensitivity, following the [AAU Data Classification Model](https://www.security.aau.dk/data-classification). The equivalent UCloud classifications are:
    - **AAU Level 0**: Public Information → **UCloud: Inherit**
    - **AAU Level 1**: Internal Information → **UCloud: Private**
    - **AAU Level 2**: Confidential Information → **UCloud: Confidential**
    - **AAU Level 3**: Sensitive Information → **UCloud: Sensitive**  
    *(Sensitive data can only be added to registered and approved project folders and must **NOT** be placed in My Workspace.)*



<br>

### Creating a sensitive folder on UCloud
Best practice for handlig sensitive data on UCloud require you to mark the folder with the data "sensitive" You can do this by going to your **files** and right-click on the folder select **Change sensitivity**.

![Marking a folder in a project as sensitive in UCloud](\assets\img\UCloud\SensitiveGuide\FolderSensitive.png){.standard_image_width}

Now click the dropdown and select *sensitive" and write the reason for the sensitivity change. 

![Marking a folder as sensitive in UCloud](\assets\img\UCloud\SensitiveGuide\FolderSensitive1.png){.standard_image_width}

### Collaboration within UCloud projects (AAU Members)
- Only individuals registered with the department of Grants and Contracts or those included via an approved data processing agreement may be added to UCloud projects.

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
   - Store all completed datasets and metadata in a data repository according to [AAU's Research Data Management Policy](https://www.ansatte.aau.dk/regler/forskning/politik-for-handtering-af-forskningsdata). You can find more information about out local archiving solution: [DataDeposit](https://www.researcher.aau.dk/guides/research-data-and-software/software-and-tools/datadeposit) 
  - Delete all data from the UCloud platform.
<!-- - Archive the project, ensuring that the final archiving date matches the GDPR notification with Grants and Contracts. -->
  - Permanently delete any files in trash folders.
  

