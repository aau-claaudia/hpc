# Le Chat

## What is Le Chat?

Le Chat is Mistral's conversational AI assistant, available at [chat.mistral.ai](https://chat.mistral.ai). It is designed for interactive, browser-based use: you write a message, the model responds, and the conversation continues. Le Chat is the right starting point for most everyday AI tasks — drafting, summarising, explaining, translating, brainstorming, and exploring ideas.

At AAU, Le Chat is available to all researchers through SSO login. See [How to Access Mistral](/mistral/how-to-access/) for step-by-step login instructions.

---

## The Chat Interface

When you open Le Chat, you land on a clean conversation screen. The main elements are:

- **Message input** — the text box at the bottom where you type your prompts
- **Conversation history** — the thread of messages above, scrollable
- **Sidebar** — your list of past conversations, organised by date and (optionally) into Projects
- **Mode selector** — a row of icons or a dropdown near the message input that lets you switch between response modes
- **Library and Project controls** — accessible from the left sidebar

New conversations start blank. Each message you send is part of a running thread; the model always has access to everything said earlier in that thread, up to its context limit.

---

## Response Modes

Le Chat offers several modes that change how the model processes and answers your prompt. The right choice depends on the type of task.

### Flash (Fast Answers)

Flash is the quickest response mode. The model answers immediately without extra reasoning steps, making it well suited for:

- Short factual questions
- Quick reformulations or rephrasing
- Generating a first draft that you will revise yourself
- Simple summarisations

Flash answers have a daily usage limit (up to 150 per day on the free tier, up to 200 per day on the Pro tier). Use this mode when speed matters more than depth.

### Standard (Default)

The default mode uses Mistral's flagship model for a balanced response: fast enough for interactive use, capable enough for most research and writing tasks. This is what you get when you send a message without selecting a specific mode.

Standard mode is a good fit for:

- Writing and editing text
- Question answering with moderate complexity
- Literature search summaries
- Code generation and explanation

### Think Mode (Extended Reasoning)

Think mode activates the model's chain-of-thought reasoning. Before giving a final answer, the model works through the problem step by step internally, then presents the result. This produces more reliable answers on tasks that require multi-step logic.

Use Think mode for:

- Mathematical or statistical calculations
- Logical problems with several constraints
- Tasks where intermediate reasoning needs to be correct (e.g. study design, method selection)
- Reviewing the plausibility of an argument

Think mode responses take longer than standard answers. The model may show its reasoning process in the response. Usage is limited (up to 30x the free baseline for Pro users).

!!! tip "When to use Think"
    If you find the model giving inconsistent answers or missing steps in a complex task, switch to Think mode. The additional processing time often produces noticeably more reliable results.

### Deep Research (Preview)

Deep Research is a multi-step autonomous research mode. Rather than answering in a single pass, the model breaks your question into sub-queries, searches the web, synthesises the results, and writes a structured report with citations.

Use Deep Research for:

- Getting a structured overview of an unfamiliar topic
- Producing a literature landscape with references before starting a systematic search
- Comparing approaches or tools across multiple sources
- Background research for grant writing or proposals

Deep Research takes several minutes to complete and produces a longer, cited document. Usage is limited (up to 5x the free baseline per day for Pro users). Always verify the citations manually — the model can occasionally misattribute or hallucinate sources.

!!! warning "Verify sources from Deep Research"
    Deep Research retrieves and synthesises information from the web, but citations must be checked before use in academic work. Do not cite a source you have not read yourself.

---

## Projects

Projects let you group related conversations into named workspaces within Le Chat. Instead of a flat list of chats, you can organise your work by topic, study, or task.

**How to create a project:**

1. In the left sidebar, click **New Project** or the folder icon.
2. Give the project a name.
3. Optionally add a system instruction — a background instruction the model will follow in all conversations within this project (e.g. "You are reviewing biomedical papers. Always respond in English. Focus on methods and limitations.").

**What projects are for:**

- Keeping conversations for one research topic together
- Sharing a consistent system instruction across multiple sessions
- Organising iterative prompt development over time

The free tier supports a limited number of projects. Pro users can create up to 1,000 projects. You can move existing conversations into a project from the conversation options menu.

---

## Libraries

Libraries allow you to upload documents and make them searchable within your conversations. This is a form of retrieval-augmented generation (RAG): the model can search your uploaded documents to ground its answers in your own material rather than relying on general training knowledge.

**What you can upload:**

- PDFs (papers, reports, manuals)
- Word documents
- Text files
- Spreadsheets and CSVs

**How to use a Library:**

1. Open the sidebar and go to **Library**.
2. Upload one or more documents.
3. Start or continue a conversation and ask questions that reference your uploaded material.
4. The model will retrieve relevant passages and answer based on them, usually with references to the source document.

**Storage limits:**

| Tier | Storage |
|---|---|
| Free | Limited |
| Pro | Up to 15 GB |
| Team | Up to 30 GB per user |

!!! info "Libraries vs. attaching a file to a chat"
    Attaching a file to a single message makes the model read that file once. Uploading to a Library makes the document persistently searchable across all your conversations. Use Libraries for documents you will return to repeatedly.

!!! warning "Data classification"
    Only upload documents classified as Level 1 under AAU's data classification policy. Documents containing personal data, sensitive research data, or confidential information must not be uploaded. See [Terms and Conditions](/mistral/terms-and-conditions/) for details.

---

## Memories

Memories allow Le Chat to remember facts about you across conversations. When the model notices something worth remembering (e.g. your preferred language, your field, your writing style preferences), it can store this as a memory and recall it in future sessions.

**Capabilities:**

- The model stores facts automatically when you share them ("I work on cardiovascular epidemiology" or "I prefer concise answers without bullet points").
- You can view, edit, and delete memories from the **Memories** section in your account settings.
- Memories are personal to your account and are not shared with others.

