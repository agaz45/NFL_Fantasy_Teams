import time

from Owner import Owner

# Establish variables
team1 = "team1"
team2 = "team2"
team3 = "team3"
team4 = "team4"
team5 = "team5"
team6 = "team6"
team7 = "team7"
team8 = "team8"
inputFile = "week3.txt"
outputFile = "standings.txt"
  
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
  #You can replace with actuals names
  owners = [team1, team2, team3, team4, team5, team6, team7, team8]

  teamOwners = []
  for x in range(len(teams)):
    teamOwners.append(Owner(owners[x], teams[x]))
  
  return teamOwners

def printResults(owners):
  output = open(outputFile, "w")
  for owner in owners:
    ownerString = owner.printAll()
    print(ownerString, file=output)
  output.close()

def sortOwners(owners):
  #can be optimized from insertion sort. But having such a small n, it is not worth the hassle
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

  input = open(inputFile, "r")
  for x in input:
    stats.append(x)
  input.close()
  
  #Update Teams
  for owner in teams:
    ownerTeams = owner.getTeams()
    for teamName in ownerTeams:
      for teamIndex in range(0, len(stats), 2):
        if(teamName in stats[teamIndex]):
          teamStat = stats[teamIndex+1].split()
          owner.setRecord(teamName, teamStat[0], teamStat[1], teamStat[2])
  
  #Update Total
  for owner in teams:
    owner.setTotal()

  #Sort Owners
  sortOwners(teams)

  #Print to file
  printResults(teams)

if __name__ == '__main__':
  main()

