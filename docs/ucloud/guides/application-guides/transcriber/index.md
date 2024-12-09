# Transcriber
**Approved for data classification level**

<a href="https://www.security.aau.dk/data-classification" target="_blank" class="icon-container">
    <span class="icon level-0" title="Approved for public data">0</span>
    <span class="icon level-1" title="Approved for internal data">1</span>
    <span class="icon level-2" title="Approved for confidential data">2</span>
    <span class="icon level-3" title="Approved for strictly confidential data">3</span>
</a>

!!! info "[Download transcriber user guide (PDF)](/assets/transcriber-userguide-1-1.pdf)"
    
# Using the Transcriber Application

## 1.1 Find the Application
- Go into the application.
- Use the search function to find Transcriber.
![Transcriber Guide Screen](/assets/img/UCloud/Transcriberguide16.jpg)
- Click on **Transcriber**.
![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide17.jpg)


## 1.2 Using the Application
You should now have the following screen:
![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide18.jpg)

There are several options here, and it can seem a bit overwhelming. For this example, we will show the "quickest" way to start a transcription.

1. **Choose a name for your job**: Pick something that will make it easy to find your data later on and distinguish between different jobs. Example: "Transcriber demo 1".  
   _Note_: Job and file names cannot include any special characters such as "æøå".
   
2. **Select the duration of your job** in hours.
   - The application can transcribe in 1:1 time, meaning that a 1-hour audio file will take approximately 1 hour to transcribe.
   - We recommend allocating double the length of the audio file. For example, a 1-hour audio file should be allocated 2 hours in the application. This ensures the transcription won't stop during the process.  
   _Note_: If you run out of allocated time before your job finishes, the file being transcribed at that point will fail to process. You can allocate more time after starting the job if you suspect time will run out.

3. **Pick a machine to use**: We recommend the machine named `u3-gpu-1` as it performed best in our tests (even better than bigger machines).  
   _Note_: Feel free to test this with a few sample files.
   
   ![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide19.jpg)


4. **Select the input file**:
   - Click the "use" button.
   ![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide20.jpg)

   - Click on the text box to select a file.
   ![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide21.jpg)

   - You will be navigated to your "drives." Click on the folder with your file, or if the file is already listed, simply click "use" on the file you wish to use.
   - In this example, we clicked on the folder "New folder" from before and selected our audio file.
    ![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide22.jpg)


5. **Select the output directory**:
   - We recommend selecting where your output will be saved.
   - Click "use" on "option: --output_dir".
   ![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide23.jpg)

   - Then click the "text box" again and select the folder you want for your transcription output. In this example, we selected the folder "New folder."
   ![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide24.jpg)

Now you are ready to begin your transcription. Click on **Submit** to start the process.  
_Note_: There are other options you can use, but more information on these can be found in the "Other Options" section.
![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide25)

At this step, you are free to close your computer until Transcriber is done. If you want to ensure everything is running smoothly, wait until a "node" has been assigned and your screen will look something like this:
![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide26.jpg)

Once the transcription is complete, you will see something like this:
![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide27.jpg)

_Note_: This is not the actual output of your transcription. The transcription files can be found in the folder you selected for output. The files may look something like this:
![Transcriber Node Assigned](/assets/img/UCloud/Transcriberguide28.jpg)


You will have several different files with your transcription. The most commonly used formats are `.txt` and `.docx`. Feel free to explore the formats and choose the one that suits your needs best.  
If you'd prefer only one specific output format, refer to the "output_format" section under "Other Options" in this guide.

For further assistance, contact CLAAUDIA at [https://serviceportal.aau.dk](https://serviceportal.aau.dk).

# 2. Optional parameters
![Transcriber optional parameters](/assets/img/UCloud/Transcriberguide32.jpg)

## 2.1 Option: --output_format
The default setting produces all 8 formats automatically. You can limit the output to a specific format by selecting one of the following:

- **CSV**: Contains all parameters outputted from the Whisper model.
- **SRT**: SubRip file format, a widely adopted subtitle format.
- **TXT**: Pure text file with the transcription.
- **VTT**: Web Video Text Tracks format, includes timestamps.
- **JSON**: JavaScript Object Notation.
- **TSV**: Tab-separated values file containing start, end, and text.
- **DOTE**: Transcription software developed by the BigSoftVideo team at AAU.
- **DOCX**: Text file with transcription and speaker recognition.

## 2.2 Option: --output_model
This option allows you to select the model size. Choices include:
- **Small**: Faster but less accurate.
- **Medium**: Slightly slower, significantly more accurate.
- **Large**: Most accurate but slowest.

The default is the **Large** model. With a machine featuring 16 vCPUs and 96GB of memory, the transcription speed is roughly the same as the audio length. For example, 1 minute of audio takes roughly 1 minute to transcribe.
## 2.3 Option: --output_language
This option allows you to specify the language the model will use to evaluate the audio for transcription. The supported languages are available in a dropdown list.
The default setting is for the Whisper model to automatically detect the audio language.  
_Note_: This setting also determines the output language of the transcribed text. The Whisper model will translate audio from multiple languages into the detected or chosen language. For example, if the detected/chosen language is English but the audio includes English, Danish, Spanish, and Greek, the output will be entirely in English.
## 2.4 Interactive mode 
Enabling interactive mode allows the job to run interactively, providing access to the app terminal or a web interface. The web interface provides a JupyterLab workspace where users can work with notebooks.
## 2.5 Archive password 
This will AES encrypt and password-protect the ZIP output archive. The user must specify a password for the archive as a text string.
## 2.6 Minimum and maximum number of speakers 
If the minimum or maximum number of speakers is known in advance these options can be used to  in some cases increase the accuracy of the speaker diarization.
## 2.7 Merge consecutive text entries from the same speaker (Recommended)
This option enables you to combine consecutive text entries from the same speaker. When the transcription model detects the same speaker across multiple entries, it merges the text into a single, continuous block, resulting in a more reader-friendly output.
Setting this option to "True" generates additional output formats in **docx**, **dote**, **json**, and **csv**, named filename_merged. These files are created alongside the original formats and will not replace them.
_Note_: To enable this option, scroll down in the optional parameter window until the setting becomes visible.
