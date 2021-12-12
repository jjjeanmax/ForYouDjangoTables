from django.http import HttpResponse
from django_tables2 import SingleTableView
from django.template import Context, loader
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from .forms import UserAuthenticationForm, UserRegistrationForm
from .models import Student, Group, Marks, Disciplines, Professor, Statement
from .tables import StudentsTable, GroupsTable, MarksTable, DisciplinesTable, ProfessorTable, StatementTable


def menu_view(request):
    template = loader.get_template('statement/menu.html')
    return HttpResponse(template.render({'' : ''}, request))


class RegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = "registration/sign_up.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StudentsView(SingleTableView):
    model = Student
    table_class = StudentsTable
    template_name = "statement/statement_template.html"


class GroupsView(SingleTableView):
    model = Group
    table_class = GroupsTable
    template_name = "statement/statement_template.html"


class MarksView(SingleTableView):
    model = Marks
    table_class = MarksTable
    template_name = "statement/statement_template.html"


class DisciplinesView(SingleTableView):
    model = Disciplines
    table_class = DisciplinesTable
    template_name = "statement/statement_template.html"


class ProfessorView(SingleTableView):
    model = Professor
    table_class = ProfessorTable
    template_name = "statement/statement_template.html"


class AuthenticateView(LoginView):
    form_class = UserAuthenticationForm


class StatementView(SingleTableView):
    model = Statement
    table_class = StatementTable
    template_name = "statement/statement_template.html"

