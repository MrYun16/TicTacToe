from abc import ABC, abstractmethod
from Game import Game
from Game import GameError
from tkinter import Tk, Frame, Button, X, Y
class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = Tk()
        root.title("Tic Tac Toe")
        frame = Frame(root)
        frame.pack()
        self.__root = root
        
        Button(
            frame,
            text="Help",
            command=self.__show_help # name of function, not calling function so no brackets
        ).pack(fill=X)  # expands button across horizontally 

        
        Button(
            frame,
            text="Play",
            command=self.__play_game 
        ).pack(fill=X) 

        
        Button(
            frame,
            text="Quit",
            command=self.__quit 
        ).pack(fill=X) 

    def __show_help(self):
        pass
    def __play_game(self):
        pass
    def __quit(self):
        self.__root.quit()

    


    def run(self):
        self.__root.mainloop()
        pass

class Terminal(Ui):
    def __init__(self):
        self.__game = Game()


    def __getInput(self):
        while True:
            try: # type check
                row = int(input("Enter row: "))
                col = int(input("Enter col: "))
                if 1 <- row <= 3 and 1 <= col <= 3: # range check
                    break
                else:
                    print("Invalid input, please type again")
            except ValueError:
                print("Invalid input, please type again")
        return row, col

    def run(self):
        while self.__game.winner == None :
            print(self.__game)
            row, col = self.__getInput()
            try:
                self.__game.play(row, col)
            except GameError as e:
                print(e)
        print(self.__game)
        if self.__game.winner == Game.DRAW:
            print(f"The game was a draw")
        else:
            print(f"The winner is {self.__game.winner}")
