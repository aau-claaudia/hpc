!!! warning "Preview — not final guide" 
    This guide is a preview of how batch LLM inference on TAAURUS *could* work. It is not the finalized and production-ready. Paths, tooling, and workflows may change before the official guide is published.

# Batch LLM Inference on TAAURUS

This guide explains how to run large-scale batch inference using **vLLM** on TAAURUS.

**Typical use case:**

> Processing 1,000–1,000,000 documents (e.g. clinical notes, journals, research text) using an LLM.


!!! info "What is vLLM?"
    **vLLM** is an open-source inference engine for large language models. It can power chat APIs and live serving, but **this guide is only for batch jobs**: you prepare a fixed input file, submit Slurm jobs, and collect output files when they finish. There is no interactive chat session or back-and-forth prompting here.

    You run vLLM inside a Singularity container and point it at model weights under `/shared/models/` (for example Llama 3 8B or Mistral 7B).

---

# What you will do in this guide

You will take a JSONL dataset, split it into chunks, and run offline inference on TAAURUS GPUs using a shared vLLM container and a model from `/shared/models/`. After a quick single-chunk test, you submit a Slurm array job so many chunks run in parallel—each job reads one chunk and writes its own output file. When the array finishes, you merge those files into one result set.

---

# 1. Shared resources (read-only)

You need to use the shared **vLLM container** (`/shared/containers/vllm-llm.sif`) and one of the shared **model weights** in `/shared/models/` (for example Llama 3 8B or Mistral 7B). Every TAAURUS project runs the same `vllm-llm.sif` image—**you do not need to copy it** into your project folder. 

Your **inputs, job scripts, logs, and outputs** stay under `/media/<your-project>/`; that is what keeps projects isolated.

```bash
/shared/containers/vllm-llm.sif    # vLLM container

/shared/models/
    llama3-8b/                     # weights — choose per job
    mistral-7b/
```

With Slurm, run the vLLM container with Singularity (for example `srun -G1 singularity exec --nv /shared/containers/vllm-llm.sif python /app/vllm_batch.py --model /shared/models/llama3-8b …`). Many projects may use the same container and models at once; that is expected.

### ✔ Why this is safe

* **`.sif` containers are immutable** — Singularity runs them as read-only images; your job cannot alter the shared `.sif` for other users.
* **Models are read-only** — weights are loaded for inference only, not written back into `/shared/models/`.
* **No project secrets in shared paths** — prompts, documents, and results live in `/media/<your-project>/`, not in `/shared/`.

---

# 2. Prepare Your Input Data

Batch jobs expect **one JSON object per line** (JSONL). Each line must have:

| Field | Meaning |
|-------|---------|
| `id` | Unique identifier for the row (number or string) |
| `text` | One **document** — the full text the model should process in a single job step |

Each document needs to be in one line. The entire body lives in `text` (use `\n` inside the string if you exported multiline text):

```json
{"id": "1042", "text": "Patient presents with chest pain radiating to the left arm.\nECG normal. Plan: observation and repeat troponin in 6 hours."}
{"id": "1043", "text": "Follow-up visit. Symptoms improved."}
```

Save the file under your project, for example:

```bash
/media/<your-project>/work/vllm/input.jsonl
```

