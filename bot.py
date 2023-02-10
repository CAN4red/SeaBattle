'''
This code was written by Isupov Alexander at 10/02/2023. All rights are reserved.
'''

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from random import randint
import string
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

'''
This class is an implementation of the game "Sea battle"
'''
class SeaBattle():
    '''
    This constructor is used to create a class object of "Sea battle"

    :param _player_board: the player's board for his ships
    :param _copy_of_player_board: the bot board for shooting at the player's ships
    :param _copy_of_comp_board: the player's board for shooting at the ships of bot
    :param _comp_board: the bot board for his ships
    :param _flag_of_shooting1: if the flag is raised, then the bot shoots through the central diagonal of the board
    :param _flag_of_shooting2: if the flag is raised, then the bot shoots through the lower diagonal of the board (from A5 to D8)
    :param flag_of_shooting2: if the flag is raised, then the bot shoots through the higher diagonal of the board (from E1 to H4)
    :param _x_shoot: the starting X-coordinate for shooting of the bot
    :param _y_shoot: the starting Y-coordinate for shooting of the bot
    :param _points: the list of available coordinates for shooting
    '''
    def __init__(self, _player_board: list, _copy_of_player_board: list, _copy_of_comp_board: list, _comp_board: list,
                 _flag_of_shooting1: bool, _flag_of_shooting2: bool, _flag_of_shooting3: bool, _x_shoot: int, _y_shoot: int, _points: list) -> None:
        self._player_board = [
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
        ]
        self._copy_of_player_board = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self._copy_of_comp_board = [
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
            ['░░', '░░', '░░', '░░', '░░', '░░', '░░', '░░'],
        ]
        self._comp_board = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self._flag_of_shooting1 = True
        self._flag_of_shooting2 = False
        self._flag_of_shooting3 = False
        self._x_shoot = 0
        self._y_shoot = 0
        self._points = points_list

    '''
    The method for implementing the output of the player's board
    
    :@return st: (str) a string that contain all the data about the player's board with the coordinates designation
    '''
    def player_board_print(self) -> str:
        st = ' '
        k = 1
        for i in string.ascii_uppercase[:8]:
            st += '     ' + i
        for i in range(len(self._player_board)):
            st += '\n' + str(k) + ' '
            for j in range(len(self._player_board[i])):
                st += ' ' + self._player_board[i][j]
            k += 1
        return st

    '''
    The method for implementing the output of the board of the bot

    :@return st: (str) a string that contain all the data about the board of the bot with the coordinates designation
    '''
    def copy_of_comp_board_print(self) -> str:  # вывод стола игрока
        st = ' '
        k = 1
        for i in string.ascii_uppercase[:8]:
            st += '     ' + i
        for i in range(len(self._copy_of_comp_board)):
            st += '\n' + str(k) + ' '
            for j in range(len(self._copy_of_comp_board[i])):
                st += ' ' + self._copy_of_comp_board[i][j]
            k += 1
        return st



    '''
    The method for implementing converting coordinates to matrix indexes and placing the symbol in the appropriate position
    
    :@param point: (str) the coordinate
    '''
    def placement(self, point: str) -> None:
        if point[0] == 'A':
            self._player_board[int(point[1]) - 1][0] = '██'
        elif point[0] == 'B':
            self._player_board[int(point[1]) - 1][1] = '██'
        elif point[0] == 'C':
            self._player_board[int(point[1]) - 1][2] = '██'
        elif point[0] == 'D':
            self._player_board[int(point[1]) - 1][3] = '██'
        elif point[0] == 'E':
            self._player_board[int(point[1]) - 1][4] = '██'
        elif point[0] == 'F':
            self._player_board[int(point[1]) - 1][5] = '██'
        elif point[0] == 'G':
            self._player_board[int(point[1]) - 1][6] = '██'
        elif point[0] == 'H':
            self._player_board[int(point[1]) - 1][7] = '██'

    '''
    The method for implementing determination of the points that will be forbidden to put ships on player's board
    '''
    def Zero_to_Two(self) -> None:
        for i in range(len(self._player_board)):
            for j in range(len(self._player_board[i])):
                if self._player_board[i][j] == '██':
                    try:
                        if self._player_board[i + 1][j] == '░░':
                            self._player_board[i + 1][j] = '▒▒'
                    except:
                        pass
                    try:
                        if self._player_board[i][j + 1] == '░░':
                            self._player_board[i][j + 1] = '▒▒'
                    except:
                        pass
                    try:
                        if i - 1 < 0:
                            raise Exception
                        if self._player_board[i - 1][j] == '░░':
                            self._player_board[i - 1][j] = '▒▒'
                    except (Exception, IndexError):
                        pass
                    try:
                        if j - 1 < 0:
                            raise Exception
                        if self._player_board[i][j - 1] == '░░':
                            self._player_board[i][j - 1] = '▒▒'
                    except (Exception, IndexError):
                        pass
                    try:
                        if self._player_board[i + 1][j + 1] == '░░':
                            self._player_board[i + 1][j + 1] = '▒▒'
                    except:
                        pass
                    try:
                        if j - 1 < 0:
                            raise Exception
                        if self._player_board[i + 1][j - 1] == '░░':
                            self._player_board[i + 1][j - 1] = '▒▒'
                    except (Exception, IndexError):
                        pass
                    try:
                        if i - 1 < 0:
                            raise Exception
                        if self._player_board[i - 1][j + 1] == '░░':
                            self._player_board[i - 1][j + 1] = '▒▒'
                    except (Exception, IndexError):
                        pass
                    try:
                        if j - 1 < 0 or i - 1 < 0:
                            raise Exception
                        if self._player_board[i - 1][j - 1] == '░░':
                            self._player_board[i - 1][j - 1] = '▒▒'
                    except (Exception, IndexError):
                        pass

    '''
    The method for checking matching of the entered values to the real coordinates
    
    :@param point: (str) the coordinate (entered value)
    :@return: (bool) does it match or not
    '''
    def check_of_coordinates(self, point: str) -> bool:

        '''
        The function for checking is it possible to put a ship on a certain point

        :@param point: (str) the coordinate
        :@return: (bool) is it possible or not
        '''
        def _can_put_point(point: str) -> bool:  # функция отвечающая за проверку можно ли поставить на определенную точку корабль
            if point[0] == 'A':
                if self._player_board[int(point[1]) - 1][0] == '██' or self._player_board[int(point[1]) - 1][0] == '▒▒':
                    return True
                else:
                    return False
            elif point[0] == 'B':
                if self._player_board[int(point[1]) - 1][1] == '██' or self._player_board[int(point[1]) - 1][1] == '▒▒':
                    return True
                else:
                    return False
            elif point[0] == 'C':
                if self._player_board[int(point[1]) - 1][2] == '██' or self._player_board[int(point[1]) - 1][2] == '▒▒':
                    return True
                else:
                    return False
            elif point[0] == 'D':
                if self._player_board[int(point[1]) - 1][3] == '██' or self._player_board[int(point[1]) - 1][3] == '▒▒':
                    return True
                else:
                    return False
            elif point[0] == 'E':
                if self._player_board[int(point[1]) - 1][4] == '██' or self._player_board[int(point[1]) - 1][4] == '▒▒':
                    return True
                else:
                    return False
            elif point[0] == 'F':
                if self._player_board[int(point[1]) - 1][5] == '██' or self._player_board[int(point[1]) - 1][5] == '▒▒':
                    return True
                else:
                    return False
            elif point[0] == 'G':
                if self._player_board[int(point[1]) - 1][6] == '██' or self._player_board[int(point[1]) - 1][6] == '▒▒':
                    return True
                else:
                    return False
            elif point[0] == 'H':
                if self._player_board[int(point[1]) - 1][7] == '██' or self._player_board[int(point[1]) - 1][7] == '▒▒':
                    return True
                else:
                    return False

        if (point[0] in string.ascii_uppercase[:8]) and (
                point[1] in [str(i) for i in range(1, 9)]) and not _can_put_point(point):
            return True
        else:
            return False

    '''
    The method for placement of bot ships
    '''
    def placement_of_ships_bot(self) -> None:

        '''
        The function for implementing determination of the points that will be forbidden to put ships on bot board
        '''
        def _Zero_to_Two_comp() -> None:
            for i in range(len(self._comp_board)):
                for j in range(len(self._comp_board[i])):
                    if self._comp_board[i][j] == 1:
                        try:
                            if self._comp_board[i + 1][j] == 0:
                                self._comp_board[i + 1][j] = 2
                        except:
                            pass
                        try:
                            if self._comp_board[i][j + 1] == 0:
                                self._comp_board[i][j + 1] = 2
                        except:
                            pass
                        try:
                            if self._comp_board[i - 1][j] == 0 and (i - 1 >= 0):
                                self._comp_board[i - 1][j] = 2
                        except:
                            pass
                        try:
                            if self._comp_board[i][j - 1] == 0 and (j - 1 >= 0):
                                self._comp_board[i][j - 1] = 2
                        except:
                            pass
                        try:
                            if self._comp_board[i + 1][j + 1] == 0:
                                self._comp_board[i + 1][j + 1] = 2
                        except:
                            pass
                        try:
                            if self._comp_board[i + 1][j - 1] == 0 and (j - 1 >= 0):
                                self._comp_board[i + 1][j - 1] = 2
                        except:
                            pass
                        try:
                            if self._comp_board[i - 1][j + 1] == 0 and (i - 1 >= 0):
                                self._comp_board[i - 1][j + 1] = 2
                        except:
                            pass
                        try:
                            if self._comp_board[i - 1][j - 1] == 0 and (j - 1 >= 0) and (i - 1 >= 0):
                                self._comp_board[i - 1][j - 1] = 2
                        except:
                            pass


        main_flag = True
        while main_flag:
            self._comp_board = [
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
                    self._comp_board[a][b] = 1
                    self._comp_board[a][b + 3] = 1
                    self._comp_board[a][b + 2] = 1
                    self._comp_board[a][b + 1] = 1
                except:
                    try:
                        self._comp_board[a][b] = 1
                        self._comp_board[a + 3][b] = 1
                        self._comp_board[a + 2][b] = 1
                        self._comp_board[a + 1][b] = 1
                    except:
                        self._comp_board[a][b] = 1
                        self._comp_board[a][b - 3] = 1
                        self._comp_board[a][b - 2] = 1
                        self._comp_board[a][b - 1] = 1

            elif direction == 2:
                try:
                    self._comp_board[a][b] = 1
                    self._comp_board[a + 3][b] = 1
                    self._comp_board[a + 2][b] = 1
                    self._comp_board[a + 1][b] = 1
                except:
                    try:
                        if b - 3 < 0:
                            raise Exception
                        self._comp_board[a][b] = 1
                        self._comp_board[a][b - 3] = 1
                        self._comp_board[a][b - 2] = 1
                        self._comp_board[a][b - 1] = 1
                    except (Exception, IndexError):
                        self._comp_board[a][b] = 1
                        self._comp_board[a - 3][b] = 1
                        self._comp_board[a - 2][b] = 1
                        self._comp_board[a - 1][b] = 1

            elif direction == 3:
                try:
                    if b - 3 < 0:
                        raise Exception
                    self._comp_board[a][b] = 1
                    self._comp_board[a][b - 3] = 1
                    self._comp_board[a][b - 2] = 1
                    self._comp_board[a][b - 1] = 1
                except (Exception, IndexError):
                    try:
                        if a - 3 < 0:
                            raise Exception
                        self._comp_board[a][b] = 1
                        self._comp_board[a - 3][b] = 1
                        self._comp_board[a - 2][b] = 1
                        self._comp_board[a - 1][b] = 1
                    except (Exception, IndexError):
                        self._comp_board[a][b] = 1
                        self._comp_board[a][b + 3] = 1
                        self._comp_board[a][b + 2] = 1
                        self._comp_board[a][b + 1] = 1

            elif direction == 4:
                try:
                    if a - 3 < 0:
                        raise Exception
                    self._comp_board[a][b] = 1
                    self._comp_board[a - 3][b] = 1
                    self._comp_board[a - 2][b] = 1
                    self._comp_board[a - 1][b] = 1
                except (Exception, IndexError):
                    try:
                        self._comp_board[a][b] = 1
                        self._comp_board[a][b + 3] = 1
                        self._comp_board[a][b + 2] = 1
                        self._comp_board[a][b + 1] = 1
                    except:
                        self._comp_board[a][b] = 1
                        self._comp_board[a + 3][b] = 1
                        self._comp_board[a + 2][b] = 1
                        self._comp_board[a + 1][b] = 1
            _Zero_to_Two_comp()

            for i in range(2):
                flag_cru = True
                a = randint(0, 7)
                b = randint(0, 7)
                direction = randint(1, 4)
                while flag_cru:
                    if direction == 1:
                        try:
                            if self._comp_board[a][b + 2] != 0 or self._comp_board[a][b + 1] != 0 or \
                                    self._comp_board[a][b] != 0:
                                raise Exception
                            self._comp_board[a][b] = 1
                            self._comp_board[a][b + 2] = 1
                            self._comp_board[a][b + 1] = 1
                            flag_cru = False
                        except (Exception, IndexError):
                            try:
                                if self._comp_board[a + 2][b] != 0 or self._comp_board[a + 1][b] != 0 or \
                                        self._comp_board[a][b] != 0:
                                    raise Exception
                                self._comp_board[a][b] = 1
                                self._comp_board[a + 2][b] = 1
                                self._comp_board[a + 1][b] = 1
                                flag_cru = False
                            except (Exception, IndexError):
                                try:
                                    if self._comp_board[a][b - 2] != 0 or self._comp_board[a][b - 1] != 0 or (
                                            b - 2 < 0) or self._comp_board[a][b] != 0:
                                        raise Exception
                                    self._comp_board[a][b] = 1
                                    self._comp_board[a][b - 2] = 1
                                    self._comp_board[a][b - 1] = 1
                                    flag_cru = False
                                except (Exception, IndexError):
                                    try:
                                        if self._comp_board[a - 2][b] != 0 or self._comp_board[a - 1][b] != 0 or (
                                                a - 2 < 0) or self._comp_board[a][b] != 0:
                                            raise Exception
                                        self._comp_board[a][b] = 1
                                        self._comp_board[a - 2][b] = 1
                                        self._comp_board[a - 1][b] = 1
                                        flag_cru = False
                                    except (Exception, IndexError):
                                        flag_cru = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)


                    elif direction == 2:
                        try:
                            if self._comp_board[a + 2][b] != 0 or self._comp_board[a + 1][b] != 0 or \
                                    self._comp_board[a][b] != 0:
                                raise Exception
                            self._comp_board[a][b] = 1
                            self._comp_board[a + 2][b] = 1
                            self._comp_board[a + 1][b] = 1
                            flag_cru = False
                        except (Exception, IndexError):
                            try:
                                if self._comp_board[a][b - 2] != 0 or self._comp_board[a][b - 1] != 0 or (
                                        b - 2 < 0) or self._comp_board[a][b] != 0:
                                    raise Exception
                                self._comp_board[a][b] = 1
                                self._comp_board[a][b - 2] = 1
                                self._comp_board[a][b - 1] = 1
                                flag_cru = False
                            except (Exception, IndexError):
                                try:
                                    if self._comp_board[a - 2][b] != 0 or self._comp_board[a - 1][b] != 0 or (
                                            a - 2 < 0) or self._comp_board[a][b] != 0:
                                        raise Exception
                                    self._comp_board[a][b] = 1
                                    self._comp_board[a - 2][b] = 1
                                    self._comp_board[a - 1][b] = 1
                                    flag_cru = False
                                except (Exception, IndexError):
                                    try:
                                        if self._comp_board[a][b + 2] != 0 or self._comp_board[a][b + 1] != 0 or \
                                                self._comp_board[a][b] != 0:
                                            raise Exception
                                        self._comp_board[a][b] = 1
                                        self._comp_board[a][b + 2] = 1
                                        self._comp_board[a][b + 1] = 1
                                        flag_cru = False
                                    except (Exception, IndexError):
                                        flag_cru = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)

                    elif direction == 3:
                        try:
                            if self._comp_board[a][b - 2] != 0 or self._comp_board[a][b - 1] != 0 or (b - 2 < 0) or \
                                    self._comp_board[a][b] != 0:
                                raise Exception
                            self._comp_board[a][b] = 1
                            self._comp_board[a][b - 2] = 1
                            self._comp_board[a][b - 1] = 1
                            flag_cru = False
                        except (Exception, IndexError):
                            try:
                                if self._comp_board[a - 2][b] != 0 or self._comp_board[a - 1][b] != 0 or (
                                        a - 2 < 0) or self._comp_board[a][b] != 0:
                                    raise Exception
                                self._comp_board[a][b] = 1
                                self._comp_board[a - 2][b] = 1
                                self._comp_board[a - 1][b] = 1
                                flag_cru = False
                            except (Exception, IndexError):
                                try:
                                    if self._comp_board[a][b + 2] != 0 or self._comp_board[a][b + 1] != 0 or \
                                            self._comp_board[a][b] != 0:
                                        raise Exception
                                    self._comp_board[a][b] = 1
                                    self._comp_board[a][b + 2] = 1
                                    self._comp_board[a][b + 1] = 1
                                    flag_cru = False
                                except (Exception, IndexError):
                                    try:
                                        if self._comp_board[a + 2][b] != 0 or self._comp_board[a + 1][b] != 0 or \
                                                self._comp_board[a][b] != 0:
                                            raise Exception
                                        self._comp_board[a][b] = 1
                                        self._comp_board[a + 2][b] = 1
                                        self._comp_board[a + 1][b] = 1
                                        flag_cru = False
                                    except (Exception, IndexError):
                                        flag_cru = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)

                    elif direction == 4:
                        try:
                            if self._comp_board[a - 2][b] != 0 or self._comp_board[a - 1][b] != 0 or (a - 2 < 0) or \
                                    self._comp_board[a][b] != 0:
                                raise Exception
                            self._comp_board[a][b] = 1
                            self._comp_board[a - 2][b] = 1
                            self._comp_board[a - 1][b] = 1
                            flag_cru = False
                        except (Exception, IndexError):
                            try:
                                if self._comp_board[a][b + 2] != 0 or self._comp_board[a][b + 1] != 0 or \
                                        self._comp_board[a][b] != 0:
                                    raise Exception
                                self._comp_board[a][b] = 1
                                self._comp_board[a][b + 2] = 1
                                self._comp_board[a][b + 1] = 1
                                flag_cru = False
                            except (Exception, IndexError):
                                try:
                                    if self._comp_board[a + 2][b] != 0 or self._comp_board[a + 1][b] != 0 or \
                                            self._comp_board[a][b] != 0:
                                        raise Exception
                                    self._comp_board[a][b] = 1
                                    self._comp_board[a + 2][b] = 1
                                    self._comp_board[a + 1][b] = 1
                                    flag_cru = False
                                except (Exception, IndexError):
                                    try:
                                        if self._comp_board[a][b - 2] != 0 or self._comp_board[a][b - 1] != 0 or (
                                                b - 2 < 0) or self._comp_board[a][b] != 0:
                                            raise Exception
                                        self._comp_board[a][b] = 1
                                        self._comp_board[a][b - 2] = 1
                                        self._comp_board[a][b - 1] = 1
                                        flag_cru = False
                                    except (Exception, IndexError):
                                        flag_cru = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)
                    _Zero_to_Two_comp()

            for i in range(3):  # расставляет эсминцы
                flag_esm = True
                a = randint(0, 7)
                b = randint(0, 7)
                direction = randint(1, 4)
                while flag_esm:
                    if direction == 1:
                        try:
                            if self._comp_board[a][b + 1] != 0 or self._comp_board[a][b] != 0:
                                raise Exception
                            self._comp_board[a][b] = 1
                            self._comp_board[a][b + 1] = 1
                            flag_esm = False
                        except (Exception, IndexError):
                            try:
                                if self._comp_board[a + 1][b] != 0 or self._comp_board[a][b] != 0:
                                    raise Exception
                                self._comp_board[a][b] = 1
                                self._comp_board[a + 1][b] = 1
                                flag_esm = False
                            except (Exception, IndexError):
                                try:
                                    if self._comp_board[a][b - 1] != 0 or (b - 1 < 0) or self._comp_board[a][b] != 0:
                                        raise Exception
                                    self._comp_board[a][b] = 1
                                    self._comp_board[a][b - 1] = 1
                                    flag_esm = False
                                except (Exception, IndexError):
                                    try:
                                        if self._comp_board[a - 1][b] != 0 or (a - 1 < 0) or self._comp_board[a][
                                            b] != 0:
                                            raise Exception
                                        self._comp_board[a][b] = 1
                                        self._comp_board[a - 1][b] = 1
                                        flag_esm = False
                                    except (Exception, IndexError):
                                        flag_esm = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)


                    elif direction == 2:
                        try:
                            if self._comp_board[a + 1][b] != 0 or self._comp_board[a][b] != 0:
                                raise Exception
                            self._comp_board[a][b] = 1
                            self._comp_board[a + 1][b] = 1
                            flag_esm = False
                        except (Exception, IndexError):
                            try:
                                if self._comp_board[a][b - 1] != 0 or (b - 1 < 0) or self._comp_board[a][b] != 0:
                                    raise Exception
                                self._comp_board[a][b] = 1
                                self._comp_board[a][b - 1] = 1
                                flag_esm = False
                            except (Exception, IndexError):
                                try:
                                    if self._comp_board[a - 1][b] != 0 or (a - 1 < 0) or self._comp_board[a][b] != 0:
                                        raise Exception
                                    self._comp_board[a][b] = 1
                                    self._comp_board[a - 1][b] = 1
                                    flag_esm = False
                                except (Exception, IndexError):
                                    try:
                                        if self._comp_board[a][b + 1] != 0 or self._comp_board[a][b] != 0:
                                            raise Exception
                                        self._comp_board[a][b] = 1
                                        self._comp_board[a][b + 1] = 1
                                        flag_esm = False
                                    except (Exception, IndexError):
                                        flag_esm = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)

                    elif direction == 3:
                        try:
                            if self._comp_board[a][b - 1] != 0 or (b - 1 < 0) or self._comp_board[a][b] != 0:
                                raise Exception
                            self._comp_board[a][b] = 1
                            self._comp_board[a][b - 1] = 1
                            flag_esm = False
                        except (Exception, IndexError):
                            try:
                                if self._comp_board[a - 1][b] != 0 or (a - 1 < 0) or self._comp_board[a][b] != 0:
                                    raise Exception
                                self._comp_board[a][b] = 1
                                self._comp_board[a - 1][b] = 1
                                flag_esm = False
                            except (Exception, IndexError):
                                try:
                                    if self._comp_board[a][b + 1] != 0 or self._comp_board[a][b] != 0:
                                        raise Exception
                                    self._comp_board[a][b] = 1
                                    self._comp_board[a][b + 1] = 1
                                    flag_esm = False
                                except (Exception, IndexError):
                                    try:
                                        if self._comp_board[a + 1][b] != 0 or self._comp_board[a][b] != 0:
                                            raise Exception
                                        self._comp_board[a][b] = 1
                                        self._comp_board[a + 1][b] = 1
                                        flag_esm = False
                                    except (Exception, IndexError):
                                        flag_esm = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)

                    elif direction == 4:
                        try:
                            if self._comp_board[a - 1][b] != 0 or (a - 1 < 0) or self._comp_board[a][b] != 0:
                                raise Exception
                            self._comp_board[a][b] = 1
                            self._comp_board[a - 1][b] = 1
                            flag_esm = False
                        except (Exception, IndexError):
                            try:
                                if self._comp_board[a][b + 1] != 0 or self._comp_board[a][b] != 0:
                                    raise Exception
                                self._comp_board[a][b] = 1
                                self._comp_board[a][b + 1] = 1
                                flag_esm = False
                            except (Exception, IndexError):
                                try:
                                    if self._comp_board[a + 1][b] != 0 or self._comp_board[a][b] != 0:
                                        raise Exception
                                    self._comp_board[a][b] = 1
                                    self._comp_board[a + 1][b] = 1
                                    flag_esm = False
                                except (Exception, IndexError):
                                    try:
                                        if self._comp_board[a][b - 1] != 0 or (b - 1 < 0) or self._comp_board[a][
                                            b] != 0:
                                            raise Exception
                                        self._comp_board[a][b] = 1
                                        self._comp_board[a][b - 1] = 1
                                        flag_esm = False
                                    except (Exception, IndexError):
                                        flag_esm = True
                                        a = randint(0, 7)
                                        b = randint(0, 7)
                                        direction = randint(1, 4)
                    _Zero_to_Two_comp()

            count_kat = 0
            for i in range(4):
                flag_kat = False
                for j in range(len(self._comp_board)):
                    for k in range(len(self._comp_board[i])):
                        if self._comp_board[j][k] == 0:
                            self._comp_board[j][k] = 1
                            _Zero_to_Two_comp()
                            flag_kat = True
                            count_kat += 1
                            break
                    if flag_kat: break
            if count_kat < 4:
                main_flag = True
            elif count_kat == 4:
                main_flag = False

    '''
    The method for player's shooting

    :@param point: (str) the coordinate
    :@return mes: (str) message about whether a player has been hit the ship
    '''
    def player_shoot(self, point: str) -> str:
        mes = 'Неверная координата'
        if point[0] == 'A':
            if self._comp_board[int(point[1]) - 1][0] == 1:
                if (int(point[1]) - 1) > 0 and (int(point[1]) - 1) < 7:
                    if self._comp_board[int(point[1]) - 2][0] != 1 and self._comp_board[int(point[1])][0] != 1 and \
                            self._comp_board[int(point[1]) - 1][1] != 1:
                        mes = 'Убит'
                        self._comp_board[int(point[1]) - 1][0] = 3
                        self._copy_of_comp_board[int(point[1]) - 1][0] = '██'
                        self._points[int(point[1]) - 1][0] = 0
                    else:
                        mes = 'Ранен'
                        self._comp_board[int(point[1]) - 1][0] = 3
                        self._copy_of_comp_board[int(point[1]) - 1][0] = '██'
                        self._points[int(point[1]) - 1][0] = 0
                elif (int(point[1]) - 1) == 0:
                    if self._comp_board[int(point[1])][0] != 1 and self._comp_board[int(point[1]) - 1][1] != 1:
                        mes = 'Убит'
                        self._comp_board[int(point[1]) - 1][7] = 3
                        self._copy_of_comp_board[int(point[1]) - 1][0] = '██'
                        self._points[int(point[1]) - 1][0] = 0
                    else:
                        mes = 'Ранен'
                        self._comp_board[int(point[1]) - 1][0] = 3
                        self._copy_of_comp_board[int(point[1]) - 1][0] = '██'
                        self._points[int(point[1]) - 1][0] = 0
                elif (int(point[1]) - 1) == 7:
                    if self._comp_board[int(point[1]) - 2][0] != 1 and self._comp_board[int(point[1]) - 1][1] != 1:
                        mes = 'Убит'
                        self._comp_board[int(point[1]) - 1][0] = 3
                        self._copy_of_comp_board[int(point[1]) - 1][0] = '██'
                        self._points[int(point[1]) - 1][0] = 0
                    else:
                        mes = 'Ранен'
                        self._comp_board[int(point[1]) - 1][0] = 3
                        self._copy_of_comp_board[int(point[1]) - 1][0] = '██'
                        self._points[int(point[1]) - 1][0] = 0

            elif self._comp_board[int(point[1]) - 1][0] == 0 or self._comp_board[int(point[1]) - 1][0] == 2:
                mes = 'Промах'
                self._comp_board[int(point[1]) - 1][0] = 4
                self._copy_of_comp_board[int(point[1]) - 1][0] = '▒▒'
                self._points[int(point[1]) - 1][0] = 0
            else:
                mes = 'Неверная координата'

        elif point[0] == 'H':
            if self._comp_board[int(point[1]) - 1][7] == 1:
                if (int(point[1]) - 1) > 0 and (int(point[1]) - 1) < 7:
                    if self._comp_board[int(point[1]) - 2][7] != 1 and self._comp_board[int(point[1])][7] != 1 and \
                            self._comp_board[int(point[1]) - 1][6] != 1:
                        mes = 'Убит'
                        self._comp_board[int(point[1]) - 1][7] = 3
                        self._copy_of_comp_board[int(point[1]) - 1][7] = '██'
                        self._points[int(point[1]) - 1][7] = 0
                    else:
                        mes = 'Ранен'
                        self._comp_board[int(point[1]) - 1][7] = 3
                        self._copy_of_comp_board[int(point[1]) - 1][7] = '██'
                        self._points[int(point[1]) - 1][7] = 0
                elif (int(point[1]) - 1) == 0:
                    if self._comp_board[int(point[1])][0] != 1 and self._comp_board[int(point[1]) - 1][6] != 1:
                        mes = 'Убит'
                        self._comp_board[int(point[1]) - 1][7] = 3
                        self._copy_of_comp_board[int(point[1]) - 1][7] = '██'
                        self._points[int(point[1]) - 1][7] = 0
                    else:
                        mes = 'Ранен'
                        self._comp_board[int(point[1]) - 1][7] = 3
                        self._copy_of_comp_board[int(point[1]) - 1][7] = '██'
                        self._points[int(point[1]) - 1][7] = 0
                elif (int(point[1]) - 1) == 7:
                    if self._comp_board[int(point[1]) - 2][7] != 1 and self._comp_board[int(point[1]) - 1][6] != 1:
                        mes = 'Убит'
                        self._comp_board[int(point[1]) - 1][7] = 3
                        self._copy_of_comp_board[int(point[1]) - 1][7] = '██'
                        self._points[int(point[1]) - 1][7] = 0
                    else:
                        mes = 'Ранен'
                        self._comp_board[int(point[1]) - 1][7] = 3
                        self._copy_of_comp_board[int(point[1]) - 1][7] = '██'
                        self._points[int(point[1]) - 1][7] = 0

            elif self._comp_board[int(point[1]) - 1][7] == 0 or self._comp_board[int(point[1]) - 1][7] == 2:
                mes = 'Промах'
                self._comp_board[int(point[1]) - 1][7] = 4
                self._copy_of_comp_board[int(point[1]) - 1][7] = '▒▒'
                self._points[int(point[1]) - 1][7] = 0
            else:
                mes = 'Неверная координата'


        else:
            count_let = 0
            for i in 'BCDEFG':
                count_let += 1
                if point[0] == i:
                    if self._comp_board[int(point[1]) - 1][count_let] == 1:
                        if (int(point[1]) - 1) > 0 and (int(point[1]) - 1) < 7:
                            if self._comp_board[int(point[1]) - 2][count_let] != 1 and self._comp_board[int(point[1])][count_let] != 1 and \
                                    self._comp_board[int(point[1]) - 1][count_let + 1] != 1 and self._comp_board[int(point[1]) - 1][count_let - 1] != 1:
                                mes = 'Убит'
                                self._comp_board[int(point[1]) - 1][count_let] = 3
                                self._copy_of_comp_board[int(point[1]) - 1][count_let] = '██'
                                self._points[int(point[1]) - 1][count_let] = 0
                            else:
                                mes = 'Ранен'
                                self._comp_board[int(point[1]) - 1][count_let] = 3
                                self._copy_of_comp_board[int(point[1]) - 1][count_let] = '██'
                                self._points[int(point[1]) - 1][count_let] = 0
                        elif (int(point[1]) - 1) == 0:
                            if self._comp_board[int(point[1])][count_let] != 1 and self._comp_board[int(point[1]) - 1][count_let + 1] != 1 and self._comp_board[int(point[1]) - 1][count_let - 1] != 1:
                                mes = 'Убит'
                                self._comp_board[int(point[1]) - 1][count_let] = 3
                                self._copy_of_comp_board[int(point[1]) - 1][count_let] = '██'
                                self._points[int(point[1]) - 1][count_let] = 0
                            else:
                                mes = 'Ранен'
                                self._comp_board[int(point[1]) - 1][count_let] = 3
                                self._copy_of_comp_board[int(point[1]) - 1][count_let] = '██'
                                self._points[int(point[1]) - 1][count_let] = 0
                        elif (int(point[1]) - 1) == 7:
                            if self._comp_board[int(point[1]) - 2][count_let] != 1 and self._comp_board[int(point[1]) - 1][count_let + 1] != 1 and self._comp_board[int(point[1]) - 1][count_let - 1] != 1:
                                mes = 'Убит'
                                self._comp_board[int(point[1]) - 1][count_let] = 3
                                self._copy_of_comp_board[int(point[1]) - 1][count_let] = '██'
                                self._points[int(point[1]) - 1][count_let] = 0
                            else:
                                mes = 'Ранен'
                                self._comp_board[int(point[1]) - 1][count_let] = 3
                                self._copy_of_comp_board[int(point[1]) - 1][count_let] = '██'
                                self._points[int(point[1]) - 1][count_let] = 0

                    elif self._comp_board[int(point[1]) - 1][count_let] == 0 or self._comp_board[int(point[1]) - 1][count_let] == 2:
                        mes = 'Промах'
                        self._comp_board[int(point[1]) - 1][count_let] = 4
                        self._copy_of_comp_board[int(point[1]) - 1][count_let] = '▒▒'
                        self._points[int(point[1]) - 1][count_let] = 0
                    else:
                        mes = 'Неверная координата'
        return mes

    '''
    The method for bot shooting
    '''
    def bot_shoot(self) -> None:
        flag_of_shooting4 = False

        '''
        The function for checking is it possible to shoot to given coordinates

        :@param i: (int) X-coordinate in the matrix
        :@param j: (int) Y-coordinate in the matrix
        :@return: (bool) is it possible or not
        '''
        def check_of_location(i, j):
            if self._copy_of_player_board[i][j] == 3:
                flag_of_location = False
                try:
                    if self._copy_of_player_board[i + 1][j] == 1:
                        flag_of_location = True
                    else: flag_of_location = False
                except:
                    pass
                try:
                    if self._copy_of_player_board[i][j + 1] == 1:
                        flag_of_location = True
                    else: flag_of_location = False
                except:
                    pass
                try:
                    if self._copy_of_player_board[i - 1][j] == 1 and (i - 1 >= 0):
                        flag_of_location = True
                    else: flag_of_location = False
                except:
                    pass
                try:
                    if self._copy_of_player_board[i][j - 1] == 1 and (j - 1 >= 0):
                        flag_of_location =True
                    else: flag_of_location = False
                except:
                    pass
                if flag_of_location:
                    return True
                elif not flag_of_location:
                    return False

        '''
        The function for next shooting if first if shot hit the ship

        :@param x: (int) X-coordinate in the matrix
        :@param y: (int) Y-coordinate in the matrix
        :@param flag: (bool) if flag goes down, then the shooting will stop
        '''
        global special_flag
        def shoot_the_ships(x: int, y: int, flag: bool) -> None:
            if self._copy_of_player_board[x][y] == 1:
                self._copy_of_player_board[x][y] = 3
                self._player_board[x][y] = '*** '
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
                                if self._copy_of_player_board[x + 1][y] == 1:
                                    self._copy_of_player_board[x + 1][y] = 3
                                    self._player_board[x + 1][y] = '*** '
                                    if x+2 >= 7:
                                        raise Exception
                                    else:
                                        if self._copy_of_player_board[x + 2][y] == 1:
                                            self._copy_of_player_board[x + 2][y] = 3
                                            self._player_board[x + 2][y] = '*** '
                                            if x+3 >= 7:
                                                raise Exception
                                            else:
                                                if self._copy_of_player_board[x + 3][y] == 1:
                                                    self._copy_of_player_board[x + 3][y] = 3
                                                    self._player_board[x + 3][y] = '*** '
                                                    flag_dir = False
                                                elif self._copy_of_player_board[x + 3][y] == 0:
                                                    self._copy_of_player_board[x + 3][y] = 4
                                                    self._player_board[x + 3][y] = '..... '
                                                    flag_dir = False
                                                else: flag_dir = True
                                        elif self._copy_of_player_board[x + 2][y] == 0:
                                            self._copy_of_player_board[x + 2][y] = 4
                                            self._player_board[x + 2][y] = '..... '
                                            flag_dir = False
                                        else: flag_dir = True
                                elif self._copy_of_player_board[x + 1][y] == 0:
                                    self._copy_of_player_board[x + 1][y] = 4
                                    self._player_board[x + 1][y] = '..... '
                                    flag_dir = False
                                else: flag_dir = True

                        except (Exception, IndexError):
                            flag_dir = True

                    elif direction == 2:
                        try:
                            if y + 1 >= 7:
                                raise Exception

                            else:
                                if self._copy_of_player_board[x][y + 1] == 1:
                                    self._copy_of_player_board[x][y + 1] = 3
                                    self._player_board[x][y + 1] = '*** '
                                    if y + 2 >= 7:
                                        raise Exception
                                    else:
                                        if self._copy_of_player_board[x][y + 2] == 1:
                                            self._copy_of_player_board[x][y + 2] = 3
                                            self._player_board[x][y + 2] = '*** '
                                            if y + 3 >= 7:
                                                raise Exception
                                            else:
                                                if self._copy_of_player_board[x][y + 3] == 1:
                                                    self._copy_of_player_board[x][y + 3] = 3
                                                    self._player_board[x][y + 3] = '*** '
                                                    flag_dir = False
                                                elif self._copy_of_player_board[x][y + 3] == 0:
                                                    self._copy_of_player_board[x][y + 3] = 4
                                                    self._player_board[x][y + 3] = '..... '
                                                    flag_dir = False
                                                else:
                                                    flag_dir = True
                                        elif self._copy_of_player_board[x][y + 2] == 0:
                                            self._copy_of_player_board[x][y + 2] = 4
                                            self._player_board[x][y + 2] = '..... '
                                            flag_dir = False
                                        else:
                                            flag_dir = True
                                elif self._copy_of_player_board[x][y + 1] == 0:
                                    self._copy_of_player_board[x][y + 1] = 4
                                    self._player_board[x][y + 1] = '..... '
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
                                if self._copy_of_player_board[x - 1][y] == 1:
                                    self._copy_of_player_board[x - 1][y] = 3
                                    self._player_board[x - 1][y] = '*** '
                                    if x - 2 < 0:
                                        raise Exception
                                    else:
                                        if self._copy_of_player_board[x - 2][y] == 1:
                                            self._copy_of_player_board[x - 2][y] = 3
                                            self._player_board[x - 2][y] = '*** '
                                            if x - 3 < 0:
                                                raise Exception
                                            else:
                                                if self._copy_of_player_board[x - 3][y] == 1:
                                                    self._copy_of_player_board[x - 3][y] = 3
                                                    self._player_board[x - 3][y] = '*** '
                                                    flag_dir = False
                                                elif self._copy_of_player_board[x - 3][y] == 0:
                                                    self._copy_of_player_board[x - 3][y] = 4
                                                    self._player_board[x - 3][y] = '..... '
                                                    flag_dir = False
                                                else:
                                                    flag_dir = True
                                        elif self._copy_of_player_board[x - 2][y] == 0:
                                            self._copy_of_player_board[x - 2][y] = 4
                                            self._player_board[x - 2][y] = '..... '
                                            flag_dir = False
                                        else:
                                            flag_dir = True
                                elif self._copy_of_player_board[x - 1][y] == 0:
                                    self._copy_of_player_board[x - 1][y] = 4
                                    self._player_board[x - 1][y] = '..... '
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
                                if self._copy_of_player_board[x][y - 1] == 1:
                                    self._copy_of_player_board[x][y - 1] = 3
                                    self._player_board[x][y - 1] = '*** '
                                    if y - 2 < 0:
                                        raise Exception
                                    else:
                                        if self._copy_of_player_board[x][y - 2] == 1:
                                            self._copy_of_player_board[x][y - 2] = 3
                                            self._player_board[x][y - 2] = '*** '
                                            if y - 3 < 0:
                                                raise Exception
                                            else:
                                                if self._copy_of_player_board[x][y - 3] == 1:
                                                    self._copy_of_player_board[x][y - 3] = 3
                                                    self._player_board[x][y - 3] = '*** '
                                                    flag_dir = False
                                                elif self._copy_of_player_board[x][y - 3] == 0:
                                                    self._copy_of_player_board[x][y - 3] = 4
                                                    self._player_board[x][y - 3] = '..... '
                                                    flag_dir = False
                                                else:
                                                    flag_dir = True
                                        elif self._copy_of_player_board[x][y - 2] == 0:
                                            self._copy_of_player_board[x][y - 2] = 4
                                            self._player_board[x][y - 2] = '..... '
                                            flag_dir = False
                                        else:
                                            flag_dir = True
                                elif self._copy_of_player_board[x][y - 1] == 0:
                                    self._copy_of_player_board[x][y - 1] = 4
                                    self._player_board[x][y - 1] = '..... '
                                    flag_dir = False
                                else:
                                    flag_dir = True
                        except (Exception, IndexError):
                            flag_dir = True

            else:
                self._copy_of_player_board[x][y] = 4
                self._player_board[x][y] = '..... '


        special_flag = True
        while special_flag:
            special_flag = False
            x_cord = self._x_shoot
            y_cord = self._y_shoot
            shoot_the_ships(x_cord, y_cord, flag_of_shooting4)
            while check_of_location(x_cord, y_cord):
                shoot_the_ships(x_cord, y_cord, flag_of_shooting4)


            if self._flag_of_shooting1:
                try:
                    if self._x_shoot + 1 > 7 or self._y_shoot + 1 > 7:
                        raise Exception
                    self._x_shoot += 1
                    self._y_shoot += 1
                except Exception:
                    self._flag_of_shooting1 = False
                    self._flag_of_shooting2 = True
                    self._x_shoot = 4
                    self._y_shoot = 0


            elif self._flag_of_shooting2:
                try:
                    if self._x_shoot + 1 > 7 or self._y_shoot + 1 > 7:
                        raise Exception
                    self._x_shoot += 1
                    self._y_shoot += 1
                except Exception:
                    self._flag_of_shooting2 = False
                    self._flag_of_shooting3 = True
                    self._x_shoot = 0
                    self._y_shoot = 4

            elif self._flag_of_shooting3:
                try:
                    if self._x_shoot + 1 > 7 or self._y_shoot + 1 > 7:
                        raise Exception
                    self._x_shoot += 1
                    self._y_shoot += 1
                except Exception:
                    self._flag_of_shooting3 = False
                    flag_of_shooting4 = True
                    ls = []
                    for i in range(len(self._copy_of_player_board)):
                        for j in range(len(self._copy_of_player_board[i])):
                            if self._copy_of_player_board[i][j] == 0 or self._copy_of_player_board[i][j] == 1:
                                ls.append([i, j])
                    rand = randint(0, len(ls)-1)
                    self._x_shoot = ls[rand][0]
                    self._y_shoot = ls[rand][1]
                    if self._copy_of_player_board[self._x_shoot][self._y_shoot] == 1:
                        special_flag = True
                    else:
                        special_flag = False

            elif not self._flag_of_shooting2 and not self._flag_of_shooting3 and not self._flag_of_shooting1:
                flag_of_shooting4 = True
                ls = []
                for i in range(len(self._copy_of_player_board)):
                    for j in range(len(self._copy_of_player_board[i])):
                        if self._copy_of_player_board[i][j] == 0 or self._copy_of_player_board[i][j] == 1:
                            ls.append([i, j])
                rand = randint(0, len(ls)-1)
                self._x_shoot = ls[rand][0]
                self._y_shoot = ls[rand][1]
                if self._copy_of_player_board[self._x_shoot][self._y_shoot] == 1:
                    special_flag = True
                else: special_flag = False

    '''
    The method for checking whether the game is over
    
    :@return: (bool) is the fame over or don't
    '''
    def game_over(self) -> bool:
        flag1 = True
        flag2 = True
        for i in range(len(self._copy_of_player_board)):
            for j in range(len(self._copy_of_player_board[i])):
                if self._copy_of_player_board[i][j] == 1:
                    flag1 = False

        for i in range(len(self._comp_board)):
            for j in range(len(self._comp_board[i])):
                if self._comp_board[i][j] == 1:
                    flag2 = False
        if flag2 or flag1:
            return True
        else:
            return False

    '''
    The method for identification of the winner

    :@return: (str) message about who won
    '''
    def who_won(self) -> str:
        flag_player = True
        flag_bot = True
        for i in range(len(self._copy_of_player_board)):
            for j in range(len(self._copy_of_player_board[i])):
                if self._copy_of_player_board[i][j] == 1:
                    flag_player = False
        for i in range(len(self._comp_board)):
            for j in range(len(self._comp_board[i])):
                if self._comp_board[i][j] == 1:
                    flag_bot = False
        if flag_player:
            return 'Вы проиграли'
        elif flag_bot:
            return 'Вы победили'
        else: return 'Произошло недоразумение :('

    '''
    The decorator that starts the game
    '''
