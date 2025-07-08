import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from core.models import Student  # Adjust to your actual app/model

class Command(BaseCommand):
    help = 'Import students from a TSV file'

    def add_arguments(self, parser):
        parser.add_argument('tsv_file', type=str)

    def handle(self, *args, **kwargs):
        tsv_file = kwargs['tsv_file']
        with open(tsv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='\t')
            for row in reader:
                try:
                    if len(row) != 8:
                        raise ValueError(f"Expected 8 values, got {len(row)}")

                    legacy_id, student_id, first_name, last_name, age, grade, birthday, email = row

                    # Clean and parse values
                    age = int(age)
                    grade = int(grade)
                    birthday_date = datetime.strptime(birthday, "%m/%d/%Y").date()

                    # Check if student already exists
                    if Student.objects.filter(username=student_id).exists():
                        self.stdout.write(self.style.WARNING(f"Skipped duplicate username: {student_id}"))
                        continue

                    student = Student.objects.create(
                        username=student_id,
                        first_name=first_name.strip(),
                        last_name=last_name.strip(),
                        age=age,
                        grade=grade,
                        birthday=birthday_date,
                        email=email.strip(),
                    )
                    self.stdout.write(self.style.SUCCESS(f"Imported student {student_id}"))

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error processing row {row}: {e}"))
