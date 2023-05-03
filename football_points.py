# Create a function that takes the number of wins, draws and losses and
# calculates the number of points a football team has obtained so far.

# Rules: wins get 3 points, draws get 1 point, & losses get 0 points
# Example: football_points(3, 4, 2) ➞ 13

def football_points(wins, draws, losses):
    num_of_wins = wins * 3
    num_of_draws = draws * 1
    num_of_losses = losses * 0
    total_points = num_of_wins + num_of_draws + num_of_losses
    
    print(total_points)
    return total_points

football_points(3, 4, 2)   # 13
football_points(5, 0, 2)   # 15
football_points(0, 0, 1)   # 0
