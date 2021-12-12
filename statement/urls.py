from django.urls import path, re_path, include
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', views.menu_view, name='index'),
    re_path('^students/?$', login_required(views.StudentsView.as_view()),
            name="students_view"),
    re_path('^groups/?$', login_required(views.GroupsView.as_view()),
            name="groups_view"),
    re_path('^marks/?$', login_required(views.MarksView.as_view()),
            name="marks_view"),
    re_path('^disciplines/?$', login_required(views.DisciplinesView.as_view()),
            name="disciplines_view"),
    re_path('^professor/?$', login_required(views.ProfessorView.as_view()),
            name="professor_view"),
    re_path('^statement/?$', login_required(views.StatementView.as_view()),
            name="statement_view"),
    re_path('^login/?$', views.AuthenticateView.as_view(), name="login"),
    re_path('registration/?$', views.RegistrationView.as_view(), name="register"),
]