# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8-sig') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # print(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

def get_phone_pattern():
    with open('regex_format_phone.txt', 'r', encoding='utf-8-sig') as txt:
        pattern = txt.read()
    return str(pattern)


def format_phone(p_pattern):
    phone_pattern = re.compile(p_pattern)
    for contact in contacts_list:
        phone_final = phone_pattern.sub(r'+7(\1)\2-\3-\4\5\6\7', contact[5])
        contact.insert(5, phone_final)
        contact.pop(6)
    return contacts_list


def format_names(contact_list):
    new_list = []
    for contact in contact_list:
        # op_ = operations
        op1 = contact[0] + ' ' + contact[1] + ' ' + contact[2]
        op2 = op1.strip().split(' ')
        if len(op2) < 3:
            op2.append('')
        op3 = op2 + contact
        op3.pop(3)
        op3.pop(3)
        op3.pop(3)
        if len(op3) > 7:
            a = op3.index('')
            op3.pop(a)
        new_list.append(op3)
    return new_list


def get_result(contact_list):
    contact_list[4].insert(5, contact_list[2][5])
    contact_list[4].pop(7)
    contact_list.pop(2)
    contact_list[6].insert(6, contact_list[7][6])
    contact_list[6].pop(7)
    contact_list.pop(7)
    return contact_list


result = get_result(
    format_names(
        format_phone(
            get_phone_pattern()
        )
    )
)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(result)