**Storage limits:**

| Tier | Memories |
|---|---|
| Free | Up to 500 memories |
| Pro | Up to 1,000 memories |

!!! tip "Getting the most from Memories"
    Tell Le Chat explicitly what you want it to remember: your role, your institution, what kind of output you prefer, which citation style you use, or anything else that would help it personalise its responses consistently.

---

## Canvas Mode

Canvas is a collaborative document-editing interface within Le Chat. Instead of the model returning an answer as chat text, it opens a side panel with a full document or code block that you can edit directly and ask the model to refine section by section.

Canvas is useful for:

- Drafting longer texts (article sections, grant application paragraphs, documentation)
- Writing and iterating on code files
- Building structured documents where you want fine-grained control over individual sections

**How to use Canvas:**

1. Start a conversation and ask the model to write or draft something longer.
2. Click the **Canvas** icon in the response toolbar, or type something like "open this in canvas".
3. The document opens in a side-by-side editor.
4. You can click any part of the document and ask the model to "rewrite this paragraph", "make this more formal", or "add a methods section".

Canvas mode is available to Pro and higher tier users.

---

## Image Generation

Le Chat can generate images directly from a text description. To use it:

1. Type a description of the image you want.
2. The model produces one or more images in the conversation.
3. You can ask for variations, adjustments, or a different style.

Free users can generate images with a daily limit. Pro users receive a higher daily quota.

!!! info "Academic use of generated images"
    Images generated by AI tools are generally not appropriate as evidence or data in academic publications. They can be useful for presentations, diagrams, or concept illustrations — but always be transparent about AI involvement and check your institution's policies.

---

## Voice Mode

Voice mode allows you to speak to Le Chat directly through your microphone. The model responds in text (or voice, depending on the interface version). This can be useful for dictating content, getting spoken summaries, or working hands-free.

Voice mode is currently available on Pro and higher plans, with expanded availability on Team and Enterprise tiers.

---

## Web Search

Le Chat can search the internet in real time to answer questions requiring current information. When web search is active, the model queries the web, retrieves relevant pages, and synthesises the answer with citations.

Web search is useful when you need:

- Recent news or developments in a field
- Current statistics or data
- Information that postdates the model's training cutoff

The number of additional web searches beyond the default is limited by plan tier.

!!! tip "Combining web search with your own documents"
    You can use web search for background context while also referencing your Library documents. Ask the model to "compare what the literature says with what is in my uploaded paper" for a grounded comparison.

---

## Code Interpreter

The code interpreter allows Le Chat to write and execute code within the conversation. The model can:

- Write Python scripts and run them to produce results
- Create plots, tables, and visualisations
- Perform calculations on data you provide
- Test and debug code step by step

This is useful for quick data analysis, statistical checks, or visualisation without needing a local development environment.

Code interpreter usage is limited (up to 5x the free quota for Pro users).

---

## Connectors

Connectors integrate Le Chat with external tools and data sources. With connectors enabled, you can interact with services directly from the chat interface.

**Available options:**

- A directory of 40+ pre-built enterprise connectors (e.g. for productivity suites, databases, and business tools) — available from the free tier
- Custom MCP (Model Context Protocol) connectors for connecting to your own tools and APIs — available on Pro and higher tiers

Connectors must be authorised and configured from your account settings before use.

---

## Agents (Preview)

Agents are customisable AI assistants that you configure for a specific task. Each agent has:

- A **system prompt** that defines its purpose and behaviour
- Optional **tools** (web search, code interpreter, document library)
- A persistent **conversation state** across sessions

You can build an agent that always functions as a literature reviewer, a data analyst, or a writing assistant, without having to re-explain the context in every session.

Agents are available on Pro and Team plans and are accessible from the sidebar.

See the [Mistral Agents documentation](https://docs.mistral.ai/agents/introduction/) for a technical overview.

---

## Practical Tips for Researchers

### Writing and editing

- Use standard mode for first drafts; switch to Think mode if you need the model to reason through structure or argument.
- Use Canvas mode for longer documents where you want iterative section-by-section refinement.
- Ask the model to adopt a specific role: "Act as a reviewer and identify weaknesses in the following methods section."

### Literature and summarisation

- Upload PDFs to your Library and ask: "What are the main findings of these papers?" or "What methods do papers 1 and 3 have in common?"
- Use Deep Research to get a rapid landscape overview before starting a formal systematic review. Use the output as a starting point, not a final source.

### Structuring your work

- Create a Project for each active research topic. Add a system instruction that gives the model context: your field, your audience, the tone you want.
- Use Memories to store your preferences so you do not need to repeat them every session.

### Checking and verifying

- Never submit AI-generated text without reading and editing it yourself.
- Always verify citations and factual claims independently.
- Deep Research reports should be treated as a first-pass synthesis, not a citable source.

---

## Important Limitations

!!! warning "Level 1 data only"
    Le Chat must only be used with data classified as Level 1 under AAU's data classification policy. Do not enter personal data, confidential research findings, or any sensitive information into Le Chat. See [Terms and Conditions](/mistral/terms-and-conditions/) for full details.

!!! info "AI output requires human review"
    Le Chat can produce plausible-sounding but incorrect information. All outputs should be reviewed critically before use in any academic or professional context.

---

## Further Reading

- [Mistral AI Documentation](https://docs.mistral.ai/) — Official documentation for all Mistral products
- [AI Studio Guide](/mistral/guides/ai-studio/) — For structured prompt work, API access, and model experimentation
- [How to Access Mistral](/mistral/how-to-access/) — Login instructions for AAU users
- [Terms and Conditions](/mistral/terms-and-conditions/) — Usage rules for the AAU deployment
