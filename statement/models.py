from django.db import models

# Create your models here.


class Group(models.Model):
    FIRST_COURSE = "1"
    SECOND_COURSE = "2"
    THIRD_COURSE = "3"
    FOURTH_COURSE = "4"
    FIFTH_COURSE = "5"
    SIXTH_COURSE = "6"
    YEAR_OF_STUDY = [
        (FIRST_COURSE, "1"),
        (SECOND_COURSE, "2"),
        (THIRD_COURSE, "3"),
        (FOURTH_COURSE, "4"),
        (FIFTH_COURSE,  "5"),
        (SIXTH_COURSE, "6")
    ]
    group_name = models.CharField(max_length=10)
    study_year = models.CharField(max_length=1, choices=YEAR_OF_STUDY, default=FIRST_COURSE)
    training_profile = models.CharField(max_length=255)

    def __str__(self):
        return self.group_name


class Student(models.Model):
    MALE_GENDER = "M"
    FEMALE_GENDER = "F"
    GENDER = [
        (MALE_GENDER, "MALE"),
        (FEMALE_GENDER, "FEMALE")
    ]

    FULL_TIME_FORM_OF_STUDY = "Очная Форма"
    CORRESPONDENCE_FORM_OF_STUDY = "Заочная Форма"
    PART_TIME_FORM_OF_STUDY = "Очно-заочная Форма"
    FORM_OF_STUDY = [
        (FULL_TIME_FORM_OF_STUDY, "ОФ"),
        (CORRESPONDENCE_FORM_OF_STUDY, "ЗФ"),
        (PART_TIME_FORM_OF_STUDY, "ОЗФ")
    ]

    EXPELLED_STATUS_OF_STUDENTS = "Отчислен"
    LEARNER_STATUS_OF_STUDENTS = "Учащийся"
    ACADEMIC_LEAVE_STATUS_OF_STUDENTS = "Академический отпуск"
    STATUS_OF_STUDENTS = [
        (EXPELLED_STATUS_OF_STUDENTS, "Отчислен"),
        (LEARNER_STATUS_OF_STUDENTS, "Учащийся"),
        (ACADEMIC_LEAVE_STATUS_OF_STUDENTS, "Академический отпуск")
    ]

    ENGLISH_BASIS_LEARNING_LANGUAGE = "Английский"
    FRENCH_BASIS_LEARNING_LANGUAGE = "Французкий"
    GERMAN_BASIS_LEARNING_LANGUAGE = "Немецкий"
    BASIS_LEARNING_LANGUAGE = [
        (ENGLISH_BASIS_LEARNING_LANGUAGE,  "Английский язык"),
        (FRENCH_BASIS_LEARNING_LANGUAGE, "Французкий язык"),
        (GERMAN_BASIS_LEARNING_LANGUAGE, "Немецкий язык")
    ]

    book_number = models.CharField(max_length=10, primary_key=True)   # null=True, blank=True
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    citizenship = models.CharField(max_length=24)  # TODO add choice
    gender = models.CharField(max_length=1, choices=GENDER, default=MALE_GENDER)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255, null=True, blank=True)
    study_form = models.CharField(max_length=32, choices=FORM_OF_STUDY, default=FULL_TIME_FORM_OF_STUDY)
    basis_learning_language = models.CharField(max_length=32, choices=BASIS_LEARNING_LANGUAGE, default=ENGLISH_BASIS_LEARNING_LANGUAGE)
    status = models.CharField(max_length=32, choices=STATUS_OF_STUDENTS, default=LEARNER_STATUS_OF_STUDENTS)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_number

class Marks(models.Model): # Todo Database
    Marks_name = models.CharField(max_length=10)


class Disciplines(models.Model): # Todo Database
    Disciplines_name = models.CharField(max_length=10)


class Professor(models.Model): # Todo Database
    Professor_name = models.CharField(max_length=10)


class Statement(models.Model): # Todo Database
    Statement_name = models.CharField(max_length=10)