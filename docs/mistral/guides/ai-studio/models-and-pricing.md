# Models and Pricing

This page describes the main Mistral models available through AI Studio, what they are suited for, and how API pricing works. For the official and always up-to-date model list, see the [Mistral models documentation](https://docs.mistral.ai/getting-started/models/models_overview/).

---

## How to Browse Models in AI Studio

In [AI Studio](https://console.mistral.ai/), click **Models** in the left navigation menu. Each model card shows:

- The model name and its API identifier (the string you use in your code)
- Context window size (how much text the model can process in one call)
- Tier: **Open** (open-weight, Apache 2.0) or **Premier** (commercial license)
- Price per million input and output tokens

You can also compare models side by side using the [Mistral model comparison tool](https://docs.mistral.ai/getting-started/models/compare).

---

## Model Families

### Generalist Models

These are the main models for writing, reasoning, question answering, summarisation, and multimodal tasks.

#### Mistral Large 3

The flagship open-weight model. Best overall performance across a wide range of tasks. Supports text and image input.

| Property | Value |
|---|---|
| API identifier | `mistral-large-latest` |
| Context window | 256k tokens |
| Tier | Open (Apache 2.0) |
| Input price | $0.50 / 1M tokens |
| Output price | $1.50 / 1M tokens |

**Best for:** Complex reasoning, nuanced writing, literature analysis, multimodal document understanding, tasks requiring high accuracy.

#### Mistral Medium 3.1

A frontier-class model balancing high performance with moderate cost. Multimodal (text + image). Good middle ground between Large and Small.

| Property | Value |
|---|---|
| API identifier | `mistral-medium-latest` |
| Context window | 128k tokens |
| Tier | Premier |
| Input price | $0.40 / 1M tokens |
| Output price | $2.00 / 1M tokens |

**Best for:** High-quality generation tasks where Large 3 is not required. Document processing with moderate complexity. Multimodal inputs.

#### Mistral Small 4

A hybrid model combining instruction following, coding, and reasoning in a compact, efficient architecture. Excellent cost-to-quality ratio.

| Property | Value |
|---|---|
| API identifier | `mistral-small-latest` |
| Context window | 256k tokens |
| Tier | Open (Apache 2.0) |
| Input price | $0.15 / 1M tokens |
| Output price | $0.60 / 1M tokens |

**Best for:** High-volume processing (classification, extraction, formatting), coding assistance, tasks where cost matters. Often sufficient for well-structured prompts.

#### Ministral 3 Family (3B, 8B, 14B)

Compact, highly efficient models for edge deployment or cost-sensitive workloads. Multimodal.

| Model | API identifier | Context | Input price | Output price |
|---|---|---|---|---|
| Ministral 3 3B | `ministral-3b-latest` | 128k | Low | Low |
| Ministral 3 8B | `ministral-8b-latest` | 128k | Low | Low |
| Ministral 3 14B | `ministral-3-14b-latest` | 128k | Low | Low |

**Best for:** Lightweight tasks, high-volume batch processing where cost is the primary constraint.

!!! info "Check current prices"
    Prices for the Ministral family and other models are regularly updated. Always verify current pricing on the [Mistral pricing page](https://mistral.ai/pricing) or the individual model pages at [docs.mistral.ai](https://docs.mistral.ai/getting-started/models/models_overview/).

---

### Reasoning Models (Magistral)

Magistral models are built for step-by-step, transparent reasoning. They think through problems explicitly before giving a final answer, which makes them significantly more reliable on tasks with multi-step logic.

#### Magistral Medium 1.2

Mistral's frontier reasoning model. Multilingual, multimodal, with transparent chain-of-thought output.

| Property | Value |
|---|---|
| API identifier | `magistral-medium-latest` |
| Context window | 128k tokens |
| Tier | Premier |
| Input price | $2.00 / 1M tokens |
| Output price | $5.00 / 1M tokens |

**Best for:** Complex reasoning tasks, mathematical calculations, multi-step logical problems, tasks where you need to see the reasoning process. More expensive — use when accuracy justifies the cost.

#### Magistral Small 1.2

A smaller, open-weight version of the Magistral reasoning approach.

| Property | Value |
|---|---|
| API identifier | `magistral-small-latest` |
| Context window | 128k tokens |
| Tier | Open (Apache 2.0) |
| Input price | Lower than Medium | 
| Output price | Lower than Medium |

**Best for:** Reasoning tasks where the Medium model is too expensive, and where a smaller model with explicit chain-of-thought is sufficient.

See [Mistral Reasoning documentation](https://docs.mistral.ai/capabilities/reasoning/) for more on how reasoning models work.

---

### Code Models

#### Codestral

Purpose-built for code generation, completion, and understanding. Optimised for low-latency, high-frequency developer workflows including fill-in-the-middle (FIM).

| Property | Value |
|---|---|
| API identifier | `codestral-latest` |
| Context window | 128k tokens |
| Tier | Premier |
| Input price | $0.30 / 1M tokens |
| Output price | $0.90 / 1M tokens |

**Best for:** Code completion, code generation from natural language, code review, debugging. Also available for use in IDE integrations.

#### Devstral 2

Mistral's frontier code-agent model. Designed for autonomous multi-step software engineering tasks — exploring codebases, editing files, executing tools.

| Property | Value |
|---|---|
| API identifier | `devstral-latest` |
| Context window | 128k tokens |
| Tier | Open (Apache 2.0) |

**Best for:** Agentic coding workflows, automated code refactoring, multi-file edits.

See [Mistral Coding documentation](https://docs.mistral.ai/capabilities/code_generation/) for examples.

---

### Document AI Models

#### OCR 3

A specialised model for optical character recognition. Extracts text, tables, and structured content from PDFs, scans, and images with high accuracy.

| Property | Value |
|---|---|
| API identifier | `mistral-ocr-latest` |
| Tier | Premier |
| Pricing | Per page processed |

**Best for:** Converting scanned documents to machine-readable text, extracting data from forms, processing large document collections.

See [Mistral Document AI documentation](https://docs.mistral.ai/capabilities/document_ai/) for details.

---

### Audio Models (Voxtral)

#### Voxtral Mini Transcribe 2

An audio model optimised for transcription of speech to text.

| Property | Value |
|---|---|
| API identifier | `voxtral-mini-latest` |
| Tier | Premier |

**Best for:** Transcribing interviews, lectures, and recordings for qualitative analysis.

See [Mistral Audio documentation](https://docs.mistral.ai/capabilities/audio_transcription/) for details.

---

### Embeddings

#### Mistral Embed

Produces numerical vector representations of text for semantic search and similarity tasks.

| Property | Value |
|---|---|
| API identifier | `mistral-embed` |
| Tier | Premier |

**Best for:** Building semantic search over document collections, clustering texts by topic, finding similar passages across a corpus.

See [Mistral Embeddings documentation](https://docs.mistral.ai/capabilities/embeddings/) for details.

---

## Understanding Token Pricing

API usage is billed in **tokens**. A token is roughly four characters or three-quarters of a word in English. One page of dense text is approximately 500–750 tokens.

Pricing is charged separately for:

- **Input tokens**: everything you send to the model (system prompt + conversation history + current message)
- **Output tokens**: everything the model generates in response

Output tokens typically cost more than input tokens.

### Example cost estimates

| Task | Estimated token usage | Approx. cost (Mistral Small 4) | Approx. cost (Mistral Large 3) |
|---|---|---|---|
| Summarise a 5-page paper | ~3,000 input + ~500 output | ~$0.0008 | ~$0.002 |
| Extract data from 100 short texts | ~50,000 input + ~10,000 output | ~$0.014 | ~$0.040 |
| Classify 1,000 abstracts (~200 tokens each) | ~200,000 input + ~10,000 output | ~$0.036 | ~$0.115 |
| Generate a 2,000-word report | ~1,000 input + ~2,500 output | ~$0.003 | ~$0.009 |

!!! info "These are estimates only"
    Actual token counts depend on the language, prompt structure, and output length. Use the [Mistral tokenizer](https://docs.mistral.ai/getting-started/glossary/) or test a few calls manually to get accurate estimates for your specific workflow.

### Batch discount

Mistral offers a 50% discount on requests submitted through the [Batch Inference API](https://docs.mistral.ai/capabilities/batch/). Batch jobs are processed asynchronously (not in real time) and are well suited for large-scale processing tasks where latency is not critical.

---

## Choosing the Right Model

Use the following decision logic as a starting point:

```
Is the task straightforward (extraction, formatting, classification)?
  → Start with Mistral Small 4. Cheap and fast.

Does the task need nuanced writing, complex reasoning, or multimodal input?
  → Use Mistral Large 3.

Does the task involve step-by-step mathematical or logical reasoning?
  → Use Magistral Medium 1.2.

Is the task primarily about code?
  → Use Codestral (completion/generation) or Devstral 2 (agents).

Do you need to process large numbers of documents with OCR?
  → Use OCR 3.

Do you need to transcribe audio?
  → Use Voxtral Mini Transcribe 2.

Do you need semantic search over documents?
  → Use Mistral Embed.
```

!!! tip "Start with the small model"
    Run your prompt on Mistral Small 4 first. If the output quality is acceptable, you can save significant cost at scale. If the small model fails consistently on a task, then move up to Large 3.

---

## Model Versioning

Mistral model identifiers include a version date (e.g. `mistral-large-2512` for the December 2025 version of Mistral Large). The `*-latest` aliases (e.g. `mistral-large-latest`) always point to the current recommended version. Pinning to a specific version date is recommended for production workflows where reproducibility matters.

Old versions are eventually deprecated. Mistral provides advance notice before deprecation. Check the [deprecation table](https://docs.mistral.ai/getting-started/models/models_overview/) for retirement dates.

---

## Further Reading

- [Full model list at docs.mistral.ai](https://docs.mistral.ai/getting-started/models/models_overview/)
- [Model comparison tool](https://docs.mistral.ai/getting-started/models/compare)
- [Batch Inference documentation](https://docs.mistral.ai/capabilities/batch/)
- [Mistral pricing page](https://mistral.ai/pricing)
- [Using the API](/mistral/guides/ai-studio/using-the-api/)
