import pdfplumber
import os

# How to get the text out in boxes????


def extract_text(DIR):
    texts = []
    for file in os.listdir(DIR):
        pdf_text = []
        with open(os.path.join(DIR, file)) as pdf:
            for page in pdf.pages:
                pdf_text.append(page.extract_text(y_tolerance=1))
        texts.append(pdf_text)
    return texts
