import shutil
import os
import re

def check_file_for_phone(my_file_path):
    my_file = open(my_file_path, 'r')
    file_content = my_file.read()
    my_file.close()
    my_re = re.search(r'\d{3}-\d{3}-\d{4}', file_content)
    if my_re:
        the_phone = my_re.group()
        print(f'The phone {the_phone} was found in file: {my_file_path}')


output_filename = 'unzip_me_for_instructions.zip'
dir_for_extract_result = 'mainor_unzip_folder'
# only run it once to unzip file:
# shutil.unpack_archive(output_filename,dir_for_extract_result,'zip')

for folder, sub_folders, files in os.walk(dir_for_extract_result):

    # print("Currently looking at folder: " + folder)
    # print('\n')
    # print("THE FILES ARE: ")
    for f in files:
        # print("\t File: " + f)
        file_path = f'{folder}/{f}'
        # print(f'\t File Path: {file_path}')
        check_file_for_phone(file_path)
    # print('\n')