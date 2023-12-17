import os
import pypandoc

docs = "assets/"


def convert_md_to_pdf(input_to_pdf, output_to_pdf):
    output = pypandoc.convert_file(input_to_pdf, "pdf", outputfile=output_to_pdf)
    assert output == ""


def convert_md_to_docx(input_to_docx, output_to_docx):
    output = pypandoc.convert_file(input_to_docx, "docx", outputfile=output_to_docx)
    assert output == ""


for filename in os.listdir(docs):
    if filename.endswith(".md"):
        output_filename = filename.replace(".md", ".pdf")

        input_file = os.path.join(docs, filename)
        output_file = os.path.join(docs, output_filename)

        convert_md_to_pdf(input_file, output_file)

for filename in os.listdir(docs):
    if filename.endswith(".md"):
        output_filename = filename.replace(".md", ".docx")

        input_file = os.path.join(docs, filename)
        output_file = os.path.join(docs, output_filename)

        convert_md_to_docx(input_file, output_file)

