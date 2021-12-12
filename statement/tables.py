import django_tables2 as tables

from .models import Student, Group, Marks, Disciplines, Professor, Statement


class StudentsTable(tables.Table):
    class Meta:
        model = Student
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id",)


class GroupsTable(tables.Table):
    class Meta:
        model = Group
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id",)


class MarksTable(tables.Table):
    class Meta:
        model = Marks
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id",)
        
        
class DisciplinesTable(tables.Table):
    class Meta:
        model = Disciplines
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id",)
        
        
class ProfessorTable(tables.Table):
    class Meta:
        model = Professor
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id",)
        
        
class StatementTable(tables.Table):
    class Meta:
        model = Statement
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id",)