@dp.message_handler(commands=['start'])
async def start_of_the_game(message: types.Message):
    global count_kat
    global count_esm
    global count_kre
    count_kat = 0
    count_esm = 0
    count_kre = 0
    global flag_of_placement
    flag_of_placement = True
    global game
    game = SeaBattle(board, board, board, board, True, False, True, 0, 0, points_list)
    await bot.send_message(message.from_user.id, (game.player_board_print()))
    await bot.send_message(message.from_user.id, (game.copy_of_comp_board_print()))
    await bot.send_message(message.from_user.id, 'Начинается расстановка кораблей')
    await bot.send_message(message.from_user.id, 'Начинается расстановка катеров')
    global flag_of_kat, flag_of_esm, flag_of_kre, flag_of_lin, flag_of_shoot
    flag_of_kat = False
    flag_of_esm = True
    flag_of_kre = True
    flag_of_lin = True
    flag_of_shoot = False

    '''
    The decorator that implements the placement of the player's ships and shooting
    '''
@dp.message_handler()
async def placement_of_kat_1(message: types.Message):
    global flag_of_placement
    if flag_of_placement:
        global flag_of_kat, flag_of_esm, flag_of_kre, flag_of_lin
        if not flag_of_kat:
            if game.check_of_coordinates(message.text) and len(message.text) == 2:
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
                            container[1][0] + container[0][0] not in string.ascii_uppercase)))) and len(message.text) == 5:
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
                            container[1][0] + c[0] + container[0][0] not in string.ascii_uppercase)))) and len(message.text) == 5:
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

        elif not flag_of_lin:
            container = message.text.split()
            if (container[0][1] == container[1][1]) and string.ascii_uppercase.index(container[1][0]) > string.ascii_uppercase.index(container[0][0]):
                c = string.ascii_uppercase[string.ascii_uppercase.index(container[0][0]) + 1] + container[0][1]
                d = string.ascii_uppercase[string.ascii_uppercase.index(container[0][0]) + 2] + container[0][1]

            elif (container[0][1] == container[1][1]) and string.ascii_uppercase.index(container[1][0]) < string.ascii_uppercase.index(container[0][0]):
                c = string.ascii_uppercase[string.ascii_uppercase.index(container[1][0]) + 1] + container[0][1]
                d = string.ascii_uppercase[string.ascii_uppercase.index(container[1][0]) + 2] + container[0][1]

            elif (container[0][0] == container[1][0]) and (abs(int(container[0][1]) - int(container[1][1])) == 3):
                c = container[0][0] + str(max(int(container[0][1]), int(container[1][1])) - 1)
                d = container[0][0] + str(max(int(container[0][1]), int(container[1][1])) - 2)

            else:
                c = 'Z1'
                d = 'X1'

            if not (game.check_of_coordinates(container[0]) and game.check_of_coordinates(container[1]) and game.check_of_coordinates(c) and game.check_of_coordinates(d) and xor((container[0][0] != container[1][0]) or (abs(int(container[0][1]) - int(container[1][1])) != 3),
                                                           (container[0][1] != container[1][1] or ((container[0][0] + c[0] + d[0] + container[1][0] not in string.ascii_uppercase) and (container[1][0] + c[0] + d[0] + container[0][0] not in string.ascii_uppercase)))) and len(message.text) == 5):
                await bot.send_message(message.from_user.id, 'Ошибка координат!')

            else:

                game.placement(container[0])
                game.placement(container[1])
                game.placement(c)
                game.placement(d)
                game.Zero_to_Two()
                flag_of_lin = True
                global flag_of_shoot
                flag_of_shoot = True
                for i in range(len(game._player_board)):
                    for j in range(len(game._player_board[i])):
                        if game._player_board[i][j] == '██':
                            game._copy_of_player_board[i][j] = 1
                await bot.send_message(message.from_user.id, (game.player_board_print()))
                await bot.send_message(message.from_user.id, 'Расстановка кораблей закончена')
                await bot.send_message(message.from_user.id, 'Начинается бой! В какую точку будем стрелять?')
                game.placement_of_ships_bot()

        if flag_of_shoot and len(message.text) == 2:
            turn = game.player_shoot(message.text)
            if turn == 'Промах':
                await bot.send_message(message.from_user.id, 'Промах')
                await bot.send_message(message.from_user.id, (game.copy_of_comp_board_print()))
                game.bot_shoot()
                await bot.send_message(message.from_user.id, (game.player_board_print()))
                if game.game_over():
                    await bot.send_message(message.from_user.id, (game.player_board_print()))
                    await bot.send_message(message.from_user.id, 'Вы проиграли...')
                    flag_of_placement = False


            elif turn == 'Ранен':
                await bot.send_message(message.from_user.id, 'Ранен')
                await bot.send_message(message.from_user.id, (game.copy_of_comp_board_print()))

            elif turn == 'Убит':
                await bot.send_message(message.from_user.id, 'Убит')
                await bot.send_message(message.from_user.id, (game.copy_of_comp_board_print()))
                if game.game_over():
                    await bot.send_message(message.from_user.id, 'Вы победили!!')
                    flag_of_placement = False

            elif turn == 'Неверная координата':
                await bot.send_message(message.from_user.id, 'Неверная координата')
                await bot.send_message(message.from_user.id, (game.copy_of_comp_board_print()))


    else:
        await bot.send_message(message.from_user.id, 'Напишите /start, чтобы начать игру')


if __name__ == "__main__": executor.start_polling(dp)