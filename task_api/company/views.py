from django.views import generic
from company.models import *


class DepartmentsView(generic.ListView):
    template_name = 'company/departments.html'
    model = Department
    context_object_name = 'departments_list'

    def get_queryset(self):
        return Department.objects.all()


class IndexView(generic.ListView):
    template_name = 'company/index.html'
    queryset = ()   # Just to type any queryset


class DepartmentView(generic.DetailView):
    template_name = 'company/department_info.html'
    model = Department


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


