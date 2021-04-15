

#### A simple tic tac toe game

board = [' ' for x in range(10)]   # this is our main board for the game

def insertLetter (letter,position):
    board[position] = letter 
    
def spaceIsFree (position):
    if board[position] == ' ' :
        return True
    else:
        return False

def printBoard (board) :
    print('   |   |')
    print(' '+ board[1]+ ' | '+board[2]+ ' | '+board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[4]+ ' | '+board[5]+ ' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[7]+ ' | '+board[8]+ ' | '+board[9])
    print('   |   |')
    print('        ')

def isWinner (board,letter) :
    if (board[1] == letter and board[2] == letter and board[3] == letter) :
        return True
    if (board[4] == letter and board[5] == letter and board[6] == letter) :
        return True
    if (board[7] == letter and board[8] == letter and board[9] == letter) :
        return True
    if (board[1] == letter and board[5] == letter and board[9] == letter) :
        return True
    if (board[3] == letter and board[5] == letter and board[7] == letter) :
        return True
    if (board[1] == letter and board[4] == letter and board[7] == letter) :
        return True
    if (board[2] == letter and board[5] == letter and board[8] == letter) :
        return True
    if (board[3] == letter and board[6] == letter and board[9] == letter) :
        return True
    else :
        return False

def playerMove ():
    run = True 
    while run :
        move = input(' Type the position to put the letter in : ')
        try :
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move) :
                    insertLetter('X', move)
                    run = False
                else :
                    print("Sorry, this space is occupied!")
            else:
                print(" Please input a number between 1 and 9!")
                
        except :
            print("Please type a number!")

def compMove ():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    if len(possibleMoves) > 0:
        move = selectRandom(possibleMoves)
        return move
    else :
        return move

def selectRandom(lis) :
    import random
    ln = len(lis)
    rand = random.randrange(0, ln)
    return lis[rand]

def isBoardFull (board):
    if board.count(' ') > 1:
        return False
    else :
        return True

def mainBody ():
    print("This is a game of Tic tac toe! ")
    printBoard(board)
    
    while not(isBoardFull(board)):
        
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else :
            print('The computer has won the game!')
            break
        
        if not(isWinner(board, 'X')):
          move = compMove()
        
          if move == 0:
              print("Tie game!")
          
          else :
              insertLetter('O', move)
              printBoard(board)
              print("The computer played : ", move)
        else :
            print("You have won the game!")
            break
        

def updateBoard():
    global board
    board = [' ' for x in range(10)]
    

def playAgain () :
    playAgain = True
    while playAgain == True:
        answer = input("Do you want to play another game? [y/n]: ")
        
            
        if answer == "yes" or answer == "y" :
            updateBoard() 
            mainBody()
        elif answer == "no" or answer == "n" :
            playAgain = False
        else:
            print("Please type yes or no!")
            
    print("See ou next time!")

    
def playGame () :
    mainBody()
    playAgain()
    
playGame() #needed to start the program
    
        

      
    
        
           

    
    

