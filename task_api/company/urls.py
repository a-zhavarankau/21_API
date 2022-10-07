from django.urls import path
from . import views

urlpatterns = [
    path('', views.hellopage),
    path('department/', views.deps),
    path('department/<int:dep_id>', views.dep_by_id),
    path('employee/<int:empl_id>', views.empl),
    path('project/<int:proj_id>', views.proj)
]