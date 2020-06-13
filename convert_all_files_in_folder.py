# Command 'ebook-convert' use for convert from fb2 to mobi

import subprocess
from os import listdir


files_to_convert_path = '/home/evgenii/Downloads/books_kindle/to_ebook/'
extensions_convert_pairs = {
    'fb2': 'mobi'
}


def get_file_type(filename):
    return filename.split('.')[-1]


def get_new_file_name(filename, convert_pairs_dict):
    return '.'.join(filename.split('.')[:-1]) + '.' + convert_pairs_dict.get(get_file_type(filename), 'unknown')


def get_list_of_files(file_path, extensions):
    return [f for f in listdir(file_path) if get_file_type(f) in extensions.keys()]


def convert_file_with_ebook_convert_util(filepath_from, filepath_to):
    subprocess.run(['ebook-convert', filepath_from, filepath_to])


if __name__ == '__main__':
    files_to_convert = get_list_of_files(files_to_convert_path, extensions_convert_pairs)
    for file_to_convert in files_to_convert:
        convert_file_with_ebook_convert_util(
            files_to_convert_path + file_to_convert,
            files_to_convert_path + get_new_file_name(file_to_convert, extensions_convert_pairs)
        )
