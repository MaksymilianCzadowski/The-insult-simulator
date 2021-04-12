
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
                board.boardList.pop(choice - 1)
                return
        return

    def attackPhase(self):
        player_damage = 0
        weakness = False
        if (len(self.phrase) > 50) and (len(self.phrase) < 60):
            player_damage = self.damage + 10
            if weakness:
                player_damage *= 1.5
        elif len(self.phrase) < 50:
            player_damage = self.damage
            if weakness:
                player_damage *= 1.5
        elif len(self.phrase) > 60:
            player_damage = self.damage + 20
            if weakness:
                player_damage *= 1.5

        return player_damage
