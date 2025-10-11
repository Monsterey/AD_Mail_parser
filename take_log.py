import os


def Logging(log_data, log_path):  # Пишем логи
    os.remove(log_path)
    fp = open(log_path, 'w')
    fp.close
    fp = open(log_path, 'r+')
    # text = fp.read()
    # print(text)
    fp.write(log_data)
    fp.close
