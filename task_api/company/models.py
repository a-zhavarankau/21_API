from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'department'

    def __repr__(self):
        return f"{self.name} (id={self.pk})"

    def __str__(self):
        return f"{self.name}"


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    # PLANNED = 'Planned'
    # ONGOING = 'Ongoing'
    # STOPPED = 'Stopped'
    # ROLE_CHOICES = [(PLANNED, 'Planned'), (ONGOING, 'Ongoing'),
    #                 (STOPPED, 'Stopped')]
    # project_status = models.CharField(
    #     max_length=20, choices=ROLE_CHOICES, default=PLANNED)
    project_status = models.CharField(
        max_length=20, choices=[('Planned', 'Planned'), ('Ongoing', 'Ongoing'), ('Stopped', 'Stopped')], default='Planned')

    created_status = models.BooleanField(default=False)
    start_date = models.DateTimeField(blank=True, null=True)
    stop_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'project'

    def __str__(self):
        return f"{self.name} (id={self.pk})"


class Employee(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    DEFAULT = 'Default'
    PM = 'PM'
    ADMINISTRATOR = 'Administrator'
    ROLE_CHOICES = [(DEFAULT, 'Default'), (PM, 'PM'),
                    (ADMINISTRATOR, 'Administrator')]
    employee_role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default=DEFAULT)

    salary = models.PositiveIntegerField(default=0)
    department = models.ForeignKey(Department, to_field='id', on_delete=models.CASCADE)       #, default=None)
    last_login_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    projects = models.ManyToManyField(Project)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return f"{self.name} (id={self.pk})"




"""
CREATE TABLE IF NOT EXISTS department (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    create_date DATE DEFAULT NULL,
    PRIMARY KEY (id)
);


CREATE DATABASE mastery_sql;

USE mastery_sql;

CREATE TABLE IF NOT EXISTS employee (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    login VARCHAR(25) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    employee_role enum('Default','PM','Administrator') NOT NULL,
    salary MEDIUMINT unsigned DEFAULT NULL,
    department INT DEFAULT NULL,
    last_login_date DATE DEFAULT NULL,
    created_date DATE DEFAULT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_employee_department_id FOREIGN KEY (department) REFERENCES department(id)
);


CREATE TABLE IF NOT EXISTS project (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) DEFAULT NULL,
    project_status enum('Planned','Ongoing','Stopped') NOT NULL,
    created_status TINYINT DEFAULT 0,
    start_date DATE DEFAULT NULL,
    stop_date DATE DEFAULT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS empl_proj (
    empl_id INT NOT NULL,
    proj_id INT NOT NULL,
    PRIMARY KEY (empl_id,proj_id),
    CONSTRAINT fk_empl_proj_employee_id FOREIGN KEY (empl_id) REFERENCES employee(id),
    CONSTRAINT fk_empl_proj_project_id FOREIGN KEY (proj_id) REFERENCES project(id)
);
"""

"""
================================================================================
empl_proj = Table(
    "empl_proj",
    Base.metadata,
    Column("empl_id", Integer, ForeignKey("employee.id")),
    Column("proj_id", Integer, ForeignKey("project.id"))
)

class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    create_date = Column(Date)
    employees = relationship("Employee", backref=backref("department_backref"))

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    surname = Column(String(50))
    login = Column(String(25))
    password = Column(String(50))
    email = Column(String(100))
    employee_role = Column(ENUM("Default", "PM", "Administrator"))
    salary = Column(Integer)
    department = Column(Integer, ForeignKey("department.id"))
    last_login_date = Column(Date)
    created_date = Column(Date)
    projects = relationship(
        "Project", secondary=empl_proj, back_populates="employees"
    )


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    project_status = Column(ENUM("Planned", "Ongoing", "Stopped"))
    created_status = Column(Boolean)
    start_date = Column(Date)
    stop_date = Column(Date)
    employees = relationship(
        "Employee", secondary=empl_proj, back_populates="projects"
    )
"""