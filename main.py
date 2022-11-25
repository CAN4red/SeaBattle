import string

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

    def player_board_print(self):
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

    def copy_of_comp_board_print(self):
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
        def placement():
            if a[0] == 'A':
                self.player_board[int(a[1])-1][0] = '▢'
            elif a[0] == 'B':
                self.player_board[int(a[1]) - 1][1] = '▢'
            elif a[0] == 'C':
                self.player_board[int(a[1]) - 1][2] = '▢'
            elif a[0] == 'D':
                self.player_board[int(a[1]) - 1][3] = '▢'
            elif a[0] == 'E':
                self.player_board[int(a[1]) - 1][4] = '▢'
            elif a[0] == 'F':
                self.player_board[int(a[1]) - 1][5] = '▢'
            elif a[0] == 'G':
                self.player_board[int(a[1]) - 1][6] = '▢'
            elif a[0] == 'H':
                self.player_board[int(a[1]) - 1][7] = '▢'
        for i in range(4):
            a = input(f'Катеров оставлось {4-i}, куда катера ставим: ')
            while (a[0] not in string.ascii_uppercase[:8]) or (a[1] not in [str(i) for i in range(1, 9)]):
                a = input(f'Ай, косячим! Катеров оставлось {4 - i}, куда катера ставим: ')
            placement()







game = SeaBattle(board, board, board, board)
game.player_board_print()
game.placement_of_ships()
game.player_board_print()