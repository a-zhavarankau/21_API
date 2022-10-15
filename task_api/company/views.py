from django.views import generic
from django.urls import reverse_lazy
# from company.forms import DepartmentForm
from company.models import *
from django.shortcuts import render, redirect


class IndexView(generic.ListView):
    template_name = 'company/index.html'
    queryset = ()   # Just to type any queryset


class DepartmentsView(generic.ListView):
    template_name = 'company/departments.html'
    model = Department
    context_object_name = 'departments_list'

    def get_queryset(self):
        return Department.objects.all()


class DepartmentView(generic.DetailView):
    template_name = 'company/department_info.html'
    model = Department


# class CreateDepartmentView(generic.CreateView):
#     queryset = ()

# def CreateDepartment(request):
#     error = ''
#     if request.method == 'POST':
#         form = DepartmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/department/")
#         else:
#             error = 'Invalid input data'
#
#     form = DepartmentForm()
#     context = {'form': form, 'error': error}
#     return render(request, 'company/create_department.html', context)


class CreateNewDepartmentView(generic.CreateView):
    model = Department
    fields = '__all__'
    template_name = 'company/create_new_department.html'
    success_url = reverse_lazy('company:deps')


class EmployeesView(generic.ListView):
    template_name = 'company/employees.html'
    model = Employee
    context_object_name = 'employees_list'

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeView(generic.DetailView):
    template_name = 'company/employee_info.html'
    model = Employee


class ProjectsView(generic.ListView):
    template_name = 'company/projects.html'
    model = Project
    context_object_name = 'projects_list'

    def get_queryset(self):
        return Project.objects.all()


class ProjectView(generic.DetailView):
    template_name = 'company/project_info.html'
    model = Project


