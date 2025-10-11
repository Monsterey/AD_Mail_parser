from tkinter import *
import yaml
from get_config import def_config
# from main import config
from main import main


with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    # print(str(config))


def default():
    config = def_config

    with open('config.yaml', 'w') as file:
        yaml.dump(config, file)
        print('config.yaml is default')

    distlist.configure(listvariable=Variable(
        value=list((config['userdata']['upd_number_adress']).keys())))
    keyslist.configure(listvariable=Variable(
        value=list((config['userdata']['upd_number_adress']).values())))
    wordlist.configure(listvariable=Variable(
        value=config['sort']['filter_word']))


def save_distr():
    (config['userdata']['distributors']).append(new_distr.get())
    (config['userdata']['upd_number_adress']
     [new_distr.get()]) = new_distr_key.get()

    with open('config.yaml', 'w') as file:
        yaml.dump(config, file)
        print('config.yaml is updated')

    distlist.configure(listvariable=Variable(
        value=list((config['userdata']['upd_number_adress']).keys())))
    keyslist.configure(listvariable=Variable(
        value=list((config['userdata']['upd_number_adress']).values())))


def save_word():
    (config['sort']['filter_word']).append(new_word.get())

    with open('config.yaml', 'w') as file:
        yaml.dump(config, file)
        print('config.yaml is updated')

    wordlist.configure(listvariable=Variable(
        value=config['sort']['filter_word']))


def save_config():
    label1['text'] = user.get() + '\n'

    if not isinstance(Mail_in.get(), str):
        raise ValueError("Назваие папки должно быть строкой")
    else:
        config['email_conf']['Mail_in'] = Mail_in.get()
    if not isinstance(password.get(), str):
        raise ValueError("пароль должен быть строкой")
    else:
        config['email_conf']['password'] = password.get()
    if not isinstance(server.get(), str):
        raise ValueError("сервер должен быть строкой")
    else:
        config['email_conf']['server'] = server.get()
    if not isinstance(user.get(), str):
        raise ValueError("имя должно быть строкой")
    else:
        config['email_conf']['user'] = user.get()

    if not isinstance(download_path.get(), str):
        raise ValueError("путь должен быть строкой")
    else:
        config['paths']['download_path'] = download_path.get()

    if not isinstance(file_type.get(), str):
        raise ValueError("тип файла должен быть строкой")
    else:
        config['sort']['file_type'] = file_type.get()

    filterwords = filter_word.get().split(',')
    if not isinstance(filterwords, list):
        raise ValueError("Слова исключения должны быть списком")
    else:
        config['sort']['filter_word'] = filter_word.get().split(',')

    distributorslist = distributors.get().split(',')
    if not isinstance(distributorslist, list):
        raise ValueError("Список поставщиков должен быть списком")
    else:
        config['userdata']['distributors'] = (distributors.get()).split(',')

    if not isinstance(pr_distr.get(), str):
        raise ValueError("Имя поставщика с доп обработкой должно быть строкой")
    else:
        config['userdata']['pr_distr'] = pr_distr.get()

    try:
        una_str = upd_number_adress.get()
        una_list = una_str.split(',')
        una_listinlist = []
        for elem in una_list:
            una_listinlist.append(elem.split(':'))
        una_dict = dict(una_listinlist)
    except ValueError:
        print('поставщик:ключ должен быть словарем')

    config['userdata']['upd_number_adress'] = una_dict

    # print(config)

    with open('config.yaml', 'w') as file:
        yaml.dump(config, file)
        print('config.yaml is updated')

    distlist.configure(listvariable=Variable(
        value=list((config['userdata']['upd_number_adress']).keys())))
    keyslist.configure(listvariable=Variable(
        value=list((config['userdata']['upd_number_adress']).values())))
    wordlist.configure(listvariable=Variable(
        value=config['sort']['filter_word']))