??? example "Need help converting your data to JSONL?"

    vLLM batch jobs cannot read PDF, Word, or Excel files directly. Every document must end up as one line in `input.jsonl` with `id` and `text`. The workflow is always the same:

    1. **Collect** raw files under `/media/<your-project>/work/vllm/raw/`
    2. **Convert** to `input.jsonl` (helper script or manual export)
    3. **Validate** the JSONL before submitting Slurm jobs

    ```mermaid
    flowchart LR
      raw[CSV Excel TXT PDF DOCX] --> jsonl[input.jsonl]
      jsonl --> validate[validate]
      validate --> chunks[chunk_*.jsonl]
    ```

    ### Get the helper script


    ```bash
    mkdir -p /media/<your-project>/work/vllm
    ```

    Copy the following helper script to your project directory 
    
    ```bash
    cp /shared/scripts/batch_llm_data.py /media/<your-project>/work/vllm
    ```
    
    The script prepares and checks JSONL. CSV and plain text need **no extra packages**. Excel, PDF, and Word need optional tools (noted per format below).
  
    Set paths once (adjust project name):

    ```bash
    mkdir -p /media/<your-project>/work/vllm/raw
    ```

    ```bash
    export PROJECT=/media/<your-project>
    export SCRIPT=$PROJECT/work/vllm/batch_llm_data.py
    export RAW=$PROJECT/work/vllm/raw
    export OUT=$PROJECT/work/vllm/input.jsonl
    ```

    ---

    ### CSV spreadsheets

    **When to use:** You already exported from a database, REDCap, R, pandas, etc. One row = one document.

    **Example file** — `raw/notes.csv`:

    ```csv
    record_id,note_text
    1042,"Patient presents with chest pain..."
    1043,"Follow-up visit. Symptoms improved."
    ```

    **Convert:**

    ```bash
    python $SCRIPT prepare \
      --source csv --csv-header \
      --id-column record_id --text-column note_text \
      --input $RAW/notes.csv \
      --output $OUT
    ```

    !!! tip "Semicolons or European Excel CSV"
        If columns are separated by `;`, open the file in LibreOffice and export as UTF-8 CSV with comma delimiter, or fix the delimiter before converting.

    ---

    ### Excel workbooks (`.xlsx`)

    **When to use:** Colleagues shared an `.xlsx` file with one row per document.

    **Example layout** — sheet `Notes`, columns `record_id` and `note_text` (same as CSV above).

    === "Option A — export to CSV (no extra install)"

    1. Open the workbook in Excel or LibreOffice.
    2. **Save As** → CSV UTF-8.
    3. Run the [CSV](#csv-spreadsheets) steps on the exported file.

    === "Option B — convert directly (needs openpyxl)"

    ```bash
    python -m pip install --user openpyxl

    python $SCRIPT prepare \
      --source xlsx \
      --id-column record_id --text-column note_text \
      --sheet Notes \
      --input $RAW/notes.xlsx \
      --output $OUT
    ```

    Use `--sheet 0` for the first sheet, or the exact sheet name.

    !!! warning "One row = one document"
        If a single cell contains a very long note, that is fine—the whole cell becomes `text`. Do not put multiple unrelated documents in one row.

    ---

    ### Plain text

    === "One `.txt` file per document (recommended)"

    **When to use:** Notes, reports, or chapters saved as separate files; filenames become `id`.

    ```bash
    $RAW/notes/
      visit_1042.txt
      visit_1043.txt
    ```

    ```bash
    python $SCRIPT prepare \
      --source txt-dir \
      --input $RAW/notes/ \
      --output $OUT
    ```

    === "One document per line in a single file"

    **When to use:** Only for short, single-line snippets—not multi-paragraph clinical notes.

    `raw/snippets.txt`:

    ```text
    First short snippet.
    Second short snippet.
    ```

    ```bash
    python $SCRIPT prepare \
      --source txt-lines \
      --input $RAW/snippets.txt \
      --output $OUT
    ```

    ---

    ### PDF files

    **When to use:** Scanned reports, papers, or exports saved as one PDF per document.

    Batch inference needs **extracted text**. Layout, figures, and tables may be lost or garbled—always spot-check a few files.

    === "Option A — `pdftotext` + helper script (recommended on Linux)"

    Requires [Poppler](https://poppler.freedesktop.org/) (`pdftotext` on PATH). One PDF per file:

    ```bash
    $RAW/pdfs/
      article_001.pdf
      article_002.pdf
    ```

    ```bash
    python $SCRIPT prepare \
      --source pdf-dir \
      --input $RAW/pdfs/ \
      --output $OUT
    ```

    === "Option B — extract to `.txt` first, then convert"

    Useful if `pdftotext` is unavailable or you want to edit OCR output before inference:

    ```bash
    mkdir -p $RAW/pdfs_txt
    for f in $RAW/pdfs/*.pdf; do
      pdftotext -enc UTF-8 "$f" "$RAW/pdfs_txt/$(basename "$f" .pdf).txt"
    done

    python $SCRIPT prepare --source txt-dir --input $RAW/pdfs_txt/ --output $OUT
    ```

    === "Option C — export on your own PC"

    Open the PDF in a desktop tool, copy or export as plain text, save under `$RAW/notes/` as `.txt`, then use [txt-dir](#plain-text).

    ---

    ### Word documents (`.docx`)

    **When to use:** Protocols, summaries, or reports stored as Word files—one file per document.

    === "Option A — LibreOffice (no Python packages)"

    ```bash
    mkdir -p $RAW/docx_txt
    libreoffice --headless --convert-to txt --outdir $RAW/docx_txt $RAW/docx/*.docx

    python $SCRIPT prepare --source txt-dir --input $RAW/docx_txt/ --output $OUT
    ```

    === "Option B — helper script (needs python-docx)"

    ```bash
    python -m pip install --user python-docx

    python $SCRIPT prepare \
      --source docx-dir \
      --input $RAW/docx/ \
      --output $OUT
    ```

    !!! warning "Legacy `.doc` format"
        Convert old `.doc` files to `.docx` or plain text in Word/LibreOffice first. The helper script only reads `.docx`.

    ---

    ### Already JSONL

    **When to use:** Another tool already produced JSONL, but field names or formatting may be inconsistent.

    ```bash
    python $SCRIPT prepare \
      --source jsonl \
      --input $RAW/export.jsonl \
      --output $OUT
    ```

    Each line must include `text`; `id` is optional (line numbers are used if missing).

    ---

    ### Validate before submitting jobs

    Always run validation after conversion—regardless of source format:

    ```bash
    python $SCRIPT validate --input $OUT
    ```

    Expected output:

    ```text
    OK: 1042 records, required fields present, ids unique
    ```

    | Problem | What to do |
    |---------|------------|
    | `missing required field 'text'` | Ensure every row has non-empty text |
    | `duplicate id` | Make filenames or ID columns unique |
    | `pdftotext` / `openpyxl` not found | Use the manual export option for that format, or install the listed package |
    | Empty PDF/Word extraction | Scanned PDFs may need OCR first; check one file manually |

---

# 3. Split Data into Batch Chunks

Slurm array jobs run **one chunk per task**. Split `input.jsonl` into smaller files (match `--num-chunks` to your planned array size, e.g. `100` chunks → `#SBATCH --array=0-99`).

You need `input.jsonl` from [section 2](#2-prepare-your-input-data) (required fields: `id` and `text` on each line). This guide uses:

```bash
/media/<your-project>/work/vllm/input.jsonl
```

If you created the file elsewhere, move or copy it there, or change `--input` below to match your path. The optional [conversion guide](#need-help-converting-your-data-to-jsonl) above uses the same layout but you do not need to have followed it.

Copy the split helper script once (from the cluster shared path):

```bash
mkdir -p /media/<your-project>/work/vllm/chunks
cp /shared/scripts/batch_llm_data.py /media/<your-project>/work/vllm/
```

Split the input file (replace `<your-project>` with your project folder name):

```bash
python /media/<your-project>/work/vllm/batch_llm_data.py split \
  --input /media/<your-project>/work/vllm/input.jsonl \
  --output /media/<your-project>/work/vllm/chunks/ \
  --num-chunks 100
```

### Result

```bash
/media/<your-project>/work/vllm/chunks/
  chunk_000.jsonl
  chunk_001.jsonl
  ...
```

---

# 4. Select Your Model

Available models:

```bash
/shared/models/llama3-8b/
/shared/models/mistral-7b/
/shared/models/mixtral-8x7b/
```

## Recommended for L40 GPUs:

✔ Llama 3 8B (fast + stable)
✔ Mistral 7B (lightweight + efficient)

---


# 5. Test Single Chunk (Recommended First Step)

Before submitting the full array, run one chunk interactively on a GPU node (replace `<your-project>`):

```bash
mkdir -p /media/<your-project>/work/vllm/outputs

srun -G1 singularity exec --nv \
  /shared/containers/vllm-llm.sif \
  python /app/vllm_batch.py \
  --model /shared/models/llama3-8b \
  --input /media/<your-project>/work/vllm/chunks/chunk_000.jsonl \
  --output /media/<your-project>/work/vllm/outputs/test.jsonl
```

✔ Confirm `/media/<your-project>/work/vllm/outputs/test.jsonl` exists  
✔ Check the job log for errors

---

# 6. Create Slurm Job Script

Create the batch script under your project (replace `<your-project>`):

```bash
mkdir -p /media/<your-project>/work/vllm/jobs \
         /media/<your-project>/work/vllm/logs \
         /media/<your-project>/work/vllm/outputs
```

File path:

```bash
/media/<your-project>/work/vllm/jobs/vllm_batch.sbatch
```

Full script (adjust partition, GPU type, and array range to match your chunk count):

```bash
#!/bin/bash
#SBATCH --job-name=vllm-batch
#SBATCH --partition=gpu
#SBATCH --gres=gpu:l40:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=80G
#SBATCH --time=04:00:00
#SBATCH --array=0-99
#SBATCH --output=/media/<your-project>/work/vllm/logs/%x_%A_%a.out

set -euo pipefail

module load singularity

export TRANSFORMERS_OFFLINE=1
export HF_DATASETS_OFFLINE=1
export VLLM_NO_USAGE_STATS=1

PROJECT=/media/<your-project>
CONTAINER=/shared/containers/vllm-llm.sif
MODEL=/shared/models/llama3-8b

INPUT_DIR=$PROJECT/work/vllm/chunks
OUTPUT_DIR=$PROJECT/work/vllm/outputs
mkdir -p "$OUTPUT_DIR"

INPUT_FILE=${INPUT_DIR}/chunk_$(printf '%03d' ${SLURM_ARRAY_TASK_ID}).jsonl
OUTPUT_FILE=${OUTPUT_DIR}/output_${SLURM_ARRAY_TASK_ID}.jsonl

singularity exec --nv \
  "$CONTAINER" \
  python /app/vllm_batch.py \
  --model "$MODEL" \
  --input "$INPUT_FILE" \
  --output "$OUTPUT_FILE"
```

Replace `<your-project>` in the `#SBATCH --output=` and `PROJECT=` lines with your real project folder name (same value as elsewhere in this guide).

---

# 7. Submit Your Job

```bash
sbatch /media/<your-project>/work/vllm/jobs/vllm_batch.sbatch
```

---

# 8. Monitor Progress

## Check running jobs

```bash
squeue -u $USER
```

## View logs

```bash
tail -f /media/<your-project>/work/vllm/logs/vllm-batch_*.out
```

---

# 9. Collect Output Results

Each array task writes one file:

```bash
/media/<your-project>/work/vllm/outputs/output_0.jsonl
/media/<your-project>/work/vllm/outputs/output_1.jsonl
...
```

## Merge results

```bash
cat /media/<your-project>/work/vllm/outputs/output_*.jsonl \
  > /media/<your-project>/work/vllm/final_results.jsonl
```

---

# 10. Output Format

Each result looks like:

```json
{
  "id": 42,
  "result": "Patient shows improved symptoms with no complications."
}
```


!!! tip "Performance Best Practices (L40 GPUs)"

    **✔ Use batching**

    * Process multiple prompts at once

    **✔ Keep chunk sizes balanced**

    * Recommended: 500–2000 documents per chunk

    **✔ Use smaller models when possible**

    * 7B–8B models are optimal
