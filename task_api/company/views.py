from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from company.models import Department, Employee, Project


def company(request):
    template = 'company/index.html'
    return render(request, template)

def deps(request):
    all_deps = Department.objects.all()
    context = {'departments_list': all_deps, }
    template = 'company/departments.html'
    return render(request, template, context)


def dep_by_id(request, dep_id):
    dep_by_id = get_object_or_404(Department, id=dep_id)
    context = {'department': dep_by_id, }
    template = 'company/department_info.html'
    return render(request, template, context)


def empl(request, empl_id):
    return HttpResponse(f"You want to see info about employee #{empl_id}")

def proj(request, proj_id):
    return HttpResponse(f"You want to see info about project #{proj_id}")