from WodList import listword
from random import randint


class board:
    board = []

    for i in range(3):
        board.append(listword.sujet[randint(0, len(listword.sujet))])
        board.append(listword.verbe[randint(0, len(listword.verbe))])
        board.append(listword.complement[randint(0, len(listword.complement))])
        board.append(listword.conjonction[randint(0, len(listword.conjonction))])

    def openBoard(self):
        for world in self.board:
            print(world)
