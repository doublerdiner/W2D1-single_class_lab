class Team:
    def __init__ (self,name,players,coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = points


    def add_player(self, name):
        self.players.append(name)

    def has_player(self, name):
        result = False
        for player in self.players:
            if player == name:
                result = True
        return result