def myscoreboard(scoreboard):
    print("\t--------------------------------")
    print("\t         SCORE BOARD       ")
    print("\t--------------------------------")

    listofplayers = list(scoreboard.keys())
    print("\t   ", listofplayers[0], "\t    ", scoreboard[listofplayers[0]])
    print("\t   ", listofplayers[1], "\t    ", scoreboard[listofplayers[1]])

    print("\t--------------------------------\n")

# Функция для печати Крестики-Нолики


def my_Krestiki_Noliki(val):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8]))
    print("\t     |     |")
    print("\n")

# Функция для проверки выигрышных вариантов


def check_Victory(playerpos, curplayer):

    # Комбинации всех выигрышей
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Цикл для проверки выигрыша
    for i in solution:
        if all(j in playerpos[curplayer] for j in i):
            return True
        return False

# Определение ф-ции для определения ничьей в игре


def check_Tie(playerpos):
    if len(playerpos['X']) + len(playerpos['O']) == 9:
        return True
    return False

# Функция для одиночной игры


def singlegame(curplayer):
    # Подставление значений Х и 0 в игре
    val = [' ' for i in range(9)]

    # Сохранение позиций, занятых X и O
    playerpos = {'X': [], 'O': []}

    # Цикл игры для одной игры
    while True:
        my_Krestiki_Noliki(val)
        # Блок для ввода значений и проверки свободных ячеек
        try:
            print("Player ", curplayer, " turn. Choose your Block : ", end="")
            chance = int(input())
        except ValueError:
            print("Invalid Input!!! Try Again")
            continue

        # Проверка работоспособности для блока ввода
        if chance < 1 or chance > 9:
            print("Invalid Input!!! Try Again")
            continue

        # Проверка , не занят ли блок
        if val[chance - 1] != ' ':
            print("Oops! The Place is already occupied. Try again!!")
            continue

        # Обновление игры и сетки
        val[chance - 1] = curplayer

        # Обновление позиции игрока
        playerpos[curplayer].append(chance)

        my_Krestiki_Noliki(val)

        # Определение победителя
        if check_Victory(playerpos, curplayer):
            my_Krestiki_Noliki(val)
            print("Congratulations! Player ", curplayer, " has won the game!")
            print("\n")
            return curplayer

        # Определение ничьей
        if check_Tie(playerpos):
            my_Krestiki_Noliki(val)
            print("Oh! Game Tied")
            print("\n")
            return 'D'

            # Переключение хода
        if curplayer == 'X':
            curplayer = 'O'
        else:
            curplayer = 'X'


if __name__ == "__main__":

    print("First Player")
    FirstPlayer = input("Specify the Name: ")
    print("\n")

    print("Second Player")
    SecondPlayer = input("Specify the Name: ")
    print("\n")

    # Сохранение ходов игроков X и O
    curplayer = FirstPlayer

    # Сохранение выбора игроков
    playerchoice = {'X': "", 'O': ""}

    # Сохранение параметров
    opt = ['X', 'O']

    # Хранение табло
    scoreboard = {FirstPlayer: 0, SecondPlayer: 0}
    myscoreboard(scoreboard)

    # Цикл для серии игры Крестики-Нолики
    while True:
        # Главное меню для игроков
        print(curplayer, "will make the choice:")
        print("Press 1 for X")
        print("Press 2 for O")
        print("Press 3 to Quit")
        # Проверка ввода значения игроком
        try:
            the_choice = int(input())
        except ValueError:
            print("Invalid Input!!! Try Again\n")
            continue

        # Условия выбора игрока
        match the_choice:
            case 1:
                playerchoice['X'] = curplayer
                if curplayer == FirstPlayer:
                    playerchoice['O'] = SecondPlayer
                else:
                    playerchoice['O'] = FirstPlayer
            case 2:
                playerchoice['O'] = curplayer
                if curplayer == FirstPlayer:
                    playerchoice['X'] = SecondPlayer
                else:
                    playerchoice['X'] = FirstPlayer
            case 3:
                print("The Final Scores")
                myscoreboard(scoreboard)
                break
            case _:
                print("Invalid Selection!! Try Again\n")

        win = singlegame(opt[the_choice - 1])

        # Обновление табло по победителю
        if win != 'D':
            playerWon = playerchoice[win]
            scoreboard[playerWon] = scoreboard[playerWon] + 1

        myscoreboard(scoreboard)

        # Переключение игрока
        if curplayer == FirstPlayer:
            curplayer = SecondPlayer
        else:
            curplayer = FirstPlayer
