# Invoice Automation App (MVP)

A minimal end-to-end demo of how AI can automate invoice processing.

Upload a PDF invoice → the app extracts the text → an LLM parses it into structured fields → the result is shown in a simple web UI.

This project is intentionally small and focused. It is the **v0.1 MVP** for a larger automation portfolio.
---

## Features

- Upload a PDF invoice through a web form
- Extract text from the PDF using `pypdf`
- Call the OpenAI API to parse:
  - `invoice_number`
  - `invoice_date`
  - `supplier_name`
  - `total_amount`
  - `currency`
- Display structured fields and raw extracted text in a browser

**Current limitation:**  
Only works reliably for **text-based PDFs**. Scanned/image-based invoices will not extract text yet (OCR planned as a next step).

---

## Tech Stack

- **Backend:** Python, FastAPI
- **AI / LLM:** OpenAI API (`gpt-4.1-mini` in JSON schema mode)
- **PDF extraction:** `pypdf`
- **Templating:** Jinja2
- **Validation:** Pydantic models
- **Server:** Uvicorn

---

## Project Structure

```text
invoice-automation-app/
  app/
    __init__.py
    main.py            # FastAPI app and routes
    schemas.py         # Pydantic Invoice model
    services/
      __init__.py
      pdf_extractor.py # PDF → text
      llm_parser.py    # text → Invoice via OpenAI
    templates/
      upload.html      # upload form
      result.html      # display parsed invoice
  static/
    styles.css         # minimal styling
  requirements.txt
  .env.example
  .gitignore
  LICENSE
  README.md
