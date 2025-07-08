from django import forms
from .models import Student
from .models import StudentNote

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "student_id", "username", "email",
            "first_name", "last_name", "grade",
            "age", "birthday",
        ]
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
        }
        labels = {
            "student_id": "Student ID",
            "first_name": "First Name",
            "last_name": "Last Name",
            "grade": "Grade Level",
            "age": "Age",
            "birthday": "Date of Birth",
        }
class StudentNoteForm(forms.ModelForm):
    class Meta:
        model = StudentNote
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a note...'}),
        }