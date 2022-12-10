import string
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
    [0, 0, 0, 0, 0, 0, 0, 0],
]

class SeaBattle():
    def __init__(self, player_board, copy_of_player_board, copy_of_comp_board, comp_board):
        self.player_board = board
        self.copy_of_player_board = board
        self.copy_of_comp_board = board
        self.comp_board = board

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

    def copy_of_comp_board_print(self):  # вывод известной информации о столе компьютера
        st = '  '
        k = 1
        for i in string.ascii_uppercase[:8]:
            st += ' | ' + i
        print(st + ' |')
        for i in range(len(self.copy_of_comp_board)):
            st = str(k) + ' '
            for j in range(len(self.copy_of_comp_board[i])):
                st += ' | ' + self.copy_of_comp_board[i][j]
            k += 1
            print(st + ' |')

    def placement_of_ships(self):

        def placement(
                point):  # функция отвечающая за перевод координат в индексы матрицы и постановку в соотвествующую позицию символ '▢'
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

    def placement_of_ships_bot(self):  # расстановка кораблей противника

        self.comp_board = bot_board
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



        k = 0
        for i in range(2):
            flag_cru = True
            a = randint(0, 7)
            b = randint(0, 7)
            while not can_put_point(a, b) and k < 2:
                a = randint(0, 7)
                b = randint(0, 7)
                direction = randint(1, 4)
                if direction == 1:
                    try:
                        if self.comp_board[a][b + 2] != 0 or self.comp_board[a][b + 1] != 0 or self.comp_board[a][b] != 0:
                            raise Exception
                        self.comp_board[a][b] = 1
                        self.comp_board[a][b + 2] = 1
                        self.comp_board[a][b + 1] = 1
                        k += 1
                        flag_cru = False
                    except (Exception, IndexError):
                        try:
                            if self.comp_board[a + 2][b] != 0 or self.comp_board[a + 1][b] != 0  or self.comp_board[a][b] != 0:
                                raise Exception
                            self.comp_board[a][b] = 1
                            self.comp_board[a + 2][b] = 1
                            self.comp_board[a + 1][b] = 1
                            k += 1
                            flag_cru = False
                        except (Exception, IndexError):
                            try:
                                if self.comp_board[a][b - 2] != 0 or self.comp_board[a][b - 1] != 0 or (b - 2 < 0) or self.comp_board[a][b] != 0:
                                    raise Exception
                                self.comp_board[a][b] = 1
                                self.comp_board[a][b - 2] = 1
                                self.comp_board[a][b - 1] = 1
                                k += 1
                                flag_cru = False
                            except (Exception, IndexError):
                                try:
                                    if self.comp_board[a - 2][b] != 0 or self.comp_board[a - 1][b] != 0 or (a - 2 < 0)  or self.comp_board[a][b] != 0:
                                        raise Exception
                                    self.comp_board[a][b] = 1
                                    self.comp_board[a - 2][b] = 1
                                    self.comp_board[a - 1][b] = 1
                                    k += 1
                                    flag_cru = False
                                except (Exception, IndexError):
                                    flag_cru = True


                elif direction == 2:
                    try:
                        if self.comp_board[a + 2][b] != 0 or self.comp_board[a + 1][b] != 0  or self.comp_board[a][b] != 0:
                            raise Exception
                        self.comp_board[a][b] = 1
                        self.comp_board[a + 2][b] = 1
                        self.comp_board[a + 1][b] = 1
                        k += 1
                        flag_cru = False
                    except (Exception, IndexError):
                        try:
                            if self.comp_board[a][b - 2] != 0 or self.comp_board[a][b - 1] != 0 or (b - 2 < 0)  or self.comp_board[a][b] != 0:
                                raise Exception
                            self.comp_board[a][b] = 1
                            self.comp_board[a][b - 2] = 1
                            self.comp_board[a][b - 1] = 1
                            k += 1
                            flag_cru = False
                        except (Exception, IndexError):
                            try:
                                if self.comp_board[a - 2][b] != 0 or self.comp_board[a - 1][b] != 0 or (a - 2 < 0)  or self.comp_board[a][b] != 0:
                                    raise Exception
                                self.comp_board[a][b] = 1
                                self.comp_board[a - 2][b] = 1
                                self.comp_board[a - 1][b] = 1
                                k += 1
                                flag_cru = False
                            except (Exception, IndexError):
                                try:
                                    if self.comp_board[a][b + 2] != 0 or self.comp_board[a][b + 1] != 0  or self.comp_board[a][b] != 0:
                                        raise Exception
                                    self.comp_board[a][b] = 1
                                    self.comp_board[a][b + 2] = 1
                                    self.comp_board[a][b + 1] = 1
                                    k += 1
                                    flag_cru = False
                                except (Exception, IndexError):
                                    flag_cru = True

                elif direction == 3:
                    try:
                        if self.comp_board[a][b - 2] != 0 or self.comp_board[a][b - 1] != 0 or (b - 2 < 0) or self.comp_board[a][b] != 0:
                            raise Exception
                        self.comp_board[a][b] = 1
                        self.comp_board[a][b - 2] = 1
                        self.comp_board[a][b - 1] = 1
                        k += 1
                        flag_cru = False
                    except (Exception, IndexError):
                        try:
                            if self.comp_board[a - 2][b] != 0 or self.comp_board[a - 1][b] != 0 or (a - 2 < 0) or self.comp_board[a][b] != 0:
                                raise Exception
                            self.comp_board[a][b] = 1
                            self.comp_board[a - 2][b] = 1
                            self.comp_board[a - 1][b] = 1
                            k += 1
                            flag_cru = False
                        except (Exception, IndexError):
                            try:
                                if self.comp_board[a][b + 2] != 0 or self.comp_board[a][b + 1] != 0 or self.comp_board[a][b] != 0:
                                    raise Exception
                                self.comp_board[a][b] = 1
                                self.comp_board[a][b + 2] = 1
                                self.comp_board[a][b + 1] = 1
                                k += 1
                                flag_cru = False
                            except (Exception, IndexError):
                                try:
                                    if self.comp_board[a + 2][b] != 0 or self.comp_board[a + 1][b] != 0 or self.comp_board[a][b] != 0:
                                        raise Exception
                                    self.comp_board[a][b] = 1
                                    self.comp_board[a + 2][b] = 1
                                    self.comp_board[a + 1][b] = 1
                                    k += 1
                                    flag_cru = False
                                except (Exception, IndexError):
                                    flag_cru = True

                elif direction == 4:
                    try:
                        if self.comp_board[a - 2][b] != 0 or self.comp_board[a - 1][b] != 0 or (a - 2 < 0) or self.comp_board[a][b] != 0:
                            raise Exception
                        self.comp_board[a][b] = 1
                        self.comp_board[a - 2][b] = 1
                        self.comp_board[a - 1][b] = 1
                        k += 1
                        flag_cru = False
                    except (Exception, IndexError):
                        try:
                            if self.comp_board[a][b + 2] != 0 or self.comp_board[a][b + 1] != 0 or self.comp_board[a][b] != 0:
                                raise Exception
                            self.comp_board[a][b] = 1
                            self.comp_board[a][b + 2] = 1
                            self.comp_board[a][b + 1] = 1
                            k += 1
                            flag_cru = False
                        except (Exception, IndexError):
                            try:
                                if self.comp_board[a + 2][b] != 0 or self.comp_board[a + 1][b] != 0 or self.comp_board[a][b] != 0:
                                    raise Exception
                                self.comp_board[a][b] = 1
                                self.comp_board[a + 2][b] = 1
                                self.comp_board[a + 1][b] = 1
                                k += 1
                                flag_cru = False
                            except (Exception, IndexError):
                                try:
                                    if self.comp_board[a][b - 2] != 0 or self.comp_board[a][b - 1] != 0 or (b - 2 < 0) or self.comp_board[a][b] != 0:
                                        raise Exception
                                    self.comp_board[a][b] = 1
                                    self.comp_board[a][b - 2] = 1
                                    self.comp_board[a][b - 1] = 1
                                    k += 1
                                    flag_cru = False
                                except (Exception, IndexError):
                                    flag_cru = True
                print(a, b, direction)
                Zero_to_Two()






    def bot_board_print(self):  # вывод стола игрока
        st = '  '
        k = 1
        for i in string.ascii_uppercase[:8]:
            st += ' | ' + i
        print(st + ' |')
        for i in range(len(self.comp_board)):
            st = str(k) + ' '
            for j in range(len(self.comp_board[i])):
                st += ' | ' + str(self.comp_board[i][j])
            k += 1
            print(st + ' |')




game = SeaBattle(board, board, board, board)
#game.player_board_print()
game.placement_of_ships_bot()
game.bot_board_print()