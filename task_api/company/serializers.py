from rest_framework import serializers
from .models import Department, Project, Employee


class DepartmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    create_date = serializers.DateTimeField(auto_now_add=True)


class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    project_status = serializers.ChoiceField([('Planned', 'Planned'), ('Ongoing', 'Ongoing'), ('Stopped', 'Stopped')], default='Planned')

    # project_status = models.CharField(
    #     max_length=20, choices=[('Planned', 'Planned'), ('Ongoing', 'Ongoing'), ('Stopped', 'Stopped')],
    #     default='Planned')

    created_status = serializers.BooleanField(default=False)
    start_date = serializers.DateTimeField(allow_null=True)
    stop_date = serializers.DateTimeField(allow_null=True)


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    surname = serializers.CharField(max_length=50)
    login = serializers.CharField(max_length=25)
    password = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=100)
    employee_role = serializers.ChoiceField([('Default', 'Default'), ('PM', 'PM'), ('Administrator', 'Administrator')], default='Default')
    # employee_role = models.CharField(
    #     max_length=20, choices=[('Default', 'Default'), ('PM', 'PM'),
    #                             ('Administrator', 'Administrator')], default='Default')

    salary = serializers.IntegerField(default=0)
    department = models.ForeignKey(Department, to_field='id', on_delete=models.CASCADE)  # , default=None)
    last_login_date = serializers.DateTimeField(auto_now=True)
    created_date = serializers.DateTimeField(auto_now_add=True)
    projects = models.ManyToManyField(Project, blank=True)