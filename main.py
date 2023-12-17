import pypandoc


def convert_md_to_pdf(input_file, output_file):
    output = pypandoc.convert_file(input_file, 'pdf', outputfile=output_file)
    assert output == ""


convert_md_to_pdf('assets/resume_br.md', 'assets/resume_br.pdf')
