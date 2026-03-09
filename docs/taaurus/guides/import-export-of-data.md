# Import & Export of Data

## Importing data

!!! info "Temporary import solution"
    Currently, to import data to/from your TAAURUS project, you need to submit a service request.

    **Important:** The service request must be submitted by the **Principal Investigator (PI)** of the project.

    **Submit a service request at:** 
    [https://serviceportal.aau.dk/](https://serviceportal.aau.dk/serviceportal?id=emp_taxonomy_topic&topic_id=82a253e8838fc21053711d447daad328)

    Please describe in your service request:

    - What should be imported
    - How much data (size/volume)
    - Where the data comes from (source location)

## Exporting data

To export data from your TAAURUS project, you can use the **SP Exporter** application. Follow these steps:

### Step 1: Open SP Exporter

1. Click the **Menu** button in the top-left corner of your remote desktop.
2. In the search bar, type `sp-exporter`.
3. Select **sp-exporter** from the search results to launch the application.

![Opening SP Exporter](/assets/img/taaurus/taaurus-export-1.png){style=max-height:600px;}

### Step 2: Create a new export

1. Once SP Exporter opens, you'll see the main window with an **Exports** section on the left.
2. Click the **Add export** button to start creating a new export.

![SP Exporter main window](/assets/img/taaurus/taaurus-export-2.png){style=max-height:600px;}

### Step 3: Select file to export

1. In the export dialog, click the **Add file:** button (marked with a plus icon).
2. A file picker dialog will open. Navigate to the location of the file you want to export. The project directory is located at the bottom of the file navigation.
3. Select the desired file from the file picker.
4. Click **Open** to confirm your selection.

![Selecting files to export](/assets/img/taaurus/taaurus-export-3.png){style=max-height:600px;}

!!! info "Exporting multiple files or folders"
    SP Exporter only allows you to select a single file at a time. To export multiple files or entire folders, you need to compress them first using the file manager:
    
    1. Open the file manager (not the file picker dialog) and navigate to the files or folders you want to export.
    2. Select the files or folders you need.
    3. Right-click on your selection.
    4. Choose **Compress** from the context menu (this will create a ZIP, RAR, or similar archive file).
    5. Then, in SP Exporter, use the file picker to select the compressed archive file you just created.

### Step 4: Add a comment and export

1. After selecting your file, you'll see it listed in the export dialog.
2. Optionally, add a comment in the **Comment:** field to describe what you're exporting (e.g., "This file contains logs from gpu test").
3. Review the file path shown in the title bar to ensure you're exporting the correct file.
4. Click the **Export** button to submit your export request.

![Finalizing the export](/assets/img/taaurus/taaurus-export-4.png){style=max-height:600px;}

### Step 5: View export status

After submitting an export, you can view its details in the SP Exporter window:

- **Date**: When the export was created
- **ID**: Unique identifier for the export
- **Approved**: Approval status (shown as an orange dot if pending)
- **Description**: The comment you provided
- **Files**: List of files included in the export

![Export details view](/assets/img/taaurus/taaurus-export-5.png){style=max-height:600px;}

!!! info "Export approval"
    Exports require approval before they are processed. Check the approval status in the export details. Once approved, you'll be able to download your exported data.

### Step 6: PI Approval

Before an export can be downloaded, it must be approved by the **Principal Investigator (PI)** of the project. The PI can approve exports using SP Exporter:

1. Open SP Exporter on the TAAURUS remote desktop.
2. In the **Approve** section, you'll see pending export requests with their details (Date, ID, User, Files).
3. Review the export request details to ensure it's appropriate.
4. Click the **Approve** button to approve the export request.

Once approved, the export will be processed and made available for download.

![PI approving an export](/assets/img/taaurus/taaurus-export-6.png){style=max-height:600px;}

### Step 7: Downloading Approved Exports

After your export has been approved by the PI, you can download it from your local computer:

1. **Connect to the AAU network** - You must be connected to the AAU network (either on-campus or via VPN).
2. Open your web browser and navigate to: `export.taaurus.aau.dk` and login with your AAU credentials.
3. You'll see a directory listing with your approved export files (ZIP archives).
4. Click on the export file you want to download (e.g., `@its.aau.dk_20f12b63-d5dd-4f33-8b48-df7ed62c0c61.zip`).
5. The file will download to your computer.

![Downloading approved exports](/assets/img/taaurus/taaurus-export-7.png){style=max-height:600px;}