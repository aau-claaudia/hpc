# Using the API

This guide covers how to authenticate with Mistral's API, make your first request, and build more advanced workflows. The API follows the OpenAI-compatible chat completions format, making it straightforward to adopt if you have used other LLM APIs before.

For the full official API reference, see [docs.mistral.ai](https://docs.mistral.ai/getting-started/quickstart/).

---

## Prerequisites

Before making API calls you need:

1. An approved workspace with API key access — see [How to Access Mistral](/mistral/how-to-access/)
2. An API key created in [AI Studio](https://console.mistral.ai/) under **API Keys**
3. A working Python (3.8+) or other programming environment

---

## Step 1 — Create an API Key

1. Log in to [AI Studio](https://console.mistral.ai/).
2. Make sure you are in the correct workspace (click the workspace selector in the top left).
3. Go to **API Keys** in the left navigation panel.
4. Click **Create new key**.
5. Give it a descriptive name (e.g. `my-research-project`).
6. Copy the key immediately — it will not be shown again.

!!! warning "Keep your API key secret"
    Never share your API key, commit it to a public repository, or paste it into a chat or email. Anyone with your key can make API calls that count against your usage quota.

**Recommended practice:** Store the key in an environment variable rather than hard-coding it in your scripts.

```bash
# In your terminal (Linux/macOS) or PowerShell (Windows)
export MISTRAL_API_KEY="your-key-here"     # Linux/macOS
$env:MISTRAL_API_KEY = "your-key-here"    # PowerShell
```

---

## Step 2 — Install the SDK

Mistral provides official SDK clients for Python and JavaScript/TypeScript. Install the Python client with:

```bash
pip install mistralai
```

See the [SDK documentation](https://docs.mistral.ai/getting-started/clients/) for other language clients.

---

## Step 3 — Your First API Call

The following example sends a single chat message and prints the response.

```python
import os
from mistralai import Mistral

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

response = client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {
            "role": "user",
            "content": "What is the difference between a systematic review and a meta-analysis?"
        }
    ]
)

print(response.choices[0].message.content)
```

**Key elements:**

- `model` — the API identifier of the model (see [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/))
- `messages` — a list of message objects, each with a `role` (`system`, `user`, or `assistant`) and `content`
- `response.choices[0].message.content` — the model's text response

---

## Step 4 — Adding a System Prompt

A system prompt sets the model's role and constraints for the entire conversation. Add it as the first message with `"role": "system"`.

```python
import os
from mistralai import Mistral

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

response = client.chat.complete(
    model="mistral-large-latest",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a scientific writing assistant. "
                "Respond in formal academic English. "
                "When summarising a study, always cover: research question, "
                "methods, key findings, and limitations. "
                "Never fabricate citations."
            )
        },
        {
            "role": "user",
            "content": "Summarise the following abstract: [paste abstract here]"
        }
    ]
)

print(response.choices[0].message.content)
```

---

## Step 5 — Multi-Turn Conversations

To maintain a conversation across multiple turns, accumulate the messages list with each exchange.

```python
import os
from mistralai import Mistral

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

messages = [
    {
        "role": "system",
        "content": "You are a helpful research assistant."
    }
]

def chat(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.complete(
        model="mistral-small-latest",
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

print(chat("What methods are used in observational epidemiology?"))
print(chat("Can you give an example of a cohort study?"))
```

Each call sends the full conversation history, so the model remembers what was said earlier.

!!! tip "Context window limits"
    The full messages list is sent with every request. For long conversations, this accumulates tokens quickly. Be aware of the model's context window limit (see [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/)). For very long workflows, you may need to trim or summarise earlier messages.

---

## Step 6 — Controlling Generation Parameters

Pass additional parameters to control how the model generates text.

```python
response = client.chat.complete(
    model="mistral-large-latest",
    messages=[...],
    temperature=0.3,        # Lower = more deterministic
    max_tokens=1024,        # Maximum response length
    random_seed=42          # Fixed seed for reproducible outputs
)
```

| Parameter | Effect | When to adjust |
|---|---|---|
| `temperature` | Randomness of output (0 = deterministic, 1 = highly varied) | Lower for extraction/classification; higher for creative tasks |
| `max_tokens` | Caps the response length | Set to avoid unexpectedly long (expensive) outputs |
| `random_seed` | Makes outputs reproducible | Set when comparing prompt variants |
| `top_p` | Alternative diversity control | Usually leave at default |

---

## Step 7 — Processing Multiple Items

A common research use case is running the same prompt over a list of inputs — for example, classifying 500 paper abstracts.

```python
import os
from mistralai import Mistral

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

SYSTEM_PROMPT = """
You are a research classifier. 
Given an abstract, classify the study design into exactly one of these categories:
RCT, Cohort study, Case-control study, Cross-sectional study, Systematic review, Other.
Respond with only the category name. No explanation.
"""

abstracts = [
    "We conducted a randomised controlled trial...",
    "This retrospective cohort study followed...",
    "We performed a meta-analysis of...",
]

results = []
for abstract in abstracts:
    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": abstract}
        ],
        temperature=0.0,
        max_tokens=20
    )
    label = response.choices[0].message.content.strip()
    results.append(label)

for abstract, label in zip(abstracts, results):
    print(f"{label}: {abstract[:60]}...")
```

For large batches (hundreds or thousands of items), see the [Batch Inference API](https://docs.mistral.ai/capabilities/batch/) below — it is significantly cheaper.

---

## Batch Inference (50% Cost Reduction)

The Batch API processes large numbers of requests asynchronously (in a queue rather than in real time). This gives a **50% discount** on token costs, making it the preferred approach for large-scale processing.

```python
import os
from mistralai import Mistral

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

# Prepare a list of requests
requests = [
    {
        "custom_id": f"abstract_{i}",
        "body": {
            "model": "mistral-small-latest",
            "messages": [
                {"role": "system", "content": "Classify the study design."},
                {"role": "user", "content": abstract}
            ],
            "max_tokens": 20,
            "temperature": 0.0
        }
    }
    for i, abstract in enumerate(abstracts)
]

# Submit batch job
batch_job = client.batch.jobs.create(
    input_files=[...],  # See official docs for file upload format
    model="mistral-small-latest",
    endpoint="/v1/chat/completions",
    metadata={"project": "abstract-classification"}
)

print(f"Batch job created: {batch_job.id}")
```

See the [Batch Inference documentation](https://docs.mistral.ai/capabilities/batch/) for the full file format and how to retrieve results.

!!! info "When to use Batch vs. synchronous"
    Use the synchronous API when you need results immediately (interactive tools, real-time workflows). Use Batch when processing large datasets where you can wait minutes to hours for results — and want to save 50% on costs.

---

## Structured Outputs (JSON Mode)

If you need the model to return a structured response (e.g. a JSON object with specific fields), use structured outputs.

```python
from pydantic import BaseModel
from mistralai import Mistral
import os

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

class StudySummary(BaseModel):
    title: str
    study_design: str
    sample_size: int | None
    main_finding: str
    limitations: list[str]

response = client.chat.complete(
    model="mistral-large-latest",
    messages=[
        {
            "role": "user",
            "content": "Extract structured information from this abstract: [abstract here]"
        }
    ],
    response_format=StudySummary
)

summary = response.choices[0].message.parsed
print(summary.study_design)
print(summary.limitations)
```

Structured outputs are particularly useful for data extraction workflows where downstream code needs to parse the model's response reliably. See the [Structured Outputs documentation](https://docs.mistral.ai/capabilities/structured_output/) for full details.

---

## Document AI (OCR)

To extract text from PDFs and scanned documents, use the OCR endpoint.

```python
import os
from mistralai import Mistral

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

with open("document.pdf", "rb") as f:
    ocr_response = client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type": "document_url",
            "document_url": "https://your-document-url.com/document.pdf"
        },
        include_image_base64=False
    )

for page in ocr_response.pages:
    print(f"--- Page {page.index} ---")
    print(page.markdown)
```

The OCR model returns the extracted content in Markdown format, preserving headers, tables, and lists. See the [Document AI documentation](https://docs.mistral.ai/capabilities/document_ai/) for local file upload and annotation features.

---

## Embeddings

Embeddings convert text into numerical vectors. Use them for semantic search, document clustering, or similarity tasks.

```python
import os
from mistralai import Mistral

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

texts = [
    "Randomised controlled trials are the gold standard for causal inference.",
    "Observational studies can identify associations but not causation.",
    "The cat sat on the mat."
]

response = client.embeddings.create(
    model="mistral-embed",
    inputs=texts
)

vectors = [item.embedding for item in response.data]
print(f"Each embedding has {len(vectors[0])} dimensions")
```

Once you have the vectors, you can use libraries like `numpy`, `scikit-learn`, or a vector database to compute similarities and perform search. See the [Embeddings documentation](https://docs.mistral.ai/capabilities/embeddings/) for details.

---

## Error Handling

Always wrap API calls in error handling for production workflows.

```python
from mistralai import Mistral
from mistralai.models import SDKError
import os
import time

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

def call_with_retry(messages, model="mistral-small-latest", max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.complete(
                model=model,
                messages=messages
            )
            return response.choices[0].message.content
        except SDKError as e:
            if e.status_code == 429:
                wait = 2 ** attempt
                print(f"Rate limited. Waiting {wait}s...")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("Max retries exceeded")
```

Common errors:

| Error code | Meaning | Fix |
|---|---|---|
| `401` | Invalid API key | Check key, check workspace |
| `429` | Rate limit exceeded | Reduce request frequency, add retry logic |
| `400` | Bad request (malformed message) | Check your messages structure |
| `500` | Server error | Retry with backoff |

---

## Tracking Usage in Code

You can access token usage information from each API response:

```python
response = client.chat.complete(
    model="mistral-small-latest",
    messages=[{"role": "user", "content": "Hello"}]
)

usage = response.usage
print(f"Input tokens: {usage.prompt_tokens}")
print(f"Output tokens: {usage.completion_tokens}")
print(f"Total tokens: {usage.total_tokens}")
```

Use this to log costs per request in your workflow, or to estimate the total cost of a large batch before running it at full scale.

---

## Best Practices for Research Workflows

- **Pin the model version** in production code: use `mistral-small-2603` not `mistral-small-latest` if you need reproducibility over time.
- **Set `random_seed`** when comparing prompt variants to isolate the effect of prompt changes.
- **Set `temperature=0.0`** for classification and extraction tasks where you want the most deterministic output.
- **Test on a small sample first.** Run five to ten items manually before processing hundreds.
- **Log inputs and outputs.** For research use, save both the prompt and the model's response so you can audit and reproduce results.
- **Do not store sensitive data.** Keep prompts and documents to Level 1 data classification only.
- **Review outputs.** Do not route AI-generated content to publication or a database without human review.

---

## Further Reading

- [Mistral Quickstart](https://docs.mistral.ai/getting-started/quickstart/) — Official getting started with SDK examples
- [Chat Completions documentation](https://docs.mistral.ai/capabilities/completion/)
- [Batch Inference documentation](https://docs.mistral.ai/capabilities/batch/)
- [Structured Outputs documentation](https://docs.mistral.ai/capabilities/structured_output/)
- [Document AI documentation](https://docs.mistral.ai/capabilities/document_ai/)
- [Embeddings documentation](https://docs.mistral.ai/capabilities/embeddings/)
- [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/)
- [AI Studio overview](/mistral/guides/ai-studio/)
