import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv


def convect_book(pattern_raw, pattern_new, testbook):
    correct_list = list()
    for line in testbook:
        line_to_string = ','.join(line)
        formatted_line = re.sub(pattern_raw, pattern_new, line_to_string)
        line_to_list = formatted_line.split(',')
        correct_list.append(line_to_list)
    return correct_list


def inspect_phonebook(phonebook):
    with open(phonebook, encoding='utf8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    # pprint(contacts_list)

    # TODO 1: выполните пункты 1-3 ДЗ
    # ваш код
    # task 1
    name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    name_pattern_new = r'\1\3\10\4\6\9\7\8'
    contacts_correct_1 = convect_book(name_pattern_raw, name_pattern_new, contacts_list)

    # task 2
    number_pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)' \
                         r'(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    contacts_correct_2 = convect_book(number_pattern_raw, number_pattern_new, contacts_correct_1)

    # task 3
    for i in contacts_correct_2:
        for j in contacts_correct_2:
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                if not i[2]:
                    i[2] = j[2]
                if not i[3]:
                    i[3] = j[3]
                if not i[4]:
                    i[4] = j[4]
                if not i[5]:
                    i[5] = j[5]
                if not i[6]:
                    i[6] = j[6]
    contacts_correct_3 = list()
    for card in contacts_correct_2:
        if card not in contacts_correct_3:
            contacts_correct_3.append(card)

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding='utf8') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(contacts_correct_3)


if __name__ == '__main__':
    inspect_phonebook('phonebook_raw.csv')
