
import yaml
import os
import email

from file_sort import File_sort1
from upd_num import Get_upd_num, Separator
from recive_mail import Recive_mail
from distr_select import Distr_select
from file_process import File_process
from chardet import detect

config = None
# Открываем файл конфигурации
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)


# объявление стартовых переменных
count_newmail = 1


def main():

    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Доступ к данным
    server = (config['email_conf']['server'])  # Выведет: адрес сервера
    user = (config['email_conf']['user'])  # Выведет: user name
    password = (config['email_conf']['password'])  # Выведет: password
    Mail_in = (config['email_conf']['Mail_in'])
    # Выведет: папку на почтовом сервере
    # для сбора входящик сообщений с документами

    # путь к корневой папке для скачаивания
    download_path = (config['paths']['download_path'])

    # Ключ-адрес ячейки в файле где содержится номер документа
    upd_number_adress = (config['userdata']['upd_number_adress'])

    distributors = (config['userdata']['distributors'])  # перечень поставщиков

    # поставщик, чей фал требует доп обработки перед импортом
    pr_distr = (config['userdata']['pr_distr'])

    # расширение файла для удаления прочих xlsx включает в себя xls
    file_type = (config['sort']['file_type'])

    # ключ- слово в имени файла для удаления
    filter_word = (config['sort']['filter_word'])

    # проверка или создание общей папки для скачивания
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    while count_newmail:
        msg = Recive_mail(server, user, password, Mail_in)
        if msg:
            for part in msg.walk():  # проверка не прочитанных писем на содержание вложенных файлов
                if part.get_content_disposition() == f'attachment':

                    filename = part.get_filename()  # получене имени вложенного файла
                    filename_bytes = email.header.decode_header(filename)[0][0]
                    # проверка фала bin/txt и привод его к формату строки
                    if isinstance(filename_bytes, bytes):
                        code = detect(filename_bytes)
                        try:
                            filename_str = filename_bytes.decode('utf-8')
                        except:
                            code = detect(filename_bytes)
                            filename_str = filename_bytes.decode(
                                code['encoding'])
                        else:
                            filename_str = filename_bytes.decode('utf-8')
                    else:
                        filename_str = filename_bytes

                    with open(f'{download_path}{filename_str}', 'wb') as f:
                        # сохранение скачанного файла
                        f.write(part.get_payload(decode=True))

                    distributor = Distr_select(msg, distributors)
                    # проверка или создание папки поставщика
                    if not os.path.exists(f'{download_path}\\{distributor}'):
                        os.makedirs(f'{download_path}\\{distributor}')

                    File_sort1(filename_str, download_path,
                               file_type, filter_word)

                    os.chdir(download_path)
                    if os.path.exists(os.path.join(download_path, filename_str)):
                        Get_upd_num(filename_str, download_path,
                                    distributor, upd_number_adress)
                        os.replace(os.path.join(download_path, filename_str),
                                   os.path.join(download_path, distributor, filename_str))
                    else:
                        continue
                    # сборка полного пути к файлу

                    # filepath = os.path.join(
                    #     f'{download_path}\\{distributor}', f'{filename_str}')
                    # # проверка существования файла
                    # if os.path.isfile(filepath):
                    #     print(f'File {filepath} already exists')
                    # else:
                    #     with open(filepath, 'wb') as f:
                    #         # сохранение скачанного файла
                    #         f.write(part.get_payload(decode=True))
                    #         print(f'Successfully downloaded {filename_str}')

        else:
            break
    # разделяет пакеты номеров документов пустой строкой

    # Separator()
    # File_sort(download_path, distributors, file_type, filter_word)

    File_process(pr_distr, download_path)

    os.chdir(download_path)
    if os.path.isfile('номера накладных.txt'):
        os.startfile('номера накладных.txt')
    Separator()
