import os
import re
import pypandoc

md_resume = "assets/"
docs = "assets/docs/"


def exclude_sections(input_file_temp, output_file):
    with open(input_file_temp, "r") as file:
        data = file.read()

    # remove all "atalhos/shortcuts" from convert file
    data = re.sub(r"\<!-- EXCLUDE - remove_init -  EXCLUDE -->.*?\<!-- EXCLUDE - remove_end -  EXCLUDE -->",
                  "", data, flags=re.DOTALL)
    data = re.sub(r"\#atalhos",
                  "", data, flags=re.DOTALL)
    data = re.sub(r"\#shortcuts",
                  "", data, flags=re.DOTALL)

    with open(output_file, "w") as file:
        file.write(data)


def convert_md_to_pdf(input_to_pdf, output_to_pdf):
    output = pypandoc.convert_file(input_to_pdf, "pdf", outputfile=output_to_pdf,
                                   extra_args=["--variable=geometry:margin=0.5cm"])
    assert output == ""


def convert_md_to_docx(input_to_docx, output_to_docx):
    output = pypandoc.convert_file(input_to_docx, "docx", outputfile=output_to_docx)
    assert output == ""


os.makedirs(docs, exist_ok=True)

for filename in os.listdir(md_resume):
    if filename.endswith(".md"):
        output_filename_pdf = filename.replace(".md", ".pdf")
        output_filename_docx = filename.replace(".md", ".docx")

        input_file = os.path.join(md_resume, filename)
        output_file_pdf = os.path.join(docs, output_filename_pdf)
        output_file_docx = os.path.join(docs, output_filename_docx)

        temp_file = "temp.md"
        exclude_sections(input_file, temp_file)

        convert_md_to_pdf(temp_file, output_file_pdf)
        convert_md_to_docx(temp_file, output_file_docx)

        os.remove(temp_file)
