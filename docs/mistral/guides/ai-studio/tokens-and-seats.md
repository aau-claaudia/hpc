# Tokens and Seats

This page explains how Mistral meters and bills usage, how seats and tokens work within the AAU setup, and how to manage your usage in AI Studio.


## Two Ways Mistral Measures Usage

Mistral uses two different models for measuring access and usage, depending on which interface you are using.

### Seats (Vibe)

**Vibe access is seat-based.** A seat is a named user license. AAU holds a number of seats as part of its institutional agreement with Mistral. After your [access application](/mistral/how-to-access/) is approved and you log in via AAU SSO, you are assigned a seat for your account.

Key points about seats:

- A seat gives you access to Vibe's full feature set.
- You do not pay per message — usage is covered institutionally up to the daily limits of the institutional agreement.
- Seats are tied to your AAU login. You cannot transfer or share a seat.
- Access depends on **seat availability**. We cannot guarantee a seat for every researcher at all times. Unused seats may be removed or reassigned so that access can be shared fairly.

### Tokens (AI Studio API)

**API access is token-based.** A token is Mistral's unit for measuring how much text is processed. Every API call you make consumes tokens — both for the text you send (input) and the text the model generates (output).

Key points about tokens:

- Input tokens: the system prompt + conversation history + your new message
- Output tokens: everything the model writes in response
- Input and output tokens are priced separately (output is generally more expensive)
- Token costs vary significantly by model — see [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/) for current rates
- At AAU, token usage within an AI Studio workspace is covered by the institution up to the workspace's standard monthly quota


## Understanding Token Consumption

### What counts as a token?

A token is approximately:

- 4 characters of English text
- ¾ of a word on average
- ~750 tokens per page of standard prose

This means:

| Item | Approximate token count |
|---|---|
| A single sentence | 15–30 tokens |
| A short paragraph (100 words) | ~130 tokens |
| One page of text | ~500–750 tokens |
| A 10-page paper | ~6,000–8,000 tokens |
| A complete conversation (5 exchanges) | 500–2,000 tokens (varies widely) |

### Why context window size matters

Every API call sends the **full conversation history** to the model, not just the latest message. This means that as a conversation grows longer, each subsequent call consumes more input tokens.

In a 10-turn conversation where each exchange is ~500 tokens, the 10th call sends approximately 5,000 tokens of history before even adding the new message.

**Practical implication:** For bulk processing, design your workflow to send each item as an independent call (no persistent history), rather than accumulating a long conversation.


## Viewing Your Usage in AI Studio

Token usage is tracked in real time in AI Studio.

### Where to find it

