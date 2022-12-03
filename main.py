import string
from operator import xor

board = [
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
]

class SeaBattle():

    def __init__(self, player_board, copy_of_player_board, copy_of_comp_board, comp_board):
        self.player_board = board
        self.copy_of_player_board =board
        self.copy_of_comp_board = board
        self.comp_board = board

    def player_board_print(self): #вывод стола игрока
        st = '  '
        k = 1
        for i in string.ascii_uppercase[:8]:
            st += ' | ' + i
        print(st + ' |')
        for i in range(len(self.player_board)):
            st = str(k) + ' '
            for j in range(len(self.player_board[i])):
                st += ' | ' + self.player_board[i][j]
            k += 1
            print(st + ' |')

    def copy_of_comp_board_print(self): #вывод известной информации о столе компьютера
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

    def placement_of_ships(self): #расстановка кораблей
        def placement(point): #функция отвечающая за перевод координат в индексы матрицы и постановку в соотвествующую позицию символ '▢'
            if point[0] == 'A':
                self.player_board[int(point[1])-1][0] = '▢'
            elif point[0] == 'B':
                self.player_board[int(point[1]) - 1][1] = '▢'
            elif point[0] == 'C':
                self.player_board[int(point[1]) - 1][2] = '▢'
            elif point[0] == 'D':
                self.player_board[int(point[1]) - 1][3] = '▢'
            elif point[0] == 'E':
                self.player_board[int(point[1]) - 1][4] = '▢'
            elif point[0] == 'F':
                self.player_board[int(point[1]) - 1][5] = '▢'
            elif point[0] == 'G':
                self.player_board[int(point[1]) - 1][6] = '▢'
            elif point[0] == 'H':
                self.player_board[int(point[1]) - 1][7] = '▢'

        def can_put_point(point): #функция отвечающая за перевод координат в индексы матрицы и постановку в соотвествующую позицию символ '▢'
            if point[0] == 'A':
                if self.player_board[int(point[1])-1][0] == '▢':
                    return True
                else:
                    return False
            elif point[0] == 'B':
                if self.player_board[int(point[1]) - 1][1] == '▢':
                    return True
                else:
                    return False
            elif point[0] == 'C':
                if self.player_board[int(point[1]) - 1][2] == '▢':
                    return True
                else:
                    return False
            elif point[0] == 'D':
                if self.player_board[int(point[1]) - 1][3] == '▢':
                    return True
                else:
                    return False
            elif point[0] == 'E':
                if self.player_board[int(point[1]) - 1][4] == '▢':
                    return True
                else:
                    return False
            elif point[0] == 'F':
                if self.player_board[int(point[1]) - 1][5] == '▢':
                    return True
                else:
                    return False
            elif point[0] == 'G':
                if self.player_board[int(point[1]) - 1][6] == '▢':
                    return True
                else:
                    return False
            elif point[0] == 'H':
                if self.player_board[int(point[1]) - 1][7] == '▢':
                    return True
                else:
                    return False
        def chekc_of_codinates(point): #функция проверяющая соответствие введенных значений реальным координатам
            if (point[0] not in string.ascii_uppercase[:8]) or (point[1] not in [str(i) for i in range(1, 9)]) or can_put_point(point):
                return True
            else: return False

        for i in range(4): #расстанока катеров
            a = input(f'Катеров оставлось {4-i}, куда катера ставим: ')
            while chekc_of_codinates(a):
                a = input(f'Ай, косячим! Катеров оставлось {4 - i}, куда катера ставим: ')
            placement(a)

        for i in range(3): #расстановка эсминцев
            a, b = input(f'Эсминцев осталось {3-i}, куда ставим: ').split(' ')
            print(a[0], b[0], a[1], b[1])
            while chekc_of_codinates(a) or chekc_of_codinates(b):
                a, b = input(f'Oй, косячим! Эсминцев осталось {3 - i}, куда ставим: ').split(' ')
            #print(abs(int(a[1]) - int(b[1])))
            while not xor((a[0] != b[0]) or (abs(int(a[1]) - int(b[1])) != 1), (a[1] != b[1] or ((a[0] + b[0] not in string.ascii_uppercase) and (b[0] + a[0] not in string.ascii_uppercase)))):
                a, b = input(f'Ай, косячим! Эсминцев осталось {3 - i}, куда ставим: ').split(' ')
            placement(a)
            placement(b)




#(a[0] != b[0] and abs(int(a[1]) - int(b[1])) != 1) or (a[1] != b[1] and ((a[0] + b[0] not in string.ascii_uppercase) and (b[0] + a[0] not in string.ascii_uppercase))):


game = SeaBattle(board, board, board, board)
game.player_board_print()
game.placement_of_ships()
game.player_board_print()