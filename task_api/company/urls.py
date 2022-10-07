from django.urls import path
from . import views

app_name = 'company'
urlpatterns = [
    path('', views.company, name='index'),
    path('department/', views.deps, name='deps'),
    path('department/<int:dep_id>', views.dep_by_id, name='dep_by_id'),
    path('employee/<int:empl_id>', views.empl, name='empl_by_id'),
    path('project/<int:proj_id>', views.proj, name='proj_by_id')
]