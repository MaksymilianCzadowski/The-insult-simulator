from Player import player
from Board import board

player1 = player('jeune')
player2 = player('ancien')

mots = board
player1.chooseWord()
print('---------------------')
print(player1.phrase)



