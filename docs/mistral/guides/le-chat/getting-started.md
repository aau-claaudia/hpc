# Getting Started with Le Chat

This page walks you through your first session in Le Chat, from logging in to using the main features.

---

## Step 1 — Log In

Go to [chat.mistral.ai](https://chat.mistral.ai) and log in using your AAU credentials via SSO.

If you have not done this before, follow the full instructions on [How to Access Mistral](/mistral/how-to-access/).

---

## Step 2 — Explore the Interface

When you open Le Chat, you see a clean conversation screen. The key elements are:

- **Message input** — the text box at the bottom of the screen. This is where you write your prompt.
- **Conversation thread** — the area above the input, where the conversation builds up as you exchange messages.
- **Left sidebar** — your history of past conversations, organised by date. This is also where Projects and Libraries are accessible.
- **Mode selector** — a row of icons near the message input that lets you switch between response modes (Flash, Think, Deep Research).
- **Model indicator** — shows which model is currently active. Clicking it may allow you to switch between available models.

---

## Step 3 — Send Your First Message

Click the message input and type a task or question. Press **Enter** or click the send button.

A good first prompt is something you would normally do yourself but that would benefit from AI assistance:

```
I'm writing an abstract for a paper on patient-reported outcomes in chronic pain management. Can you help me structure the key elements it should include?
```

The model will respond in the thread above. You can continue the conversation by asking follow-up questions — the model keeps track of everything said in the current thread.

---

## Step 4 — Choose the Right Response Mode

Near the message input, you will see mode options. The most important ones are:

### Flash
Fast responses for simple tasks. Use this when you need a quick answer, a short rewrite, or a rapid draft. It has a daily usage limit.

### Standard (default)
The default mode. Balanced speed and quality. Good for most research writing and question-answering tasks.

### Think
The model reasons step by step before answering. Slower, but more reliable for complex tasks — calculations, multi-step logic, reviewing an argument. Use this when accuracy matters more than speed.

### Deep Research
The model breaks your question into sub-queries, searches the web, synthesises results, and writes a structured report with citations. Takes several minutes. Use this for background research, literature landscapes, or topic overviews before starting a formal search.

!!! tip "Try Think mode on hard questions"
    If you are asking something that requires multi-step reasoning or involves comparing several options, switch to Think mode. The extra processing time often produces noticeably more reliable results.

---

## Step 5 — Switch Models

Le Chat typically uses the best available Mistral model by default. Depending on your account tier, you may be able to select a different model from the model dropdown near the input bar. This can be useful to compare output quality or to choose a faster model for simpler tasks.

For a full description of Mistral's model families, see [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/).

---

## Step 6 — Save and Organise Conversations

### Saving conversations

Conversations are saved automatically in your history (left sidebar). Each session is listed with a short title generated from your first message.

### Renaming conversations

Click the three-dot menu next to a conversation in the sidebar and select **Rename** to give it a descriptive name you can find later.

### Deleting conversations

From the same three-dot menu, select **Delete** to remove a conversation permanently.

### Sharing conversations

Some versions of Le Chat allow you to generate a shareable link to a conversation. Use this with caution — shared links make the conversation's content visible to anyone with the link.

---

## Step 7 — Use Projects for Ongoing Work

If you are working on a research project over multiple sessions, create a **Project** to keep related conversations together and apply a consistent instruction to all of them.

1. In the left sidebar, click **New Project** (or the folder icon).
2. Name the project (e.g. "Systematic Review – COPD").
3. Optionally add a system instruction — a background prompt the model will always follow, for example:

```
You are assisting a researcher working on a systematic review of COPD interventions.
Always respond in formal academic English.
Focus on study design, outcomes, and limitations.
Do not fabricate citations.
```

All conversations you start within this project will follow that instruction automatically.

---

## Step 8 — Upload Documents to Your Library

If you have PDFs or other documents you want to query, upload them to your **Library**:

1. In the left sidebar, go to **Library**.
2. Click **Upload** and select your files.
3. Start a new conversation and ask questions that reference your documents.

Le Chat will retrieve relevant passages from your uploaded files and use them to ground its answers. This works well for:

- Asking questions across multiple papers at once
- Finding where a specific claim appears in a long report
- Summarising sections across several documents

See the [Le Chat overview](/mistral/guides/le-chat/) for storage limits per tier.

!!! warning "Level 1 data only"
    Only upload documents classified as Level 1 under AAU's data classification policy. Do not upload documents containing personal data, sensitive research data, or confidential information.

---

## Practical Tips for Getting Better Responses

### Be specific about the task

Vague prompts produce vague answers. Compare:

| Vague | Specific |
|---|---|
| "Help me with my abstract" | "Rewrite the following abstract to be more concise, targeting a general medical audience. Remove jargon and aim for 200 words." |
| "Summarise this" | "Summarise the methods section of the following paper in 3 bullet points, focusing on sample size, data collection method, and statistical analysis." |
| "What should I do?" | "I have interview data from 12 participants. What qualitative analysis methods are commonly used in health communication research, and which would you recommend for thematic analysis?" |

### State the output format

Tell the model how you want the answer presented:

- "Reply as a numbered list"
- "Write this as a short paragraph, max 100 words"
- "Format this as a table with columns for Author, Year, and Method"

### Use follow-up messages to refine

You do not need to get everything right in the first message. Ask for a first draft, then refine it:

- "Make it more formal"
- "Shorten the third paragraph"
- "Add a sentence about limitations"

### Give the model a role

Setting a role helps the model calibrate its response:

- "You are a statistician reviewing a clinical trial. Point out any problems with the reported statistical methods."
- "You are a native English speaker and academic editor. Improve the grammar and flow of the following text without changing the meaning."

---

## What to Do When the Output Is Wrong

- **Hallucinated citations**: Le Chat can invent references that do not exist. Always verify any citation independently before using it.
- **Incorrect facts**: Cross-check factual claims against authoritative sources, especially for recent events (the model has a training cutoff).
- **Off-topic responses**: If the model drifts from your intent, restate the task more explicitly in a new message or start a new conversation.
- **Too long / too short**: Specify the length explicitly ("Answer in no more than 150 words").

---

## Further Reading

- [Le Chat overview](/mistral/guides/le-chat/) — Full feature guide (Projects, Libraries, Memories, Canvas, and more)
- [Workflows and tips](/mistral/guides/le-chat/workflows-and-tips/) — Common research task patterns
- [Le Chat vs. AI Studio](/mistral/le-chat-vs-ai-studio/) — Choosing the right tool for the task
- [Official Mistral documentation](https://docs.mistral.ai/) — Full technical documentation
