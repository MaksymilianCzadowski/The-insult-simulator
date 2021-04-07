from WorlList import list
from random import randint

class board:

    def __init__(self):
        self.board = []

    def addWord(self):
        self.board.append(list.sujet[randint(0, len(list.sujet))])
        self.board.append(list.sujet[randint(0, len(list.sujet))])
        self.board.append(list.sujet[randint(0, len(list.sujet))])
        self.board.append(list.verbe[randint(0, len(list.verbe))])
        self.board.append(list.verbe[randint(0, len(list.verbe))])
        self.board.append(list.complement[randint(0, len(list.complement))])
        self.board.append(list.complement[randint(0, len(list.complement))])
        self.board.append(list.conjonction[randint(0, len(list.conjonction))])
        self.board.append(list.conjonction[randint(0, len(list.conjonction))])

    def __str__(self):
        print(self.board)