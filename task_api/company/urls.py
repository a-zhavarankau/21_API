from django.urls import path
from . import views

app_name = 'company'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('department/', views.DepartmentsView.as_view(), name='deps'),
    path('department/<int:pk>', views.DepartmentView.as_view(), name='dep_by_id'),
    path('employee/', views.EmployeesView.as_view(), name='empls'),
    path('employee/<int:pk>', views.EmployeeView.as_view(), name='empl_by_id'),
    path('project/', views.ProjectsView.as_view(), name='projs'),
    path('project/<int:pk>', views.ProjectView.as_view(), name='proj_by_id'),
]
