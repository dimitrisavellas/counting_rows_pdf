
from PyPDF2 import PdfReader

def pdf_line_count(pdf_file):
    reader = PdfReader(pdf_file)
    line_count = 0
    for page in reader.pages:
        text = page.extract_text()
        if text:  # Ensure text is not None
            line_count += len(text.splitlines())
    return line_count

file_name = r"______.pdf" #enter the path of the desired pdf file
row_count = pdf_line_count(file_name)

print(f"Row count in the PDF is {row_count}")