# complete game of rock, paper, scissors


# player 1 and player 2 values
player1 = 'scissors'
player2 = 'scissors'

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
   