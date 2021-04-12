from Player import player
from Board import board
from time import sleep

player1 = player('jeune')
player2 = player('ancien')
board = board()

def game():
    while not (player1.vie < 0 or player2.vie < 0):
        while len(board.boardList) > 2:
            player1.chooseWord(board)
            player2.chooseWord(board)

        print("La phrase de player1 est : \"", player1.phrase, "\"")
        print("La phrase de player2 est : \"", player2.phrase, "\"")

        print("------------------")
        print(len(player1.phrase))
        print(len(player2.phrase))
        print("-------------------")
        player1.vie -= player2.attackPhase()
        player2.vie -= player1.attackPhase()

        print("player1 :", player1.vie, "PV")
        print("player2 :", player2.vie, "PV")
        sleep(3)
        board.newBoard()
        player1.phrase = ""
        player2.phrase = ""


game()
