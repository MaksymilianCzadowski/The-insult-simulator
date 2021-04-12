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

        self.phrase = ""
        self.vie = 100
        self.damage = 5

    def openBoard(self):
        count = 1
        for word in board.boardList:
            print('[', count, ']', word)
            count += 1


    def chooseWord(self):

        self.openBoard()
        print()
        choice = int(input("Entre une valeur : "))

        while choice > len(board.boardList):
            print('valeur incorrect, veulliez saisir une valeur entre 1 et', len(board.boardList))
            choice = int(input())


        for i in board.boardList:
            if i == board.boardList[choice-1]:
                self.phrase += i + " "
                board.boardList.pop(choice-1)
                return
        return


    def attackPhase(self):
        player_health = 0
        weakness = False
        if (len(self.phrase) > 50) and (len(self.phrase) < 60):
            player_health = player_health - self.damage + 10
            if weakness:
                player_health *= 1.5
        elif len(self.phrase) < 50:
            player_health = player_health - self.damage
            if weakness:
                player_health *= 1.5
        elif len(self.phrase) < 60:
            player_health = player_health - self.damage + 20
            if weakness:
                player_health *= 1.5

        return int(player_health)






