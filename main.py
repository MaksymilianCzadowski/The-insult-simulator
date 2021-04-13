from Player import player
from Board import board
from time import sleep

board = board()


def game():
    print("Le jeux va commencer!!")
    sleep(2)
    print("Personnage disponible : ")
    print("[ 1 ] L'ancien")
    print("Faiblesse : Cette vielle personnes détestent quand on insulte sa famille et son physique de vieux.")
    sleep(2)
    print("[ 2 ] Le jeune")
    print("Ce jeune ado prépubère déteste quand on insulte sa manière de s'habiller et son physique d'enfant.")
    sleep(2)
    print("[ 3 ] Le noble")
    print("Ce personnage issue de la haute noblesse n'aime pas quand on se moque de sa hierarchie et qu'on l'insulte.")
    sleep(2)
    print("[ 4 ] L'intello")
    print("Cet homme aillant un QI plus élevé n'aime pas qu'on "
          "insulte sa famille et d'être comparé a certaine personnes.")
    sleep(2)
    print()


    choice = int(input("Joueur 1 choississez votre personnage : "))
    while choice < 1 or choice > 4:
        choice = int(input("Joueur 1 choississez votre personnage : "))
    player1 = player(choice)
    choice = int(input("Joueur 2 choississez votre personnage : "))
    while choice < 1 or choice > 4:
        choice = int(input("Joueur 2 choississez votre personnage : "))
    player2 = player(choice)
    print("Le jeux se lance!")
    sleep(2)

    while not (player1.vie <= 0 or player2.vie <= 0):
        while len(board.boardList) > 2:
            print("player1 :", player1.phrase)
            player1.chooseWord(board)
            print("player2 :", player2.phrase)
            player2.chooseWord(board)


        print("La phrase de player1 est : \"", player1.phrase, "\"")
        print("La phrase de player2 est : \"", player2.phrase, "\"")

        print("------------------")

        player1.vie -= player2.attackPhase()
        player2.vie -= player1.attackPhase()
        player1.bonusAtt = 0
        player2.bonusAtt = 0

        print("player1 :", player1.vie, "PV")
        print("player2 :", player2.vie, "PV")

        sleep(3)
        board.newBoard()
        player1.phrase = ""
        player2.phrase = ""

    if player1.vie <= 0:
        print("Vainqueur de la rencontre : Joueur 2 !")
    elif player2.vie <= 0:
        print("Vainqueur de la rencontre : Joueur 1 !")
    else:
        print("Egalité... Dommage !")

game()
