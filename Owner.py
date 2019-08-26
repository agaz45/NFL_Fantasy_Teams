class Owner:
  def __init__(self, owner, teams):
    self.owner = owner
    self.total = 0
    self.teams = []
    for city, name in teams.items():
      self.teams.append(Team(city, name))

  def setTotal(self):
    for team in self.teams:
      self.total = self.total + team.getPoints()
    return

  def getTotal(self):
    return self.total

  def setRecord(self, name, wins, losses, ties):
    for team in self.teams:
      if team.getName() == name:
        team.setRecord(wins, losses, ties)
        return
    return

  def getTeams(self):
    teamNames = []
    for team in self.teams:
      teamNames.append(team.getName())
    return teamNames

  def printAll(self):
    builtStr = []
    builtStr.append(self.owner)
    builtStr.append(": ")
    builtStr.append(str(self.total))
    builtStr.append("\n")
    for team in self.teams:
      builtStr.append(team.getFullName())
      builtStr.append(" (")
      builtStr.append(team.getRecord())
      builtStr.append(")\n")

    allString = ''.join(builtStr)
    return allString


class Team:
  def __init__(self, city, name):
    self.city = city
    self.name = name
    self.wins = 0
    self.losses = 0
    self.ties = 0

  def getName(self):
    return self.name

  def getFullName(self):
    concatStr = []
    concatStr.append(self.city)
    concatStr.append(" ")
    concatStr.append(self.name)

    
    return ''.join(concatStr)

  def setRecord(self, wins, losses, ties):
    self.wins = wins
    self.losses = losses
    self.ties = ties
    return

  def getRecord(self):
    teamRecord = []
    teamRecord.append(self.wins)
    teamRecord.append("-")
    teamRecord.append(self.losses)

    if self.ties != '0':
      teamRecord.append("-")
      teamRecord.append(self.ties)

    return ''.join(teamRecord)

  def getPoints(self):
    return float(self.wins) + float(self.ties) * 0.5
