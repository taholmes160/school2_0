import csv

input_file = 'students_raw.txt'    # Your CSV input file
output_file = 'students_clean.tsv' # Cleaned output

def clean_field(field):
    return field.strip().strip("('\" )")  # strip spaces, parentheses, quotes

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.reader(infile, delimiter=',')
    writer = csv.writer(outfile, delimiter='\t')
    
    # Write header
    writer.writerow(['student_id', 'username', 'first_name', 'last_name', 'age', 'grade', 'birthday'])
    
    for i, row in enumerate(reader):
        if len(row) < 4:
            continue
        
        student_id = clean_field(row[0])
        username = clean_field(row[1])
        first_name = clean_field(row[2])
        last_name = clean_field(row[3])
        
        # Example logic: Assign age cycling between 17 and 20
        age = 5 + (i % 13)
        # Assign grade according to age (assuming US high school grades)
        grade = 12 if age >= 18 else (age - 4)  # e.g., 17yo=11th grade, 18+=12th grade
        
        # Simple birthday calculation (not exact) for demo:
        birth_year = 2025 - age
        birthday = f"01/01/{birth_year}"
        
        writer.writerow([student_id, username, first_name, last_name, age, grade, birthday])

print(f"Cleaned data saved to {output_file}")
