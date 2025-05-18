class Owner:
    def __init__(self, owner: str, teams: dict):
        self.owner = owner
        self.total = 0
        self.weekWins = 0
        self.weekLosses = 0
        self.weekTies = 0
        self.teams = [Team(city, name) for name, city in teams.items()]

    def setTotal(self):
        self.total = sum(team.getPoints() for team in self.teams)

    def getTotal(self):
        return self.total

    def setRecord(self, name: str, wins: int, losses: int, ties: int):
        for team in self.teams:
            if team.getName() == name:
                team.setRecord(wins, losses, ties)
                break

    def getTeams(self):
        return [team.getName() for team in self.teams]

    def setWeekRecord(self, wins: int, losses: int, ties: int):
        self.weekWins = wins
        self.weekLosses = losses
        self.weekTies = ties

    def printAll(self, weekRecords: bool):
        result = [f"{self.owner}: {self.total}"]
        if weekRecords:
            record = f" ({self.weekWins}-{self.weekLosses}"
            if self.weekTies:
                record += f"-{self.weekTies}"
            record += ")"
            result.append(record)

        result.append("\n")
        for team in self.teams:
            result.append(f"- {team.getFullName()} ({team.getRecord()})\n")

        return "".join(result)


class Team:
    def __init__(self, city: str, name: str):
        self.city = city
        self.name = name
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def getName(self):
        return self.name

    def getFullName(self):
        return f"{self.city} {self.name}"

    def setRecord(self, wins, losses, ties):
        self.wins = int(wins)
        self.losses = int(losses)
        self.ties = int(ties)

    def getRecord(self):
        record = f"{self.wins}-{self.losses}"
        if self.ties != 0:
            record += f"-{self.ties}"
        return record

    def getPoints(self):
        return self.wins + self.ties * 0.5
