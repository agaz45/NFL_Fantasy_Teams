import time
from selenium import webdriver

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
outputFile = "standings.txt"
cDriverLoc = "./chromedriver"
  
def initialSetup():
  teams = [{"Jacksonville": "Jaguars", "Los Angeles": "Chargers", "Denver": "Broncos", "Miami": "Dolphins"},
           {"New Orleans": "Saints", "Atlanta": "Falcons", "Oakland": "Raiders", "Chicago": "Bears"},
           {"New Englands": "Patriots", "Baltimore": "Ravens", "San Francisco": "49ers", "Cleveland": "Browns"},
           {"Los Angeles": "Rams", "Kansas City": "Chiefs", "New York": "Giants", "Arizona": "Cardinals"},
           {"Minnesota": "Vikings", "Carolina": "Panthers", "Detroit": "Lions", "Buffalo": "Bills"},
           {"Cincinnati": "Bengals", "Green Bay": "Packers", "Indianapolis": "Colts", "Tampa Bay": "Buccaneers"},
           {"Philadelphia": "Eagles", "Dallas": "Cowboys", "Seattle": "Seahawks", "Washington": "Redskins"},
           {"Pittsburgh": "Steelers", "Houston": "Texans", "Tennessee": "Titans", "New York": "Jets"},
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

  #Use whatever folder your chromedriver is in
  driver = webdriver.Chrome(cDriverLoc)
  driver.get("https://www.foxsports.com/nfl/standings")
  tableResults = driver.find_element_by_css_selector("table.wisbb_standardTable")

  #Update Teams
  for owner in teams:
    ownerTeams = owner.getTeams()
    for teamName in ownerTeams:
      teamStats = tableResults.find_element_by_xpath("//span[contains(text(), '%s')]" % teamName).find_elements_by_xpath('../../../td')
      owner.setRecord(teamName, teamStats[1].text, teamStats[2].text, teamStats[3].text)
      
  driver.quit()
  
  #Update Total
  for owner in teams:
    owner.setTotal()

  #Sort Owners
  sortOwners(teams)

  #Print to file
  printResults(teams)

if __name__ == '__main__':
  main()

