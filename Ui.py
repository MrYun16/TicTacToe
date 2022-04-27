from abc import ABC, abstractmethod
from Game import Game
class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        self.__game = Game()


    def __getInput(self):
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        return row, col

    def run(self):
        while self.__game.winner == None:
            print(self.__game)
            row, col = self.__getInput()
            self.__game.play(row, col)

        print(f"The winner is {self.__game.winnder}") # assuming no draw
