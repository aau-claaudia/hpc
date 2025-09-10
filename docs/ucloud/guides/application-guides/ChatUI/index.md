# ChatUI 
    
**Approved for data classification level**

<a href="https://www.security.aau.dk/data-classification" target="_blank" class="icon-container">
    <span class="icon level-0" title="Approved for public data">0</span>
    <span class="icon level-1" title="Approved for internal data">1</span>
    <span class="icon level-2" title="Approved for confidential data">2</span>
    <span class="icon level-3" title="Approved for strictly confidential data">3</span>
</a>

---

## Introduction  
ChatUI on UCloud is an intuitive application designed for working with large language models (LLMs). This guide will walk you through the process of setting up, configuring, and effectively using ChatUI. It covers both personal use—where ChatUI can handle sensitive data securely—and shared use, where you can provide multiple users access via a public link, making it ideal for teaching or similar collaborative scenarios.

## Configuring the ChatUI application  

### 1. Create a data directory  
To save configurations and avoid repeated setups, create an empty folder on your drive in UCloud. This folder will later be used as the input parameter `DATA_DIR` .  
![Create a data directory](/assets/img/UCloud/ChatUI%201.png){.standard_image_width}

### 2. Find and start the ChatUI application  
Search for "chatui" under the apps section of UCloud and select it to begin setup.  
![Find ChatUI in apps](/assets/img/UCloud/ChatUI%202.png){.standard_image_width}
 
### 3. Select the optimal machine configuration  
Choose a machine with **one** GPU, such as `u3-GPU` (SDU) or `uc1-l4`/`uc1-l40` (AAU/K8). Set the runtime duration in hours and select the previously created folder as `DATA_DIR`.  
![Configure server settings](/assets/img/UCloud/ChatUI%203.png){.standard_image_width}

??? info "ChatUI public link for sharing with user outside UCloud"
    Note applying a public link will decrease the approved sensitivity level to only 
    <a href="https://www.security.aau.dk/data-classification" target="_blank" class="icon-container">
    <span class="icon level-0" title="Approved for public data">0</span>
    <span class="icon level-1" title="Approved for internal data">1</span>
    </a>


    To enable access outside UCloud, scroll down and click "Add Public Link." Create a link within the same provider as the machine (`SDU` or `AAU/K8`) in this example we use the `AAU/K8`. 
    ![Add public link](/assets/img/UCloud/ChatUI%204.png){.standard_image_width}
    ![Create public link](/assets/img/UCloud/ChatUI%205.png)

    Once the link is created, click "Use." This will generate a URL to access the application.  
    ![Click on Use](/assets/img/UCloud/ChatUI%206.png){.standard_image_width}

### 4. Launch the application  
Click the green "Submit" button at the top of the page to start the application. After launching, wait for the application to build and then click "Open Interface" to access ChatUI. Refresh the page if it doesn't load.  
![Sign up page](/assets/img/UCloud/ChatUI first launch.png){.standard_image_width}

---

### 5. Set up admin and user roles
The next step is to create an account by clicking "Sign Up." Enter your name, email, and password, then click "Create Account." The first user (you) will automatically be assigned the admin role. 

??? info "How to give access to other users"

    There are two options for allowing other users to access the ChatUI interface.
    **1.** Enable the "Allow New Sign-Ups" option in the settings panel. This allows new users to apply for an account, which you can then review and approve.      
    
    **2.** Create a dedicated account for each user through the settings menu, as shown below. Ensure that new users are assigned the appropriate role — either "User" or "Admin"—to maintain control over the application settings.
    ![How to add users to ChatUI](/assets/img/UCloud/ChatUI%209.png){.standard_image_width}  

---

### 6. Download and manage models  
Go to **Adminstrationpanel > Settings** > **Models** to download models. If you’re unsure of the model name, use the provided link to explore available options. For example, type "llama3" or "mistral:7b" and click the download button.  
![Download a model](/assets/img/UCloud/ChatUI download models1.png){.standard_image_width}  
![Download a model step2](/assets/img/UCloud/ChatUI download models2.png){width=250}   

Once downloaded, the model will appear in the **Workspace** under the **Models** section. By default, the model is only visible to the person who downloads it. To make the model accessible to all users, click on the model name, change the visibility to "Public," and press Save. 
![Model visible in the workspace](/assets/img/UCloud/ChatUI%2012.png){.standard_image_width}

---

### 7. Set up a knowledge base for RAG functionality  
In the **Knowledge** section, you can create a knowledge base to upload documents for retrieval-augmented generation (RAG).  
![Set up a knowledge base](/assets/img/UCloud/ChatUI%2012a.png){.standard_image_width}

Provide a name and description for the knowledge base, and select the visibility for other users. Afterwards you can upload documents or directories to the knowledge base. 

![Upload documents for RAG functionality](/assets/img/UCloud/ChatUI%2013.png){.standard_image_width}
> **Note:** It may take some time for larger documents to be uploaded.
---

## Using ChatUI for inference  

### 1. Start a new chat  
Click "New Chat" in the upper-left corner. Select the downloaded model (e.g., llama3) from the dropdown. Use `#` in the prompt input field to reference the knowledge base.  
![Using the application](/assets/img/UCloud/ChatUI%2014.png){.standard_image_width}

### 2. Submit queries and view responses  
Type a query in the input field. Responses will indicate the source document used in the reply.  
![Example query and response](/assets/img/UCloud/ChatUI%2015.png){.standard_image_width}

<!-- Students can log in with their designated account to access the same models and knowledge bases. -->

---

## Reusing configurations  
Next time you want to use the same settings:  
1. Click **Import parameters** on the app start page.  
2. Import the configuration from the previous session.  
3. Click "Submit" to relaunch the app.  
![Using the application](/assets/img/UCloud/ChatUI%2016.png){.standard_image_width}  
![Import parameters](/assets/img/UCloud/ChatUI%2017.png){.standard_image_width}

---

## FAQ  

### 1. Why does the first response take longer to complete?  
The model needs to load into memory before processing queries. Subsequent responses will be faster.

### 2. Why is there no response to my first query?  
The model might not be fully loaded. Click "Edit," then "Save," and resend the query. Alternatively, monitor the log file `ollama-log.txt` to confirm the model is ready.  
![Monitor log file](/assets/img/UCloud/ChatUI%2018.png){.standard_image_width}

### 3. How to extend server runtime?  
Locate your server in UCloud’s **recent runs** tab, select the instance, and add more time using the +1, +8, or +24-hour buttons.

### 4. How to stop the server?  
In the **recent runs** tab, select the server and click "Stop application." Confirm the shutdown to free resources and avoid unnecessary costs.

### 5. Why is shutting down the server important?  
- **Cost management**: Servers consume resources billed by the hour.  
- **Resource allocation**: Free up resources for other users or projects.

### 6. What to do if I cannot start a server due to "not enough credits"?  
Check if you’re in the correct project. If resources are depleted, apply for more using the designated application form.

### 7. What does "Job is unavailable" mean?  
This error appears if the server isn't ready. Wait 30 seconds and try "Open Interface" again.

