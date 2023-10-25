import re



class Board:

    def __init__(self, rows, columns):
        self.board = [[" " for i in range(columns)] for j in range(rows)]
        self.rows = rows
        self.columns = columns
        self.get_players()
        self.start_game()

    def __str__(self):
        res = "    " + "   ".join([str(i+1) for i in range(len(self.board[0]))]) + "\n"
        res += "  " + "-" * (4 * len(self.board[0]) + 1) + "\n"

        for i, row in enumerate(self.board):
            res += str(i+1) + " | " + " | ".join(row) + " |\n"
            res += "  " + "-" * (4 * len(self.board[0]) + 1) + "\n"
        
        return res


    def get_players(self):
        p1_name = input("Navn spiller 1:")
        p2_name = input("Navn spiller 2:")
        self.p1 = Player(p1_name, 1, "X")
        self.p2 = Player(p2_name, 2, "O")

    def start_game(self):
        winner = False
        round = 0
        while not winner:
            if round % 2 == 0:
                p = self.p1
            else:
                p = self.p2

            self.place(p)
            winner = self.has_won(p.rep)

            if winner:
                print("################################################################")
                print(f"{p.name} has won")
                print("################################################################")

            round += 1
            print(self)


    def has_won(self, rep):
        # horisontal
        for row in self.board:
            if all([cell == rep for cell in row]):
                return True

        # vertikal
        for col in range(len(self.board[0])):
            if all([self.board[row][col] == rep for row in range(len(self.board))]):
                return True

        # diagonaler
        if all([self.board[i][i] == rep for i in range(len(self.board))]):
            return True
        if all([self.board[i][len(self.board) - 1 - i] == rep for i in range(len(self.board))]):
            return True

        return False

    def place(self, player):
        legal_move = False
        while not legal_move:
            pos = self.get_player_move(player)

            if self.is_legal_move(pos):
                legal_move = True
        self.board[pos[0]][pos[1]] = player.rep

    def get_player_move(self, player):
        string = input(f"{player.name} place coordinate (numbers separated by commas or spaces:  x,y or x y)")
        substrings = re.sub(r',+', ',', re.sub(r'\s+', ',', string.strip())).split(",")
        pos = [(int(x) - 1)  for x in substrings if x.isdigit()]
        return pos[:2]



    def is_legal_move(self, pos):
        if pos[0] >= 0 and pos[0] < self.rows and pos[1] >= 0 and pos[1] < self.columns:
            if self.board[pos[0]][pos[1]] == " ":
                return True

        print("illegal move, give legal coordinate")
        return False

class Player():
    def __init__(self, name, playernum, rep):
        self.name = name
        self.playernum = playernum
        self.rep = rep




rows = 3
columns = 3
b = Board(rows,columns)


