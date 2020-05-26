import os


def extract_filenames(pdf_dir):
    """Extract filename without suffix"""

    all_files=[]

    for item in os.listdir(pdf_dir):
        filename, _ = os.path.splitext(item)
        all_files.append(filename)

    return sorted(all_files)


if __name__ == "__main__":
    print(extract_filenames())