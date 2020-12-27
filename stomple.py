import numpy as np

class Player:
    """ Créé une instance de la classe joueur\n
    Chaque joueur est caractérisé par sa couleur\n
    Couleurs :\n
    noir : 1\n
    violet : 2\n
    vert: 3\n
    orange: 4\n
    jaune : 5\n
    blanc: 6\n
    """

    def __init__(self, color, board):
        self.color = color
        self.position = (-1, -1)
        self.board = board
        self.last_color = -1

    def possible_moves(self):
        """
        Fait tous les mouvements possibles au début du tour\n
        """
        if self.position == (-1, -1):
            index = [(0, i) for i in range(7)]
            index.extend([(i, 0) for i in range(7)])
            index.extend([(i, 6) for i in range(7)])
            index.extend([(6, i) for i in range(7)])
            return index
        if self.last_color != -1:
            return self.__check_surrounding()
        index = []
        for i in range(7):
            for j in range(7):
                if self.color == self.board[i, j]:
                    index.append((i, j))
        x, y = self.position
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if 0 <= x + i < 7 and 0 <= y + j < 7 and (i != x or j != y) and self.board[x+i, y+j] != -1:
                    index.append((x + i, y + j))
        return index
    
    def __check_surrounding(self):
        """
        Vérifie le prochain mouvement possible au sein du même tour
        """
        index = []
        x, y = self.position
        for i in [-1, 0, 1]:
            for j in [-1, 0 , 1]:
                if 0 <= x + i < 7 and 0 <= y + j < 7 and (i != x or j != y) and self.last_color == board[x+i, y+j]:
                    index.append((x+i, y+j))

    def make_move(self, x, y, first = False):
        """
        Fait un mouvement\n
        argument:  \n
        x et y sont les coordonnées\n
        first est True si c'est le premier tour\n
        renvoie vrai si le joueur doit encore bouger pendant ce tour
        """
        print(self.possible_moves())
        if (x, y) in self.possible_moves():
            self.position = (x, y)
            if first:
                self.board[x, y] = -1
                return False
            self.last_color = self.board[x, y]
            self.board[x, y] = -1
            next_moves = self.__check_surrounding()
            if len(next_moves) > 0:
                return True
            else:
                self.last_color = -1
                return False
        return True

    def lost(self):
        return len(self.possible_moves()) == 0




class Board:

    def __init__(self):
        self.board = self.__init_board()

    def __init_board(self):
        b = np.arange(7*7) % 7
        np.random.shuffle(b)
        b = np.reshape(b, (7, 7))
        return b


class Game:
    """
        Créé un partie de jeu de stomple\n
        arguments:\n
        players: nombre de joueurs
    """

    def __init__(self, players):
        if players < 7:
            self.players = []
            self.board = Board()
            for i in range(players):
                self.players.append(Player(i + 1, self.board.board))

    def fin(self):
        count = 0
        for player in self.players:
            if player.lost():
                count = count + 1
        return count + 1 >= len(self.players)

