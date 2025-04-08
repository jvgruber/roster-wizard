def parse_input_to_asp(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    with open(output_file, 'w') as outfile:
        for line in lines:
            if not line.strip():
                continue  # skip empty lines

            name_part, days_part = line.strip().split(':')
            name = name_part.strip().lower()
            days = [d.strip() for d in days_part.split(',') if d.strip()]

            outfile.write(f"% {name}\n")
            for day in days:
                outfile.write(f"-available({name}, {day}).\n")
            outfile.write("\n")


if __name__ == '__main__':
    parse_input_to_asp('input.txt', 'asp/off-days.pl')