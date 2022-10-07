from django.urls import path
from . import views

urlpatterns = [
    path('', views.hellopage),
    path('department/<int:dep_id>', views.dep),
    path('employee/<int:empl_id>', views.empl),
    path('project/<int:proj_id>', views.proj)
]