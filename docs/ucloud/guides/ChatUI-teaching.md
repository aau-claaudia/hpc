# ChatUI classroom guide

**Table of content**

1. [Setting up the Application](#setting-up-the-application)
2. [Using the Application for Inference](#using-the-application-for-inference)
3. [FAQ](#faq)
  
## Setting up the application

The Chat UI application on UCloud is a great tool for working with LLMs and is simple to set up and use. The app supports saving your work in a directory on your personal drive on UCloud. It is a good idea to use this option so that you only need to go through the setup process once. The first step is to create an empty folder to use as the application input parameter `DATA_DIR`.

![ChatUI - Create empty folder](/assets/img/UCloud/ChatUI 1.png)

Now it is time to find and start the application. Search for “chatui” under apps.

![ChatUI - Create empty folder](/assets/img/UCloud/ChatUI 2.png)

Running inference against LLMs is much faster on a machine with one GPU and a large amount of memory. Remember to select the empty directory that was created in the first step as `DATA_DIR`. Notice also that you should specify the number of hours that the application should run for. 

![Find ChatUI under apps](/assets/img/UCloud/ChatUI 3.png)

The application needs a public link in order for the students to be able to access it from outside UCloud. Scroll down and click "add public link".

![Settings for the server](/assets/img/UCloud/ChatUI 4.png)

In this example, we are using a machine in the AAU/K8 provider, so we will create the link on this provider.

![Create public link](/assets/img/UCloud/ChatUI 5.png)

Click on “Use” after the link is created.

![Click on use](/assets/img/UCloud/ChatUI 6.png)

With this configuration, the application will be accessible over the internet on the URL listed above. Lastly, click the green “Submit” button at the top of the page to start the application. The number of hours that the application runs can be extended after it has started. And since we are using a data directory, the application can be started again with the same configuration. 

When the application has been started, click on “Open interface” to open the user interface. You may need to refresh the page since it can take a minute to start up.

The first user that accesses the welcome page can click on “Sign up” to create the admin user.

![Sign up](/assets/img/UCloud/ChatUI 7.png)

Fill in your name, email, and password, and click on “Create Account”.

In the settings, we can disable new sign-ups and create a user that students can log in with.

![Disable sign-ups in settings](/assets/img/UCloud/ChatUI 8.png)

Under the “Dashboard” pane, a new user called e.g., “student” can be created. Remember to create the user as a normal user and not as an admin. This user can be used by the students to log in, and in this way, only you have control over the application configuration.

![Create a new user for the students](/assets/img/UCloud/ChatUI 9.png)

Toggle off “Enable New Sign Ups” under “Settings” and “General” in the admin panel. **Remember to click the save button in the bottom right corner.**

![Toggle New Sign Ups off](/assets/img/UCloud/ChatUI 10.png)

To download a model, click on “Settings” and “Models.” If you don’t know the name of the model you want to use, there is a link with information about the available models. For instance, type in “llama3” and click the download button on the right.

![Download a model](/assets/img/UCloud/ChatUI 11.png)

The downloaded model should now be visible if you click on “Workspace” on the left.

![Model visible in the workspace ](/assets/img/UCloud/ChatUI 12.png)

In the “Documents” section, it is possible to upload documents for adding RAG functionality. Try to upload a document. Notice the text with information about how to use/load the documents for use in prompts .

![Load documents for RAG functionality](/assets/img/UCloud/ChatUI 13.png)
---

## Using the application for inference

Now that the model has been downloaded, try to make a prompt by clicking “New Chat” in the upper left corner. Then select the model (in this case llama3) from the dropdown. In the prompt input field, type `#` to select which/all documents to use.

![Using the application](/assets/img/UCloud/ChatUI 14.png)

This is an example of a query. The query is at the top, and notice under the reply that it is mentioned which document was used as the source in generating the reply.

![Using the application](/assets/img/UCloud/ChatUI 15.png)

When the appropriate documents have been uploaded, the application is ready for use. When the students log in with the user created for this purpose, they will also have access to the same model and documents.

To summarize, with the configuration used in this example, a student would go to:
```
http://app-chatui-example.cloud.aau.dk/
```
and log in with the username “student@email.com” with the password created for this user.

The next time you need to run the app with the same data and configuration, use the “Import parameters” option.

![Using the application](/assets/img/UCloud/ChatUI 16.png)

Click on “Import” to import the configuration from the last run. Everything should be the same, and just click “Submit” to start the job.

![Using the application](/assets/img/UCloud/ChatUI 17.png)
---

## FAQ

### 1. Why does the first response take longer to complete?

The first response takes longer because the model needs to load into memory before processing any prompts. This initial loading process can take some time, especially if the model is large. After the model is loaded, subsequent responses will be faster.

### 2. Why is there no response to my first query?

It takes a minute or two for the application to fully load the LLM. If you send a query before the model has been completely loaded, you will not get an answer, and the UI would, for instance, keep looking like this. In this case, you can first click "edit," then "save," and after that click on the "resend" button.

For the technical user: It is possible to open a terminal and monitor the logfile `ollama-log.txt` to see when the model is fully loaded. As the admin user, try to make a prompt before the students use the application to ensure the model is fully loaded. You need to redo this when restarting the application.

![Using the application](/assets/img/UCloud/ChatUI 18.png)

### 3. How to Add More Time to a Currently Running Server

If you need to extend the time for a currently running server in the Chat UI application, follow these steps:

- Access the UCloud dashboard and locate the running Chat UI server in the “recent runs” tab.
- Click on the server instance to access its details page.
- Extend the running time by clicking on the +1, +8, or +24-hours buttons.

### 4. How Can I Turn Off the Server?

To turn off the server running the Chat UI application, follow these steps:

- Access the UCloud dashboard and locate the running Chat UI server in the “recent runs” tab.
- Click on the server instance to access its details page.
- Click and hold the “Stop application” button.
- Confirm the shutdown when prompted. The server will begin to stop, and you’ll see its status update to “Completed.”

### 5. Why Is It Important to Shut Down the Server?

- **Cost Management:** Running a server on UCloud consumes resources, which are billed by the hour. If you forget to turn off a server, it will continue to run and accrue costs even if it’s no longer in use. To ensure you have resources available when needed, it is important to shut down the server after each usage.
  
- **Resource Allocation:** UCloud resources like GPUs and memory are limited. Keeping a server running when it’s not in use can block these resources, preventing others from utilizing them. Shutting down the server frees up these resources for other projects or users.

### 6. What should I do if I cannot start a server due to "not enough credits"?

Ensure you're in the correct project. Check the current project on the UCloud front page in the top right corner. If you are out of resources, apply for more using our application form.

### 7. I get the page “Job is unavailable” when selecting “Open interface”

This page appears because the server isn't fully ready yet. Please close the tab, wait for 30 seconds, and then try selecting "Open Interface" again.

--- 

