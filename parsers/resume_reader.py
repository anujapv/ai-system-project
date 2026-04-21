import fitz  # PyMuPDF
import docx


def read_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)

    for page in doc:
        # use "blocks" instead of plain text
        blocks = page.get_text("blocks")

        # sort blocks top to bottom
        blocks = sorted(blocks, key=lambda b: b[1])

        for block in blocks:
            text += block[4] + "\n"

    return text


def read_docx(file_path):
    doc = docx.Document(file_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return "\n".join(text)


def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return read_pdf(file_path)
    elif file_path.endswith(".docx"):
        return read_docx(file_path)
    else:
        return ""