from WorlList import listworld
from random import randint


class board:
    board = []

    for i in range(3):
        board.append(listworld.sujet[randint(0, len(listworld.sujet))])
        board.append(listworld.verbe[randint(0, len(listworld.verbe))])
        board.append(listworld.complement[randint(0, len(listworld.complement))])
        board.append(listworld.conjonction[randint(0, len(listworld.conjonction))])

    def openBoard(self):
        for world in self.board:
            print(world)
