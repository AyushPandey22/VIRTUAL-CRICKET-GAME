from player import Player

class Team:
    def __init__(self):
        self.totalRunsScored = 0
        self.wicketsLost = 0
        self.totalBallsBowled = 0
        self.name = ''
        self.players = []

    def getBestBowler(self):
            best_bowler = self.players[0]
            for player in self.players:
                if player.wicketsTaken > best_bowler.wicketsTaken:
                    best_bowler = player
            return best_bowler
    
    def addPlayer(self, player):
        self.players.append(player)

    def getBestBatsman(self):
        bestBatsman = None
        for player in self.players:
            if bestBatsman is None or player.runsScored > bestBatsman.runsScored:
                bestBatsman = player
        return bestBatsman
