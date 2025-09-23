from django.shortcuts import render, get_object_or_404
from .models import Department, Speciality, Home


def home(request):
    home_content = Home.objects.first()
    return render(request, "home.html", {"home": home_content})

def specialities_list(request):
    specialities = Speciality.objects.all()
    return render(request, "speciality_list.html", {"specialities": specialities})

def specialities_detail(request, id):
    specialities_content = get_object_or_404(Speciality, id = id)
    disciplines = specialities_content.disciplines.all()
    return render(request, "speciality_detail.html", {"specialities_content": specialities_content, "disciplines": disciplines})

def department_list(request):
    departments = Department.objects.all()
    return render(request, "department_list.html", {"department_list": departments})

def department_detail(request, id):
    departments_detail = get_object_or_404(Department, id = id)
    professors = departments_detail.professors.all()
    specialities = departments_detail.specialities.all()
    return render(request, "department_detail.html", {"departments_detail": departments_detail, "professors": professors, "specialities": specialities})