def gui():

    fr.pack(expand=True, fill=X)
    fr1.pack(expand=True, fill=X)
    frdata.pack(expand=True, fill=BOTH)

    user.pack(anchor=NW, padx=6, pady=6, fill=X)
    password.pack(anchor=NW, padx=6, pady=6, fill=X)
    server.pack(anchor=NW, padx=6, pady=6, fill=X)
    Mail_in.pack(anchor=NW, padx=6, pady=6, fill=X)
    download_path.pack(anchor=NW, padx=6, pady=6, fill=X)
    file_type.pack(anchor=NW, padx=6, pady=6, fill=X)
    filter_word.pack(anchor=NW, padx=6, pady=6, fill=X)
    distributors.pack(anchor=NW, padx=6, pady=6, fill=X)
    pr_distr.pack(anchor=NW, padx=6, pady=6, fill=X)
    upd_number_adress.pack(anchor=NW, padx=6, pady=6, fill=X)

    bt1.pack(anchor=CENTER, padx=6, pady=6)
    btn_go.pack(anchor=CENTER, padx=6, pady=6, fill=X)

    new_distr.grid(row=1, column=1, sticky=E)
    new_distr_key.grid(row=1, column=2, sticky=W)
    btn_savedistr.grid(row=1, column=3, sticky=W)

    new_word.grid(row=1, column=5, sticky=E)
    btn_saveword.grid(row=1, column=6, sticky=W)

    btn_def.grid(row=2, column=2)

    cud_label.grid(row=1, column=1)
    key_label.grid(row=1, column=2)
    wd_label.grid(row=1, column=4)
    distlist.grid(row=2, column=1)
    keyslist.grid(row=2, column=2, sticky=W)
    wordlist.grid(row=2, column=4, sticky=N)

    root.mainloop()


root = Tk()
root.geometry('900x680')

fr = Frame(root, background='gray', borderwidth=5, relief=RAISED, height=300)
fr1 = Frame(root, background='gray', borderwidth=5, relief=RAISED, height=5)
frdata = Frame(root, background='gray', borderwidth=5,
               relief=RAISED, height=500)

fr1.columnconfigure(index=1, weight=10)
fr1.columnconfigure(index=2, weight=1)
fr1.columnconfigure(index=3, weight=10)
fr1.columnconfigure(index=5, weight=10)
fr1.columnconfigure(index=6, weight=10)


# frdata.columnconfigure(index=2, weight=1)

user = Entry(fr, border=3)
user.insert(0, 'login')
password = Entry(fr, border=3)
password.insert(0, 'password (для почтовых программ)')
server = Entry(fr, border=3)
server.insert(0, 'адрес почтового сервера IMAP')
Mail_in = Entry(fr, border=3)
Mail_in.insert(0, 'Папка на почтовом сервере')

download_path = Entry(fr, border=3)
download_path.insert(0, 'Путь к основной папке  для документов')

file_type = Entry(fr, border=3)
file_type.insert(
    0, 'расширение файла для удаления прочих xlsx включает в себя xls')
filter_word = Entry(fr, border=3)
filter_word.insert(
    0, 'ключ - слова в имени файла для удаления,указываются через запятую')

distributors = Entry(fr, border=3)
distributors.insert(
    0, 'перечень поставщиков через , (обязательно должно совпадать с именем в списке ключей)')

pr_distr = Entry(fr, border=3)
pr_distr.insert(
    0, 'поставщик, чей файл требует доп обработки перед импортом(опционально) по умолчанию стоит ixora')

upd_number_adress = Entry(fr, border=3)
upd_number_adress.insert(
    0, 'Ключ-адрес ячейки в файле где содержится номер документа(заполняется в формате "поставщик":"адрес ячейки в файле," , на пример ixora:r3)')


bt1 = Button(fr, bd=3, text='save', command=save_config)
label1 = Label(fr)
btn_go = Button(fr, bd=3, text='GO', command=main, background='green')


new_distr = Entry(fr1, border=3)
new_distr.insert(0, 'новый поставщик')
new_distr_key = Entry(fr1, border=3)
new_distr_key.insert(0, 'ключ')
btn_savedistr = Button(
    fr1, bd=3, text='добавить поставщика', command=save_distr)


new_word = Entry(fr1, border=3)
new_word.insert(0, 'новое фильтр-слово')
btn_saveword = Button(
    fr1, bd=3, text='новое фильтр-слово', command=save_word)


btn_def = Button(fr1, text='Сбросить все настройки',
                 command=default, background='yellow')


cud_label = Label(frdata, text='Поставщики')
cud = Variable(value=list((config['userdata']['upd_number_adress']).keys()))
distlist = Listbox(frdata, listvariable=cud, bd=3,
                   relief=RAISED)

key_label = Label(frdata, text='ключи')
keys = Variable(value=list((config['userdata']['upd_number_adress']).values()))
keyslist = Listbox(frdata, listvariable=keys, bd=3,
                   relief=RAISED)

wd_label = Label(frdata, text='фильтр-слова')
wd = Variable(value=config['sort']['filter_word'])
wordlist = Listbox(frdata, listvariable=wd, bd=3,
                   relief=RAISED)
