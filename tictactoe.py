#Things to do:
# - if they play again allow to keep names and count the series (have a back to main menu option
#    main menu should be number of players and names)
# - when there is a winner have '*' next to winning cells
# - make the 'AI' smarter (come up with a stragety)
# - make UI better and neater
#
import numpy as np
import random

def aiMove(board):
  validMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  move = random.choice(validMoves)
  
  while vaildateMove(board, move) != 0:
    move = random.choice(validMoves)
  
  return move

def checkForWinner(board):
  # CHECKS ROWS
  if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
    return 1
  if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
    return 1
  
  if board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
    return 1
  if board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
    return 1
  
  if board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
    return 1
  if board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
    return 1
  
  #CHECKS COLUMNS
  if board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
    return 1
  if board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
    return 1
  
  if board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
    return 1
  if board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
    return 1
  
  if board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
    return 1
  if board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
    return 1
  
  #CHECK DIAGONLS
  if board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
    return 1
  if board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
    return 1
  
  if board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
    return 1
  if board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
    return 1
  
def vaildateMove(board, playerMove):
  vaild = 0
  invaild = 1
  if board[playerMove - 1] == 'X':
    return invaild
  elif board[playerMove - 1] == 'O':
    return invaild
  else:
    return vaild

def updateBoard(board, currentPlayer, playerMove):
  if currentPlayer == 1:
    board[playerMove - 1] = 'X'
    
  if currentPlayer == 2:
    board[playerMove - 1] = 'O'

def display(board):
  print("  ", board[0], "  |  ", board[1], "  |  ", board[2],"  ")
  print("-------|-------|-------")
  print("  ", board[3], "  |  ", board[4], "  |  ", board[5],"  ")
  print("-------|-------|-------")
  print("  ", board[6], "  |  ", board[7], "  |  ", board[8],"  ")
  
def createBoard():
  board = np.array(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
  return board

def playTicTacToe(player1Name, player2Name, mode):
  gameStatus = True
  currentPlayer = 1
  rounds = 1
  # create board
  ticTacToeBoard = createBoard()

  while gameStatus == True and rounds <= 9:
    # display board
    if mode == 1:
      if currentPlayer == 1:
        display(ticTacToeBoard)
    else:
      display(ticTacToeBoard)
    print(" ")
    if currentPlayer == 1:
      playerMove = int(input("Where would you like to place X: "))
    elif currentPlayer == 2:
      if mode == 1:
        playerMove = aiMove(ticTacToeBoard)
      elif mode == 2:
        playerMove = int(input("Where would you like to place O: "))
    if playerMove == 99:
      print("Exited Game!")
      gameStatus == False
      break
    while playerMove < 0 or playerMove > 9:
      print("Invaild cell slection! ")
      if currentPlayer == 1:
        playerMove = int(input("Where would you like to place X: "))
      elif currentPlayer == 2:
        playerMove = int(input("Where would you like to place O: "))
        
    if vaildateMove(ticTacToeBoard, playerMove) != 0:
      print("Cell already taken! ")
      if currentPlayer == 1:
        playerMove = int(input("Where would you like to place X: "))
      elif currentPlayer == 2:
        playerMove = int(input("Where would you like to place O: "))
      
    updateBoard(ticTacToeBoard, currentPlayer, playerMove)
    
    winnerStatus = checkForWinner(ticTacToeBoard)
    
    if rounds == 9 and winnerStatus != 1:
      print(" ")
      print("TIE No Winner!")
      print(" ")
      display(ticTacToeBoard)
      gameStatus = False
    elif winnerStatus == 1:
      if currentPlayer == 1:
        print(" ")
        print("TIC TAC TOE YOU WIN",player1Name.upper(),"!")
      elif currentPlayer == 2:
        print(" ")
        print("TIC TAC TOE YOU WIN",player2Name.upper(),"!")
      print(" ")
      display(ticTacToeBoard)
      gameStatus = False
        
    
    
    if currentPlayer == 1:
      currentPlayer = currentPlayer + 1
    elif currentPlayer == 2:
      currentPlayer = currentPlayer - 1
  
    if mode == 1:
      if currentPlayer == 1:
        print(" ")
        print("-------------------------------------------------------------")
        print(" ")
    else:
        print(" ")
        print("-------------------------------------------------------------")
        print(" ")
    
    rounds += 1
    
def main():
  playGame = 0
  print("Welcome to Tic Tac Toe!")
  
  while playGame == 0:
    mode = int(input("How many players will there be(1-2)?: "))
    while mode < 1 or mode > 2:
      mode = int(input("How many players will there be(1-2)?: "))
    
    if mode == 1:
      player1 = 1
      player2 = 2
      player1Name = input("Player 1 name: ")
      player2Name = "AI"
      print(" ")
      print("... Start of Tic Tac Toe Game ", player1Name.upper(), " vs. AI ...")
      print(" ")
    elif mode == 2:
      player1 = 1
      player2 = 2
      player1Name = input("Player 1 name: ")
      print(" ")
      player2Name = input("Player 2 name: ")
      print(" ")
      print("... Start of Tic Tac Toe Game ", player1Name.upper(), " vs. ", player2Name.upper(), " ...")
      print(" ")
      
    
    playTicTacToe(player1Name, player2Name, mode)
    playGameInput = input("Play again?(Yes or No): ")
    if playGameInput.upper() == "YES":
      playGame = 0
    elif playGameInput.upper() == "NO":
      playGame = 1
  
  print(" ")
  print("bye ...")
if __name__ == "__main__":
  main()
