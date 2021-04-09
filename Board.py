from WorlList import listworld
from random import randint

class board:

    def __init__(self):
        self.board = []

    def addWord(self):
        for i in range(3):
            self.board.append(listworld.sujet[randint(0, len(listworld.sujet))])
            self.board.append(listworld.verbe[randint(0, len(listworld.verbe))])
            self.board.append(listworld.complement[randint(0, len(listworld.complement))])
            self.board.append(listworld.conjonction[randint(0, len(listworld.conjonction))])

    def __str__(self):
        print(self.board)