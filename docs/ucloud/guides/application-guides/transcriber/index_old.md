# Transcriber batch

!!! success  "New Transcriber interface available!"
    We are excited to announce the launch of a brand new, user-friendly interface for the Transcriber application! This updated version offers an improved experience and new features to make your transcription tasks even easier. 

    To try it out, go to [UCloud](https://cloud.sdu.dk/app/jobs/create?app=transcriber-gui), select **Transcriber**, and choose the **Default** version. 

    For a step-by-step guide to the new interface, see [Transcriber Interface Guide](https://hpc.aau.dk/ucloud/guides/application-guides/transcriber/transcriber-interface/).
    
    If you prefer the previous version simply switch the version to **Batch** on the top of the job page.  and follow this guide, you can still access it by selecting **Batch** on the top of the job page. 


**Approved for data classification level**

<a href="https://www.security.aau.dk/data-classification" target="_blank" class="icon-container">
    <span class="icon level-0" title="Approved for public data">0</span>
    <span class="icon level-1" title="Approved for internal data">1</span>
    <span class="icon level-2" title="Approved for confidential data">2</span>
    <span class="icon level-3" title="Approved for strictly confidential data">3</span>
</a>

**[Download Transcriber User Guide (PDF)](/assets/transcriber-userguide-1-2.pdf)**

---

## 1. Using the Transcriber batch application

### 1.1 Finding the application

- Go into the application and use the search function to find **Transcriber**.
  
  ![Transcriber Guide Screen](/assets/img/UCloud/Transcriberguide16.jpg)
  
- Click on **Transcriber**.

  ![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide17.jpg)

### 1.2 Using the application

You should now see the following screen:

![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide18.jpg)

There are several options here, and it can seem overwhelming. For this example, we’ll walk through the quickest way to start a transcription.

#### 1.2.1 Choose a name for your job
- Pick a name that makes it easy to find your data later and distinguish between different jobs.
  - Example: "Transcriber demo 1".
  
  > **Note**: Job and file names cannot include special characters such as "æøå".

#### 1.2.2 Select the duration of your job
- The application can transcribe in 1:1 time. For instance, a 1-hour audio file will take approximately 1 hour to transcribe.
- We recommend allocating **double** the length of the audio file to avoid interruptions.
  - Example: For a 1-hour audio file, allocate 2 hours.
  
  > **Note**: If you run out of allocated time, the file being transcribed will fail. You can allocate more time after starting the job if needed.

#### 1.2.3 Pick a machine to use
- We recommend the `u3-gpu-1` machine, which performed best in our tests. If the option is unavailable we recommend the `u1-standard-16` as an alternative.
  
  > Feel free to test with sample files to see what works best for you.

  ![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide19.jpg)

#### 1.2.4 Select the input file
- Click the "use" button.

  ![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide20.jpg)

- Click the text box to select your file.

  ![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide21.jpg)

- Navigate to your "drives" and select the folder with your file or click "use" if it's already listed.
  
  ![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide22.jpg)

> **Note**: The app can only process `.mp3`, `.mp4`, `.m4a`, `.wav`, and `.mpg` files. If your file is in another format, we recommend using VLC to convert it. VLC can be downloaded from the Software Center/Company Portal.

#### 1.2.5 Select the output directory
- Choose where your output will be saved.
- Click "use" on "option: --output_dir".

  ![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide23.jpg)

- Select the folder you want for your transcription output.

  ![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide24.jpg)

> **Note**: The app supports `.mp3`, `.mp4`, `.m4a`, `.wav`, and `.mpg` files. For other formats, consider converting using VLC.

Now, you are ready to begin your transcription. Click **Submit** to start the process.

***There are additional options available. These are covered in the "Other Options" section.***

![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide25.jpg)

Once the process starts, you can close your computer. If you want to ensure everything is running smoothly, wait until a "node" is assigned. Your screen will look like this:

![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide26.jpg)

Once the transcription is complete, you will see the following screen:

![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide27.jpg)

> **Note**: This is not the actual output of your transcription. The transcription files are located in the folder you selected for output. You’ll find something like this:

![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide28.jpg)

---

### 1.3 Transcription output formats

You will have several different files with your transcription. Commonly used formats include `.txt` and `.docx`. You can choose the format that suits your needs best. If you want a specific output format, refer to the "output_format" section under "Other Options".

---

## 2. Optional parameters

![Transcriber Optional Parameters](/assets/img/UCloud/Transcriberguide32.jpg)

### 2.1 Option: --output_format

By default, the application produces all 8 formats. You can limit the output to a specific format by selecting one of the following:

- **CSV**: Contains all parameters outputted from the Whisper model.
- **SRT**: SubRip file format, a widely adopted subtitle format.
- **TXT**: Pure text file with the transcription.
- **VTT**: Web Video Text Tracks format, includes timestamps.
- **JSON**: JavaScript Object Notation.
- **TSV**: Tab-separated values file containing start, end, and text.
- **DOTE**: Transcription software developed by the BigSoftVideo team at AAU.
- **DOCX**: Text file with transcription and speaker recognition.

### 2.2 Option: --output_model

Select the model size:

- **Small**: Faster but less accurate.
- **Medium**: Slightly slower, more accurate.
- **Large**: Most accurate but slowest.

The default is **Large**. With a machine featuring 16 vCPUs and 96GB of memory, transcription speed is about the same as the audio length (e.g., 1 minute of audio takes approximately 1 minute to transcribe).

### 2.3 Option: --output_language

Specify the language for transcription. The Whisper model can detect and automatically choose the language. If you select a language manually, the model will translate audio into that language.

> **Note**: The detected or chosen language determines the output language. For example, if the chosen language is English, the model will translate multiple languages into English.

### 2.4 Interactive mode

Enable interactive mode for access to the app terminal or a web interface. The web interface includes a JupyterLab workspace for working with notebooks.

### 2.5 Archive password

Encrypt and password-protect the ZIP output archive. Specify a password for the archive as a text string.

### 2.6 Minimum and maximum number of speakers

Specify the number of speakers to improve speaker diarization accuracy in some cases.

### 2.7 Merge consecutive text entries from the same speaker (Recommended)

This option combines consecutive text entries from the same speaker into a single block, improving readability.

- When enabled, the app generates additional files with merged text in **docx**, **dote**, **json**, and **csv** formats. These files are named `filename_merged` and are created alongside the original files.
  
  >  To make the option visible, scroll down in the optional parameter window.

---

For further assistance, contact CLAAUDIA at [https://serviceportal.aau.dk](https://serviceportal.aau.dk).

---


## Who made it?

**Research & development by**

* CLAAUDIA, ITS, AAU 

**With support from**

* DeiC (The Danish e-Infrastructure consortium)
* Aalborg University
* University of Southern Denmark
* Aarhus University
* Center for Humanities Computing

**Citation**

CLAAUDIA, ITS, AAU (2024). Transcriber (Version1.0) [App]. UCloud interactive HPC system, eScience Center at the University of Southern Denmark. https://cloud.sdu.dk/app/jobs/create?app=transcriber&version=1.0  