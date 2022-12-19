from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from random import randint
import string
import time
from operator import xor

TOKEN = '5715751545:AAGrYQdShHpUpPgNGRVFOxZQMZ1bg51DXJI'

bot = Bot(TOKEN)
dp = Dispatcher(bot)



board = [
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
]

bot_board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

point_board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

points_list = [
    ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'],
    ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
    ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
    ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
    ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
    ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
    ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
    ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
]


class SeaBattle():
    def __init__(self, player_board, copy_of_player_board, copy_of_comp_board, comp_board, flag_of_shooting1, flag_of_shooting2, flag_of_shooting3, x_shoot, y_shoot, points):
        self.player_board = [
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
    ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
]
        self.copy_of_player_board = board
        self.copy_of_comp_board = board
        self.comp_board = board
        self.flag_of_shooting1 = True
        self.flag_of_shooting2 = False
        self.flag_of_shooting3 = False
        self.x_shoot = 0
        self.y_shoot = 0
        self.points = points_list

    def player_board_print(self):  # вывод стола игрока
        st = ' '
        k = 1
        for i in string.ascii_uppercase[:8]:
            st += '     ' + i
        for i in range(len(self.player_board)):
            st += '\n' + str(k) + ' '
            for j in range(len(self.player_board[i])):
                st += ' ' + self.player_board[i][j]
            k += 1
        return st

    def placement(self, point):  # функция отвечающая за перевод координат в индексы матрицы и постановку в соотвествующую позицию символ
        if point[0] == 'A':
            self.player_board[int(point[1]) - 1][0] = '██'
        elif point[0] == 'B':
            self.player_board[int(point[1]) - 1][1] = '██'
        elif point[0] == 'C':
            self.player_board[int(point[1]) - 1][2] = '██'
        elif point[0] == 'D':
            self.player_board[int(point[1]) - 1][3] = '██'
        elif point[0] == 'E':
            self.player_board[int(point[1]) - 1][4] = '██'
        elif point[0] == 'F':
            self.player_board[int(point[1]) - 1][5] = '██'
        elif point[0] == 'G':
            self.player_board[int(point[1]) - 1][6] = '██'
        elif point[0] == 'H':
            self.player_board[int(point[1]) - 1][7] = '██'

    def Zero_to_Two(self):  # определяет область на которой запрещено будет ставить корабли
        for i in range(len(self.player_board)):
            for j in range(len(self.player_board[i])):
                if self.player_board[i][j] == '██':
                    try:
                        if self.player_board[i + 1][j] == '░░':
                            self.player_board[i + 1][j] = '▒▒'
                    except:
                        pass
                    try:
                        if self.player_board[i][j + 1] == '░░':
                            self.player_board[i][j + 1] = '▒▒'
                    except:
                        pass
                    try:
                        if i - 1 < 0:
                            raise Exception
                        if self.player_board[i - 1][j] == '░░':
                            self.player_board[i - 1][j] = '▒▒'
                    except (Exception, IndexError):
                        pass
                    try:
                        if j - 1 < 0:
                            raise Exception
                        if self.player_board[i][j - 1] == '░░':
                            self.player_board[i][j - 1] = '▒▒'
                    except (Exception, IndexError):
                        pass
                    try:
                        if self.player_board[i + 1][j + 1] == '░░':
                            self.player_board[i + 1][j + 1] = '▒▒'
                    except:
                        pass
                    try:
                        if j - 1 < 0:
                            raise Exception
                        if self.player_board[i + 1][j - 1] == '░░':
                            self.player_board[i + 1][j - 1] = '▒▒'
                    except (Exception, IndexError):
                        pass
                    try:
                        if i - 1 < 0:
                            raise Exception
                        if self.player_board[i - 1][j + 1] == '░░':
                            self.player_board[i - 1][j + 1] = '▒▒'
                    except (Exception, IndexError):
                        pass
                    try:
                        if j - 1 < 0 or i - 1 < 0:
                            raise Exception
                        if self.player_board[i - 1][j - 1] == '░░':
                            self.player_board[i - 1][j - 1] = '▒▒'
                    except (Exception, IndexError):
                        pass


    def check_of_coordinates(self, point):  # функция проверяющая соответствие введенных значений реальным координатам
        def can_put_point(point):  # функция отвечающая за проверку можно ли поставить на определенную точку корабль
            if point[0] == 'A':
                if self.player_board[int(point[1]) - 1][0] == '██' or self.player_board[int(point[1]) - 1][0] == '▒▒':
                    return True
                else:
                    return False
            elif point[0] == 'B':
                if self.player_board[int(point[1]) - 1][1] == '██' or self.player_board[int(point[1]) - 1][1] == '▒▒':
                    return True
                else:
                    return False
            elif point[0] == 'C':
                if self.player_board[int(point[1]) - 1][2] == '██' or self.player_board[int(point[1]) - 1][2] == '▒▒':
                    return True
                else:
                    return False
            elif point[0] == 'D':
                if self.player_board[int(point[1]) - 1][3] == '██' or self.player_board[int(point[1]) - 1][3] == '▒▒':
                    return True
                else:
                    return False
            elif point[0] == 'E':
                if self.player_board[int(point[1]) - 1][4] == '██' or self.player_board[int(point[1]) - 1][4] == '▒▒':
                    return True
                else:
                    return False
            elif point[0] == 'F':
                if self.player_board[int(point[1]) - 1][5] == '██' or self.player_board[int(point[1]) - 1][5] == '▒▒':
                    return True
                else:
                    return False
            elif point[0] == 'G':
                if self.player_board[int(point[1]) - 1][6] == '██' or self.player_board[int(point[1]) - 1][6] == '▒▒':
                    return True
                else:
                    return False
            elif point[0] == 'H':
                if self.player_board[int(point[1]) - 1][7] == '██' or self.player_board[int(point[1]) - 1][7] == '▒▒':
                    return True
                else:
                    return False

        if (point[0] in string.ascii_uppercase[:8]) and (
                point[1] in [str(i) for i in range(1, 9)]) and not can_put_point(point):
            return True
        else:
            return False


