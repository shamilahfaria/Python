# complete Rock, Paper, Scissors, v2 in this code cell.

def rps(player1, player2):
  """
  input: player1 & player 2 values
  output: winner or outcome of game
  """
  # case: tie
  if player1 == player2:
    print('It\'s a tie!')

  # case: player 1 == rock
  elif player1 == 'rock':
  # player 2 == paper: player 2 wins
      if player2 == 'paper':
          print('Player 2 won!')
  # player 2 == scissors: player 1 wins
      else:
          print('Player 1 won!')


  # case: player 1 == paper
  elif player1 == 'paper':
  # player 2 == scissors: player 2 wins
      if player2 == 'scissors':
          print('Player 2 won!')
  # player 2 == rock: player 1 wins
      else:
          print('Player 1 won!')


  # case: player 1 == scissors
  else:
  # player 2 == rock: player 2 wins
      if player2 == 'rock':
          print('Player 2 won!')
  # player 2 == paper: player 1 wins
      else :
          print('Player 1 won!')

rps('rock','scissors') # => "Player 1 won!"
rps('paper','paper') # => "It's a tie!"