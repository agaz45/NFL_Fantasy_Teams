import sys
from Owner import Owner

week = int(sys.argv[1])

# Establish variables
team1 = "team1"
team2 = "team2"
team3 = "team3"
team4 = "team4"
team5 = "team5"
team6 = "team6"
team7 = "team7"
team8 = "team8"
lastWeek = "week" + str(week - 1) + ".txt"
currentWeek = "week" + str(week) +".txt"
outputFile = "standings.txt"

weekRecords = True

def initialSetup():
  teams = [{"Kansas City": "Chiefs", "New York": "Giants", "Atlanta": "Falcons", "Washington": "Football Team"},
           {"Baltimore": "Ravens", "Houston": "Texans", "New England": "Patriots", "Jacksonville": "Jaguars"},
           {"New Orleans": "Saints", "Tennessee": "Titans", "Los Angeles": "Rams", "Carolina": "Panthers"},
           {"San Francisco": "49ers", "Philadelphia": "Eagles", "Cleveland": "Browns", "New York": "Jets"},
           {"Tampa Bay": "Buccaneers", "Green Bay": "Packers", "Arizona": "Cardinals", "Miami": "Dolphins"},
           {"Buffalo": "Bills", "Minnesota": "Vikings", "Denver": "Broncos", "Chicago": "Bears"},
           {"Indianapolis": "Colts", "Pittsburgh": "Steelers", "Los Angeles": "Chargers", "Detroit": "Lions"},
           {"Dallas": "Cowboys", "Seattle": "Seahawks", "Las Vegas": "Raiders", "Cincinnati": "Bengals"},
          ]
  owners = [team1, team2, team3, team4, team5, team6, team7, team8]

  teamOwners = []
  for x in range(len(teams)):
    teamOwners.append(Owner(owners[x], teams[x]))
  
  return teamOwners

def printResults(owners):
  output = open(outputFile, "w")
  for owner in owners:
    ownerString = owner.printAll(weekRecords)
    print(ownerString, file=output)
  output.close()

def sortOwners(owners):
  # Can be optimized from insertion sort. But having such a small n, it is not worth the hassle
  for i in range(len(owners)):
    big = i
    for j in range(i+1, len(owners)):
      if owners[big].getTotal() < owners[j].getTotal():
        big = j
    owners[big], owners[i] = owners[i], owners[big]
  return

def main():
  teams = initialSetup()
  stats = []
  lastWeekStats = []

  input = open(currentWeek, "r")
  for x in input:
    stats.append(x)
  input.close()
  
  if weekRecords:
    input = open(lastWeek, "r")
    for x in input:
      lastWeekStats.append(x)
    input.close()
  
  # Update Teams
  for owner in teams:
    weekWins = 0
    weekLosses = 0
    weekTies = 0

    ownerTeams = owner.getTeams()
    for teamName in ownerTeams:
      teamWins = 0
      teamLosses = 0
      teamTies = 0
      for teamIndex in range(0, len(stats), 2):
        if(teamName in stats[teamIndex]):
          # Update Overall Records
          teamStat = stats[teamIndex+1].split()
          teamWins = teamStat[0]
          teamLosses = teamStat[1]
          teamTies = teamStat[2]
		  
          owner.setRecord(teamName, teamWins, teamLosses, teamTies)
          break
          
      # Update Week Record
      if weekRecords:    
        for teamIndex in range(0, len(lastWeekStats), 2):
          if(teamName in lastWeekStats[teamIndex]):
            teamStat = lastWeekStats[teamIndex+1].split()
          
            if (teamStat[0] != teamWins):
              weekWins = weekWins + 1
            elif (teamStat[1] != teamLosses):
              weekLosses = weekLosses + 1
            elif (teamStat[2] != teamTies):
              weekTies = weekTies + 1
            break
          
    # Set Week Record for owner
    if weekRecords:
      owner.setWeekRecord(weekWins, weekLosses, weekTies)
      
  # Update Total
  for owner in teams:
    owner.setTotal()

  # Sort Owners
  sortOwners(teams)

  # Print to file
  printResults(teams)

if __name__ == '__main__':
  main()

