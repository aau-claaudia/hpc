# TAAURUS batch LLM helper scripts

Used by [Batch LLM inference on TAAURUS](../../docs/taaurus/guides/batch-llm.md).

## `batch_llm_data.py`

Prepare `input.jsonl`, validate it, and split into Slurm chunks.

```bash
mkdir -p /media/<your-project>/scripts
cp batch_llm_data.py /media/<your-project>/scripts/
```

### Commands

| Command | Purpose |
|---------|---------|
| `prepare` | Convert source data → `input.jsonl` |
| `validate` | Check required fields and unique `id`s |
| `split` | Create `chunk_000.jsonl`, … for Slurm arrays |

### `prepare --source` formats

| `--source` | Input | Extra requirements |
|------------|--------|-------------------|
| `csv` | `.csv` file | Optional `--csv-header`, `--id-column`, `--text-column` |
| `xlsx` | `.xlsx` file | `pip install openpyxl`, `--sheet` name or index |
| `txt-dir` | folder of `.txt` files | None |
| `txt-lines` | one snippet per line | None |
| `pdf-dir` | folder of `.pdf` files | `pdftotext` (Poppler) on PATH |
| `docx-dir` | folder of `.docx` files | `pip install python-docx` |
| `jsonl` | existing JSONL | None |

### Examples

```bash
SCRIPT=/media/myproject/scripts/batch_llm_data.py
OUT=/media/myproject/data/input.jsonl

# CSV
python $SCRIPT prepare --source csv --csv-header \
  --id-column id --text-column text \
  --input notes.csv --output $OUT

# Excel
python $SCRIPT prepare --source xlsx --sheet 0 \
  --id-column record_id --text-column note_text \
  --input notes.xlsx --output $OUT

# PDF folder
python $SCRIPT prepare --source pdf-dir \
  --input pdfs/ --output $OUT

# Word folder
python $SCRIPT prepare --source docx-dir \
  --input docx/ --output $OUT

# Validate + split
python $SCRIPT validate --input $OUT
python $SCRIPT split --input $OUT --output chunks/ --num-chunks 100
```
