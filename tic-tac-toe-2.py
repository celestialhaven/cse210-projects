# Create game gameBoard with 5x5 using array
gameBoard = ['-', '-', '-','-', '-',
        '-', '-', '-','-', '-',
        '-', '-', '-','-', '-',
        '-', '-', '-','-', '-',
        '-', '-', '-','-', '-',]

currentPlayer = "X"
winner = None
continueGame = True

#printing gameBoard
def printgameBoard(gameBoard):
    print(gameBoard[0] + " | " + gameBoard[1] + " | " + gameBoard[2] + " | " + gameBoard[3] + " | " + gameBoard[4])
    print("-" * 17)
    print(gameBoard[5] + " | " + gameBoard[6] + " | " + gameBoard[7] + " | " + gameBoard[8] + " | " + gameBoard[9])
    print("-" * 17)
    print(gameBoard[10] + " | " + gameBoard[11] + " | " + gameBoard[12] + " | " + gameBoard[13] + " | " + gameBoard[14])
    print("-" * 17)
    print(gameBoard[15] + " | " + gameBoard[16] + " | " + gameBoard[17] + " | " + gameBoard[18] + " | " + gameBoard[19])
    print("-" * 17)
    print(gameBoard[20] + " | " + gameBoard[21] + " | " + gameBoard[22] + " | " + gameBoard[23] + " | " + gameBoard[24])

# player input
def playerInput(gameBoard):
    while True:
        if currentPlayer == "X":
            inp = int(input(f"Enter a number 1-25 \033[95m Player 'X' \033[00m : ")) 
        else:
            inp = int(input(f"Enter a number 1-25 \033[94m Player (0) \033[00m : "))
        if inp >= 1 and inp <= 25 and gameBoard[inp-1] == "-":
            gameBoard[inp-1] = currentPlayer
            break
        else:
            if currentPlayer == "X":
                print(f"The number has been selected by the other player! Please select another number. - \033[95m Player 'X' \033[00m : ")
            else:
                print(f"The number has been selected by the other player! Please select another number. - \033[94m Player (0) \033[00m : ")
            printgameBoard(gameBoard)


# function to check the column line
def rowCheck(gameBoard):
    global winner
    if (gameBoard[0] == gameBoard[1] == gameBoard[2] == gameBoard[3] == gameBoard[4] and gameBoard[0] != "-") or (gameBoard[5] == gameBoard[6] == gameBoard[7] == gameBoard[8] == gameBoard[9] and gameBoard[5] != "-") or (gameBoard[10] == gameBoard[11] == gameBoard[12] == gameBoard[13] == gameBoard[14] and gameBoard[10] != "-") or (gameBoard[15] == gameBoard[16] == gameBoard[17] == gameBoard[18] == gameBoard[19] and gameBoard[15] != "-") or (gameBoard[20] == gameBoard[21] == gameBoard[22] == gameBoard[23] == gameBoard[24] and gameBoard[20] != "-"):
        winner = currentPlayer
        return True
    
# function to check every row line
def columnCheck(gameBoard):
    global winner
    if (gameBoard[0] == gameBoard[5] == gameBoard[10] == gameBoard[15] == gameBoard[20] and gameBoard[0] != "-") or (gameBoard[1] == gameBoard[6] == gameBoard[11] == gameBoard[16] == gameBoard[21] and gameBoard[1] != "-") or (gameBoard[2] == gameBoard[7] == gameBoard[12] == gameBoard[17] == gameBoard[22] and gameBoard[2] != "-") or (gameBoard[3] == gameBoard[8] == gameBoard[13] == gameBoard[18] == gameBoard[23] and gameBoard[3] != "-") or (gameBoard[4] == gameBoard[9] == gameBoard[14] == gameBoard[19] == gameBoard[24] and gameBoard[4] != "-"):
        winner = currentPlayer
        return True
    
# function for checking the diagonal line
def diagonalCheck(gameBoard):
    global winner
    if (gameBoard[0] == gameBoard[6] == gameBoard[12] == gameBoard[18] == gameBoard[24] and gameBoard[0] != "-") or (gameBoard[4] == gameBoard[8] == gameBoard[12] == gameBoard[16] == gameBoard[20] and gameBoard[4] != "-"):
        winner = currentPlayer
        return True
    
# function to check the tie
def tieCheck(gameBoard):
    global continueGame
    if "-" not in gameBoard:
        printgameBoard(gameBoard)
        print("Its a tie")
        continueGame = False
        
# function to check the winner
def winCheck():
    if diagonalCheck(gameBoard) or columnCheck(gameBoard) or columnCheck(gameBoard):
        print(f"The winner is {winner}")

#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#check for win or tie again
while continueGame:
    printgameBoard(gameBoard)
    if winner != None:
        break
    playerInput(gameBoard)
    winCheck()
    tieCheck(gameBoard)
    switchPlayer()