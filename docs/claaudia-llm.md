# CLAAUDIA LLM
This is a PoC for a local LLM platform at AAU. The platform runs on Strato with 6 NVIDIA T4 GPUs and utilizes Open WebUI and Ollama for model management and interaction. Open WebUI provides a user-friendly interface, while Ollama handles model execution and optimization. Researchers can create groups and collaborate on RAG systems by integrating their own datasets. The goal is to create a flexible, GPU-optimized solution for research use.

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