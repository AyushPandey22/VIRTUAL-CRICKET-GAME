# Import the Team class if it hasn't been imported already
from player import Player
from team import Team
import random
import time

# Define the Game class
class Game:
    def __init__(self):
        self.playersPerTeam = 4
        self.maxBalls = 6
        self.totalPlayers = 11

        self.players = ["Virat", "Rohit", "Dhawan", "Pant", "Karthik", "KLRahul",
                        "Jadeja", "Hardik", "Bumrah", "BKumar", "Ishant"]

        self.isFirstInnings = False
        self.teamA = Team()
        self.teamB = Team()
        self.teamA.name = "Team-A"
        self.teamB.name = "Team-B"
        self.batsman = None
        self.bowler = None


    def welcome(self):
        print("")
        print("")
        print("\t\t---------------------------------------\t")
        print("\t\t|============== CRIC-IN ==============|\t")
        print("\t\t|-------------------------------------|\t")
        print("\t\t|   Welcome to Virtual Cricket Game   |\t")
        print("\t\t---------------------------------------\t")

        time.sleep(1)
        print("")
        print("\t----------------------------------------------------\t")
        print("\t|================== Instructions ==================|\t")
        print("\t----------------------------------------------------\t")
        print("\t|--------------------------------------------------|\t")
        print("\t| 1. Create 2 teams (Team-A and Team-B with 4      |\t")
        print("\t|    players each) from a given pool of 11 players.|\t")
        print("\t| 2. Lead the toss and decide the choice of play.  |\t")
        print("\t| 3. Each innings will be of 6 balls.              |\t")
        print("\t|--------------------------------------------------|\t")
        print("\t----------------------------------------------------\t")

    def showAllPlayers(self):
        print("\t\t---------------------------------------\t")
        print("\t\t|========== Pool of Players ==========|\t")
        print("\t\t---------------------------------------\t")
        time.sleep(0.1)

        for i in range(self.totalPlayers):
            time.sleep(0.1)
            print("\t[" + str(i) + "] " + self.players[i])

    def takeIntegerInput(self):
        while True:
            try:
                n = int(input())
                return n
            except ValueError:
                print("Invalid input! Please try again with valid input: ")
                continue

    def validateSelectedPlayer(self, index):
        players = self.teamA.players
        n = len(players)
        for i in range(n):
            if players[i].id == index:
                return False

        players = self.teamB.players
        n = len(players)
        for i in range(n):
            if players[i].id == index:
                return False

        return True
    
    def selectPlayers(self):
        print("\t\t------------------------------------------------\t")
        print("\t\t|========== Create Team-A and Team-B ==========|\t")
        print("\t\t------------------------------------------------\t")

        print("")
        time.sleep(0.1)
        print("------------------------------------------------\t")
        for i in range(self.playersPerTeam):
        # Add player to team A
            while True:
                print("\nSelect player", i + 1, "of Team A - ", end="")
                playerIndexTeamA = self.takeIntegerInput()

                if playerIndexTeamA < 0 or playerIndexTeamA > 10:
                    print("\nPlease select from the given players")
                elif not self.validateSelectedPlayer(playerIndexTeamA):
                    print("\nPlayer has already been selected. Please select other player")
                else:
                    teamAPlayer = Player()
                    teamAPlayer.id = playerIndexTeamA
                    teamAPlayer.name = self.players[playerIndexTeamA]
                    self.teamA.players.append(teamAPlayer)
                    break

            # Add player to team B
            while True:
                print("\nSelect player", i + 1, "of Team B - ", end="")
                playerIndexTeamB = self.takeIntegerInput()

                if playerIndexTeamB < 0 or playerIndexTeamB > 10:
                    print("\nPlease select from the given players")
                elif not self.validateSelectedPlayer(playerIndexTeamB):
                    print("\nPlayer has already been selected. Please select other player")
                else:
                    teamBPlayer = Player()
                    teamBPlayer.id = playerIndexTeamB
                    teamBPlayer.name = self.players[playerIndexTeamB]
                    self.teamB.players.append(teamBPlayer)
                    break
        print("------------------------------------------------\t")
    
    def showTeamPlayers(self):
        teamAPlayers = self.teamA.players
        teamBPlayers = self.teamB.players

        time.sleep(1)

        print("\t--------------------------\t\t--------------------------\t")
        print("\t|=======  Team-A  =======|\t\t|=======  Team-B  =======|\t")
        print("\t--------------------------\t\t--------------------------\t")

        for i in range(self.playersPerTeam):
            time.sleep(0.1)
            print("\t|\t" + "[" + str(i) + "] " + teamAPlayers[i].name + "\t |" +
                "\t\t" +
                "|\t" + "[" + str(i) + "] " + teamBPlayers[i].name + "\t |")
        print("\t--------------------------\t\t--------------------------\n\n")

    def toss(self, teamA, teamB):
        print("\t\t----------------------------------\t")
        print("\t\t|========== Let's Toss ==========|\t")
        print("\t\t----------------------------------\t")
        print("Tossing the coin...\n")
        time.sleep(2)

        randomValue = random.randint(0, 1)  # 0 or 1
        if randomValue == 0:
            time.sleep(0.2)
            print("Team-A won the toss\n")
            self.tossChoice(teamA)
        else:
            time.sleep(0.2)
            print("Team-B won the toss\n")
            self.tossChoice(teamB)
            
    def tossChoice(self, tossWinnerTeam):
        time.sleep(0.5)
        print("what would you like to do?")
        time.sleep(1)

        while True:
            time.sleep(0.2)
            print("")
            print("Enter 1 to bat or 2 to bowl first.")
            print("1. Bat")
            print("2. Bowl")

            tossInput = self.takeIntegerInput()

            if tossInput == 1:
                time.sleep(0.1)
                print("\n" + tossWinnerTeam.name + " won the toss and elected to bat first.\n")
                if tossWinnerTeam == self.teamA:
                    self.teamA.isBatting = True
                else:
                    self.teamB.isBatting = True
                break
            elif tossInput == 2:
                time.sleep(0.1)
                print("\n" + tossWinnerTeam.name + " won the toss and elected to bowl first.\n")
                if tossWinnerTeam == self.teamA:
                    self.teamB.isBatting = True
                else:
                    self.teamA.isBatting = True
                break
            else:
                print("\nInvalid input! Please enter a valid choice.")

    def startMatch(self):
        print("\t\t========================================\t")
        print("\t\t||| CRICKET MATCH BETWEEN TEAM A & B |||\t")
        print("\t\t========================================\t\n")
        self.startFirstInnings()
        self.startSecondInnings()


    def startFirstInnings(self):
        time.sleep(1)
        print("\t\t\t==========================\t")
        print("\t\t\t||| 1st INNINGS STARTS |||\t")
        print("\t\t\t==========================\t\n")
        self.isFirstInnings = True
        self.initializePlayers()
        self.playInnings()

    def startSecondInnings(self):
        time.sleep(1)
        print("\t\t\t==========================\t")
        print("\t\t\t||| 2nd INNINGS STARTS |||\t")
        print("\t\t\t==========================\t\n")
        self.isFirstInnings = False
        self.initializePlayers()
        self.playInnings()
    
    def initializePlayers(self):
        # Choose batsman and bowler: Initialize self.batsman and self.bowler
        if self.isFirstInnings:
            self.battingTeam = self.teamA
            self.bowlingTeam = self.teamB
        else:
            self.battingTeam = self.teamB
            self.bowlingTeam = self.teamA

        self.batsman = self.battingTeam.players[0]
        self.bowler = self.bowlingTeam.players[0]
        print(self.battingTeam.name + " - " + self.batsman.name + " is batting\n")
        print(self.bowlingTeam.name + " - " + self.bowler.name + " is bowling\n")
        
    def playInnings(self):
        for i in range(self.maxBalls):
            time.sleep(0.4)
            input("Press Enter to bowl...")
            time.sleep(0.5)
            print("Bowling.....\n")
            time.sleep(0.5)

            self.bat()

            if not self.validateInningsScore():
                break
                
    def bat(self):
        runsScored = random.randint(0,6)

        # Update batting team and batsman score
        self.batsman.runsScored += runsScored
        self.battingTeam.totalRunsScored += runsScored
        self.batsman.ballsPlayed += 1

        # Update bowling team and bowler score
        self.bowler.ballsBowled += 1
        self.bowlingTeam.totalBallsBowled += 1
        self.bowler.runsGiven += runsScored

        if runsScored != 0: # if runsScored = 1, 2, 3, 4, 5, or 6
            print(f"\t\n{self.bowler.name} to {self.batsman.name} {runsScored} runs!")
            self.showGameScorecard()
        else: # else runScored = 0 and the batsman is ‘OUT’
            print(f"\t\n{self.bowler.name} to {self.batsman.name} OUT!")

            self.battingTeam.wicketsLost += 1
            self.bowler.wicketsTaken += 1

            self.showGameScorecard()

            nextPlayerIndex = self.battingTeam.wicketsLost
            self.batsman = self.battingTeam.players[nextPlayerIndex]
            
    def validateInningsScore(self):
        if self.isFirstInnings:
            if self.battingTeam.wicketsLost == self.playersPerTeam or self.bowlingTeam.totalBallsBowled == self.maxBalls:
                time.sleep(0.5)
                print("\t\t\t==========================\t")
                print("\t\t\t||| FIRST INNINGS ENDS |||\t")
                print("\t\t\t==========================\t")
                time.sleep(1)
                print(f"{self.battingTeam.name} {self.battingTeam.totalRunsScored} - {self.battingTeam.wicketsLost} ({self.bowlingTeam.totalBallsBowled})")
                print(f"{self.bowlingTeam.name} needs {self.battingTeam.totalRunsScored + 1} runs to win the match \n")
                return False
        else: # Else 2nd innings
            if self.battingTeam.totalRunsScored > self.bowlingTeam.totalRunsScored:
                time.sleep(0.5)
                input("Press Enter for Result")
                print("\t\t\t==================\t")
                print("\t\t\t||| MATCH ENDS |||\t")
                print("\t\t\t==================\t")
                time.sleep(1)
                print(f"{self.battingTeam.name} {self.battingTeam.totalRunsScored} - {self.battingTeam.wicketsLost} ({self.bowlingTeam.totalBallsBowled})")
                print(f"{self.battingTeam.name} won the match by {self.playersPerTeam - self.battingTeam.wicketsLost} wickets\n")
                return False
            
            elif self.battingTeam.totalRunsScored == self.bowlingTeam.totalRunsScored:
                time.sleep(0.5)
                input("Press Enter for Result")
                print("\t\t\t==================\t")
                print("\t\t\t||| MATCH ENDS |||\t")
                print("\t\t\t==================\t")
                time.sleep(1)
                print(f"{self.battingTeam.name} {self.battingTeam.totalRunsScored} - {self.battingTeam.wicketsLost} ({self.bowlingTeam.totalBallsBowled})")
                print("Match tied!\n")
                return False
            
            elif self.battingTeam.wicketsLost == self.playersPerTeam or self.bowlingTeam.totalBallsBowled == self.maxBalls:
                time.sleep(0.5)
                input("Press Enter for Result")
                print("\t\t\t==================\t")
                print("\t\t\t||| MATCH ENDS |||\t")
                print("\t\t\t==================\t")
                time.sleep(1)
                print(f"{self.battingTeam.name} {self.battingTeam.totalRunsScored} - {self.battingTeam.wicketsLost} ({self.bowlingTeam.totalBallsBowled})")
                print(f"{self.bowlingTeam.name} won the match by {self.battingTeam.totalRunsScored - self.bowlingTeam.totalRunsScored} runs\n")
                return False
            pass
        return True
    
    def showGameScorecard(self):
        time.sleep(0.5)
        print("--------------------------------------------------------------------------")
        print("\t{} {} - {} ({}) | {} {} ({}) \t{} {} - {} - {}".format(
            self.battingTeam.name, self.battingTeam.totalRunsScored, self.battingTeam.wicketsLost,
            self.bowlingTeam.totalBallsBowled, self.batsman.name, self.batsman.runsScored,
            self.batsman.ballsPlayed, self.bowler.name, self.bowler.ballsBowled,
            self.bowler.runsGiven, self.bowler.wicketsTaken))
        print("--------------------------------------------------------------------------\n")
