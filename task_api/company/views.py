from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from company.forms import RegisterUserForm
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


class CreateDepartmentView(generic.CreateView):
    model = Department
    fields = '__all__'
    template_name = 'company/create_department.html'
    success_url = reverse_lazy('company:deps')
    extra_context = {"extra": "Many-many-extra-context",
                     'title': 'department',
                     'create_url': "{% url 'company:create_dep' %}"}


class UpdateDepartmentView(generic.UpdateView):
    model = Department
    fields = '__all__'
    # pk_url_kwarg = 'pk'   # ???
    template_name = 'company/update_department.html'
    success_url = reverse_lazy('company:deps')


class DeleteDepartmentView(generic.DeleteView):
    model = Department
    # pk_url_kwarg = 'pk'   # ???
    template_name = 'company/delete_department.html'
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


class CreateEmployeeView(generic.CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'company/create_employee.html'
    success_url = reverse_lazy('company:empls')


class ProjectsView(generic.ListView):
    template_name = 'company/projects.html'
    model = Project
    context_object_name = 'projects_list'

    def get_queryset(self):
        return Project.objects.all()


class ProjectView(generic.DetailView):
    template_name = 'company/project_info.html'
    model = Project


class CreateProjectView(generic.CreateView):
    model = Project
    fields = '__all__'
    template_name = 'company/create_project.html'
    success_url = reverse_lazy('company:projs')


class RegisterUserView(generic.CreateView):
    form_class = RegisterUserForm   # Here UserCreationForm changed with our own new form
    template_name = 'company/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('company:index')


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'company/login.html'

    def get_success_url(self):               # success_url = reverse_lazy('company:index')
        return reverse_lazy('company:index') # doesn't work
    # Instead of the above function we can put the next line in the "settings.py":
    # LOGIN_REDIRECT_URL = "/"


def logout_user(request):
    logout(request)
    return redirect('company:login')


def search_1(request):
    pass
#     search_result =
#
#     query_employees_names_from_department = (
#         session
#             .query((Employee.name + " " + Employee.surname).label("fullname"))
#             .join(Department)
#             .filter(Department.name == dep_name)
#     )
#     context = {'search_result': search_result}
#     return render(request, 'search.html', context)
