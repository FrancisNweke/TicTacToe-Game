import time
import os

gameBoard = {9: ' ', 8: ' ', 7: ' ',
             6: ' ', 5: ' ', 4: ' ',
             3: ' ', 2: ' ', 1: ' '}

boardPositions = []

for position in gameBoard:
    boardPositions.append(position)


# print original board
def PrintBoardSample():
    print('                 Game board with possible positions below:\n')
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(9, 8, 7))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(6, 5, 4))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(3, 2, 1))
    print("\t     |     |")
    print("\n")


# load game
def LoadGame(delayTime):
    print("\nPlease wait while we setup the game....\n")
    time.sleep(delayTime)

    if os.name == 'nt':
        lambda: os.system('cls')
    else:
        os.system('clear')


# print the score-board
def ShowScoreBoard(scoreBoard):
    print("\t\t--------------------------------")
    print("\t\t              SCOREBOARD       ")
    print("\t\t--------------------------------")

    players = list(scoreBoard.keys())

    print("\t\t   ", players[0], f"-[{scoreBoard['1']}]\t\t   ", scoreBoard[players[0]])
    print("\t\t   ", players[1], f"-[{scoreBoard['2']}]\t\t   ", scoreBoard[players[1]])

    print("\t\t--------------------------------\n")


# ask user if he/she wants to play again
def RestartGame():
    try:

        restart = input(
            'Would you like to play again? (Yes/No): ')
        if restart in ('Yes', 'Y', 'y', 'yes'):
            for position in boardPositions:
                gameBoard[position] = ' '

            return 0
            # GamePlay()
        else:
            print('Thank you for playing.')

            return -1

    except ValueError:
        print("Invalid Input! We will reload the game now.")
        GamePlay()


# print game board
def PrintBoard(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[9], board[8], board[7]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[6], board[5], board[4]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(board[3], board[2], board[1]))
    print("\t     |     |")
    print("\n")


# game funtionalities
def GamePlay():
    turn = 'X'
    count = 0
    replay = 0

    scoreBoardPlayers = {'Player 1': 0, 'Player 2': 0, '1': 'X', '2': 'O'}

    LoadGame(2)

    PrintBoardSample()

    playerSwitch = input("[X] is player 1 and [O] is player 2. Do you wish to switch players? (Yes/No): ")

    if playerSwitch in ('Yes', 'yes', 'Y', 'y'):
        turn = 'O'
        scoreBoardPlayers['1'] = turn
        scoreBoardPlayers['2'] = 'X'
        print("\n[O] is player 1 and [X] is player 2.")

    while (replay == 0):
        for i in range(10):
            ShowScoreBoard(scoreBoardPlayers)

            PrintBoard(gameBoard)

            try:
                print(turn + ", Which position would you take on the board? ")

                position = int(input())

                if position > 0 and position < 10:
                    if gameBoard[position] == ' ':
                        gameBoard[position] = turn
                        count += 1
                    else:
                        print(f"Position {position} is occupied already! Please enter another position. ")
                        continue
                else:
                    print("Invalid Input! Try a number between 1 and 9.")
            except ValueError:
                print("Invalid Input! Try a number between 1 and 9.")
                continue

                # check if there is winner after 5 moves has been made on the board
            if count >= 5:
                if gameBoard[9] == gameBoard[8] == gameBoard[7] != ' ':  # top-board
                    PrintBoard(gameBoard)
                    print('\nGame Over\n')
                    print(f'*** {turn} won! ***')
                    break
                elif gameBoard[6] == gameBoard[5] == gameBoard[4] != ' ':  # mid-board
                    PrintBoard(gameBoard)
                    print('\nGame Over\n')
                    print(f'*** {turn} won! ***')
                    break
                elif gameBoard[3] == gameBoard[2] == gameBoard[1] != ' ':  # bottom-baord
                    PrintBoard(gameBoard)
                    print('\nGame Over\n')
                    print(f'*** {turn} won! ***')
                    break
                elif gameBoard[3] == gameBoard[5] == gameBoard[7] != ' ':  # diagonally
                    PrintBoard(gameBoard)
                    print('\nGame Over\n')
                    print(f'*** {turn} won! ***')
                    break
                elif gameBoard[1] == gameBoard[4] == gameBoard[9] != ' ':  # diagonally
                    PrintBoard(gameBoard)
                    print('\nGame Over\n')
                    print(f'*** {turn} won! ***')
                    break
                elif gameBoard[3] == gameBoard[6] == gameBoard[9] != ' ':  # down-top left
                    PrintBoard(gameBoard)
                    print('\nGame Over\n')
                    print(f'*** {turn} won! ***')
                    break
                elif gameBoard[2] == gameBoard[5] == gameBoard[8] != ' ':  # down-top middle
                    PrintBoard(gameBoard)
                    print('\nGame Over\n')
                    print(f'*** {turn} won! ***')
                    break
                elif gameBoard[1] == gameBoard[4] == gameBoard[7] != ' ':  # down-top right
                    PrintBoard(gameBoard)
                    print('\nGame Over\n')
                    print(f'*** {turn} won! ***')
                    break

            # end the game as a tie.
            if count == 9:
                print('\nGame Over! No Winner.')
                response = RestartGame()
                if response != 0:
                    replay = response
                    break

            # switch player after each play.
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

    # RestartGame()


if __name__ == "__main__":
    GamePlay()
