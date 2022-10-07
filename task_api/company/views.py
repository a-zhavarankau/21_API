from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from company.models import Department, Employee, Project


def hellopage(request):
    all_deps = ", ".join([f"{d.name} (id={d.id})" for d in Department.objects.all()])
    all_empls = ", ".join([f"{e.name} (id={e.id})" for e in Employee.objects.all()])
    all_projs = ", ".join([f"{p.name} (id={p.id})" for p in Project.objects.all()])
    return HttpResponse(f"<h3>Hi there! It's company's main page. <br>Company consists of 3 tables:<h4><li>Department: {all_deps}</li><li>Employee: {all_empls}</li><li>Project: {all_projs}</li></h4></h3>")

def deps(request):
    # all_deps = ", ".join([f"{d.name} (id={d.id})" for d in Department.objects.all()])
    all_deps = Department.objects.all()
    context = {'departments_list': all_deps, }
    template = 'company/departments.html'
    return render(request, template, context)


def dep_by_id(request, dep_id):
    try:
        dep_id_values = Department.objects.values().get(id=dep_id)
        dep_id_info_list = [f"{k}: {v}" for k, v in dep_id_values.items()]
    except Department.DoesNotExist:
        raise Http404("Department does not exist")
    else:
        context = {'department_info': dep_id_info_list, }
    template = 'company/department_info.html'
    return render(request, template, context)


# return HttpResponse(f"You want to see info about department #{dep_id}:   {dep_id_info}")
    # dep_id_info = ", ".join([str(i) for i in Department.objects.filter(id=dep_id).values()])

def empl(request, empl_id):
    return HttpResponse(f"You want to see info about employee #{empl_id}")

def proj(request, proj_id):
    return HttpResponse(f"You want to see info about project #{proj_id}")