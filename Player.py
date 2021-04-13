from Personnages.Jeune import jeune
from Personnages.Noble import noble
from Personnages.Ancien import ancien
from Personnages.Intello import intello
from time import sleep

class player:
    def __init__(self, personnage):
        self.personnage = personnage
        if personnage == 1:
            self.faiblesse = ancien.faiblesse
        if personnage == 2:
            self.faiblesse = jeune.faiblesse
        if personnage == 3:
            self.faiblesse = noble.faiblesse
        if personnage == 4:
            self.personnage = intello.faiblesse

        self.phrase = ""
        self.phraseList = []
        self.vie = 100
        self.damage = 5
        self.bonus = True
        self.bonusAtt = 0
        self.newBoardBonus = False

    def chooseWord(self, board):

        board.openBoard()
        print()
        choice = int(input("Entré une valeur : "))

        if choice == 100:
            self.Bonus()
            if self.newBoardBonus:
                board.newBoard()
            board.openBoard()
            choice = int(input("Entré une valeur : "))

        while choice > len(board.boardList) + 1:
            print('valeur incorrect, veulliez saisir une valeur entre 1 et', len(board.boardList))
            choice = int(input())

        if choice < len(board.boardList):

            for i in board.boardList:
                if i == board.boardList[choice - 1]:
                    self.phrase += i + " "
                    self.phraseList.append(i)
                    board.boardList.pop(choice - 1)
                    return
            return
        else:
            print('valeur incorrect, veulliez saisir une valeur entre 1 et', len(board.boardList))
            choice = int(input())

    def hasWeakness(self):
        for i in self.phraseList:
            if i in self.faiblesse:
                return True
        return False

    def attackPhase(self):
        player_damage = 0
        faiblesse = self.hasWeakness()
        if (len(self.phrase) > 50) and (len(self.phrase) < 60):
            player_damage = self.damage + 10 + self.bonusAtt
            if faiblesse:
                player_damage *= 1.5
        elif len(self.phrase) < 50:
            player_damage = self.damage +self.bonusAtt
            if faiblesse:
                player_damage *= 1.5
        elif len(self.phrase) > 60:
            player_damage = self.damage + 20 + self.bonusAtt
            if faiblesse:
                player_damage *= 1.5

        return player_damage

    def Bonus(self):
        print()
        if self.bonus:
            listBonus = ["Nouveau tableau de mot", "+5 d'attaque pendant ce tour", "+10 de points vie"]
            count = 1
            for i in listBonus:
                print('[', count, ']', i)
                count += 1

            choice = int(input("Vous avez le droit à un seul bonus par patie, lequelle voulez-vous utilser : "))
            while choice < 1 or choice > 3:
                choice = int(input("Viellez rentrer une valeur entre 1 et 3 : "))

            if choice == 1:
                self.newBoardBonus = True
            elif choice == 2:
                self.bonusAtt = 5
            elif choice == 3:
                self.vie += 5
        else:
            print("Bonus déjà utilisé!")
            sleep(1)
        self.bonus = False
