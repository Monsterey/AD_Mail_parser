from chardet import detect


def Distr_select(msg_body, distributors):  # поиск имени поставщика в письме
    for elem in distributors:
        try:
            str_msg_body = str(msg_body.as_bytes().decode('utf-8'))
        except:
            code = detect(msg_body.as_bytes())
            str_msg_body = str(msg_body.as_bytes().decode(code['encoding']))
        else:
            str_msg_body = str(msg_body.as_bytes().decode('utf-8'))

        if elem in str_msg_body:
            distributor = elem
    return distributor