global flag_of_placement
flag_of_placement = False

@dp.message_handler(commands=['start'])
async def start_of_the_game(message: types.Message):
    global count_kat
    global count_esm
    global count_kre
    global count_lin
    count_kat = 0
    count_esm = 0
    count_kre = 0
    count_lin = 0
    global flag_of_placement
    flag_of_placement = True
    global game
    game = SeaBattle(board, board, board, board, True, False, True, 0, 0, points_list)
    await bot.send_message(message.from_user.id, (game.player_board_print()))
    await bot.send_message(message.from_user.id, 'Начинается расстановка кораблей')
    await bot.send_message(message.from_user.id, 'Начинается расстановка катеров')
    global flag_of_kat, flag_of_esm, flag_of_kre, flag_of_lin
    flag_of_kat = False
    flag_of_esm = True
    flag_of_kre = True
    flag_of_lin = True


@dp.message_handler()
async def placement_of_kat_1(message: types.Message):
    if flag_of_placement:
        global flag_of_kat, flag_of_esm, flag_of_kre, flag_of_lin
        if not flag_of_kat:
            if game.check_of_coordinates(message.text) and len(message.text) <= 3:
                game.placement(message.text)
                game.Zero_to_Two()
                await bot.send_message(message.from_user.id, (game.player_board_print()))
                global count_kat
                count_kat += 1
                if count_kat == 4:
                    flag_of_kat = True
                    flag_of_esm = False
                    await bot.send_message(message.from_user.id, 'Начинается расстановка эсмницев')
            else:
                await bot.send_message(message.from_user.id, 'Ошибка координат!')

        elif not flag_of_esm:
            container = message.text.split()
            if game.check_of_coordinates(container[0]) and game.check_of_coordinates(container[1]) and xor(
                    (container[0][0] != container[1][0]) or (abs(int(container[0][1]) - int(container[1][1])) != 1), (container[0][1] != container[1][1] or (
                            (container[0][0] + container[1][0] not in string.ascii_uppercase) and (
                            container[1][0] + container[0][0] not in string.ascii_uppercase)))):
                game.placement(container[0])
                game.placement(container[1])
                game.Zero_to_Two()
                await bot.send_message(message.from_user.id, (game.player_board_print()))
                global count_esm
                count_esm += 1
                if count_esm == 3:
                    flag_of_esm = True
                    flag_of_kre = False
                    await bot.send_message(message.from_user.id, 'Начинается расстановка крейсеров')
            else:
                await bot.send_message(message.from_user.id, 'Ошибка координат!')

        elif not flag_of_kre:
            container = message.text.split()
            c = 'Z1'
            for letter in string.ascii_uppercase[:8]:
                if (container[0][0] == container[1][0]) and (abs(int(container[0][1]) - int(container[1][1])) == 2):
                    c = container[0][0] + str(max(int(container[0][1]), int(container[1][1])) - 1)

                elif (container[0][1] == container[1][1]) and (((container[0][0] + letter + container[1][0]) in string.ascii_uppercase) or (
                        (container[1][0] + letter + container[0][0]) in string.ascii_uppercase)):
                    c = letter + container[0][1]

            if game.check_of_coordinates(container[0]) and game.check_of_coordinates(container[1]) and game.check_of_coordinates(c) and xor(
                    (container[0][0] != container[1][0]) or (abs(int(container[0][1]) - int(container[1][1])) != 2), (container[0][1] != container[1][1] or (
                            (container[0][0] + c[0] + container[1][0] not in string.ascii_uppercase) and (
                            container[1][0] + c[0] + container[0][0] not in string.ascii_uppercase)))):
                game.placement(container[0])
                game.placement(container[1])
                game.placement(c)
                game.Zero_to_Two()
                await bot.send_message(message.from_user.id, (game.player_board_print()))
                global count_kre
                count_kre += 1
                if count_kre == 2:
                    flag_of_kre = True
                    flag_of_lin = False
                    await bot.send_message(message.from_user.id, 'Начинается расстановка линкора')
            else:
                await bot.send_message(message.from_user.id, 'Ошибка координат!')
    else:
        await bot.send_message(message.from_user.id, 'Напишите /start, чтобы начать игру')




if __name__ == "__main__":
    executor.start_polling(dp)