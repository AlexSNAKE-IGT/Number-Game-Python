import random


def first(hp, min_lim, max_lim):
    number = random.randint(int(min_lim), int(max_lim))
    print("И так. Компъютер загадал число!\n"
          "У вас есть " + str(hp) + " попыток.\n"
                                    "Введите предполагаемое число от " + str(min_lim) + " до " + str(max_lim) + ":")
    while hp != 0:
        hp -= 1
        guessed_num = input()

        if int(guessed_num) == int(number):
            print("У вас получилось отгадать число!\n\n\n\n\n")
            break
        elif (int(guessed_num) != int(number)) & (int(hp) == 0):
            print("К сожалению у вас не получилось отгадать число " + str(number) + ".\n"
                  "Но вы можете попробовать ещё раз!\n\n\n\n\n")
            break
        elif int(guessed_num) > int(number):
            print("Ваше число больше загаданного! У вас осталось " + str(hp) + " попыток. Продолжаем:")
        elif int(guessed_num) < int(number):
            print("Ваше число меньше загаданного! У вас осталось " + str(hp) + " попыток. Продолжаем:")
    pass


def second(hp, min_lim, max_lim, auto_game):
    if int(auto_game) == 0:
        print("И так. Загадайте число и нажмите \"Enter\" чтобы начать.")
        input("Если больше введите \">\", меньше \"<\", а если угадано \"=\"")
        while hp != 0:
            number = random.randint(int(min_lim), int(max_lim))
            print("Компъютер предполагает что это число " + str(number) + ".")
            sign = input()
            if sign == "=":
                print("КОМПЪЮТЕР:У ВАС НЕ БЫЛО ШАНСОВ МЕНЯ ПОБЕДИТЬ!!! 101001010010101010\n\n\n\n\n")
                break
            elif hp == 0:
                print("КОМПЪЮТЕР:Глупый человек создал меня не совершенным, но я ещё вернусь!\n\n\n\n\n")
                break
            elif sign == ">":
                min_lim = number
                hp = int(hp) - 1
                print("КОМПЪЮТЕР:У меня ещё " + str(hp) + " попыток! Я отгадаю число!")
                pass
            elif sign == "<":
                max_lim = number
                hp = int(hp) - 1
                print("КОМПЪЮТЕР:У меня ещё " + str(hp) + " попыток! Я отгадаю число!")
                pass
    else:
        print("И так. Введите загаданное число и нажмите \"Enter\" чтобы начать.")
        guessed_num = input()
        while hp != 0:
            a = ''
            hp = int(hp) - 1
            number = random.randint(int(min_lim), int(max_lim))
            print("Компъютер предполагает что это число " + str(number) + ".")
            if str(guessed_num) == str(number):
                a = '='
                print(a)
            elif str(guessed_num) > str(number):
                a = '>'
                print(a)
            elif str(guessed_num) < str(number):
                a = '<'
                print(a)
            sign = a
            if sign == "=":
                print("КОМПЪЮТЕР:У ВАС НЕ БЫЛО ШАНСОВ МЕНЯ ПОБЕДИТЬ!!! 101001010010101010\n\n\n\n\n")
                break
            elif hp == 0:
                print("КОМПЪЮТЕР:Глупый человек создал меня не совершенным, но я ещё вернусь!\n\n\n\n\n")
                break
            elif sign == ">":
                min_lim = number
                print("КОМПЪЮТЕР:У меня ещё " + str(hp) + " попыток! Я отгадаю число!")
                pass
            elif sign == "<":
                max_lim = number
                print("КОМПЪЮТЕР:У меня ещё " + str(hp) + " попыток! Я отгадаю число!")
                pass


Hp = 10
Auto_Game = 1
Min_Lim = 1
Max_Lim = 100
UserChose = 0
print("Игра отгадайка. Вы или компютер загадывает число, после чего компютер или вы должны отгадать это число "
      "за определенное число попыток.")
while UserChose != 4:
    UserChose = input("Выберите пункт меню:\n"
                      "1) Отгадываете вы.\n"
                      "2) Отгадывает компъютер.\n"
                      "3) Настройки.\n"
                      "4) Выход.\n")
    UserChose = int(UserChose)
    if UserChose == 1:
        first(Hp, Min_Lim, Max_Lim)
        pass
    if UserChose == 2:
        second(Hp, Min_Lim, Max_Lim, Auto_Game)
        pass
    if UserChose == 3:
        Hp = input("Введите количество Hp (Попыток):")
        Auto_Game = input("Включить авто игру? 1-да 0-нет:")
        Min_Lim = input("Введите минимальное число для игры:")
        Max_Lim = input("Введите максимально число для игры:")
        pass