1. Log in to [console.mistral.ai](https://console.mistral.ai).
2. Click **Usage** in the left navigation panel.

### What the Usage view shows

- **Total tokens used** over a selected date range
- **Breakdown by model** — useful for identifying which model is driving most of your costs
- **Breakdown by API key** — useful if you have multiple keys for different workflows
- **Daily trend** — shows peaks that may correspond to large batch runs

### Getting usage per call in code

You can also log token usage from each individual API response:

```python
response = client.chat.complete(
    model="mistral-small-latest",
    messages=[{"role": "user", "content": "Hello"}]
)

usage = response.usage
print(f"Input tokens:  {usage.prompt_tokens}")
print(f"Output tokens: {usage.completion_tokens}")
print(f"Total tokens:  {usage.total_tokens}")
```

Logging this per call allows you to estimate the total cost of a workflow before running it at full scale.


## Token budget and quotas at AAU

At AAU, API access is tied to a dedicated workspace. Each AI Studio workspace has a **standard monthly usage quota**. AAU may adjust the monthly quota at any time if needed. See the [T&C](/mistral/terms-and-conditions/#15-fair-usage).

### How to check your remaining budget

Token usage at the workspace level is visible in AI Studio's Usage section. If you need to know the specific quota for your workspace, contact us.

### What happens when you approach the limit

- Monitor usage regularly during active development and batch runs.
- If your project requires a higher quota, request an increase through the [Serviceportal](https://serviceportal.aau.dk/serviceportal?id=emp_taxonomy_topic&topic_id=82a253e8838fc21053711d447daad328){target="_blank"}.
- Unexpected overruns may be caused by inefficient prompts, long context windows, or unintended loops in code — check the per-key breakdown in the Usage view.

### API key rotation

Rotate each API key at least every **30 days**. Deactivate the key when the project ends, you leave AAU, your role changes, or you suspect misuse. AAU can revoke any API key at any time.

**How to rotate a key:** In AI Studio, select the correct workspace. Go to **API Keys** → **My API keys** and use **Rotate key**. Then update your code with the new key.

If you suspect that an API key has been compromised or misused, revoke it at once and notify us. See [Responsible use of Mistral](/mistral/guides/responsible-use/#using-the-api) and [T&C §5](/mistral/terms-and-conditions/#5-api-keys).


## Cost Estimation Before a Large Run

Before running a batch job over hundreds or thousands of items, estimate the cost:

1. **Run 5–10 representative samples** through the API with usage logging.
2. **Calculate average tokens per call** (input + output).
3. **Multiply by the number of items** to get estimated total tokens.
4. **Check the price per million tokens** for your chosen model on [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/).

**Example calculation:**

- 500 abstracts to classify
- Average: 300 input tokens + 20 output tokens = 320 tokens per call
- Total: 500 × 320 = 160,000 tokens
- Model: Mistral Small 4 ($0.15/M input, $0.60/M output)
- Estimated cost: (500 × 300 / 1,000,000 × 0.15) + (500 × 20 / 1,000,000 × 0.60) ≈ $0.023 + $0.006 = **~$0.03**

For a large job using a more expensive model:

- 500 abstracts at Mistral Large 3 ($0.50/M input, $1.50/M output)
- Same token counts: (500 × 300 / 1,000,000 × 0.50) + (500 × 20 / 1,000,000 × 1.50) ≈ $0.075 + $0.015 = **~$0.09**

Always start with the smallest model that produces acceptable quality. The cost difference across models can be 10x or more.


## Reducing Token Usage

If you want to minimise token consumption:

| Strategy | Effect |
|---|---|
| Use a smaller model | Large cost reduction — often 5–10x cheaper with minimal quality loss for well-structured tasks |
| Shorten the system prompt | Fewer input tokens per call |
| Truncate conversation history | Prevents input tokens from growing with each turn |
| Reduce `max_tokens` | Prevents unexpectedly long (and expensive) outputs |
| Use Batch Inference | 50% discount on all token costs for async jobs |
| Set `temperature=0.0` for deterministic tasks | Avoids wasted tokens on re-runs due to inconsistent outputs |


## Batch Inference (50% Discount)

Batch inference processes requests asynchronously — you submit a job, it runs in the background, and results are available when the job completes. The cost is **50% lower** than synchronous API calls.

Batch inference is well suited for:

- Classifying or annotating large document collections
- Generating summaries for a corpus of papers
- Running extraction tasks over datasets

It is not suited for:

- Interactive use (results are not immediate)
- Workflows that need the model's response before deciding the next step


## Vibe usage limits

Although Vibe is seat-based, individual features have daily usage caps that reset each day. AAU users are on the institutional agreement; check the limits shown in the Vibe interface. For vendor-published tier comparisons, see [mistral.ai/pricing](https://mistral.ai/pricing).


## Summary

| | Vibe | AI Studio API |
|---|---|---|
| **How usage is measured** | Seats | Tokens |
| **Who pays** | Institution (seat license) | Institution (standard monthly quota) |
| **How to monitor** | Daily limits shown in Vibe interface | Usage dashboard in AI Studio |
| **Limits** | Per-feature daily caps; seat availability | Standard monthly quota, which AAU may adjust |
| **Cost control tips** | Stay within daily limits | Use small models, batch inference, efficient prompts |


## Further Reading

- [Models and Pricing](/mistral/guides/ai-studio/models-and-pricing/) — Per-model token costs
- [Responsible use of Mistral](/mistral/guides/responsible-use/#using-the-api) — How to rotate a key; binding rules in the T&C
- [How to access Mistral](/mistral/how-to-access/) — Applying for a dedicated workspace and API key access
- [Mistral pricing page](https://mistral.ai/pricing) — Official current pricing
- [Support](/mistral/support/) — Who to contact for quota questions
