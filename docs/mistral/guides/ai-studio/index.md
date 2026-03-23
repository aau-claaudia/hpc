# AI Studio

## What is AI Studio?

[Mistral AI Studio](https://console.mistral.ai/) (previously called "La Plateforme") is the developer-oriented counterpart to Le Chat. Where Le Chat is designed for conversational use, AI Studio is built for structured experimentation, API integration, and building repeatable AI-powered workflows.

At AAU, AI Studio is available through the same SSO login as Le Chat. API key access requires an additional step — see [How to Access Mistral](/mistral/how-to-access/) for details on requesting workspace access.

---

## When to Use AI Studio vs. Le Chat

| Use case | Le Chat | AI Studio |
|---|---|---|
| Quick Q&A, drafting, summarisation | Yes | — |
| Iterative prompt refinement | Possible | Better |
| Testing multiple models on the same prompt | — | Yes |
| Programmatic API access from code | — | Yes |
| Building repeatable, automated workflows | — | Yes |
| Configuring and deploying custom agents | Limited | Yes |
| Tracking usage and token costs | — | Yes |

Use Le Chat when you need fast, conversational assistance. Use AI Studio when you want to work deliberately with prompts, compare models, or connect Mistral to your own code and tools.

---

## Key Sections of AI Studio

### Playground

The Playground is an interactive interface for testing models directly in the browser, without writing code. It is the fastest way to experiment with different models, system prompts, and parameters.

See [Getting Started with AI Studio](/mistral/guides/ai-studio/getting-started/) for a step-by-step walkthrough of the Playground.

### Models

The Models section lists all available Mistral models with their capabilities, context window sizes, and pricing. You can filter by category (generalist, code, reasoning, audio, document AI) and see which API identifier to use in your code.

See [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/) for a full overview.

### API Keys

API keys are what allow your code to authenticate with Mistral's API. You create and manage API keys in the **API Keys** section of AI Studio. Each key is associated with your workspace.

See [Using the API](/mistral/guides/ai-studio/using-the-api/) for instructions on creating keys and making your first API call.

### Workspaces

A Workspace is an organisational container in AI Studio. It groups API keys, usage statistics, and deployed agents. At AAU, researchers who apply for API access will receive a named workspace (separate from the default workspace). You can switch between workspaces using the workspace selector in the top-left corner of AI Studio.

### Usage

The Usage section shows your token consumption over time, broken down by model and date. This is where you track how much API usage your project is accumulating and identify which models or prompts are consuming the most tokens.

### Agents

AI Studio's Agents interface lets you configure, test, and deploy custom AI agents. An agent has:

- A **model** (which Mistral model powers it)
- A **system prompt** (instructions that always apply)
- Optional **tools** (web search, code interpreter, document library, or custom function calls)
- A **deployment endpoint** so external applications can call the agent via API

Agents are useful for building repeatable AI workflows that go beyond single-turn chat. See the [Mistral Agents documentation](https://docs.mistral.ai/agents/introduction/) for technical details.

### Fine-Tuning

Fine-tuning allows you to adapt a Mistral base model to your own dataset. This produces a custom model that behaves differently from the standard version — for example, one that always formats output in your preferred structure, or that is specialised in a narrow domain.

Fine-tuning is an advanced feature. See the [Mistral Fine-Tuning documentation](https://docs.mistral.ai/deprecated/finetuning/) for guidance on dataset format and the training process.

---

## A Practical Workflow for Researchers

A typical AI Studio workflow for a research task looks like this:

1. **Define the task clearly.** What exactly do you want the model to do? Write it as a precise instruction.
2. **Open the Playground.** Choose a model appropriate for the task (see [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/)).
3. **Write a system prompt.** This is background context the model always follows, e.g. "You are a scientific writing assistant. Always respond in formal academic English. Be concise. Do not fabricate citations."
4. **Test with several examples.** Try the prompt on at least three to five representative inputs. Note where it works and where it fails.
5. **Refine the prompt.** Change one thing at a time. Compare before and after.
6. **Move to the API.** Once the prompt works reliably, move to code using the API so the workflow can be run programmatically or in bulk.
7. **Track usage.** Monitor the Usage section to understand token consumption and cost.

---

## Good Practices

- Change one variable at a time when refining prompts. Changing both the model and the prompt simultaneously makes it hard to know which change caused the improvement.
- Document successful prompt patterns. AI Studio does not save your prompt history automatically. Copy good prompts into your own notes or a shared document.
- Use the cheapest model that does the job well. Smaller models are dramatically cheaper and faster, and they often handle well-structured tasks just as well as larger ones.
- Start with a small sample. Test your prompt on five to ten examples before running it over hundreds of documents.
- Build human review into the workflow. Do not route AI outputs directly to publication or submission without a review step.

---

## Important Limitations

!!! warning "Level 1 data only"
    AI Studio must only be used with data classified as Level 1 under AAU's data classification policy. Do not enter personal data, confidential research findings, patient data, or any sensitive information into prompts or uploaded documents. See [Terms and Conditions](/mistral/terms-and-conditions/) for full details.

!!! info "API keys are per workspace"
    API keys generated in your personal workspace will not work against a project workspace, and vice versa. Make sure you are creating keys in the correct workspace before starting an integration.

!!! info "AI output requires human review"
    All AI-generated content must be reviewed by a human before use. This applies whether the output was generated in Le Chat, in the Playground, or via the API.

---

## Further Reading

- [Getting Started with AI Studio](/mistral/guides/ai-studio/getting-started/) — Playground walkthrough and first steps
- [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/) — Model comparison and token costs
- [Using the API](/mistral/guides/ai-studio/using-the-api/) — API keys, code examples, and best practices
- [Le Chat Guide](/mistral/guides/le-chat/) — Conversational interface for everyday AI assistance
- [Mistral AI Studio documentation](https://docs.mistral.ai/deployment/ai-studio/) — Official Mistral documentation
- [How to Access Mistral](/mistral/how-to-access/) — Login and workspace access for AAU users
