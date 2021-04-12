from Personnages.Jeune import jeune
from Personnages.Noble import noble
from Personnages.Ancien import ancien
from Personnages.Intello import intello


class player:
    def __init__(self, personnage):
        self.personnage = personnage
        if personnage == "1":
            self.faiblesse = ancien.faiblesse
        if personnage == "2":
            self.faiblesse = jeune.faiblesse
        if personnage == "3":
            self.faiblesse = noble.faiblesse
        if personnage == "4":
            self.personnage = intello.faiblesse

        self.phrase = ""
        self.phraseList = []
        self.vie = 100
        self.damage = 5

    def chooseWord(self, board):

        board.openBoard()
        print()
        choice = int(input("Entre une valeur : "))

        while choice > len(board.boardList):
            print('valeur incorrect, veulliez saisir une valeur entre 1 et', len(board.boardList))
            choice = int(input())

        for i in board.boardList:
            if i == board.boardList[choice - 1]:
                self.phrase += i + " "
                self.phraseList.append(i)
                board.boardList.pop(choice - 1)
                return
        return

    def hasWeakness(self):
        for i in self.phraseList:
            if i in self.faiblesse:
                return True
        return False

    def attackPhase(self):
        player_damage = 0
        faiblesse = self.hasWeakness()
        if (len(self.phrase) > 50) and (len(self.phrase) < 60):
            player_damage = self.damage + 10
            if faiblesse:
                player_damage *= 1.5
        elif len(self.phrase) < 50:
            player_damage = self.damage
            if faiblesse:
                player_damage *= 1.5
        elif len(self.phrase) > 60:
            player_damage = self.damage + 20
            if faiblesse:
                player_damage *= 1.5

        return player_damage