def displayBoard(board):
    print(" ", end="")
    print(getFieldValue(board[1]), end="")
    print("|", end="")
    print(getFieldValue(board[2]), end="")
    print("|", end="")
    print(getFieldValue(board[3]))

    print(" ", end="")
    print("-", end="")
    print("+", end="")
    print("-", end="")
    print("+", end="")
    print("-")

    print(" ", end="")
    print(getFieldValue(board[4]), end="")
    print("|", end="")
    print(getFieldValue(board[5]), end="")
    print("|", end="")
    print(getFieldValue(board[6]))

    print(" ", end="")
    print("-", end="")
    print("+", end="")
    print("-", end="")
    print("+", end="")
    print("-")

    print(" ", end="")
    print(getFieldValue(board[7]), end="")
    print("|", end="")
    print(getFieldValue(board[8]), end="")
    print("|", end="")
    print(getFieldValue(board[9]))


def getFieldValue(value):
    if value == '':
        return ' '
    else:
        return value


def copyBoard(originalBoard):
    newBoard = []
    for i in originalBoard:
        newBoard.append(i)
    return newBoard


theBoard = ['', '', '', '', '', '', '', '', '', '']
currentTurn = 'O'
nextTurn = 'X'


def setBoardValue(value, position):
    if value == 'X' or value == 'O':
        if theBoard[position] == '':
            theBoard[position] = value
            return True
    return False


def isGameDone(board):
    if (board[1] == board[2] == board[3]) and board[1] != '' \
            or (board[4] == board[5] == board[6]) and board[4] != '' \
            or (board[7] == board[8] == board[9]) and board[7] != '' \
            or (board[1] == board[4] == board[7]) and board[1] != '' \
            or (board[2] == board[5] == board[8]) and board[2] != '' \
            or (board[3] == board[6] == board[9]) and board[3] != '' \
            or (board[1] == board[5] == board[9]) and board[1] != '' \
            or (board[3] == board[5] == board[7]) and board[3] != '':
        print("there's a winner.")
        return True
    if board[1] == '' \
            or board[2] == '' \
            or board[3] == '' \
            or board[4] == '' \
            or board[5] == '' \
            or board[6] == '' \
            or board[7] == '' \
            or board[8] == '' \
            or board[9] == '':
        print("there are still some chances.")
        return False

    print("there's a tie")
    return True


displayBoard(theBoard)

while not isGameDone(theBoard):
    moved = False
    while moved == False:
        print("what's your next move?", end="")
        move = int(input())
        if move < 1 or move > 9:
            print("that's not a valid move.")
        else:
            if not setBoardValue(currentTurn, move):
                print("this move is not possible anymore.")
            else:
                moved = True

    tmp = currentTurn
    currentTurn = nextTurn
    nextTurn = tmp

    displayBoard(theBoard)
