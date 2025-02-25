from random import randint
from tkinter import *

class Jogo:
    #interface do jogo
    def __init__(self, master=None):
        self.fontTitle = ("Comic Sans MS", "14", "bold")
        self.fontText = ("Arial", "12")

        self.principal = Frame(master)
        self.principal.pack()

        self.body = Frame(master)
        self.body.pack()

        self.resulting = Frame(master)
        self.resulting.pack()

        self.title = Label(self.principal, text="JOGO DO ADIVINHA", font=self.fontTitle)
        self.title.pack()

        self.textNumberTry = Label(self.body, text="Adivinhe o número entre 0 e 10: ", font=self.fontText)
        self.textNumberTry.pack(side=LEFT)

        self.numberTry = Entry(self.body, width=5, font=self.fontText)
        self.numberTry.pack(side=LEFT)

        self.buttonTry = Button(self.resulting, text="Chutar", font=self.fontText, width=10, command=self.script)     
        self.buttonTry.pack()

        self.result = Label(self.resulting, text="", font=self.fontText)
        self.result.pack()

    #script do jogo
    def script(self, master=None):
        numero = str(randint(0,10))
        chute = self.numberTry.get()

        if chute != numero:
            self.result["text"] = 'Você errou e mudamos o número. Tente novamente!'
        else:    
            self.result["text"] = 'Você acertou!'

root = Tk()
Jogo(root)
root.mainloop()