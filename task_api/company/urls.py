from django.urls import path
from . import views

app_name = 'company'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('departments/', views.DepartmentsView.as_view(), name='deps'),
    path('department/<int:pk>/', views.DepartmentView.as_view(), name='dep_by_id'),
    path('update_department/<int:pk>/', views.UpdateDepartmentView.as_view(), name='update_dep'),
    path('delete_department/<int:pk>/', views.DeleteDepartmentView.as_view(), name='delete_dep'),
    path('employees/', views.EmployeesView.as_view(), name='empls'),
    path('employee/<int:pk>/', views.EmployeeView.as_view(), name='empl_by_id'),
    path('projects/', views.ProjectsView.as_view(), name='projs'),
    path('project/<int:pk>/', views.ProjectView.as_view(), name='proj_by_id'),
    path('create_department/', views.CreateDepartmentView.as_view(), name='create_dep'),
    path('create_employee/', views.CreateEmployeeView.as_view(), name='create_empl'),
    path('create_project/', views.CreateProjectView.as_view(), name='create_proj'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('search_1/', views.search_1, name='search_1'),


]
