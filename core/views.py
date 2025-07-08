from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Student
from django.shortcuts import get_object_or_404, redirect
from .forms import StudentForm, StudentNoteForm
from django.contrib.auth.decorators import login_required

def student_list(request):
    search_query = request.GET.get("q", "").strip()
    sort_by = request.GET.get("sort", "last_name")
    order = request.GET.get("order", "asc")
    page = request.GET.get("page", 1)

    # Base queryset
    students = Student.objects.all()

    # Search logic
    if search_query:
        terms = search_query.split()
        base_filter = (
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(username__icontains=search_query)
        )

        if len(terms) >= 2:
            first_term, second_term = terms[0], terms[1]
            full_name_filter = (
                Q(first_name__icontains=first_term, last_name__icontains=second_term) |
                Q(first_name__icontains=second_term, last_name__icontains=first_term)
            )
            base_filter |= full_name_filter

        students = students.filter(base_filter)

    # Sorting
    if sort_by not in ["student_id", "username", "first_name", "last_name", "grade", "age", "birthday", "email"]:
        sort_by = "last_name"
    if order == "desc":
        sort_by = "-" + sort_by

    students = students.order_by(sort_by)

    # Pagination
    paginator = Paginator(students, 20)
    page_obj = paginator.get_page(page)

    return render(request, "core/student_list.html", {
        "page_obj": page_obj,
        "search_query": search_query,
        "sort_by": sort_by.lstrip('-'),
        "order": "desc" if sort_by.startswith('-') else "asc",

    })


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'core/student_form.html', {'form': form, 'student': None})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/student_form.html', {'form': form, 'student': student})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return render(request, "core/student_confirm_delete.html", {"student": student})

def home(request):
    return render(request, 'core/home.html')



@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    notes = student.notes.all()

    if request.method == 'POST':
        form = StudentNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.student = student
            note.author = request.user
            note.save()
            return redirect('student_detail', pk=pk)
    else:
        form = StudentNoteForm()

    return render(request, 'core/student_detail.html', {
        'student': student,
        'notes': notes,
        'form': form,
    })



