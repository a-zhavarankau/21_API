from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from company.models import Department, Employee, Project


def hellopage(request):
    all_deps = ", ".join([f"{d.name} (id={d.id})" for d in Department.objects.all()])
    all_empls = ", ".join([f"{e.name} (id={e.id})" for e in Employee.objects.all()])
    all_projs = ", ".join([f"{p.name} (id={p.id})" for p in Project.objects.all()])
    return HttpResponse(f"<h3>Hi there! It's company's main page. <br>Company consists of 3 tables:<h4><li>Department: {all_deps}</li><li>Employee: {all_empls}</li><li>Project: {all_projs}</li></h4></h3>")

def dep(request, dep_id):
    dep_id_info = [f"{k}: {v}" for k, v in Department.objects.values().get(id=dep_id).items()]
    template = loader.get_template('company/department.html')
    context = {'department_info': dep_id_info}
    return HttpResponse(template.render(context, request))

    # return HttpResponse(f"You want to see info about department #{dep_id}:   {dep_id_info}")
    # dep_id_info = ", ".join([str(i) for i in Department.objects.filter(id=dep_id).values()])

def empl(request, empl_id):
    return HttpResponse(f"You want to see info about employee #{empl_id}")

def proj(request, proj_id):
    return HttpResponse(f"You want to see info about project #{proj_id}")