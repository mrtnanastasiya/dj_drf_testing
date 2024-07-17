import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture()
def client_api():
    return APIClient()

@pytest.fixture()
def courses_factory(students_factory):
    def factory(*args, **kwargs):
        courses = baker.make(Course, *args, **kwargs)
        for course in courses:
            students = [students_factory() for _ in range(3)]
            course.students.add(*students)
        return courses
    return factory

@pytest.fixture()
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory