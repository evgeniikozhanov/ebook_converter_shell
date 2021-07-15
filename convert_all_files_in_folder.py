# Command 'ebook-convert' use for convert from fb2 to mobi

import subprocess
from os import path, walk, remove


FILES_TO_CONVERT_PATH = './files/'
EXTENSIONS_CONVERT_PAIRS = {
    'fb2': 'mobi'
}


def get_file_type(filename):
    return filename.split('.')[-1]


def get_new_file_name(filename, convert_pairs_dict):
    return '.'.join(filename.split('.')[:-1]) + '.' + convert_pairs_dict.get(get_file_type(filename), 'unknown')


def get_list_of_files(file_path, extensions):
    all_files_deep_list = [path.join(dp, f) for dp, dn, fn in walk(path.realpath(file_path)) for f in fn]
    return [f for f in all_files_deep_list if get_file_type(f) in extensions.keys()]


def convert_file_with_ebook_convert_util(filepath_from, filepath_to):
    subprocess.run(['ebook-convert', filepath_from, filepath_to])


if __name__ == '__main__':
    files_to_convert = get_list_of_files(FILES_TO_CONVERT_PATH, EXTENSIONS_CONVERT_PAIRS)
    for file_to_convert in files_to_convert:
        convert_file_with_ebook_convert_util(
            file_to_convert,
            get_new_file_name(file_to_convert, EXTENSIONS_CONVERT_PAIRS)
        )
        remove(file_to_convert)
