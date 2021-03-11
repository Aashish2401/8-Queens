import numpy as np

board = [[0,0,0,0,0,0,0,0],                                         #Initialization of empty chess board. HeHe Bouyyy :"D
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]

count = 1                                                           #Solution number

def possible(x,y) :                                                 #Checking if its possible
    global board
    
    for i in range(8) :        
        if board[y][i] == 1 : #Checking the row for attacks
            return False
        if board[i][x] == 1 : #Checking the column for attacks
            return False

    ind = 0

    while x + ind < 8 and y + ind < 8: #Checking the bottom half of the major diagonal
        if board[y + ind][x + ind] == 1 :
            return False
        ind = ind + 1

    ind = 0
    
    while x - ind >= 0 and y - ind >= 0: #Checking the top half of the major diagonal
        if board[y - ind][x - ind] == 1 :
            return False
        ind = ind + 1

    ind = 0

    while x + ind < 8 and y - ind >= 0: #Checking the top half of the minor diagonal
        if board[y - ind][x + ind] == 1 :
            return False
        ind = ind + 1

    ind = 0
    
    while x - ind >= 0 and y + ind < 8: #Checking the bottom half of the minor diagonal
        if board[y + ind][x - ind] == 1 :
            return False
        ind = ind + 1

    return True

def solve(y) :                                                      #Method to define the backtracking search algorithm
    global board
    global count

    if y == 8 : #This block prints the board after a solution has been found
        print()
        print("Solution {0}:".format(count))
        print()
        count += 1
        print(np.matrix(board))
        return
    
    for j in range(8) : 
        if board[y][j] == 0 :
            if possible(j,y) :
                board[y][j] = 1
                solve(y + 1) #Recursive call
                board[y][j] = 0

    return

solve(0) #Initial call
input()
