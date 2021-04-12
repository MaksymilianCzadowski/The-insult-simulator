from Player import player
from Board import board

player1 = player('jeune')
player2 = player('ancien')


def game():
    while len(board.boardList) > 2:
        player1.chooseWord()
        player2.chooseWord()

    print("La phrase de player1 est : \"", player1.phrase, "\"")
    print("La phrase de player2 est : \"", player2.phrase, "\"")


game()
