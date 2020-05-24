import os
import pathlib

# from primely.views import utils

PDF_DIR_PATH = 'data/input'


def extract_filenames(all_files=[]):
    """Extract filename without suffix"""
    print('listdir:', os.listdir(PDF_DIR_PATH))

    for item in os.listdir(PDF_DIR_PATH):
        filename, _ = os.path.splitext(item)
        all_files.append(filename)

    return sorted(all_files)

# class InputQueue(object):
    # def __init__(self, all_files=None):

    # def extract_filenames(self, all_files=[]):
    #     """Extract filename without suffix"""

    #     for item in os.listdir(PDF_DIR_PATH):
    #         filename, _ = os.path.splitext(item)
    #         all_files.append(filename)
    #     # self.all_files = sorted(all_files)
    #     return sorted(all_files)

    # def get_filename_list(self):
    #     return self.all_files



if __name__ == "__main__":
    # inputQueue = InputQueue()
    # inputQueue.load_pdf_filenames()
    # inputQueue.extract_filenames()
    # print('pdf_files:', inputQueue.pdf_files)
    # print('all_files:', inputQueue.all_files)

    # print(inputQueue.extract_filenames())
    print(extract_filenames())