import csv
from datetime import datetime

input_file = "all_students.tsv"
output_file = "all_students_fixed.tsv"

with open(input_file, newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.DictReader(infile, delimiter='\t')
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()

    for row in reader:
        # Convert MM/DD/YYYY to YYYY-MM-DD
        row['birthday'] = datetime.strptime(row['birthday'], "%m/%d/%Y").strftime("%Y-%m-%d")
        writer.writerow(row)

print("✅ Date format fixed in", output_file)
