from WodList import listword
from random import randint


class board:
    boardList = []

    for i in range(3):
        boardList.append(listword.sujet[randint(0, len(listword.sujet)-1)])
        boardList.append(listword.verbe[randint(0, len(listword.verbe)-1)])
        boardList.append(listword.complement[randint(0, len(listword.complement)-1)])
        boardList.append(listword.conjonction[randint(0, len(listword.conjonction)-1)])


