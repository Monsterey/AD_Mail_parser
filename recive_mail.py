import imaplib
import email


# Логинимся и получаем информацию о письмах
def Recive_mail(server, user, password, Mail_in):
    mail = imaplib.IMAP4_SSL(server)
    mail.login(user, password)

    mail.list
    mail.select(Mail_in)

    # Находим не прочитанные письма в папке
    result, data = mail.search(None, 'NOT SEEN')

    # logging(str(data), logdata_path)

    id_strings = data[0]             # Получаем список ID писем
    id_list = id_strings.split()
    count_newmail = len(id_list)

    if count_newmail == 0:
        return

    latest_email_id = id_list[-1]  # Получаем ID последнего письма
    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    return msg
