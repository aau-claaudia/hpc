# Workflows and Tips

This page collects practical workflows and prompt patterns for common research tasks in Le Chat, along with guidance on getting consistent, high-quality results.

---

## Core Principles

Before diving into specific workflows, a few principles apply across all tasks:

- **Be specific.** The more concrete your instruction, the better the result. Vague prompts produce vague answers.
- **State the format.** Tell the model how you want the answer: bullet list, table, paragraph, numbered steps, or a specific word count.
- **Give the model a role.** "Act as an academic editor" or "You are a statistician reviewing a methods section" produces more targeted responses than an uncontextualized request.
- **Refine in steps.** You do not need to get everything right in the first message. Ask for a draft, then ask for specific improvements.
- **Verify everything.** The model can be wrong. Always check factual claims, citations, calculations, and code before using them.

---

## Writing and Editing Workflows

### Drafting an abstract

```
Write an abstract for a research paper with the following details:
- Topic: [your topic]
- Study design: [e.g. cross-sectional survey of 320 participants]
- Main finding: [your key result]
- Target journal: [journal name or type, e.g. general medical journal]
- Word limit: 250 words
Use standard IMRaD structure: background, objective, methods, results, conclusion.
```

### Improving clarity and flow

```
The following paragraph is from a methods section. Improve the grammar and clarity 
without changing the meaning. Keep it formal and academic.
Do not add information that is not already present.

[paste your paragraph]
```

### Reducing word count

```
Shorten the following text to no more than 150 words. 
Preserve all key findings and do not change the meaning. 
Remove redundant phrases and overly long sentences.

[paste your text]
```

### Translating between registers

```
Rewrite the following academic paragraph for a general (non-specialist) audience. 
Replace jargon with plain language. Aim for a reading level suitable for 
a newspaper article.

[paste your paragraph]
```

### Peer review simulation

```
Act as a critical peer reviewer for a top-tier journal in [your field].
Read the following methods section and identify:
1. Weaknesses in study design
2. Missing information that reviewers are likely to ask about
3. Potential sources of bias

[paste your methods section]
```

---

## Literature and Summarisation Workflows

### Summarising a paper

```
Summarise the following paper using these four headings:
1. Research question
2. Methods (include sample size, study design, and key measures)
3. Key findings
4. Limitations

Keep each section to 2-3 sentences. Do not add information not present in the text.

[paste the abstract or full text]
```

### Comparing multiple papers

Upload the papers to your [Library](/mistral/guides/le-chat/#libraries), then:

```
I have uploaded three papers on [topic]. 
Compare them on the following dimensions:
- Study design
- Sample characteristics
- Outcome measures
- Key findings

Present the comparison as a table.
```

### Identifying gaps in a field

```
Based on the following five abstracts, identify what research questions 
are not addressed by any of the studies. 
List potential gaps as bullet points.

[paste abstracts]
```

### Using Deep Research for background overviews

Switch to **Deep Research** mode and ask:

```
Give me a structured overview of the current state of research on 
[your topic]. Include key findings, main debates, and gaps. 
Cite sources.
```

!!! warning "Verify Deep Research citations"
    Deep Research retrieves information from the web and synthesises it, but citations can contain errors or hallucinations. Check every source independently before using it in academic work.

---

## Data and Analysis Workflows

### Designing a coding scheme

```
I am conducting qualitative analysis of interview transcripts about [topic].
Suggest an initial thematic coding scheme with 5-8 codes, each with:
- A code label
- A short definition
- An example of what would be coded under it
```

### Reviewing statistical methods

```
Act as a statistician. Review the following description of the statistical 
analysis plan for a clinical study. Identify any issues with:
- Choice of statistical test
- Handling of missing data
- Multiple comparisons
- Reporting of effect sizes

[paste your analysis plan]
```

### Generating a data extraction template

```
I am conducting a systematic review on [topic]. 
Design a data extraction table with columns for all variables 
I should record from each included study.
Include: study design, population, intervention/exposure, 
comparator, outcomes, and follow-up duration.
```

---

## Prompt Patterns That Work Well

### The role + task + constraint pattern

```
[Role]: You are a scientific writing assistant.
[Task]: Rewrite the following abstract to improve clarity and conciseness.
[Constraints]: Keep it under 200 words. Do not change the meaning. 
Use formal academic English.
```

### The few-shot example pattern

Show the model an example of what you want:

```
I want you to classify research abstracts by study design. 
Here is an example:

Abstract: "We conducted a randomised controlled trial with 200 participants..."
Classification: RCT

Abstract: "In this retrospective cohort study, we followed 1,500 patients..."
Classification: Cohort study

Now classify the following abstract:
[paste your abstract]
```

### The step-by-step instruction pattern

For multi-part tasks, break them into numbered steps:

```
1. Read the following abstract.
2. Identify the main research question.
3. Identify the study design.
4. List the outcome measures.
5. Write a two-sentence critical appraisal of the methods.

Abstract:
[paste your abstract]
```

### The critique-and-improve pattern

```
Here is a draft paragraph. 
First, list its weaknesses as bullet points.
Then rewrite it addressing those weaknesses.

[paste your draft]
```

---

## Using Projects Effectively

Projects in Le Chat let you apply a persistent system instruction to all conversations within a topic. This removes the need to re-explain context every session.

**Example system instructions for common research use cases:**

*For a literature review project:*
```
You are a research assistant helping with a systematic review of [topic].
Always respond in English.
When asked to summarise a study, include: study design, sample, methods, 
main findings, and limitations.
Never fabricate citations.
```

*For a writing project:*
```
You are an academic writing assistant for a researcher in [field].
Always respond in formal academic English.
When editing text, explain your changes briefly.
Do not add content that is not already present in the original.
```

*For a teaching preparation project:*
```
You are helping a university lecturer prepare teaching materials for 
an undergraduate course in [subject].
Explain concepts clearly and at the level of a second-year student.
Use concrete examples.
```

---

## Common Mistakes and How to Avoid Them

| Mistake | What happens | What to do instead |
|---|---|---|
| Asking a vague question | The model gives a generic, unhelpful answer | Add context: who you are, what the task is, what format you need |
| Trusting citations without checking | You cite a non-existent paper | Always verify references in a database (e.g. PubMed, Scopus) |
| Using the same conversation for many unrelated tasks | The model gets confused by conflicting context | Start a new conversation for each distinct task |
| Not using Projects for recurring tasks | You repeat the same setup instructions every session | Create a Project with a system instruction for recurring work |
| Pasting sensitive data | Data may be stored or logged | Only use Level 1 data. Never paste personal data or confidential information. |
| Accepting the first draft | First drafts are rarely optimal | Ask for revisions, alternatives, or a critique of the output |

---

## Important Reminders

!!! warning "Level 1 data only"
    Only use data classified as Level 1 under AAU's data classification policy. Do not paste personal data, patient information, confidential research findings, or any restricted information into Le Chat.

!!! info "Human review is always required"
    All AI-generated content must be reviewed before use. Check facts, verify citations, and edit for accuracy and appropriateness before submitting anything produced with AI assistance.

---

## Further Reading

- [Le Chat overview](/mistral/guides/le-chat/) — Full feature guide
- [Getting started with Le Chat](/mistral/guides/le-chat/getting-started/) — First steps and interface walkthrough
- [Le Chat vs. AI Studio](/mistral/le-chat-vs-ai-studio/) — When to use which tool
- [Terms and Conditions](/mistral/terms-and-conditions/) — Usage rules for AAU researchers
