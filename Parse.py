import sys
import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_table_data(table):
    def extract_row(tr, tag='td'):
        return [td.get_text(strip=True) for td in tr.find_all(tag)]

    rows = []
    trs = table.find_all('tr')
    if trs:
        header = extract_row(trs[0], 'th')
        if header:
            rows.append(header)
            trs = trs[1:]

        for tr in trs:
            rows.append(extract_row(tr))
    return rows

def fetch_standings(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        logger.error(f"Error fetching standings: {e}")
        sys.exit(1)

def write_week_data(filename, data):
    try:
        with open(filename, 'w') as f:
            for row in data[1:33]:  # Skip header and limit to 32 teams
                record = f"{row[0]} {row[1]} {row[2]} {row[3]}\n"
                f.write(record)
        logger.info(f"Data written to {filename}")
    except Exception as e:
        logger.error(f"Error writing to file: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        logger.error("Usage: python parse.py <week_number>")
        sys.exit(1)

    week = int(sys.argv[1])
    url = "https://www.nfl.com/standings/league/2024/reg/"
    html = fetch_standings(url)

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')

    if not table:
        logger.error("No table found on the page.")
        sys.exit(1)

    standings = extract_table_data(table)
    write_week_data(f"week{week}.txt", standings)

if __name__ == '__main__':
    main()
