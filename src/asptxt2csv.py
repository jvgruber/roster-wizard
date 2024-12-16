import csv
import sys

def main(input_file, output_file):
    # Read the input data from the file
    with open(input_file, "r") as file:
        input_data = file.read()

    # Parse input into a dictionary
    assignments = input_data.split()
    day_employee_map = {}

    for assignment in assignments:
        employee, day = assignment.strip("assigned()").split(",")
        employee = employee.capitalize()
        day = day.capitalize()
        
        if day not in day_employee_map:
            day_employee_map[day] = []
        day_employee_map[day].append(employee)

    # Prepare CSV data
    csv_data = [("Day", "Employee 1", "Employee 2")]
    for day, employees in sorted(day_employee_map.items()):
        if len(employees) < 2:
            employees.append("")  # Add empty string if less than 2 employees
        csv_data.append((day, employees[0], employees[1]))

    # Write to CSV file
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)

    print(f"CSV file '{output_file}' has been created.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
