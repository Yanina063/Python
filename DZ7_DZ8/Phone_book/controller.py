from operation import *


def run_phonebook() -> None:
    print('\nДобро пожаловать в телефонную книгу!')
    check_file()
    while True:
        good_action = False
        while not good_action:
            action = input('\nВыберите нужное действие:'
                           '\n1 - Показать все контакты в книге'
                           '\n2 - Добавить контакт в книгу'
                           '\n3 - Найти и показать контакт по заданному значению'
                           '\n4 - Удалить контакт из книги'
                           '\n5 - Выход\n\n')
            if action.isdigit():
                action = int(action)
                if 1 <= action <= 5:
                    good_action = True
                else:
                    print('Для выбора действия ввведите число от 1 до 5-х!')
            else:
                print('Для выбора действия ввведите число от 1 до 5-х!')

            match action:
                case 1: print_all()
                case 2: add_person()
                case 3: find_person()
                case 4: del_person()
                case 5: exit()
