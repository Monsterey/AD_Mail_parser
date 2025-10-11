import pandas as pd
import os

# Получение номеров накладных из загружаемых документов
# (для каждого поставщика нужно изначально указывать адрес ячейки с номером документа,
#  указывается в словаре "upd_number_adress")


def Get_upd_num(filename, download_path, distributor, upd_number_adress):
    # проверка на соответствие типа файла
    strVal = ''
    rowVal = ''
    # проверка на принадлежность файла поставщику с требование доп обработки
    if distributor != 'ixora':
        # получение адреса папки поставщика
        # filedownload_path = f'{download_path}\\{distributor}'
        # получение адреса ячейки с номером документа
        upd_number_adress_str = (upd_number_adress[distributor])
        # парсинг строкии столбца ячейки адреса
        for elem in upd_number_adress_str:
            if elem.isdigit():
                strVal += elem
            else:
                rowVal += elem
            # переход в папку с файлом
        os.chdir(download_path)
        # получение датафрэйма с ячейкой
        df = pd.read_excel(filename, header=(int(strVal)-2),
                           usecols=rowVal, nrows=1)
        # получение значения ячейки(номер документа)
        dfVal = df.values[0]
        # переход в корневую папку
        # os.chdir(download_path)
        # создание или дополнение текстового файла с номерами новых документов по поставщикам
        with open('номера накладных.txt', 'a') as file:
            file.write(
                f'Назване поставщика: {distributor} номер накладной {dfVal} \n')

        # print(str(dfVal))
        # проверка на принадлежность файла поставщику с требование доп обработки
    else:
        # получение адреса папки поставщика
        # filedownload_path = f'{download_path}\\{distributor}'
        # получение адреса ячейки с номером документа
        upd_number_adress_str = (upd_number_adress[distributor])
        # парсинг строкии столбца ячейки адреса
        for elem in upd_number_adress_str:
            if elem.isdigit():
                strVal += elem
            else:
                rowVal += elem
            # переход в папку с файлом
        os.chdir(download_path)
        # получение датафрэйма с ячейкой
        df = pd.read_excel(filename, sheet_name='УПД', header=(int(strVal)-2),
                           usecols=rowVal, nrows=1)
        # получение значения ячейки(номер документа)
        dfVal = df.values[0]
        # переход в корневую папку
        # os.chdir(download_path)
        # создание или дополнение текстового файла с номерами новых документов по поставщикам
        with open('номера накладных.txt', 'a') as file:
            file.write(
                f'Назване поставщика: {distributor} номер накладной {dfVal} \n')

        # print(str(dfVal))


def Separator():  # разделяет пакеты номеров документов пустой строкой
    with open('номера накладных.txt', 'a') as file:
        file.write(
            f' \n')
