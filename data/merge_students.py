import csv

# Input file paths
cleaned_file = "students_clean.tsv"
generated_file = "generated_students.tsv"
output_file = "all_students.tsv"

merged_data = []

# Process students_clean.tsv
with open(cleaned_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        id_ = row['student_id'].replace('stu', '')  # numeric ID
        username = row['username']
        merged_data.append({
            "id": id_,
            "student_id": row['student_id'],
            "username": username,
            "first_name": row['first_name'],
            "last_name": row['last_name'],
            "age": row['age'],
            "grade": row['grade'],
            "birthday": row['birthday'],
            "email": f"{username}@school.net"
        })

# Process generated_students.tsv
with open(generated_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        merged_data.append({
            "id": row['id'],
            "student_id": row['student_id'],
            "username": row['student_id'],  # username = student_id
            "first_name": row['first_name'],
            "last_name": row['last_name'],
            "age": row['age'],
            "grade": row['grade'],
            "birthday": row['birthday'],
            "email": row['email']
        })

# Write combined TSV
with open(output_file, "w", newline='', encoding='utf-8') as f:
    fieldnames = ["id", "student_id", "username", "first_name", "last_name", "age", "grade", "birthday", "email"]
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    writer.writerows(merged_data)

print(f"✅ Merged {len(merged_data)} students into {output_file}")
