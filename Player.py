from Board import board
import time


class player:
    def __init__(self, personnage):
        self.personnage = personnage
        if personnage == "ancien":
            self.faiblesse = "vielle"
        if personnage == "jeune":
            self.faiblesse = "physique"
        if personnage == "noble":
            self.faiblesse = "hierarchie"
        if personnage == "intello":
            self.personnage = "intelligence"

        self.phrase = []
        self.vie = 100

    def openBoard(self):
        for world in board.boardList:
            print(world)


    def chooseWord(self):
        ok = 'ajout du mot'
        non = 'non'
        self.openBoard()
        choice = int(input())

        while choice > len(board.boardList):
            print('valeur incorrect')
            choice = int(input())

        for i in board.boardList:
            if i == board.boardList[choice-1]:
                self.phrase.append(i)
                return ok
        return non




