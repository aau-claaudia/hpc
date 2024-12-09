# ChatUI teaching guide   
**Approved for data classification level**

<a href="https://www.security.aau.dk/data-classification" target="_blank" class="icon-container">
    <span class="icon level-0" title="Approved for public data">0</span>
    <span class="icon level-1" title="Approved for internal data">1</span>
</a>


---

## Introduction  
ChatUI on UCloud is an intuitive application for working with large language models (LLMs). This guide will walk you through the process of setting up, configuring, and using ChatUI effectively, including optimizing the app for teaching.

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

### 4. Create a public link for accessibility  
To enable student access outside UCloud, scroll down and click "Add Public Link." Create a link within the same provider as the machine (`SDU` or `AAU/K8`) in this example we use the `AAU/K8`. 
![Add public link](/assets/img/UCloud/ChatUI%204.png){.standard_image_width}
![Create public link](/assets/img/UCloud/ChatUI%205.png)

Once the link is created, click "Use." This will generate a URL to access the application.  
![Click on Use](/assets/img/UCloud/ChatUI%206.png){.standard_image_width}

### 5. Launch the application  
Click the green "Submit" button at the top of the page to start the application. After launching, wait for the application to build and then click "Open Interface" to access ChatUI. Refresh the page if it doesn't load.  

---

### 6. Set up admin and student users
The next step is to create an account by clicking "Sign Up." Enter your name, email, and password, then click "Create Account." The first user (you) will automatically be assigned the admin role. 

![Sign up page](/assets/img/UCloud/ChatUI%207.png)

Currently, anyone who accesses the URL can create a user and access ChatUI, we therefore recommend that after logging in, go to **Settings** > **General** to disable new sign-ups. This ensures that only authorized users can access the application.  
![Disable sign-ups in settings](/assets/img/UCloud/ChatUI%208.png){.standard_image_width}

You then have two options for providing your students with access:  
**1.** Activate new sign-ups the first time students need to use ChatUI, such as in the classroom. Once all students have signed up, you can disable sign-ups again as described above.  
   
**2.** Create a single student user with a generic email and password for all students to use.**Note:** Using this method allows students to see each other's queries.

- Under the **Dashboard**, create a user account for students. Assign the user as "Normal" instead of "Admin" to maintain control over the application settings.  
![Create a new user for the students](/assets/img/UCloud/ChatUI%209.png){.standard_image_width}  

---

### 7. Download and manage models  
Go to **Settings** > **Models** to download models. If you’re unsure of the model name, use the provided link to explore available options. For example, type "llama3" and click the download button.  
![Download a model](/assets/img/UCloud/ChatUI%2011.png)  

Once downloaded, the model will appear in the **Workspace** under the **Models** section.  
![Model visible in the workspace](/assets/img/UCloud/ChatUI%2012.png){.standard_image_width}

---

### 8. Set up a knowledge base for RAG functionality  
In the **Knowledge** section, you can create a knowledge base to upload documents for retrieval-augmented generation (RAG).  
![Set up a knowledge base](/assets/img/UCloud/ChatUI%2012a.png){.standard_image_width}

Provide a name and description for the knowledge base, then upload documents or directories.  
![Upload documents for RAG functionality](/assets/img/UCloud/ChatUI%2013.png){.standard_image_width}

---

## Using ChatUI for inference  

### 1. Start a new chat  
Click "New Chat" in the upper-left corner. Select the downloaded model (e.g., llama3) from the dropdown. Use `#` in the prompt input field to reference the knowledge base.  
![Using the application](/assets/img/UCloud/ChatUI%2014.png){.standard_image_width}

### 2. Submit queries and view responses  
Type a query in the input field. Responses will indicate the source document used in the reply.  
![Example query and response](/assets/img/UCloud/ChatUI%2015.png){.standard_image_width}

Students can log in with their designated account to access the same models and knowledge bases.

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

