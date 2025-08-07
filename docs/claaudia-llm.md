# CLAAUDIA LLM
This is a PoC for a local LLM platform at AAU. The platform runs on Strato with 6 NVIDIA T4 GPUs and utilizes Open WebUI and Ollama for model management and interaction. Open WebUI provides a user-friendly interface, while Ollama handles model execution and optimization. Researchers can create groups and collaborate on RAG systems by integrating their own datasets. The goal is to create a flexible, GPU-optimized solution for research use.

## Installation

1. Start an instance on Strato with Cuda Ubuntu 24.04 with Docker image
2. Go to Security Groups and add a new. Make a new TCP rule to port 3000. Add the security Group to the instance.
3. Install Docker:
   https://docs.docker.com/engine/install/ubuntu/
4. Install NVIDIA toolkit: 
   https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-with-apt
5. Configure with Docker: 
   https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-docker
6. Enter the following to run Open WebUI: 
   sudo docker run -d --restart unless-stopped -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui-llm --privileged ghcr.io/open-webui/open-webui:ollama
7. Check that its running at: http://[replace with server IP]:3000 (it make take 5 minutes before its running)

Update server:
1. sudo docker stop open-webui-llm
2. sudo docker rm open-webui-llm
3. sudo docker pull ghcr.io/open-webui/open-webui:ollama
4. sudo docker run -d --restart unless-stopped -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui-llm --privileged ghcr.io/open-webui/open-webui:ollama

Nice commands:
1. sudo docker ps: checks the status of the Docker container

## Getting started

To start using the CLAAUDIA LLM platform, please follow these steps:

1. Ensure you are connected to the [AAU network](https://www.en.its.aau.dk/instructions/wi-fi) (including [VPN](https://www.en.its.aau.dk/instructions/vpn)).
2. Go to [http://10.92.1.195:3000/](http://10.92.1.195:3000/).
3. Sign up as a new user.
4. Wait for an approval email.
5. Refer to the [Open WebUI documentation](https://docs.openwebui.com/) for more how-to guides

## API Endpoints

Cerate a new Bearer API key from **Settings > Account**. To test the connection you can fetch all models by using:

```
curl -H "Authorization: Bearer YOUR_API_KEY" http://10.92.1.195:3000/api/models
```

Replace `YOUR_API_KEY` with the API Key you created. To send a chat request, you can do so by using:

```
curl -X POST http://10.92.1.195:3000/api/chat/completions \
-H "Authorization: Bearer YOUR_API_KEY" \
-H "Content-Type: application/json" \
-d '{
      "model": "mistral:7b",
      "messages": [
        {
          "role": "user",
          "content": "Why is the sky blue?"
        }
      ]
    }'
```

## Python Guide

### Overview
This guide explains how to use the Ollama OpenWebUI API with Python. It supports two methods:

1. Using the `openai` Python library (for compatibility with existing OpenAI-compatible codebases).
2. Using the `requests` library (for a simpler, direct approach).

### Installation & Configuration

#### Installing Dependencies
Ensure you have the required Python libraries installed:
```bash
pip install openai requests
```

#### Configuring Your API
- Ensure your Ollama OpenWebUI instance is running and accessible via the URL:
  ```
  http://10.92.1.195:3000/api
  ```
- Obtain your API token (`sk-xxx`) from your Ollama configuration.

### Using the `openai` Python Library

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://10.92.1.195:3000/api",
    api_key="sk-xxx"  # Replace with your actual API key
)

response = client.chat.completions.create(
    model="mistral:7b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Why is the sky blue?"}
    ]
)

print(response.choices[0].message.content)
```

### Using the `requests` Library

```python
import requests

token= "sk-xxx"  # Replace with your actual API key

def chat_with_model(token):
    url = 'http://10.92.1.195:3000/api/chat/completions'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": "mistral:7b",
        "messages": [
            {"role": "user", "content": "Why is the sky blue?"}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

result = chat_with_model(token)
print(result["choices"][0]["message"]["content"])
```

### Explanation
- **`openai` Library:** Uses the standard OpenAI client library for compatibility with existing tools.
- **`requests` Library:** Direct interaction with the API, providing more flexibility.
