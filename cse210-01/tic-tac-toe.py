from tkinter import *
import random

# fuction for the next turn in index row and column
def nextTurn(row, column):
    
    global player

    if buttons[row][column]['text'] == "" and checkWinner() is False:
        # index 0 for player "x"
        if player == players[0]:

            # The player selects the button in the game
            buttons[row][column]['text'] = player

            # if there is not winner, changing players turn after a player selected a button
            if checkWinner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            # if there is a winner, displayers player's name and winner
            elif checkWinner() is True:
                label.config(text=(players[0]+" wins"))

            #  if the game is tie, display "Tie"
            elif checkWinner() == "Tie":
                label.config(text="Tie!")

        else:
             # The player selects the button in the game
            buttons[row][column]['text'] = player

            # if there is not winner, changing players turn after a player selected a button
            if checkWinner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            # if there is a winner, displayers player's name and winner
            elif checkWinner() is True:
                label.config(text=(players[1]+" wins"))

            #  if the game is tie, display "Tie"
            elif checkWinner() == "Tie":
                label.config(text="Tie!")

# fuction to checck the winner in row, columnm and diagonal.
def checkWinner():
    # loop check for row in range 5
    for row in range(5):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] == buttons[row][3]['text'] == buttons[row][4]['text'] != "":
            # changes background color in any row using config
            buttons[row][0].config(bg="#3A8891")
            buttons[row][1].config(bg="#3A8891")
            buttons[row][2].config(bg="#3A8891")
            buttons[row][3].config(bg="#3A8891")
            buttons[row][4].config(bg="#3A8891")
            return True

    # loop check for column in range 5
    for column in range(5):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] == buttons[3][column]['text'] == buttons[4][column]['text'] != "":
            # changes background color in any column using config
            buttons[0][column].config(bg="#3A8891")
            buttons[1][column].config(bg="#3A8891")
            buttons[2][column].config(bg="#3A8891")
            buttons[3][column].config(bg="#3A8891")
            buttons[4][column].config(bg="#3A8891")
            return True

    #  checking for diagonal conditions from index [0,0] to [4,4]
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == buttons[3][3]['text'] == buttons[4][4]['text']!= "":
        # changes the color of the diagonal using config
        buttons[0][0].config(bg="#3A8891")
        buttons[1][1].config(bg="#3A8891")
        buttons[2][2].config(bg="#3A8891")
        buttons[3][3].config(bg="#3A8891")
        buttons[4][4].config(bg="#3A8891")
        return True

    #  checking for diagonal conditions from index [0,4] to [4,0]
    elif buttons[0][4]['text'] == buttons[1][3]['text'] == buttons[2][2]['text'] == buttons[3][1]['text'] == buttons[4][0]['text'] != "":
        # changes the color of the diagonal using config
        buttons[0][4].config(bg="#3A8891") 
        buttons[1][3].config(bg="#3A8891")
        buttons[2][2].config(bg="#3A8891")
        buttons[3][1].config(bg="#3A8891")
        buttons[4][0].config(bg="#3A8891")
        return True

    #  checkign for empty spaces and if all occupied it will return as "Tie"
    elif emptySpaces() is False:

        for row in range(5):
            for column in range(5):
                buttons[row][column].config(bg="#0E5E6F")
        return "Tie"

    else:
        return False

# function for empty spaces
def emptySpaces():

    # since it five by fice = total spaces is 25 
    spaces = 25

    for row in range(5):
        for column in range(5):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    #  return false if the spaces is zero and return a "Tie"
    if spaces == 0:
        return False
    else:
        return True

#  function for the setting new game
def newGame():

    global player
    #  random choice for player
    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(5):
        for column in range(5):
            buttons[row][column].config(text="",bg="#F2DEBA")

#  creating a window for the Tic-tac-toe game
window = Tk()
# window title
window.title("cse210 - Tic-Tac-Toe")
# name of global players
players = ["x","o"]
#  random choice of players
player = random.choice(players)
# creating button for 5x5 window
buttons = [[0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0]]

# creating labels for the player and pack the label
label = Label(text=player + " turn", font=('Roboto',40))
label.pack(side="top")

# creating reset button and pack the reset button
reset_button = Button(text="reset", font=('Roboto',20), command=newGame)
reset_button.pack(side="bottom")

# making frame to a frame window and pack the frame
frame = Frame(window)
frame.pack()

# nestes for loops in creating button inside the frame
for row in range(5):
    for column in range(5):
        buttons[row][column] = Button(frame, text="",font=('Roboto',40), width=5, height=2,
                                      command= lambda row=row, column=column: nextTurn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()