# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"

def rps(p1, p2):
    
    if len(p1) - len(p2) == 3 or len(p1) - len(p2) == 1 or len(p1) - len(p2) == -4:
        return "Player 1 won!"
    else:
        return "Player 2 won!" if len(p2) != len(p1) else "Draw!"


print(rps("scissors", "rock"))