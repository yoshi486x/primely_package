import configparser
import os
import pathlib
import subprocess
import sys

OUTPUT_DIR_PATH = 'data/tmp/txt'
PDF_DIR_PATH = 'data/input'
EXEC_CMD = 'pdf2txt.py'


class PdfReader(object):
    def __init__(self, filename):
        self.filename = filename

    def get_pdf_dir(self, suffix='.pdf'):
        """Organize input pdf path info"""

        return pathlib.Path(PDF_DIR_PATH, self.filename).with_suffix(suffix)

    def get_txt_dir(self, suffix='.txt'):
        """Organize output txt path info"""

        return pathlib.Path(OUTPUT_DIR_PATH, self.filename).with_suffix(suffix)

    # TODO Set classmethod regarding pdf and txt imports
    def convert_pdf_to_txt(self, input_file, output_file):
        """Call pdf2text.py
        :type input_file :str
        :type output_file :str
        """
        # TODO Error handle this process call
        try:
            subprocess.call([EXEC_CMD, '-V', '-o', str(output_file), str(input_file)])
        except:
            raise

        return 'success'


def main():
    filename = 'K_20180425'
    reader = PdfReader(filename)
    input_file = reader.get_pdf_dir()
    output_file = reader.get_txt_dir()

    A = reader.convert_pdf_to_txt(input_file, output_file)
    print(A)

if __name__ == "__main__":
    main()