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

        def chooseWord(self):
            
