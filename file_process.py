
import os
import pandas as pd

# доп обработка фала поставщика, приведение его к виду доступному для импорта (под каждого поставщика -индивидуально)


def File_process(distr, download_path):
    # получение адреса папки поставщика
    file_path = os.path.join(
        f'{download_path}\\{distr}')
    # переход в папку поставщика
    if os.path.exists(file_path):
        os.chdir(file_path)
    else:
        os.mkdir(file_path)
    # получение списка файлов в папке
    file_list = os.listdir(file_path)

    # получение нужной информации из каждого файла и пересохранене в требуемом виде
    for file in file_list:
        if '.xlsx' in file:
            continue
        df = pd.read_excel(file, 'УПД',  header=17,
                           usecols='C,I,Z,ag,bk,bv,cc')
        df.to_excel(f"{file}.xlsx")
        os.remove(file)


# file_process('ixora')
