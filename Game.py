
class Game:
    EMPTY = " "
    P1 = "o"
    P2 = "x"

    def __init__(self):
        self.__board = [[Game.EMPTY for _ in range(3)] for _ in range(3)]
        self.__player = Game.p1

    def __repr__(self):
        result = "  " + " ".join(str(i+1) for i in range(3))
        for row in range(3):
            result += f"\n{row+1} " + "|".join(self._board[row])
            if row != 2:
                dashes = "-" * 5
                result += f"\n  {dashes}"
        result += f"\n\n{self._player} turn to play"
        return result
        
    def play(self,row,col):
        row -= 1 # to zero base
        col -= 1
        self.board[row][col] = self.__player
        self.__player = Game.P2 if self.__player == Game.P1 else Game.P1
        

    @property
    def winner(self):
        for p in Game.P1, Game.P2:
            for row in range(3): # checking rows
                if all(self.__board[row][col] == p for col in range(3)):
                    return p
            for col in range(3): # checking cols
                if all(self.__board[row][col] == p for row in range(3)):
                    return p
            if all(self.__board[i][i] == p for i in range(3)):
                return p
            if all(self.__board[2 - i][i] == p for i in range(3)):
                return p
        return None


        return None
        

if __name__ == "__main__":
    pass
