import csv
from pathlib import Path
import os
from colorama import Fore, Back, Style
from model import Person

FILENAME = "phone_book.csv"

COLUMNS = ['id', 'name', 'surname', 'phone', 'comment']


def input_name() -> str:
    print('Введите имя: ')
    name = input()
    return name


def input_surname() -> str:
    print('Введите фамилие: ')
    surname = input()
    return surname


def input_phone() -> str:
    print('Введите телефон: ')
    phone = input()
    return phone


def input_comment() -> str:
    print('Введите комментарий: ')
    comment = input()
    return comment


def get_current_directory_path():
    return os.path.dirname(os.path.realpath(__file__))


def read_persons() -> list[Person]:
    persons = []
    filepath = Path(get_current_directory_path(), FILENAME)
    with open(filepath, "r", newline="", encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == 'id':
                continue
            p = Person(**row)
            persons.append(p)
    return persons


def check_file():
    filepath = Path(get_current_directory_path(), FILENAME)
    if filepath.exists():
        return
    with open(filepath, "w", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()


def append_person(person: Person) -> None:
    filepath = Path(get_current_directory_path(), FILENAME)
    with open(filepath, "a", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS)
        writer.writerow(person.to_dict())


def add_person() -> None:
    person = Person()
    person.name = input_name()
    person.surname = input_surname()
    person.phone = input_phone()
    person.comment = input_comment()
    append_person(person)


def del_person():
    action = input('\n: Выбирите по какому полю искать записи для удаления:'
                   '\n1 - id'
                   '\n2 - имя'
                   '\n3 - фамилия'
                   '\n4 - номер'
                   '\n5 - комментарии\n\n')
    if action.isdigit():
        action = int(action)
        if 1 > action or action > 5:
            return
    else:
        return

    search = input('\nВведите значение для поиска:')
    field = COLUMNS[action - 1]
    persons = read_persons()
    persons_for_remove = list(
        filter(lambda person: person.to_dict()[field] is not None and search in person.to_dict()[field], persons)
    )
    for p in persons_for_remove:
        p.print()
    confirm = input('\nУдалить ?'
                    '\n1 - Да'
                    '\n2 - Нет')
    if confirm.isdigit():
        confirm = int(confirm)
        if confirm == 2:
            return
    else:
        return
    rows = list(
        map(
            lambda person: person.to_dict(),
            filter(lambda person: person.id not in map(lambda x: x.id, persons_for_remove), persons)
            )
    )
    filepath = Path(get_current_directory_path(), FILENAME)
    with open(filepath, "w", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def find_person():  # поиск данных контакта
    search = input('\nВведите значение для поиска:')
    persons = read_persons()
    for p in persons:
        if p.name is not None and search in p.name:
            p.name = f"{Fore.GREEN}{p.name}{Style.RESET_ALL}"
            p.print()
        elif p.surname is not None and search in p.surname:
            p.surname = f"{Fore.GREEN}{p.surname}{Style.RESET_ALL}"
            p.print()
        elif p.phone is not None and search in p.phone:
            p.phone = f"{Fore.GREEN}{p.phone}{Style.RESET_ALL}"
            p.print()
        elif p.comment is not None and search in p.comment:
            p.comment = f"{Fore.GREEN}{p.comment}{Style.RESET_ALL}"
            p.print()


def print_all() -> None:
    persons = read_persons()
    for p in persons:
        p.print()
    input()
