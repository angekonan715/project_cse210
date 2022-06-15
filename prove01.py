
'''
Solution to Tic-Tac-Toe game
Author: Kouadio Ange Konan

'''

print("!!!Welcome to my Tic-Tac-Toe game!!!")
print(""+'\n')

#create afunction that return a list containing 9 elements from range(1,9)
def gameElement():
    list =[]
    for i in range(1,10):
        list.append(i)
    return list

# create a function to display our game board
def displayGameBoard(list):
    print("{}|{}|{}".format(list[0],list[1], list[2] ))
    print("-+-+-")
    print("{}|{}|{}".format(list[3],list[4], list[5] ))
    print("-+-+-")
    print("{}|{}|{}".format(list[6],list[7], list[8] ))



def winningCond(list):
    if ((list[0] ==list[1] ==list[2])
        or (list[3] ==list[4] ==list[5])
        or (list[6] == list[7] == list[8])
        or (list[0] == list[3] == list[6])
        or (list[1] == list[4] == list[7])
        or (list[2] == list[5] == list[8])
        or (list[0] == list[4] == list[6])
        or(list[2] ==  list[4] == list[6])):
        return True
    else:
        return False

def playingGame(list):
    
    while (winningCond(list) != True):
         x = int(input("x's turn to choose a square (1-9): "))
         if (x>=1 and x<=9):
             list[x-1] = "x"
             print("")
             displayGameBoard(list)
             if (winningCond(list) == True):
                 print("")
                 return("Good game. Thanks for playing!")
             else:
                 y = int(input("O's turn to choose a square (1-9): "))
                 if (y>=1 and y<=9):
                     list[y-1] = "o"
                     print("")
                     displayGameBoard(list)
                     if (winningCond(list) == True):
                         print("")
                         return("Good game. Thanks for playing!")
                   
        
        
def main():
    list = gameElement()
    displayGameBoard(list)
    print("")
    print(playingGame(list)) 
if __name__ == "__main__":
    main()    

            