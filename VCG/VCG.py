from game import Game
from team import Team
import time

# Create a game object
game = Game()

# Display the welcome message
game.welcome()
time.sleep(1)
print("\nPress Enter to continue....")
input()

# Show all players
game.showAllPlayers()
print("\nPress Enter to continue....")
input()

# Select players for teams A and B
game.selectPlayers()
print("\nPress Enter to continue....")
input()

# Display the selected players
game.showTeamPlayers()

print("\nPress Enter to toss......")
input()

# Toss and choose to bat or bowl
game.toss(game.teamA, game.teamB)
print("\nPress Enter to continue......")
input()

# Start the game
game.startMatch()
