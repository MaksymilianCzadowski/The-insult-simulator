from WordList import listword
from random import randint
from Player import player

class board:
    def __init__(self):
        self.boardList = []

        for i in range(3):
            self.boardList.append(listword.sujet[randint(0, len(listword.sujet) - 1)])
            self.boardList.append(listword.verbe[randint(0, len(listword.verbe) - 1)])
            self.boardList.append(listword.complement[randint(0, len(listword.complement) - 1)])
            self.boardList.append(listword.conjonction[randint(0, len(listword.conjonction) - 1)])

    def newBoard(self):
        boardList = []
        for i in range(3):
            boardList.append(listword.sujet[randint(0, len(listword.sujet) - 1)])
            boardList.append(listword.verbe[randint(0, len(listword.verbe) - 1)])
            boardList.append(listword.complement[randint(0, len(listword.complement) - 1)])
            boardList.append(listword.conjonction[randint(0, len(listword.conjonction) - 1)])

        self.boardList = boardList
        return self.boardList

    def openBoard(self):
        count = 1
        for word in self.boardList:
            print('[', count, ']', word)
            count += 1
        print('[', 100, ']', "Bonus")
