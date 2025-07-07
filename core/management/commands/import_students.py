import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from core.models import Student

class Command(BaseCommand):
    help = "Import students from a TSV file with ID, student_id, first name, last name, age, grade, birthday"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to the TSV file")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        with open(file_path, newline='', encoding='utf-8') as tsvfile:
            reader = csv.reader(tsvfile, delimiter='\t')

            for row in reader:
                if not row:
                    continue

                try:
                    # Unpack the 7 columns
                    id_str, student_id_str, first_name, last_name, age_str, grade_str, birthday_str = row

                    id = int(id_str.strip().lstrip('('))  # Remove leading '(' if any
                    student_id = student_id_str.strip()
                    username = student_id  # Already like 'stu20240438'
                    email = f"{username}@school.net"
                    first_name = first_name.strip()
                    last_name = last_name.strip()
                    age = int(age_str.strip())
                    grade = int(grade_str.strip())
                    birthday = datetime.strptime(birthday_str.strip(), "%m/%d/%Y").date()

                    Student.objects.update_or_create(
                        id=id,  # lookup by primary key id
                        defaults={
                            'student_id': student_id,
                            'username': username,
                            'email': email,
                            'first_name': first_name,
                            'last_name': last_name,
                            'age': age,
                            'grade': grade,
                            'birthday': birthday,
                        }
                    )

                    self.stdout.write(self.style.SUCCESS(f"Imported {first_name} {last_name}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error processing row {row}: {e}"))
