import re
import warnings
import src.utils as utils

def update_static():
    """Opens and modifies your static.py file for first time setup"""
    if not utils.get_bool_input("Update static.py configuration?"):
        print('Aborting update_static')
        return None
    else:
        msg = "Provide path to the data directory used on your machine:"
        data_dir = utils.get_filepath(msg)
        while data_dir.endswith('CS504-Project'):
            print("Provided data directory is inside of curent repo. Do not upload data to GitHub ",
                  "reference a local data directory outide of the local repo.")
            data_dir = utils.get_filepath(msg)
        with open('./src/static.py', 'r') as file_handle:
            python = file_handle.readlines()
        new_lines = list()
        for line in python:
            pat = 'DATA_DIR: str = '
            if pat in line:
                match = re.search(pat, line)
                try:
                    start, end = match.span()
                except Exception as error:
                    raise error('config.py failed, set DATA_DIR manually.')
                line = line[:end] + f'"{data_dir}"'
            new_lines.append(line)
        with open('./src/static.py', 'w') as file_handle:
            file_handle.writelines(new_lines)

if __name__ == '__main__':
    update_static()