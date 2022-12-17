import string
import time
from operator import xor
from random import randint

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
        self.player_board = board
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
        st = '  '
        k = 1
        for i in string.ascii_uppercase[:8]:
            st += '  ' + i
        print(st)
        for i in range(len(self.player_board)):
            st = str(k) + ' '
            for j in range(len(self.player_board[i])):
                st += ' ' + self.player_board[i][j]
            k += 1
            print(st)


    def placement_of_ships(self):

        def placement(
                point):  # функция отвечающая за перевод координат в индексы матрицы и постановку в соотвествующую позицию символ
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

        def Zero_to_Two():  # определяет область на которой запрещено будет ставить корабли
            for i in range(len(self.player_board)):
                for j in range(len(self.player_board[i])):
                    if self.comp_board[i][j] == '██':
                        try:
                            if self.comp_board[i + 1][j] == '░░':
                                self.comp_board[i + 1][j] = '▒▒'
                        except:
                            pass
                        try:
                            if self.comp_board[i][j + 1] == '░░':
                                self.comp_board[i][j + 1] = '▒▒'
                        except:
                            pass
                        try:
                            if i - 1 < 0:
                                raise Exception
                            if self.comp_board[i - 1][j] == '░░':
                                self.comp_board[i - 1][j] = '▒▒'
                        except (Exception, IndexError):
                            pass
                        try:
                            if j - 1 < 0:
                                raise Exception
                            if self.comp_board[i][j - 1] == '░░':
                                self.comp_board[i][j - 1] = '▒▒'
                        except (Exception, IndexError):
                            pass
                        try:
                            if self.comp_board[i + 1][j + 1] == '░░':
                                self.comp_board[i + 1][j + 1] = '▒▒'
                        except:
                            pass
                        try:
                            if j - 1 < 0:
                                raise Exception
                            if self.comp_board[i + 1][j - 1] == '░░':
                                self.comp_board[i + 1][j - 1] = '▒▒'
                        except (Exception, IndexError):
                            pass
                        try:
                            if i - 1 < 0:
                                raise Exception
                            if self.comp_board[i - 1][j + 1] == '░░':
                                self.comp_board[i - 1][j + 1] = '▒▒'
                        except (Exception, IndexError):
                            pass
                        try:
                            if j - 1 < 0 or i - 1 < 0:
                                raise Exception
                            if self.comp_board[i - 1][j - 1] == '░░':
                                self.comp_board[i - 1][j - 1] = '▒▒'
                        except (Exception, IndexError):
                            pass

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

        def check_of_codinates(point):  # функция проверяющая соответствие введенных значений реальным координатам
            if (point[0] in string.ascii_uppercase[:8]) and (
                    point[1] in [str(i) for i in range(1, 9)]) and not can_put_point(point):
                return True
            else:
                return False

        for i in range(4):  # расстанока катеров
            a = input(f'Катеров оставлось {4 - i}, куда катера ставим: ')
            while not check_of_codinates(a):
                a = input(f'Ай, косячим! Катеров оставлось {4 - i}, куда катера ставим: ')
            placement(a)
            Zero_to_Two()
        self.player_board_print()

        for i in range(3):  # расстановка эсминцев
            a, b = input(f'Эсминцев осталось {3 - i}, куда ставим: ').split(' ')
            while (not check_of_codinates(a) or not check_of_codinates(b)) or not xor(
                    (a[0] != b[0]) or (abs(int(a[1]) - int(b[1])) != 1), (a[1] != b[1] or (
                            (a[0] + b[0] not in string.ascii_uppercase) and (
                            b[0] + a[0] not in string.ascii_uppercase)))):
                a, b = input(f'Ай, косячим! Эсминцев осталось {3 - i}, куда ставим: ').split(' ')
            placement(a)
            placement(b)
            Zero_to_Two()
        self.player_board_print()

        for i in range(2):  # расстановка крейсеров
            a, b = input(f'Крейсеров осталось {2 - i}, куда ставим: ').split(' ')
            c = 'Z1'
            for letter in string.ascii_uppercase[:8]:
                if (a[0] == b[0]) and (abs(int(a[1]) - int(b[1])) == 2):
                    c = a[0] + str(max(int(a[1]), int(b[1])) - 1)

                elif (a[1] == b[1]) and (((a[0] + letter + b[0]) in string.ascii_uppercase) or (
                        (b[0] + letter + a[0]) in string.ascii_uppercase)):
                    c = letter + a[1]

            while not check_of_codinates(a) or not check_of_codinates(b) or not check_of_codinates(c) or not xor(
                    (a[0] != b[0]) or (abs(int(a[1]) - int(b[1])) != 2), (a[1] != b[1] or (
                            (a[0] + c[0] + b[0] not in string.ascii_uppercase) and (
                            b[0] + c[0] + a[0] not in string.ascii_uppercase)))):
                a, b = input(f'Ой, косячим! Крейсеров осталось {2 - i}, куда ставим: ').split(' ')
                for letter in string.ascii_uppercase[:8]:
                    if (a[0] == b[0]) and (abs(int(a[1]) - int(b[1])) == 2):
                        c = a[0] + str(max(int(a[1]), int(b[1])) - 1)

                    elif (a[1] == b[1]) and (((a[0] + letter + b[0]) in string.ascii_uppercase) or (
                            (b[0] + letter + a[0]) in string.ascii_uppercase)):
                        c = letter + a[1]
            placement(a)
            placement(c)
            placement(b)
            Zero_to_Two()
        self.player_board_print()  # ◙░▒▓█

        a, b = input(f'Линкоров осталось 1, куда ставим: ').split(' ')

        if (a[1] == b[1]) and string.ascii_uppercase.index(b[0]) > string.ascii_uppercase.index(a[0]):
            c = string.ascii_uppercase[string.ascii_uppercase.index(a[0]) + 1] + a[1]
            d = string.ascii_uppercase[string.ascii_uppercase.index(a[0]) + 2] + a[1]

        elif (a[1] == b[1]) and string.ascii_uppercase.index(b[0]) < string.ascii_uppercase.index(a[0]):
            c = string.ascii_uppercase[string.ascii_uppercase.index(b[0]) + 1] + a[1]
            d = string.ascii_uppercase[string.ascii_uppercase.index(b[0]) + 2] + a[1]

        elif (a[0] == b[0]) and (abs(int(a[1]) - int(b[1])) == 3):
            c = a[0] + str(max(int(a[1]), int(b[1])) - 1)
            d = a[0] + str(max(int(a[1]), int(b[1])) - 2)

        else:
            c = 'Z1'
            d = 'X1'

        while not check_of_codinates(a) or not check_of_codinates(b) or not check_of_codinates(
                c) or not check_of_codinates(d) or not xor((a[0] != b[0]) or (abs(int(a[1]) - int(b[1])) != 3),
                                                           (a[1] != b[1] or (
                                                                   (a[0] + c[0] + d[0] + b[
                                                                       0] not in string.ascii_uppercase) and (
                                                                           b[0] + c[0] + d[0] + a[
                                                                       0] not in string.ascii_uppercase)))):
            a, b = input(f'Ой, косячим! Линкоров осталось 1, куда ставим: ').split(' ')

            if (a[1] == b[1]) and string.ascii_uppercase.index(b[0]) > string.ascii_uppercase.index(a[0]):
                c = string.ascii_uppercase[string.ascii_uppercase.index(a[0]) + 1] + a[1]
                d = string.ascii_uppercase[string.ascii_uppercase.index(a[0]) + 2] + a[1]

            elif (a[1] == b[1]) and string.ascii_uppercase.index(b[0]) < string.ascii_uppercase.index(a[0]):
                c = string.ascii_uppercase[string.ascii_uppercase.index(b[0]) + 1] + a[1]
                d = string.ascii_uppercase[string.ascii_uppercase.index(b[0]) + 2] + a[1]

            elif (a[0] == b[0]) and (abs(int(a[1]) - int(b[1])) == 3):
                c = a[0] + str(max(int(a[1]), int(b[1])) - 1)
                d = a[0] + str(max(int(a[1]), int(b[1])) - 2)

            else:
                c = 'Z1'
                d = 'X1'
            print(a, c, d, b)
        placement(a)
        placement(b)
        placement(c)
        placement(d)
        Zero_to_Two()
        self.player_board_print()
        self.copy_of_player_board = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        for i in range(len(self.player_board)):
            for j in range(len(self.player_board[i])):
                if self.player_board[i][j] == '██':
                    self.copy_of_player_board[i][j] = 1

    def placement_of_ships_bot(self):  # расстановка кораблей противника

        '''self.copy_of_player_board = [
            [1, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 1, 1]
        ]'''

        self.comp_board = bot_board
        self.copy_of_comp_board = point_board
        def Zero_to_Two():  # определяет область на которой запрещено будет ставить корабли
            for i in range(len(self.comp_board)):
                for j in range(len(self.comp_board[i])):
                    if self.comp_board[i][j] == 1:
                        try:
                            if self.comp_board[i + 1][j] == 0:
                                self.comp_board[i + 1][j] = 2
                        except:
                            pass
                        try:
                            if self.comp_board[i][j + 1] == 0:
                                self.comp_board[i][j + 1] = 2
                        except:
                            pass
                        try:
                            if self.comp_board[i - 1][j] == 0 and (i - 1 >= 0):
                                self.comp_board[i - 1][j] = 2
                        except:
                            pass
                        try:
                            if self.comp_board[i][j - 1] == 0 and (j - 1 >= 0):
                                self.comp_board[i][j - 1] = 2
                        except:
                            pass
                        try:
                            if self.comp_board[i + 1][j + 1] == 0:
                                self.comp_board[i + 1][j + 1] = 2
                        except:
                            pass
                        try:
                            if self.comp_board[i + 1][j - 1] == 0 and (j - 1 >= 0):
                                self.comp_board[i + 1][j - 1] = 2
                        except:
                            pass
                        try:
                            if self.comp_board[i - 1][j + 1] == 0 and (i - 1 >= 0):
                                self.comp_board[i - 1][j + 1] = 2
                        except:
                            pass
                        try:
                            if self.comp_board[i - 1][j - 1] == 0 and (j - 1 >= 0) and (i - 1 >= 0):
                                self.comp_board[i - 1][j - 1] = 2
                        except:
                            pass
        def can_put_point(x, y):
            if self.comp_board[x][y] == 1 or self.comp_board[x][y] == 2:
                return True
            else: return False



        # расставляет линкор
        main_flag = True
        while main_flag:
            self.comp_board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
            a = randint(0, 7)
            b = randint(0, 7)
            direction = randint(1, 4)
            if direction == 1:
                try:
                    self.comp_board[a][b] = 1
                    self.comp_board[a][b + 3] = 1
                    self.comp_board[a][b + 2] = 1
                    self.comp_board[a][b + 1] = 1
                except:
                    try:
                        self.comp_board[a][b] = 1
                        self.comp_board[a + 3][b] = 1
                        self.comp_board[a + 2][b] = 1
                        self.comp_board[a + 1][b] = 1
                    except:
                        self.comp_board[a][b] = 1
                        self.comp_board[a][b - 3] = 1
                        self.comp_board[a][b - 2] = 1
                        self.comp_board[a][b - 1] = 1

            elif direction == 2:
                try:
                    self.comp_board[a][b] = 1
                    self.comp_board[a + 3][b] = 1
                    self.comp_board[a + 2][b] = 1
                    self.comp_board[a + 1][b] = 1
                except:
                    try:
                        if b - 3 < 0:
                            raise Exception
                        self.comp_board[a][b] = 1
                        self.comp_board[a][b - 3] = 1
                        self.comp_board[a][b - 2] = 1
                        self.comp_board[a][b - 1] = 1
                    except (Exception, IndexError):
                        self.comp_board[a][b] = 1
                        self.comp_board[a - 3][b] = 1
                        self.comp_board[a - 2][b] = 1
                        self.comp_board[a - 1][b] = 1

            elif direction == 3:
                try:
                    if b - 3 < 0:
                        raise Exception
                    self.comp_board[a][b] = 1
                    self.comp_board[a][b - 3] = 1
                    self.comp_board[a][b - 2] = 1
                    self.comp_board[a][b - 1] = 1
                except (Exception, IndexError):
                    try:
                        if a - 3 < 0:
                            raise Exception
                        self.comp_board[a][b] = 1
                        self.comp_board[a - 3][b] = 1
                        self.comp_board[a - 2][b] = 1
                        self.comp_board[a - 1][b] = 1
                    except (Exception, IndexError):
                        self.comp_board[a][b] = 1
                        self.comp_board[a][b + 3] = 1
                        self.comp_board[a][b + 2] = 1
                        self.comp_board[a][b + 1] = 1

            elif direction == 4:
                try:
                    if a - 3 < 0:
                        raise Exception
                    self.comp_board[a][b] = 1
                    self.comp_board[a - 3][b] = 1
                    self.comp_board[a - 2][b] = 1
                    self.comp_board[a - 1][b] = 1
                except (Exception, IndexError):
                    try:
                        self.comp_board[a][b] = 1
                        self.comp_board[a][b + 3] = 1
                        self.comp_board[a][b + 2] = 1
                        self.comp_board[a][b + 1] = 1
                    except:
                        self.comp_board[a][b] = 1
                        self.comp_board[a + 3][b] = 1
                        self.comp_board[a + 2][b] = 1
                        self.comp_board[a + 1][b] = 1
            Zero_to_Two()


            #расставляет крейсеры
            for i in range(2):
                flag_cru = True
                a = randint(0, 7)
                b = randint(0, 7)
                direction = randint(1, 4)
                while flag_cru:
                    if direction == 1:
                        try:
                            if self.comp_board[a][b + 2] != 0 or self.comp_board[a][b + 1] != 0 or self.comp_board[a][b] != 0:
                                raise Exception
                            self.comp_board[a][b] = 1
                            self.comp_board[a][b + 2] = 1
                            self.comp_board[a][b + 1] = 1
                            flag_cru = False
                        except (Exception, IndexError):
                            try:
                                if self.comp_board[a + 2][b] != 0 or self.comp_board[a + 1][b] != 0  or self.comp_board[a][b] != 0:
                                    raise Exception
                                self.comp_board[a][b] = 1
                                self.comp_board[a + 2][b] = 1
                                self.comp_board[a + 1][b] = 1
                                flag_cru = False
                            except (Exception, IndexError):
                                try:
                                    if self.comp_board[a][b - 2] != 0 or self.comp_board[a][b - 1] != 0 or (b - 2 < 0) or self.comp_board[a][b] != 0:
                                        raise Exception
                                    self.comp_board[a][b] = 1
                                    self.comp_board[a][b - 2] = 1
                                    self.comp_board[a][b - 1] = 1
                                    flag_cru = False
                                except (Exception, IndexError):
                                    try:
                                        if self.comp_board[a - 2][b] != 0 or self.comp_board[a - 1][b] != 0 or (a - 2 < 0)  or self.comp_board[a][b] != 0:
                                            raise Exception
                                        self.comp_board[a][b] = 1
                                        self.comp_board[a - 2][b] = 1
                                        self.comp_board[a - 1][b] = 1
                                        flag_cru = False
                                    except (Exception, IndexError):
                                        flag_cru = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)


                    elif direction == 2:
                        try:
                            if self.comp_board[a + 2][b] != 0 or self.comp_board[a + 1][b] != 0  or self.comp_board[a][b] != 0:
                                raise Exception
                            self.comp_board[a][b] = 1
                            self.comp_board[a + 2][b] = 1
                            self.comp_board[a + 1][b] = 1
                            flag_cru = False
                        except (Exception, IndexError):
                            try:
                                if self.comp_board[a][b - 2] != 0 or self.comp_board[a][b - 1] != 0 or (b - 2 < 0)  or self.comp_board[a][b] != 0:
                                    raise Exception
                                self.comp_board[a][b] = 1
                                self.comp_board[a][b - 2] = 1
                                self.comp_board[a][b - 1] = 1
                                flag_cru = False
                            except (Exception, IndexError):
                                try:
                                    if self.comp_board[a - 2][b] != 0 or self.comp_board[a - 1][b] != 0 or (a - 2 < 0)  or self.comp_board[a][b] != 0:
                                        raise Exception
                                    self.comp_board[a][b] = 1
                                    self.comp_board[a - 2][b] = 1
                                    self.comp_board[a - 1][b] = 1
                                    flag_cru = False
                                except (Exception, IndexError):
                                    try:
                                        if self.comp_board[a][b + 2] != 0 or self.comp_board[a][b + 1] != 0  or self.comp_board[a][b] != 0:
                                            raise Exception
                                        self.comp_board[a][b] = 1
                                        self.comp_board[a][b + 2] = 1
                                        self.comp_board[a][b + 1] = 1
                                        flag_cru = False
                                    except (Exception, IndexError):
                                        flag_cru = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)

                    elif direction == 3:
                        try:
                            if self.comp_board[a][b - 2] != 0 or self.comp_board[a][b - 1] != 0 or (b - 2 < 0) or self.comp_board[a][b] != 0:
                                raise Exception
                            self.comp_board[a][b] = 1
                            self.comp_board[a][b - 2] = 1
                            self.comp_board[a][b - 1] = 1
                            flag_cru = False
                        except (Exception, IndexError):
                            try:
                                if self.comp_board[a - 2][b] != 0 or self.comp_board[a - 1][b] != 0 or (a - 2 < 0) or self.comp_board[a][b] != 0:
                                    raise Exception
                                self.comp_board[a][b] = 1
                                self.comp_board[a - 2][b] = 1
                                self.comp_board[a - 1][b] = 1
                                flag_cru = False
                            except (Exception, IndexError):
                                try:
                                    if self.comp_board[a][b + 2] != 0 or self.comp_board[a][b + 1] != 0 or self.comp_board[a][b] != 0:
                                        raise Exception
                                    self.comp_board[a][b] = 1
                                    self.comp_board[a][b + 2] = 1
                                    self.comp_board[a][b + 1] = 1
                                    flag_cru = False
                                except (Exception, IndexError):
                                    try:
                                        if self.comp_board[a + 2][b] != 0 or self.comp_board[a + 1][b] != 0 or self.comp_board[a][b] != 0:
                                            raise Exception
                                        self.comp_board[a][b] = 1
                                        self.comp_board[a + 2][b] = 1
                                        self.comp_board[a + 1][b] = 1
                                        flag_cru = False
                                    except (Exception, IndexError):
                                        flag_cru = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)

                    elif direction == 4:
                        try:
                            if self.comp_board[a - 2][b] != 0 or self.comp_board[a - 1][b] != 0 or (a - 2 < 0) or self.comp_board[a][b] != 0:
                                raise Exception
                            self.comp_board[a][b] = 1
                            self.comp_board[a - 2][b] = 1
                            self.comp_board[a - 1][b] = 1
                            flag_cru = False
                        except (Exception, IndexError):
                            try:
                                if self.comp_board[a][b + 2] != 0 or self.comp_board[a][b + 1] != 0 or self.comp_board[a][b] != 0:
                                    raise Exception
                                self.comp_board[a][b] = 1
                                self.comp_board[a][b + 2] = 1
                                self.comp_board[a][b + 1] = 1
                                flag_cru = False
                            except (Exception, IndexError):
                                try:
                                    if self.comp_board[a + 2][b] != 0 or self.comp_board[a + 1][b] != 0 or self.comp_board[a][b] != 0:
                                        raise Exception
                                    self.comp_board[a][b] = 1
                                    self.comp_board[a + 2][b] = 1
                                    self.comp_board[a + 1][b] = 1
                                    flag_cru = False
                                except (Exception, IndexError):
                                    try:
                                        if self.comp_board[a][b - 2] != 0 or self.comp_board[a][b - 1] != 0 or (b - 2 < 0) or self.comp_board[a][b] != 0:
                                            raise Exception
                                        self.comp_board[a][b] = 1
                                        self.comp_board[a][b - 2] = 1
                                        self.comp_board[a][b - 1] = 1
                                        flag_cru = False
                                    except (Exception, IndexError):
                                        flag_cru = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)
                    Zero_to_Two()


            for i in range(3): #расставляет эсминцы
                flag_esm = True
                a = randint(0, 7)
                b = randint(0, 7)
                direction = randint(1, 4)
                while flag_esm:
                    if direction == 1:
                        try:
                            if self.comp_board[a][b + 1] != 0 or self.comp_board[a][b] != 0:
                                raise Exception
                            self.comp_board[a][b] = 1
                            self.comp_board[a][b + 1] = 1
                            flag_esm = False
                        except (Exception, IndexError):
                            try:
                                if self.comp_board[a + 1][b] != 0  or self.comp_board[a][b] != 0:
                                    raise Exception
                                self.comp_board[a][b] = 1
                                self.comp_board[a + 1][b] = 1
                                flag_esm = False
                            except (Exception, IndexError):
                                try:
                                    if self.comp_board[a][b - 1] != 0 or (b - 1 < 0) or self.comp_board[a][b] != 0:
                                        raise Exception
                                    self.comp_board[a][b] = 1
                                    self.comp_board[a][b - 1] = 1
                                    flag_esm = False
                                except (Exception, IndexError):
                                    try:
                                        if self.comp_board[a - 1][b] != 0 or (a - 1 < 0)  or self.comp_board[a][b] != 0:
                                            raise Exception
                                        self.comp_board[a][b] = 1
                                        self.comp_board[a - 1][b] = 1
                                        flag_esm = False
                                    except (Exception, IndexError):
                                        flag_esm = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)


                    elif direction == 2:
                        try:
                            if self.comp_board[a + 1][b] != 0  or self.comp_board[a][b] != 0:
                                raise Exception
                            self.comp_board[a][b] = 1
                            self.comp_board[a + 1][b] = 1
                            flag_esm = False
                        except (Exception, IndexError):
                            try:
                                if self.comp_board[a][b - 1] != 0 or (b - 1 < 0)  or self.comp_board[a][b] != 0:
                                    raise Exception
                                self.comp_board[a][b] = 1
                                self.comp_board[a][b - 1] = 1
                                flag_esm = False
                            except (Exception, IndexError):
                                try:
                                    if self.comp_board[a - 1][b] != 0 or (a - 1 < 0)  or self.comp_board[a][b] != 0:
                                        raise Exception
                                    self.comp_board[a][b] = 1
                                    self.comp_board[a - 1][b] = 1
                                    flag_esm = False
                                except (Exception, IndexError):
                                    try:
                                        if self.comp_board[a][b + 1] != 0  or self.comp_board[a][b] != 0:
                                            raise Exception
                                        self.comp_board[a][b] = 1
                                        self.comp_board[a][b + 1] = 1
                                        flag_esm = False
                                    except (Exception, IndexError):
                                        flag_esm = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)

                    elif direction == 3:
                        try:
                            if self.comp_board[a][b - 1] != 0 or (b - 1 < 0) or self.comp_board[a][b] != 0:
                                raise Exception
                            self.comp_board[a][b] = 1
                            self.comp_board[a][b - 1] = 1
                            flag_esm = False
                        except (Exception, IndexError):
                            try:
                                if self.comp_board[a - 1][b] != 0 or (a - 1 < 0) or self.comp_board[a][b] != 0:
                                    raise Exception
                                self.comp_board[a][b] = 1
                                self.comp_board[a - 1][b] = 1
                                flag_esm = False
                            except (Exception, IndexError):
                                try:
                                    if self.comp_board[a][b + 1] != 0 or self.comp_board[a][b] != 0:
                                        raise Exception
                                    self.comp_board[a][b] = 1
                                    self.comp_board[a][b + 1] = 1
                                    flag_esm = False
                                except (Exception, IndexError):
                                    try:
                                        if self.comp_board[a + 1][b] != 0 or self.comp_board[a][b] != 0:
                                            raise Exception
                                        self.comp_board[a][b] = 1
                                        self.comp_board[a + 1][b] = 1
                                        flag_esm = False
                                    except (Exception, IndexError):
                                        flag_esm = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)

                    elif direction == 4:
                        try:
                            if self.comp_board[a - 1][b] != 0 or (a - 1 < 0) or self.comp_board[a][b] != 0:
                                raise Exception
                            self.comp_board[a][b] = 1
                            self.comp_board[a - 1][b] = 1
                            flag_esm = False
                        except (Exception, IndexError):
                            try:
                                if self.comp_board[a][b + 1] != 0 or self.comp_board[a][b] != 0:
                                    raise Exception
                                self.comp_board[a][b] = 1
                                self.comp_board[a][b + 1] = 1
                                flag_esm = False
                            except (Exception, IndexError):
                                try:
                                    if self.comp_board[a + 1][b] != 0 or self.comp_board[a][b] != 0:
                                        raise Exception
                                    self.comp_board[a][b] = 1
                                    self.comp_board[a + 1][b] = 1
                                    flag_esm = False
                                except (Exception, IndexError):
                                    try:
                                        if self.comp_board[a][b - 1] != 0 or (b - 1 < 0) or self.comp_board[a][b] != 0:
                                            raise Exception
                                        self.comp_board[a][b] = 1
                                        self.comp_board[a][b - 1] = 1
                                        flag_esm = False
                                    except (Exception, IndexError):
                                        flag_esm = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)
                    Zero_to_Two()

            count_kat = 0
            for i in range(4): #расставляет катера
                flag_kat = False
                for j in range(len(self.comp_board)):
                    for k in range(len(self.comp_board[i])):
                        if self.comp_board[j][k] == 0:
                            self.comp_board[j][k] = 1
                            Zero_to_Two()
                            flag_kat = True
                            count_kat += 1
                            break
                    if flag_kat: break
            if count_kat < 4:
                main_flag = True
            elif count_kat == 4:
                main_flag = False


    def bot_board_print(self):  # вывод стола игрока
        st = ''
        k = 1
        for i in self.comp_board:
            print(*i)

    def check_point(self, point):
        if len(point) == 2:
            if point[0] in string.ascii_uppercase[:8] and point[1] in '12345678' and (point in self.points[0] or point in self.points[1] or point in self.points[2] or point in self.points[3] or point in self.points[4] or point in self.points[5] or point in self.points[6] or point in self.points[7]):
                return True
        else: return False


    def player_shoot(self, point): # 3 - попал    4 - промах
        if point[0] == 'A':
            if self.comp_board[int(point[1]) - 1][0] == 1:
                if (int(point[1]) - 1) > 0 and (int(point[1]) - 1) < 7:
                    if self.comp_board[int(point[1]) - 2][0] != 1 and self.comp_board[int(point[1])][0] != 1 and self.comp_board[int(point[1]) - 1][1] != 1:
                        print('Убит')
                        self.comp_board[int(point[1]) - 1][0] = 3
                        self.copy_of_comp_board[int(point[1]) - 1][0] = 'x'
                        self.points[int(point[1]) - 1][0] = 0
                        return True
                    else:
                        print('Ранен')
                        self.comp_board[int(point[1]) - 1][0] = 3
                        self.copy_of_comp_board[int(point[1]) - 1][0] = 'x'
                        self.points[int(point[1]) - 1][0] = 0
                        return True
                elif (int(point[1]) - 1) == 0:
                    if self.comp_board[int(point[1])][0] != 1 and self.comp_board[int(point[1]) - 1][1] != 1:
                        print('Убит')
                        self.comp_board[int(point[1]) - 1][0] = 3
                        self.copy_of_comp_board[int(point[1]) - 1][0] = 'x'
                        self.points[int(point[1]) - 1][0] = 0
                        return True
                    else:
                        print('Ранен')
                        self.comp_board[int(point[1]) - 1][0] = 3
                        self.copy_of_comp_board[int(point[1]) - 1][0] = 'x'
                        self.points[int(point[1]) - 1][0] = 0
                        return True
                elif (int(point[1]) - 1) == 7:
                    if self.comp_board[int(point[1]) - 2][0] != 1 and self.comp_board[int(point[1]) - 1][1] != 1:
                        print('Убит')
                        self.comp_board[int(point[1]) - 1][0] = 3
                        self.copy_of_comp_board[int(point[1]) - 1][0] = 'x'
                        self.points[int(point[1]) - 1][0] = 0
                        return True
                    else:
                        print('Ранен')
                        self.comp_board[int(point[1]) - 1][0] = 3
                        self.copy_of_comp_board[int(point[1]) - 1][0] = 'x'
                        self.points[int(point[1]) - 1][0] = 0
                        return True

            else:
                print('Промах')
                self.comp_board[int(point[1]) - 1][0] = 4
                self.copy_of_comp_board[int(point[1]) - 1][0] = 'o'
                self.points[int(point[1]) - 1][0] = 0
                return False


        elif point[0] == 'H':
            if self.comp_board[int(point[1]) - 1][7] == 1:
                if (int(point[1]) - 1) > 0 and (int(point[1]) - 1) < 7:
                    if self.comp_board[int(point[1]) - 2][7] != 1 and self.comp_board[int(point[1])][7] != 1 and \
                            self.comp_board[int(point[1]) - 1][6] != 1:
                        print('Убит')
                        self.comp_board[int(point[1]) - 1][7] = 3
                        self.copy_of_comp_board[int(point[1]) - 1][7] = 'x'
                        self.points[int(point[1]) - 1][7] = 0
                        return True
                    else:
                        print('Ранен')
                        self.comp_board[int(point[1]) - 1][7] = 3
                        self.copy_of_comp_board[int(point[1]) - 1][7] = 'x'
                        self.points[int(point[1]) - 1][7] = 0
                        return True
                elif (int(point[1]) - 1) == 0:
                    if self.comp_board[int(point[1])][0] != 1 and self.comp_board[int(point[1]) - 1][6] != 1:
                        print('Убит')
                        self.comp_board[int(point[1]) - 1][7] = 3
                        self.copy_of_comp_board[int(point[1]) - 1][7] = 'x'
                        self.points[int(point[1]) - 1][7] = 0
                        return True
                    else:
                        print('Ранен')
                        self.comp_board[int(point[1]) - 1][7] = 3
                        self.copy_of_comp_board[int(point[1]) - 1][7] = 'x'
                        self.points[int(point[1]) - 1][7] = 0
                        return True
                elif (int(point[1]) - 1) == 7:
                    if self.comp_board[int(point[1]) - 2][7] != 1 and self.comp_board[int(point[1]) - 1][6] != 1:
                        print('Убит')
                        self.comp_board[int(point[1]) - 1][7] = 3
                        self.copy_of_comp_board[int(point[1]) - 1][7] = 'x'
                        self.points[int(point[1]) - 1][7] = 0
                        return True
                    else:
                        print('Ранен')
                        self.comp_board[int(point[1]) - 1][7] = 3
                        self.copy_of_comp_board[int(point[1]) - 1][7] = 'x'
                        self.points[int(point[1]) - 1][7] = 0
                        return True

            else:
                print('Промах')
                self.comp_board[int(point[1]) - 1][7] = 4
                self.copy_of_comp_board[int(point[1]) - 1][7] = 'o'
                self.points[int(point[1]) - 1][7] = 0
                return False


        else:
            count_let = 0
            for i in 'BCDEFG':
                count_let += 1
                if point[0] == i:
                    if self.comp_board[int(point[1]) - 1][count_let] == 1:
                        if (int(point[1]) - 1) > 0 and (int(point[1]) - 1) < 7:
                            if self.comp_board[int(point[1]) - 2][count_let] != 1 and self.comp_board[int(point[1])][count_let] != 1 and \
                                    self.comp_board[int(point[1]) - 1][count_let + 1] != 1 and self.comp_board[int(point[1]) - 1][count_let - 1] != 1:
                                print('Убит')
                                self.comp_board[int(point[1]) - 1][count_let] = 3
                                self.copy_of_comp_board[int(point[1]) - 1][count_let] = 'x'
                                self.points[int(point[1]) - 1][count_let] = 0
                                return True
                            else:
                                print('Ранен')
                                self.comp_board[int(point[1]) - 1][count_let] = 3
                                self.copy_of_comp_board[int(point[1]) - 1][count_let] = 'x'
                                self.points[int(point[1]) - 1][count_let] = 0
                                return True
                        elif (int(point[1]) - 1) == 0:
                            if self.comp_board[int(point[1])][count_let] != 1 and self.comp_board[int(point[1]) - 1][count_let + 1] != 1 and self.comp_board[int(point[1]) - 1][count_let - 1] != 1:
                                print('Убит')
                                self.comp_board[int(point[1]) - 1][count_let] = 3
                                self.copy_of_comp_board[int(point[1]) - 1][count_let] = 'x'
                                self.points[int(point[1]) - 1][count_let] = 0
                                return True
                            else:
                                print('Ранен')
                                self.comp_board[int(point[1]) - 1][count_let] = 3
                                self.copy_of_comp_board[int(point[1]) - 1][count_let] = 'x'
                                self.points[int(point[1]) - 1][count_let] = 0
                                return True
                        elif (int(point[1]) - 1) == 7:
                            if self.comp_board[int(point[1]) - 2][count_let] != 1 and self.comp_board[int(point[1]) - 1][count_let + 1] != 1 and self.comp_board[int(point[1]) - 1][count_let - 1] != 1:
                                print('Убит')
                                self.comp_board[int(point[1]) - 1][count_let] = 3
                                self.copy_of_comp_board[int(point[1]) - 1][count_let] = 'x'
                                self.points[int(point[1]) - 1][count_let] = 0
                                return True
                            else:
                                print('Ранен')
                                self.comp_board[int(point[1]) - 1][count_let] = 3
                                self.copy_of_comp_board[int(point[1]) - 1][count_let] = 'x'
                                self.points[int(point[1]) - 1][count_let] = 0
                                return True

                    else:
                        print('Промах')
                        self.comp_board[int(point[1]) - 1][count_let] = 4
                        self.copy_of_comp_board[int(point[1]) - 1][count_let] = 'o'
                        self.points[int(point[1]) - 1][count_let] = 0
                        return False


    def copy_of_comp_board_print(self):  # вывод известной информации о столе компьютера
        st = ' '
        k = 1
        for i in string.ascii_uppercase[:8]:
            st += ' | ' + i
        print(st + ' |')
        for i in range(len(self.copy_of_comp_board)):
            st = str(k)
            for j in range(len(self.copy_of_comp_board[i])):
                st += ' | ' + self.copy_of_comp_board[i][j]
            k += 1
            print(st + ' |')

    def bot_shoot(self):
        flag_of_shooting4 = False

        def check_of_location(i, j):  # определяет область на которой запрещено будет ставить корабли
            if self.copy_of_player_board[i][j] == 3:
                flag_of_location = False
                try:
                    if self.copy_of_player_board[i + 1][j] == 1:
                        flag_of_location = True
                    else: flag_of_location = False
                except:
                    pass
                try:
                    if self.copy_of_player_board[i][j + 1] == 1:
                        flag_of_location = True
                    else: flag_of_location = False
                except:
                    pass
                try:
                    if self.copy_of_player_board[i - 1][j] == 1 and (i - 1 >= 0):
                        flag_of_location = True
                    else: flag_of_location = False
                except:
                    pass
                try:
                    if self.copy_of_player_board[i][j - 1] == 1 and (j - 1 >= 0):
                        flag_of_location =True
                    else: flag_of_location = False
                except:
                    pass
                if flag_of_location:
                    return True
                elif not flag_of_location:
                    return False


        global special_flag
        def shoot_the_ships(x, y, flag):
            if self.copy_of_player_board[x][y] == 1:
                self.copy_of_player_board[x][y] = 3
                self.player_board[x][y] = '**'
                flag_dir = True
                while flag_dir:
                    if not check_of_location(x, y) and flag:
                        break
                    direction = randint(1, 4)
                    if direction == 1:
                        try:
                            if x+1 >= 7:
                                raise Exception

                            else:
                                if self.copy_of_player_board[x+1][y] == 1:
                                    self.copy_of_player_board[x+1][y] = 3
                                    self.player_board[x+1][y] = '**'
                                    if x+2 >= 7:
                                        raise Exception
                                    else:
                                        if self.copy_of_player_board[x + 2][y] == 1:
                                            self.copy_of_player_board[x + 2][y] = 3
                                            self.player_board[x + 2][y] = '**'
                                            if x+3 >= 7:
                                                raise Exception
                                            else:
                                                if self.copy_of_player_board[x + 3][y] == 1:
                                                    self.copy_of_player_board[x + 3][y] = 3
                                                    self.player_board[x + 3][y] = '**'
                                                    flag_dir = False
                                                elif self.copy_of_player_board[x + 3][y] == 0:
                                                    self.copy_of_player_board[x + 3][y] = 4
                                                    self.player_board[x + 3][y] = '**'
                                                    flag_dir = False
                                                else: flag_dir = True
                                        elif self.copy_of_player_board[x + 2][y] == 0:
                                            self.copy_of_player_board[x + 2][y] = 4
                                            self.player_board[x + 2][y] = '**'
                                            flag_dir = False
                                        else: flag_dir = True
                                elif self.copy_of_player_board[x+1][y] == 0:
                                    self.copy_of_player_board[x + 1][y] = 4
                                    self.player_board[x + 1][y] = '**'
                                    flag_dir = False
                                else: flag_dir = True

                        except (Exception, IndexError):
                            flag_dir = True

                    elif direction == 2:
                        try:
                            if y + 1 >= 7:
                                raise Exception

                            else:
                                if self.copy_of_player_board[x][y+1] == 1:
                                    self.copy_of_player_board[x][y+1] = 3
                                    self.player_board[x][y+1] = '**'
                                    if y + 2 >= 7:
                                        raise Exception
                                    else:
                                        if self.copy_of_player_board[x][y+2] == 1:
                                            self.copy_of_player_board[x][y+2] = 3
                                            self.player_board[x][y + 2] = '**'
                                            if y + 3 >= 7:
                                                raise Exception
                                            else:
                                                if self.copy_of_player_board[x][y+3] == 1:
                                                    self.copy_of_player_board[x][y+3] = 3
                                                    self.player_board[x][y + 3] = '**'
                                                    flag_dir = False
                                                elif self.copy_of_player_board[x][y+3] == 0:
                                                    self.copy_of_player_board[x][y+3] = 4
                                                    self.player_board[x][y + 3] = '**'
                                                    flag_dir = False
                                                else:
                                                    flag_dir = True
                                        elif self.copy_of_player_board[x][y+2] == 0:
                                            self.copy_of_player_board[x][y+2] = 4
                                            self.player_board[x][y + 2] = '**'
                                            flag_dir = False
                                        else:
                                            flag_dir = True
                                elif self.copy_of_player_board[x][y+1] == 0:
                                    self.copy_of_player_board[x][y+1] = 4
                                    self.player_board[x][y + 1] = '**'
                                    flag_dir = False
                                else:
                                    flag_dir = True

                        except (Exception, IndexError):
                            flag_dir = True

                    elif direction == 3:
                        try:
                            if x - 1 < 0:
                                raise Exception

                            else:
                                if self.copy_of_player_board[x - 1][y] == 1:
                                    self.copy_of_player_board[x - 1][y] = 3
                                    self.player_board[x - 1][y] = '**'
                                    if x - 2 < 0:
                                        raise Exception
                                    else:
                                        if self.copy_of_player_board[x - 2][y] == 1:
                                            self.copy_of_player_board[x - 2][y] = 3
                                            self.player_board[x - 2][y] = '**'
                                            if x - 3 < 0:
                                                raise Exception
                                            else:
                                                if self.copy_of_player_board[x - 3][y] == 1:
                                                    self.copy_of_player_board[x - 3][y] = 3
                                                    self.player_board[x - 3][y] = '**'
                                                    flag_dir = False
                                                elif self.copy_of_player_board[x - 3][y] == 0:
                                                    self.copy_of_player_board[x - 3][y] = 4
                                                    self.player_board[x - 3][y] = '**'
                                                    flag_dir = False
                                                else:
                                                    flag_dir = True
                                        elif self.copy_of_player_board[x - 2][y] == 0:
                                            self.copy_of_player_board[x - 2][y] = 4
                                            self.player_board[x - 2][y] = '**'
                                            flag_dir = False
                                        else:
                                            flag_dir = True
                                elif self.copy_of_player_board[x - 1][y] == 0:
                                    self.copy_of_player_board[x - 1][y] = 4
                                    self.player_board[x - 1][y] = '**'
                                    flag_dir = False
                                else:
                                    flag_dir = True

                        except (Exception, IndexError):
                            flag_dir = True

                    elif direction == 4:
                        try:
                            if y - 1 < 0:
                                raise Exception

                            else:
                                if self.copy_of_player_board[x][y - 1] == 1:
                                    self.copy_of_player_board[x][y - 1] = 3
                                    self.player_board[x][y - 1] = '**'
                                    if y - 2 < 0:
                                        raise Exception
                                    else:
                                        if self.copy_of_player_board[x][y - 2] == 1:
                                            self.copy_of_player_board[x][y - 2] = 3
                                            self.player_board[x][y - 2] = '**'
                                            if y - 3 < 0:
                                                raise Exception
                                            else:
                                                if self.copy_of_player_board[x][y - 3] == 1:
                                                    self.copy_of_player_board[x][y - 3] = 3
                                                    self.player_board[x][y - 3] = '**'
                                                    flag_dir = False
                                                elif self.copy_of_player_board[x][y - 3] == 0:
                                                    self.copy_of_player_board[x][y - 3] = 4
                                                    self.player_board[x][y - 3] = '**'
                                                    flag_dir = False
                                                else:
                                                    flag_dir = True
                                        elif self.copy_of_player_board[x][y - 2] == 0:
                                            self.copy_of_player_board[x][y - 2] = 4
                                            self.player_board[x][y - 2] = '**'
                                            flag_dir = False
                                        else:
                                            flag_dir = True
                                elif self.copy_of_player_board[x][y - 1] == 0:
                                    self.copy_of_player_board[x][y - 1] = 4
                                    self.player_board[x][y - 1] = '**'
                                    flag_dir = False
                                else:
                                    flag_dir = True
                        except (Exception, IndexError):
                            flag_dir = True

            else:
                self.copy_of_player_board[x][y] = 4
                self.player_board[x][y] = '**'


        special_flag = True
        while special_flag:
            special_flag = False
            x_cord = self.x_shoot
            y_cord = self.y_shoot
            shoot_the_ships(x_cord, y_cord, flag_of_shooting4)
            while check_of_location(x_cord, y_cord):
                shoot_the_ships(x_cord, y_cord, flag_of_shooting4)




            if self.flag_of_shooting1:
                try:
                    if self.x_shoot + 1 > 7 or self.y_shoot + 1 > 7:
                        raise Exception
                    self.x_shoot += 1
                    self.y_shoot += 1
                except Exception:
                    self.flag_of_shooting1 = False
                    self.flag_of_shooting2 = True
                    self.x_shoot = 4
                    self.y_shoot = 0


            elif self.flag_of_shooting2:
                try:
                    if self.x_shoot + 1 > 7 or self.y_shoot + 1 > 7:
                        raise Exception
                    self.x_shoot += 1
                    self.y_shoot += 1
                except Exception:
                    self.flag_of_shooting2 = False
                    self.flag_of_shooting3 = True
                    self.x_shoot = 0
                    self.y_shoot = 4

            elif self.flag_of_shooting3:
                try:
                    if self.x_shoot + 1 > 7 or self.y_shoot + 1 > 7:
                        raise Exception
                    self.x_shoot += 1
                    self.y_shoot += 1
                except Exception:
                    self.flag_of_shooting3 = False
                    flag_of_shooting4 = True
                    ls = []
                    for i in range(len(self.copy_of_player_board)):
                        for j in range(len(self.copy_of_player_board[i])):
                            if self.copy_of_player_board[i][j] == 0 or self.copy_of_player_board[i][j] == 1:
                                ls.append([i, j])
                    rand = randint(0, len(ls)-1)
                    self.x_shoot = ls[rand][0]
                    self.y_shoot = ls[rand][1]
                    if self.copy_of_player_board[self.x_shoot][self.y_shoot] == 1:
                        special_flag = True
                    else:
                        special_flag = False

            elif not self.flag_of_shooting2 and not self.flag_of_shooting3 and not self.flag_of_shooting1:
                flag_of_shooting4 = True
                ls = []
                for i in range(len(self.copy_of_player_board)):
                    for j in range(len(self.copy_of_player_board[i])):
                        if self.copy_of_player_board[i][j] == 0 or self.copy_of_player_board[i][j] == 1:
                            ls.append([i, j])
                rand = randint(0, len(ls)-1)
                self.x_shoot = ls[rand][0]
                self.y_shoot = ls[rand][1]
                if self.copy_of_player_board[self.x_shoot][self.y_shoot] == 1:
                    special_flag = True
                else: special_flag = False



    def game_over(self):
        flag1 = True
        flag2 = True
        for i in range(len(self.copy_of_player_board)):
            for j in range(len(self.copy_of_player_board[i])):
                if self.copy_of_player_board[i][j] == 1:
                    flag1 = False

        for i in range(len(self.comp_board)):
            for j in range(len(self.comp_board[i])):
                if self.comp_board[i][j] == 1:
                    flag2 = False
        if flag2 or flag1:
            return True
        else:
            return False

    def who_won(self):
        flag_player = True
        flag_bot = True
        for i in range(len(self.copy_of_player_board)):
            for j in range(len(self.copy_of_player_board[i])):
                if self.copy_of_player_board[i][j] == 1:
                    flag_player = False
        for i in range(len(self.comp_board)):
            for j in range(len(self.comp_board[i])):
                if self.comp_board[i][j] == 1:
                    flag_bot = False
        if flag_player:
            print('Вы проиграли')
        elif flag_bot:
            print('Вы победили')
        else: print('Произошло недоразумение :(')


game = SeaBattle(board, board, board, board, True, False, True, 0, 0, points_list)
game.player_board_print()
game.placement_of_ships()
game.placement_of_ships_bot()
game.player_board_print()
print()
while not game.game_over():
    game.copy_of_comp_board_print()
    print()
    a = input("Введите точку, по которой хотите выстреллить: ")
    while (not game.check_point(a) or game.player_shoot(a)):
        a = input("Введите точку, по которой хотите выстреллить: ")
        if game.game_over():
            break
    if game.game_over():
        break
    game.bot_shoot()
    game.player_board_print()
    print()

game.who_won()