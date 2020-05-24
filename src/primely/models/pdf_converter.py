import os
import pathlib
import subprocess

EXEC_CMD = 'pdf2txt.py'


def convert_pdf_to_txt(filename, pdf_dir, txt_dir):
    """From given filename, convert a corresponding PDF file to Text file"""

    pdf_path = pathlib.Path(pdf_dir, filename).with_suffix('.pdf')
    txt_path = pathlib.Path(txt_dir, filename).with_suffix('.txt')

    subprocess.call([EXEC_CMD, '-V', '-o', str(txt_path), str(pdf_path)])

    return 'success'


if __name__ == "__main__":
    pass