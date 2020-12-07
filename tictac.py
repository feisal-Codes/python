
import random
import time


board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
turn = 'X'

MoveCount = 0
defaultt = ''


def printBoard(board):
    print('   |   |')

    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

    print('   |   |')


def chooseOpponent():
    global defaultt
    print('Choose Opponent to play against')

    print('Player:   1')
    print('Computer: 2')
    print('Help:     3')

    try:
        playerChoice = int(input())
        if playerChoice == 1:
            defaultt = False
        elif playerChoice == 2:
            defaultt = True
        elif playerChoice == 3:
            print('..................')
            print('Welcome to TicTacToe game')
            print('Press The Numbers on the board to play the game')
            print('Match X or O in a row , column or diagnol to win the game')
            print('..................')

            chooseOpponent()
    except ValueError:
        print('enter an integer')


def game(board):
    chooseOpponent()
    global defaultt
    if defaultt == True or defaultt == False:
        printBoard(board)
        playerToStart()
        gameplay(board)


def playerToStart():
    global turn
    global defaultt
    start = random.randint(0, 1)
    if defaultt:
        if start == 0:
            print('player 1 to start the game')
            print('player 1 is X ')
            turn = 'X'
        else:
            print('Computer to start the game')
            print('Computer is O')
            turn = 'O'
    else:
        if start == 0:
            print('player 1 to start the game')
            print('player 1 is X ')
            turn = 'X'
        else:
            print('Player 2 to start the game')
            print('Player is O')
            turn = 'O'


def gameplay(board):

    while True:
        global MoveCount
        global turn

        if turn == '':
            print('Game over')
            return

        if MoveCount == 9:
            print("it's Tie")
            printBoard(board)
            print('Game Over')
            break

        if turn == 'X':
            player1(board)
        if defaultt:
            if turn == 'O':
                print('Computer to select a move')
                print('thinking ....')
                time.sleep(1)
                computerTurn(board)
        else:
            if turn == 'O':
                player2(board)


def checkwin(board):
    global turn
    if board[0] == board[1] == board[2]:
        turn = ''
        return True
    elif board[3] == board[4] == board[5]:
        turn = ''
        return True

    elif board[6] == board[7] == board[8]:
        turn = ''
        return True
    elif board[0] == board[3] == board[6]:
        turn = ''
        return True
    elif board[1] == board[4] == board[7]:
        turn = ''
        return True
    elif board[2] == board[5] == board[8]:
        turn = ''
        return True
    elif board[0] == board[4] == board[8]:
        turn = ''
        return True
    elif board[2] == board[4] == board[6]:
        turn = ''
        return True

    return False


def isSpaceFree(board, move):
    return board[move] != 'X' or board[move] != 'O'


def computerTurn(board):
    global MoveCount, turn

    availableMoves = validMove(board)
    if availableMoves == None:
        return
    else:
        MoveCount += 1

        ComAi(board)
        com(board)


def com(board):
    global turn
    if checkwin(board):
        print('Computer Wins')
        printBoard(board)
        return
    else:
        printBoard(board)
        turn = 'X'


def player1(board):
    global MoveCount, turn
    try:
        print('Player 1 to select a move')

        move = int(input())
        MoveCount += 1

        if board[move] == 'X' or board[move] == 'O':
            print('Slot Already occupied')
            MoveCount -= 1

        else:
            board[move] = turn
            if checkwin(board):
                print('player 1 wins')
                printBoard(board)
                return
            else:
                printBoard(board)
                turn = 'O'
    except (IndexError, ValueError):
        print('Please Enter An integer between 0-8')
        MoveCount -= 1


def player2(board):
    global MoveCount, turn
    try:
        print('Player 2 to select a move')

        move = int(input())
        MoveCount += 1

        if cannotMove(board, move):
            print('Slot Already occupied')
            MoveCount -= 1

        else:
            board[move] = turn
            if checkwin(board):
                print('player 2 wins')
                printBoard(board)
                return
            else:
                printBoard(board)
                turn = 'X'
    except (IndexError, ValueError):
        print('Please Enter An integer between 0-8')
        MoveCount -= 1


def cannotMove(board, move):
    if board[move] == 'X' or board[move] == 'O':

        return True
    return False


def isPlayerWining(board):

    if board[0] == board[1] == 'X' or board[0] == board[2] == 'X' or board[1] == board[2] == 'X':
        return (0, 1, 2)
    elif board[3] == board[4] == 'X' or board[3] == board[5] == 'X' or board[4] == board[5] == 'X':
        return (3, 4, 5)

    elif board[6] == board[7] == 'X' or board[7] == board[8] == 'X' or board[6] == board[8] == 'X':
        return (6, 7, 8)

    elif board[0] == board[3] == 'X' or board[0] == board[6] == 'X' or board[3] == board[6] == 'X':
        return (0, 3, 6)

    elif board[1] == board[4] == 'X' or board[1] == board[7] == 'X' or board[4] == board[7] == 'X':
        return (1, 4, 7)

    elif board[2] == board[5] == 'X' or board[2] == board[8] == 'X' or board[5] == board[8] == 'X':
        return (2, 5, 8)

    elif board[0] == board[4] == 'X' or board[0] == board[8] == 'X' or board[4] == board[8] == 'X':
        return (0, 4, 8)

    elif board[2] == board[4] == 'X' or board[2] == board[6] == 'X' or board[4] == board[6] == 'X':
        return (2, 4, 6)


def validMove(bod):
    global board
    moveList = []

    if type(bod[0]) == int:
        for space in bod:
            if board[space] != 'X' and board[space] != 'O':
                if cannotMove(board, space) == False:
                    return space

    else:
        moveList = []
        for space in range(len(bod)):
            if bod[space] != 'X' and bod[space] != 'O':
                moveList += [space]
        return moveList

# Computer Medium Level


def ComAi(board):
    global turn
    # block player win move
    if isPlayerWining(board):

        values = isPlayerWining(board)
        for i in values:
            if board[i] != "X" and board[i] != "O":
                board[i] = turn
                return
    # Move to the center
    elif board[4] != "X" and board[4] != "O":
        board[4] = turn
        return
    # Move to the sides
    for b in (0, 2, 6, 8):
        if board[b] != "X" and board[b] != "O":
            board[b] = turn
            return
    # Move across the first row
    for b in range(3):
        if board[b] != "X" and board[b] != "O":
            board[b] = turn
            return
    # Move across the second row
    for b in range(3, 6):
        if board[b] != "X" and board[b] != "O":
            board[b] = turn
            return
    # Move across the third row
    for b in range(6, 9):
        if board[b] != "X" and board[b] != "O":
            board[b] = turn
            return

if __name__=="__main__":
  game(board)
