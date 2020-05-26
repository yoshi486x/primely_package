import configparser
import os
import pathlib

OUTPUT_PATH = 'data/tmp/txt'

def get_base_dir_path(file_path):
    """
    input: __file__
    output: Return a path of the package's home directory (three upper parents)"""
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(file_path))))

# def setup_output_dir(child_dir=''):
def setup_output_dir(output_dir):

    # output_dir = pathlib.Path(OUTPUT_PATH, child_dir)
    if not os.path.exists(output_dir):
        pathlib.Path(output_dir).mkdir(parents=True)
    else:
        # print('Designated directory `{}{}` already exists.'.format(OUTPUT_PATH, child_dir))    
        print('Designated directory `{}` already exists.'.format(output_dir))    