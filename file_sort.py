import os


def File_sort1(file_name, download_path, file_type='xls', f_word=['+']):
    file_path = f'{download_path}{file_name}'
    for fword in f_word:
        if fword in file_name or file_type not in file_name:
            print(f'file {file_path} is deleted')
            os.remove(file_path)
            break
