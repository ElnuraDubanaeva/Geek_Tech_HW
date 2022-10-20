import re

with open('data.txt', 'r', encoding='UTF - 8') as data:
    result = data.read()


def colors():
    color_list = re.findall(r'(?:#\S*)', result)
    with open('colors.txt', 'w', encoding='UTF-8') as color:
        color.writelines('%s\n' % item for item in color_list)
        color.close()


def emails():
    email_file = re.findall(r'(?:\w*@\S+\.\w+|\.\w+&)', result)
    with open('emails.txt', 'w', encoding='UTF-8') as email:
        email.writelines('%s\n' % item for item in email_file)
        email.close()


def files():
    file_list = re.findall(r'(?:\s\w+\.\w+)', result)
    with open('files.txt', 'w', encoding='UTF-8') as gmail:
        gmail.writelines('%s\n' % item for item in file_list)
        gmail.close()


def names():
    name_list = re.findall(r'(?:^\S*\s\S*)', result)
    with open('names.txt', 'w', encoding='UTF-8') as name:
        name.writelines('%s\n' % item for item in name_list)
        name.close()


def show_info():
    return f'1 - Считать имена и фамилии\n2 - Считать все емайлы\n3 - Считать названия файлов\n4 - Считать цвета\n5 - Выход'


def choice():
    if n == 1:
        names()
    elif n == 2:
        emails()
    elif n == 3:
        files()
    else:
        colors()


print(show_info())
global n
n = int(input('Введите число:'))
while True:
    if n == 5:
        break
    else:
        print(show_info())
        n = int(input('Введите число:'))
        choice()
