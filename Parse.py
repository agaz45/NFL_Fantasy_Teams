from bs4 import BeautifulSoup
import requests
import sys

def tableDataText(table):    
    def rowgetDataText(tr, coltag='td'): # td (data) or th (header)       
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]  
    rows = []
    trs = table.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append(rowgetDataText(tr, 'td') ) # data row
    return rows

def main():
    week = int(sys.argv[1])

    req = requests.get("https://www.nfl.com/standings/league/2024/reg/")
    soup = BeautifulSoup(req.content)

    htmlTable = soup.find('table')
    listTable = tableDataText(htmlTable)
    
    fileName = "week" + str(week) + ".txt"

    for row in range(1,33):
        with open(fileName, 'a') as f:
            record = listTable[row][0] + " " + listTable[row][1] + " " + listTable[row][2] + " " + listTable[row][3] + "\n"
            f.write(record)

if __name__ == '__main__':
    main()