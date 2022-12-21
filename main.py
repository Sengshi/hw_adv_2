import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv


def corrected_book(pattern_raw, pattern_new, testbook):
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
    contacts_correct_1 = corrected_book(name_pattern_raw, name_pattern_new, contacts_list)

    # task 2
    number_pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)' \
                         r'(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    contacts_correct_2 = corrected_book(number_pattern_raw, number_pattern_new, contacts_correct_1)
    # print(contacts_correct_2)
    # task 3
    contacts_correct_3 = list()
    temp_dict = dict()
    double_dict = dict()
    for i in contacts_correct_2:
        count = 0
        if any(' '.join(i[:3]) in keys for keys in temp_dict.keys()):
            double_dict[' '.join(i[:3])] = i[3:]
            filter_obj = list(filter(lambda name: ' '.join(i[:3]) in name, temp_dict.keys()))
            while count <= 3:
                temp_date = temp_dict[filter_obj[0]][count]
                double_date = double_dict[' '.join(i[:3])][count]
                if temp_date != double_date and temp_date == '' and double_date != '':
                    temp_dict[filter_obj[0]][count] = double_date
                count += 1
        else:
            temp_dict[' '.join(i[:3])] = i[3:]

    for k, v in temp_dict.items():
        line = k.split() + v
        contacts_correct_3.append(line)

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding='utf8') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(contacts_correct_3)


if __name__ == '__main__':
    inspect_phonebook('phonebook_raw.csv')
