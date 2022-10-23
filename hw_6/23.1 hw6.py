import re

with open('data.txt', 'r', encoding='UTF - 8') as data:
    result = data.read()


def names():
    name_list = re.findall(r'(?:\b[A-Z][a-zA-Z\'\-\. ]+[\s]+[a-zA-Z\'\-\. ]+\b)', result)
    with open('names.txt', 'w', encoding='UTF-8') as name:
        name.writelines('%s\n' % item for item in name_list)
        name.close()
        return f'created a file called names.txt'


def colors():
    color_list = re.findall(r'(?:#\S*)', result)
    with open('colors.txt', 'w', encoding='UTF-8') as color:
        color.writelines('%s\n' % item for item in color_list)
        color.close()
        return f'created a file called colors.txt'


def emails():
    email_list = re.findall(r'(?:\w*@\S+\.\w+|\.\w+&)', result)
    with open('emails.txt', 'w', encoding='UTF-8') as email:
        email.writelines('%s\n' % item for item in email_list)
        email.close()
        return f'created a file called emails.txt'


def files():
    file_list = re.findall(r'(?:\s\w+\.\w+)', result)
    with open('files.txt', 'w', encoding='UTF-8') as file:
        file.writelines('%s\n' % item for item in file_list)
        file.close()
        return f'created a file called files.txt'


def show_info():
    return f'1 - Считать имена и фамилии\n2 - Считать все емайлы\n3 - Считать названия файлов\n4 - Считать цвета\n5 - Выход'


def choice():
    print(show_info())
    while True:
        n = int(input('Введите число:'))
        if n == 1:
            print(names())
            print(show_info())
        elif n == 2:
            print(emails())
            print(show_info())
        elif n == 3:
            print(files())
            print(show_info())
        elif n == 4:
            print(colors())
            print(show_info())
        else:
            print('Exit')
            break


choice()
