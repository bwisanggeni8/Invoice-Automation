import os
from typing import Any, Dict

from openai import OpenAI
from dotenv import load_dotenv
from pydantic import ValidationError

from app.schemas import Invoice

#run on terminal with:
# "python3 -m app.services.llm_parser" make sure to run it on "Invoice-Automation" folder

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

import json

SYSTEM_PROMPT = (
    "You are an assistant that extracts structured data from invoices. "
    "Only respond with valid JSON with the fields: "
    "invoice_number, invoice_date, supplier_name, total_amount, currency."
)


def build_user_prompt(invoice_text: str) -> str:
    return (
        "Extract the following fields from this invoice text:\n"
        "- invoice_number\n"
        "- invoice_date\n"
        "- supplier_name\n"
        "- total_amount\n"
        "- currency\n\n"
        "If a field is missing, use null.\n\n"
        f"Invoice text:\n{invoice_text}"
    )


def parse_invoice_from_text(invoice_text: str) -> Invoice:
    """
    Calls the LLM to extract invoice data and returns an Invoice model.
    """

    prompt = build_user_prompt(invoice_text)

    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        # if your version complains about this, just delete response_format and keep rest
        response_format={"type": "json_object"},
    )

    raw_output = completion.choices[0].message.content  # JSON string
    data: Dict[str, Any] = json.loads(raw_output)

    try:
        invoice = Invoice(**data)
    except ValidationError as e:
        raise ValueError(f"Failed to validate invoice data: {e}")

    return invoice

