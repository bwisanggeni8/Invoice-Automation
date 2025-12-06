from io import BytesIO
from pypdf import PdfReader


def extract_text_from_pdf(file_bytes: bytes) -> str:
    from io import BytesIO
    from pypdf import PdfReader

    pdf_file = BytesIO(file_bytes)
    reader = PdfReader(pdf_file)
    texts = []

    for page in reader.pages:
        page_text = page.extract_text() or ""
        texts.append(page_text)

    full_text = "\n".join(texts).strip()
    print("DEBUG: extracted text length =", len(full_text))  # <--- add this

    return full_text
