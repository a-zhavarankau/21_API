from django.contrib import admin
from .models import *


admin.site.register((Department, Project, Employee))
# admin.site.register(Project)
# admin.site.register(Employee)