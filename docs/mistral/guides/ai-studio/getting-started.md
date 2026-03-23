# Getting Started with AI Studio

This page walks you through your first session in AI Studio, from logging in to running your first test in the Playground.

---

## Step 1 — Log In

Go to [console.mistral.ai](https://console.mistral.ai/) and log in with your AAU credentials via SSO. If you have not set this up yet, follow the instructions on the [How to Access Mistral](/mistral/how-to-access/) page first.

After logging in, you will land on the AI Studio home screen. At the top left, you will see your workspace name. If you have received a dedicated project workspace, click the workspace selector to switch to it before doing anything else.

---

## Step 2 — Explore the Interface

AI Studio is organised around a left-hand navigation panel with the following main sections:

| Section | What it does |
|---|---|
| **Build > Playground** | Interactive model testing in the browser |
| **Build > Agents** | Create and configure custom AI agents |
| **Models** | Browse all available models with specs and pricing |
| **API Keys** | Create and manage authentication keys |
| **Usage** | Monitor token consumption and costs |
| **Workspace Settings** | Manage members, billing, and workspace preferences |

---

## Step 3 — Use the Playground

The Playground is where you test models interactively without writing any code. It is the fastest way to prototype a prompt before building a full workflow.

### Opening the Playground

Click **Build → Playground** in the left navigation menu.

### The Playground interface

The screen is divided into two main areas:

- **Left panel — settings**: model selector, system prompt, and generation parameters
- **Right panel — chat**: the conversation thread where you type messages and see responses

### Choosing a model

At the top of the left panel, you will see a model selector dropdown. Click it to see the available models.

Each model is labelled with:

- Its name (e.g. `mistral-large-latest`, `mistral-small-latest`)
- A tier badge: **Open** (open-weight, Apache 2.0 licensed) or **Premier** (closed, commercial)
- Its context window size (e.g. 128k or 256k tokens)

For most research writing and reasoning tasks, start with **Mistral Large 3** (`mistral-large-latest`). For faster, cheaper iteration, try **Mistral Small 4** (`mistral-small-latest`). For complex reasoning, try **Magistral Medium** (`magistral-medium-latest`).

See [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/) for a full comparison.

### Writing a system prompt

The system prompt is a background instruction that the model always follows, regardless of what the user says. It is the main way to give the model a consistent role and set of constraints for your use case.

**Example system prompt for a literature assistant:**

```
You are a scientific writing assistant helping researchers at a university.
Always respond in clear, formal academic English.
When summarising a paper, include: main research question, methods, key findings, and limitations.
Never fabricate citations or references.
If you are unsure about something, say so explicitly.
```

Type your system prompt into the **System** field at the top of the left panel, then press Enter or click outside the field to save it.

### Sending your first message

Type a message in the chat input at the bottom of the right panel and press Enter or click the send button.

Try something straightforward to start:

```
Summarise the key differences between qualitative and quantitative research methods in three short paragraphs.
```

The model will respond in the right panel. You can continue the conversation by sending follow-up messages.

### Adjusting generation parameters

Below the system prompt, you will find several parameters that control how the model generates text:

| Parameter | What it does | Typical range |
|---|---|---|
| **Temperature** | Controls randomness. Higher = more varied, lower = more focused | 0.0 – 1.0; start at 0.3–0.7 |
| **Max tokens** | Maximum number of tokens in the response | 512 – 8192 depending on task |
| **Top P** | Alternative to temperature for controlling diversity | Usually leave at default |
| **Random seed** | Fix this to get reproducible outputs for the same input | Any integer |

For most research tasks, start with **Temperature 0.3** for factual or analytical tasks, and **Temperature 0.7** for creative or generative tasks. Leave other parameters at their defaults until you have a reason to change them.

!!! tip "Reproducibility"
    If you need to compare prompts fairly, set a fixed random seed. This ensures that differences between outputs come from your prompt changes, not random variation in generation.

### Comparing outputs across runs

A common workflow is to run the same prompt several times (with different seeds or slight prompt variations) to check whether the model gives consistent answers. If outputs vary widely, the task may need a tighter system prompt or a lower temperature.

---

## Step 4 — Save Your Prompts

AI Studio does not automatically save your Playground sessions permanently. Before closing the browser, copy any successful prompts (system prompt + example messages) into:

- A personal notes document
- A shared project folder
- A version-controlled file in your codebase

This allows you to rebuild the configuration next time and track how your prompts evolve.

---

## Step 5 — Request an API Key (if needed)

If you want to use Mistral models from your own code (Python, R, or any other language), you will need an API key. API keys are managed in the **API Keys** section of AI Studio.

At AAU, API key access is subject to an additional approval step. See [How to Access Mistral](/mistral/how-to-access/) for instructions on applying for workspace access with API key permissions.

Once approved, see [Using the API](/mistral/guides/ai-studio/using-the-api/) for step-by-step instructions.

---

## Step 6 — Monitor Usage

Once you start making API calls, click **Usage** in the left navigation panel. This shows:

- Total tokens consumed over time
- Breakdown by model
- Date range filters

Use the usage view to estimate costs before scaling up a workflow, and to identify unexpectedly expensive runs.

---

## Common Starting Tasks

| Task | Suggested starting point |
|---|---|
| Summarise a collection of PDFs | Playground with Mistral Large 3 + system prompt for summarisation |
| Generate code for data analysis | Playground with Mistral Small 4 or Codestral |
| Complex reasoning or calculation | Playground with Magistral Medium (Think-style model) |
| High-volume text processing via script | API with Mistral Small 4 for cost efficiency |
| Custom agent for a repeatable workflow | Agents section |

---

## Further Reading

- [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/) — Full model list with context windows and token costs
- [Using the API](/mistral/guides/ai-studio/using-the-api/) — API keys and code examples
- [AI Studio overview](/mistral/guides/ai-studio/) — What AI Studio offers and when to use it
- [Mistral Quickstart](https://docs.mistral.ai/getting-started/quickstart/) — Official quickstart guide with SDK examples
