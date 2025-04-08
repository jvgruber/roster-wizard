import re
import csv
import argparse
from collections import defaultdict

# Argument-Parser für Command-Line Optionen
parser = argparse.ArgumentParser(description="Convert ASP assignments to CSV.")
parser.add_argument("--show_date", dest="show_date", action="store_true", default=True,
                    help="Include date column in output CSV (default: True)")
parser.add_argument("--no-show_date", dest="show_date", action="store_false",
                    help="Exclude date column in output CSV")
args = parser.parse_args()

# Datei einlesen
with open("asp-answer.txt", "r") as file:
    content = file.read()

# "assigned(person,day)" Einträge extrahieren
assignments = re.findall(r'assigned\((\w+),d(\d+)\)', content)

# Personen pro Tag sammeln
day_to_people = defaultdict(list)
max_day = 0

for person, day in assignments:
    day_num = int(day)
    day_to_people[day_num].append(person)
    max_day = max(max_day, day_num)

# CSV schreiben
with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Header schreiben
    if args.show_date:
        writer.writerow(["date", "person1", "person2"])
    else:
        writer.writerow(["person1", "person2"])

    # Zeilen schreiben
    for day in range(1, max_day + 1):
        people = day_to_people.get(day, [])
        row = []

        if args.show_date:
            row.append(str(day))

        if len(people) == 2:
            row.extend(people)
        elif len(people) == 1:
            row.extend([people[0], ""])
        else:
            row.extend(["", ""])

        writer.writerow(row)
