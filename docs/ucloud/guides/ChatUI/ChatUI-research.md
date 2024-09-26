# ChatUI for Researchers

**Table of content**

1. [Setting up the Application](#setting-up-the-application)
2. [Using the Application for Inference](#using-the-application-for-inference)
3. [FAQ](#faq)
  
## Setting up the application

The Chat UI application on UCloud is an excellent tool for working with large language models (LLMs) and is straightforward to set up. You can save your work in a directory on your personal UCloud drive, allowing you to reuse the setup later. First, create an empty folder to use as the application input parameter `DATA_DIR`.

![ChatUI - Create empty folder](/assets/img/UCloud/ChatUI 1.png)

Next, find and start the ChatUI application by searching for “chatui” under UCloud apps.

![ChatUI - Create empty folder](/assets/img/UCloud/ChatUI 2.png)

Running inference on LLMs is faster on a machine with a GPU and ample memory. Choose the folder you created as the `DATA_DIR` and specify how many hours the application should run.

![Find ChatUI under apps](/assets/img/UCloud/ChatUI 3.png)

**Optional**: If you need to make the server remotely available, you'll need to create a public link. Scroll down and click "add public link."

![Settings for the server](/assets/img/UCloud/ChatUI 4.png)

In this example, we use a machine from the AAU/K8 provider. You’ll create the link on this provider.

![Create public link](/assets/img/UCloud/ChatUI 5.png)

Once the link is created, click on “Use.”

![Click on use](/assets/img/UCloud/ChatUI 6.png)

The application will now be accessible online via the generated URL. Finally, click the green “Submit” button to start the application. You can extend the running time if needed and restart the app later with the same settings by using the data directory.

Once the application has started, click on “Open interface.” The first time the interface may take a minute to start up, so you might need to refresh the page.

As the first user, you'll create an admin account by clicking “Sign up.”

![Sign up](/assets/img/UCloud/ChatUI 7.png)

Fill in your details and click “Create Account.”

To maintain control over the configuration, disable new sign-ups under the settings and create an additional user account for any collaborators.

![Disable sign-ups in settings](/assets/img/UCloud/ChatUI 8.png)

Under “Dashboard,” you can create a new user account that others can use, making sure they are given normal user permissions.

![Create a new user for the students](/assets/img/UCloud/ChatUI 9.png)

Toggle off “Enable New Sign Ups” under “Settings” → “General” and click the save button.

![Toggle New Sign Ups off](/assets/img/UCloud/ChatUI 10.png)

To download a model, navigate to “Settings” → “Models.” If you're unsure of the model name, there’s a link to available models. For instance, search for “llama3” and click the download button.

![Download a model](/assets/img/UCloud/ChatUI 11.png)

Once the model is downloaded, it will appear under “Workspace.”

![Model visible in the workspace ](/assets/img/UCloud/ChatUI 12.png)

In the “Documents” section, you can upload documents to enable Retrieval-Augmented Generation (RAG) functionality. Uploaded documents can then be used for prompts.

![Load documents for RAG functionality](/assets/img/UCloud/ChatUI 13.png)

---

## Using the application for inference

After downloading the model, start a new prompt by clicking “New Chat” in the upper-left corner. Select the downloaded model (e.g., llama3) and, in the prompt input field, type `#` to select which documents to use.

![Using the application](/assets/img/UCloud/ChatUI 14.png)

Here’s an example of a query, with the document source used in generating the response listed below.

![Using the application](/assets/img/UCloud/ChatUI 15.png)

Now that your model and documents are set up, the application is ready for use. If you need to run the app again with the same configuration, select the “Import parameters” option during setup.

![Using the application](/assets/img/UCloud/ChatUI 16.png)

Click “Import,” and then “Submit” to start the app using the same settings as the previous run.

![Using the application](/assets/img/UCloud/ChatUI 17.png)

---

## FAQ

### 1. Why does the first response take longer to complete?

The first response takes longer because the model needs to load into memory before processing your query. This initial loading can take time, especially with large models. Afterward, responses will be quicker.

### 2. Why is there no response to my first query?

If you send a query before the model fully loads, the UI will not respond. Wait a minute or two after starting the app and then resend your query. You can monitor the logfile `ollama-log.txt` to see when the model is fully loaded. 

![Using the application](/assets/img/UCloud/ChatUI 18.png)

### 3. How to Add More Time to a Currently Running Server

To extend the time of a running server:

- Go to the UCloud dashboard and locate the running server under “recent runs.”
- Select the instance and click +1, +8, or +24-hours to extend its runtime.

### 4. How Can I Turn Off the Server?

To stop the server:

- Go to the UCloud dashboard and locate the running instance.
- Click “Stop application” and confirm the shutdown.

### 5. Why Is It Important to Shut Down the Server?

- **Cost Management:** Servers are billed hourly, so leaving one running when it's not in use can increase costs unnecessarily. 
- **Resource Management:** Shutting down unused servers frees resources like GPUs and memory, allowing others to use them.

### 6. What should I do if I cannot start a server due to "not enough credits"?

Make sure you're in the correct UCloud project. If you're out of resources, apply for more using the application form on UCloud.

### 7. I get the page “Job is unavailable” when selecting “Open interface.”

This means the server isn’t ready yet. Wait 30 seconds and try again.

--- 