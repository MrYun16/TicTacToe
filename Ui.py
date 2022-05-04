from abc import ABC, abstractmethod
from Game import Game
from Game import GameError
from tkinter import Tk, Frame, Button, X, Y, Toplevel, StringVar, Scrollbar, Text, LEFT, RIGHT, Grid, N, S, E, W
from itertools import product
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

        scroll = Scrollbar(frame)
        console = Text(frame, height=4, width=50)
        
        scroll.pack(side=RIGHT, fill=Y)
        console.pack(side=LEFT, fill=Y)

        scroll.config(command=console.yview)
        console.config(yscrollcommand=scroll.set)

    def __show_help(self):
        pass

    def __play_game(self):
        self.__game = Game()

        game_win = Toplevel(self.__root)
        game_win.title("Game")
        frame = Frame(game_win)
        frame.grid(row=0,column=0)

        # to allow resizing of game window
        Grid.columnconfigure(game_win, 0, weight=1)
        Grid.rowconfigure(game_win, 0, weight=1)
        frame.grid(row=0, column=0, sticky=N + S + E + W)

        self.__buttons = [[None for _ in range(3)] for _ in range(3)]
        for row,col in product(range(3), range(3)):
            b = StringVar()
            b.set(self.__game.at(row,col))
            self.__buttons[row][col] = b

            cmd = lambda r=row, c=col: self.__play(r,c)
            Button(
                frame,
                textvariable=b,
                command=cmd
            ).grid(row=row,column=col, sticky=N+S+W+E)

        # to allow resizing
        for i in range(3):
            Grid.rowconfigure(frame, i, weight=1)
            Grid.columnconfigure(frame, i, weight=1)

        Button(game_win, text="Dismiss", command=game_win.destroy).grid(row=1,column=0)

    def __play(self,r,c):
        self.__game.play(r+1,c+1)
        self.__buttons[r][c].set(self.__game.at(r+1,c+1))


    def __quit(self):
        self.__root.quit()

    


    def run(self):
        print("Run")
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
