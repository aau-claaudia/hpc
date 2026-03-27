# When to use Le Chat vs. AI Studio

Mistral offers two distinct interfaces under the same login. This page explains what each one is, how they differ in access and cost, and when to use which.

---

## Quick overview

| | Le Chat | AI Studio |
|---|---|---|
| **What it is** | A conversational chat interface | A developer and experimentation platform |
| **Who it's for** | Anyone using Mistral for writing, research, or day-to-day tasks | Researchers and developers building structured workflows or using the API |
| **Access required** | AAU SSO login (immediate) | AAU SSO login + optional workspace application for API keys |
| **Interface** | [chat.mistral.ai](https://chat.mistral.ai) | [console.mistral.ai](https://console.mistral.ai) |

---

## Le Chat — The Chat Interface

Think of Le Chat like a smarter version of a search engine you have a conversation with. You type a message, it responds, and you keep the dialogue going. No setup, no code, no technical knowledge needed.

**Use Le Chat when you want to:**

- Get help writing or editing — abstracts, emails, reports, grant sections
- Summarise a paper, document, or set of notes
- Ask questions and explore a topic through conversation
- Upload a PDF and ask questions about it 
- Give the model a standing instruction it always follows 
- Generate images or get research ideas quickly

**Do not use Le Chat when you need to:**

- Process many documents automatically (e.g. classify 500 abstracts)
- Connect Mistral to your own code or data pipeline
- Track exactly how much each request costs

### Model selection in Le Chat

Yes — Le Chat has a model selector near the message input. You can switch between available Mistral models (such as Mistral Large or Mistral Small) depending on whether you want faster or more capable responses. The available models may vary by account tier.

### RAG in Le Chat (Libraries)

**RAG** stands for Retrieval-Augmented Generation. It means the AI searches through your own documents before answering, so responses are grounded in your material rather than just general knowledge.

In Le Chat this is called **Libraries**: you upload PDFs or other documents, and the model searches them when you ask questions. This is useful for querying a set of papers, a report, or any document you want to interrogate without reading it manually.

### Custom instructions in Le Chat (Projects)

You can give the model a **standing instruction** that applies to every conversation within a Project — for example: *"Always reply in formal academic English. When summarising a paper, include the study design, findings, and limitations."* This is set once and remembered for all sessions in that project.

---

## AI Studio — The Developer Platform

AI Studio is for users who want to go beyond chat. It lets you test models more systematically, call Mistral from code, and build automated workflows — but it requires more technical comfort.

**Use AI Studio when you want to:**

- Test whether a prompt works reliably before using it at scale
- Choose exactly which model to use and fine-tune its behaviour
- Call Mistral from Python or another programming language
- Run the same task across many documents automatically
- Build a custom RAG pipeline over your own document collection
- Track token usage and control costs precisely
- Build a custom AI agent or automate a research workflow

**You do not need AI Studio if** you are only looking for conversational help — Le Chat handles that faster and more simply.

### Model selection in AI Studio

Yes — and with full control. In the **Playground** you select any model from a dropdown before sending a message. In code via the **API** you specify the exact model by name (e.g. `mistral-large-latest` or `mistral-small-latest`). This lets you compare models side by side or pick the most cost-efficient one for a given task. See [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/) for the full list.

### RAG in AI Studio

In AI Studio you can build more advanced RAG pipelines: use the **Embeddings API** to convert your documents into searchable vectors, store them in a database, and retrieve relevant passages before each model call. This scales to large document collections and gives you full control over what the model sees. For a simpler starting point, the **Agents** feature includes a built-in document library tool that handles retrieval automatically — no extra code needed.

### Custom instructions in AI Studio (system prompt)

Every model call — in the Playground or via the API — accepts a **system prompt**: a standing instruction the model always follows. This is the same concept as Projects in Le Chat, but more flexible. You can change it per task, test different versions side by side, and include it programmatically in every API request.

---

## Quick Comparison

| | Le Chat | AI Studio |
|---|---|---|
| Needs coding knowledge | No | For API access: yes |
| Good for writing and Q&A | Yes | Use Le Chat instead |
| Select which model to use | Yes — limited choice | Yes — full control |
| Search your own documents (RAG) | Yes — via Libraries | Yes — via Agents or Embeddings API |
| Give the model standing instructions | Yes — via Projects | Yes — via system prompt |
| Process many documents at once | No | Yes |
| Control model parameters (temperature etc.) | No | Yes |
| Track costs per request | No | Yes |
| Build automated workflows | No | Yes |

---

## How Each Product Meters Usage

Mistral uses two different models for measuring access and usage, depending on which interface you are using.

### Seat-based access (Le Chat)

Le Chat access at AAU is managed as **seats** — the institution holds a number of named user licenses. Your AAU SSO login grants you a seat automatically. You do not pay per message or per token; usage is covered institutionally.

Each seat gives you access to Le Chat's full feature set, subject to daily limits per feature (see [Le Chat Guide](/mistral/guides/le-chat/) for details).

### Token-based access (AI Studio API)

API access is billed by **tokens** — the unit Mistral uses to measure how much text is processed. Tokens are consumed for every API call:

- **Input tokens** — everything you send to the model (system prompt + conversation history + new message)
- **Output tokens** — the model's response

Token costs vary by model. Pricing is listed on the [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/) page and on [mistral.ai/pricing](https://mistral.ai/pricing).

At AAU, API token usage within an approved project workspace is covered by the institution up to an agreed quota. Contact CLAAUDIA if you need to understand your project's token budget.

!!! info "Keep track of your usage"
    Token usage is visible in the **Usage** section of AI Studio. Check it regularly to avoid unexpected overruns, especially during development and testing.

---

## Which Should You Use?

### Use Le Chat if you:

- Want a quick answer, draft, or summary
- Are exploring a topic or refining ideas through conversation
- Need to upload and interrogate a specific document
- Want the model to remember your preferences across sessions
- Are not writing code and do not need bulk processing

### Use AI Studio if you:

- Want to test multiple prompt variants systematically
- Need to run a task over many inputs (classification, extraction, summarisation at scale)
- Want to call Mistral from Python or another programming language
- Are building an automated research pipeline
- Need to track token usage and control costs
- Want to build a reusable agent with specific tools

### Use both if you:

- Want to prototype a prompt quickly in Le Chat, then move the refined version to AI Studio for bulk processing
- Are exploring whether Mistral fits a task (Le Chat first, then AI Studio to scale it)

---

## Quick Reference

| What you want to do | What to do |
|---|---|
| Use Le Chat for writing and research assistance | Log in via AAU SSO — no application needed |
| Test models in the AI Studio Playground | Log in via AAU SSO — no application needed |
| Use the API from code | Log in first, then apply for workspace access via the CLAAUDIA Serviceportal |
| Understand token costs | See [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/) |
| Get help | See [Support](/mistral/guides/ai-studio/support/) or contact CLAAUDIA |

---

## Before You Start

- You must comply with [AAU's terms and conditions](/mistral/terms-and-conditions/) for Mistral.
- You must accept [Mistral's terms of service](https://chat.mistral.ai/legal/terms) on first login.
- You must only use the service with data classified as Level 1 under [AAU's data classification policy](https://www.security.aau.dk/data-classification).

---

## Further Reading

- [How to Access Mistral](/mistral/how-to-access/) — Step-by-step login and API key application
- [Le Chat Guide](/mistral/guides/le-chat/) — Full feature walkthrough for Le Chat
- [AI Studio Guide](/mistral/guides/ai-studio/) — Full guide for AI Studio
- [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/) — Which model to choose and what it costs
- [Tokens and Seats](/mistral/guides/ai-studio/tokens-and-seats/) — Detailed explanation of usage metering
- [Official Mistral documentation](https://docs.mistral.ai/) — Mistral's own documentation for both products
