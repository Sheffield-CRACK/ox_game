__version__ = "0.1.0"

# TODO: Make Python3 compatible

#  We create the grid of the game. 
#  The keys are strings because that's what comes out of the player's input.
#  When the player picks a square we will change the value associated with that key to either 'x' or 'o'.
grid_dic = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# We need to print the grid so that the players will know what numbers correspond to which square
print " ", grid_dic['1'],"|", grid_dic['2'],"|", grid_dic['3']
print "------------"
print " ", grid_dic['4'],"|", grid_dic['5'],"|", grid_dic['6']
print "------------"
print " ", grid_dic['7'],"|", grid_dic['8'],"|", grid_dic['9']

winner = None   # The value of this variable changes when a winning condition is met
player = 'x'    # Currently the first player is always 'x'. TODO: Have the option for 'o' to go first
turn = 0

while winner is None:   # Loop until someone wins
    # increase the turn counter
    turn += 1
    
    #check if we have reached the end of the game
    if turn == 10:
        winner = 'no one'
        break

    # Ask the player to pick a square.
    pick = raw_input(player+" pick a square: ")
    # TODO: What if the square is already taken?
    # TODO: What if they pick a number that is not on the grid?

    # Change the value of the square in the dictionary to either 'x' or 'o' (depending on who's playing).
    grid_dic[pick] = player

    # Print the grid again. TODO: This code is repeated from above, it should be a function
    print " ", grid_dic['1'],"|", grid_dic['2'],"|", grid_dic['3']
    print "------------"
    print " ", grid_dic['4'],"|", grid_dic['5'],"|", grid_dic['6']
    print "------------"
    print " ", grid_dic['7'],"|", grid_dic['8'],"|", grid_dic['9']

    # Here we check our winning condition: 3 squares in a row that have the same value.
    if (grid_dic['1'] == grid_dic['2'] == grid_dic['3']
       or grid_dic['4'] == grid_dic['5'] == grid_dic['6']
       or grid_dic['7'] == grid_dic['8'] == grid_dic['9']
       or grid_dic['1'] == grid_dic['5'] == grid_dic['9']
       or grid_dic['7'] == grid_dic['5'] == grid_dic['3']
       or grid_dic['1'] == grid_dic['4'] == grid_dic['7']
       or grid_dic['2'] == grid_dic['5'] == grid_dic['8']
       or grid_dic['3'] == grid_dic['6'] == grid_dic['9']):
       
       # If the condition is met then our variable 'winner' is changed to the current player.
       # This will break out of the loop on the next pass (as 'winner' is no longer None).
       winner = player

    else:
        # If no winning condition has been met then it's the other player's turn.
        if player is 'x':
            player = 'o'
        else:
            player = 'x'

# Print a congratulatory message to the winner to boost their ego.
print "The winner is ", winner

