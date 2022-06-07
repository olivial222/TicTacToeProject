board = ['-','-','-','-','-','-','-','-','-']
end = 0
valid = 0
place = 0
inputplace = "-"
currentplayer = 1
def main():
  global board, inputplace, place, valid, currentplayer, player1name, player2name
  player1name = input('What is the name of player 1?')
  print(f'Hello {player1name}!')
  player2name = input('What is the name of player 2?')
  print(f'Hello {player2name}!')
  print(f'{player1name} you are X, {player2name} you are O')
  print('Please input coordinates with letter first (ex: a3)')
  printboard()
  while end == 0:
    currentplayer = 1
    detinput()
    print(f'{player1name} goes {inputplace}!')
    board[place] = "X"
    printboard()
    gameover()
    if end == 0:
      currentplayer = 2
      detinput()
      print(f'{player2name} goes {inputplace}!')
      board[place] = "O"
      printboard()
      gameover()
  
  
def printboard():
  global board, end
  if end == 0:
    print("    a   b   c")
    print("  -------------")
    print(f"1 | {board[0]} | {board[1]} | {board[2]} |")
    print("  -------------")
    print(f"2 | {board[3]} | {board[4]} | {board[5]} |")
    print("  -------------")
    print(f"3 | {board[6]} | {board[7]} | {board[8]} |")
    print("  -------------")

def detinput():
  global board, inputplace, place, valid, currentplayer, player1name, player2name
  valid = 1
  while valid == 1 and end == 0:
    if currentplayer == 1:
      inputplace = input(f'{player1name} where would you like to go?')
    else: inputplace = input(f'{player2name} where would you like to go?')
    if inputplace == "a1":
      if board[0] == "-":
        place = 0
        valid = 0
      else:
        print('Spot is already taken. Please choose another one.')
    elif inputplace == "b1":
      if board[1] == "-":
        place = 1
        valid = 0
      else:
        print('Spot is already taken. Please choose another one.')
    elif inputplace == "c1":
      if board[2] == "-":
        place = 2
        valid = 0
      else:
        print('Spot is already taken. Please choose another one.')
    elif inputplace == "a2":
      if board[3] == "-":
        place = 3
        valid = 0
      else:
        print('Spot is already taken. Please choose another one.')
    elif inputplace == "b2":
      if board[4] == "-":
        place = 4
        valid = 0
      else:
        print('Spot is already taken. Please choose another one.')
    elif inputplace == "c2":
      if board[5] == "-":
        place = 5
        valid = 0
      else:
        print('Spot is already taken. Please choose another one.')
    elif inputplace == "a3":
      if board[6] == "-":
        place = 6
        valid = 0
      else:
        print('Spot is already taken. Please choose another one.')
    elif inputplace == "b3":
      if board[7] == "-":
        place = 7
        valid = 0
      else:
        print('Spot is already taken. Please choose another one.')
    elif inputplace == "c3":
      if board[8] == "-":
        place = 8
        valid = 0
      else:
        print('Spot is already taken. Please choose another one.')
    else: print("Invalid command please try again")
def gameover ():
  global board, player1name, player2name, end
  if board[0] == "X" and board[1] == "X" and board[2] == "X":
    print(f'{player1name} has won!')
    end = 1
  if board[3] == "X" and board[4] == "X" and board[5] == "X":
    print(f'{player1name} has won!')
    end = 1
  if board[6] == "X" and board[7] == "X" and board[8] == "X":
    print(f'{player1name} has won!')
    end = 1
  if board[0] == "X" and board[3] == "X" and board[6] == "X":
    print(f'{player1name} has won!')
    end = 1
  if board[1] == "X" and board[4] == "X" and board[7] == "X":
    print(f'{player1name} has won!')
    end = 1
  if board[2] == "X" and board[5] == "X" and board[8] == "X":
    print(f'{player1name} has won!')
    end = 1
  if board[0] == "X" and board[4] == "X" and board[8] == "X":
    print(f'{player1name} has won!')
    end = 1
  if board[2] == "X" and board[4] == "X" and board[6] == "X":
    print(f'{player1name} has won!')
    end = 1

  if board[0] == "O" and board[1] == "O" and board[2] == "O":
    print(f'{player2name} has won!')
    end = 1
  if board[3] == "O" and board[4] == "O" and board[5] == "O":
    print(f'{player2name} has won!')
    end = 1
  if board[6] == "O" and board[7] == "O" and board[8] == "O":
    print(f'{player2name} has won!')
    end = 1
  if board[0] == "O" and board[3] == "O" and board[6] == "O":
    print(f'{player2name} has won!')
    end = 1
  if board[1] == "O" and board[4] == "O" and board[7] == "O":
    print(f'{player2name} has won!')
    end = 1
  if board[2] == "O" and board[5] == "O" and board[8] == "O":
    print(f'{player2name} has won!')
    end = 1
  if board[0] == "O" and board[4] == "O" and board[8] == "O":
    print(f'{player2name} has won!')
    end = 1
  if board[2] == "O" and board[4] == "O" and board[6] == "O":
    print(f'{player2name} has won!')
    end = 1
  if '-' not in board:
    print('You have tied.')
    end = 1
main()
