import sys
import json
from Owner import Owner

def get_week_files(week, owners_file):
    output_file = "standings_fam.txt" if "fam" in owners_file else "standings.txt"
    return f"week{week - 1}.txt", f"week{week}.txt", output_file

def load_owners_and_teams(filename="owners.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return data["owners"]

def initial_setup(owner_data):
    owners = []
    for owner_entry in owner_data:
        name = owner_entry["name"]
        teams = owner_entry["teams"]
        owners.append(Owner(name, teams))
    return owners

def read_file_lines(filename):
    with open(filename, "r") as f:
        return f.readlines()

def update_owners(owners, current_stats, last_stats=None):
    for owner in owners:
        week_wins = week_losses = week_ties = 0

        for team_name in owner.getTeams():
            current_record = next(
                (line.split()[-3:] for line in current_stats if team_name in line),
                None
            )
            if current_record:
                wins, losses, ties = current_record
                owner.setRecord(team_name, wins, losses, ties)

            if last_stats:
                previous_record = next(
                    (line.split()[-3:] for line in last_stats if team_name in line),
                    None
                )
                if previous_record and current_record:
                    if previous_record[0] != current_record[0]:
                        week_wins += 1
                    elif previous_record[1] != current_record[1]:
                        week_losses += 1
                    elif previous_record[2] != current_record[2]:
                        week_ties += 1

        if last_stats:
            owner.setWeekRecord(week_wins, week_losses, week_ties)

def sort_owners(owners):
    owners.sort(key=lambda o: o.getTotal(), reverse=True)

def write_standings(owners, filename, show_week_records=True):
    with open(filename, "w") as f:
        for owner in owners:
            f.write(owner.printAll(show_week_records))

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <week_number> [owners_json_file]")
        sys.exit(1)

    week = int(sys.argv[1])
    owners_json = sys.argv[2] if len(sys.argv) > 2 else "owners.json"

    last_week_file, current_week_file, output_file = get_week_files(week, owners_json)

    owner_data = load_owners_and_teams(owners_json)
    owners = initial_setup(owner_data)
    current_stats = read_file_lines(current_week_file)
    last_stats = read_file_lines(last_week_file) if week > 1 else None

    update_owners(owners, current_stats, last_stats)

    for owner in owners:
        owner.setTotal()

    sort_owners(owners)
    write_standings(owners, output_file, show_week_records=(week > 1))

if __name__ == '__main__':
    main()
