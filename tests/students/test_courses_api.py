import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture()
def client_api():
    return APIClient()

@pytest.fixture()
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture()
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory

@pytest.mark.django_db
def test_get_first_course(client, courses_factory, students_factory):
    students = students_factory(_quantity=1)
    courses = courses_factory(_quantity=1)
    response = client.get("/api/v1/courses/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)

@pytest.mark.django_db
def test_get_list_courses(client, courses_factory, students_factory):
    students = students_factory(_quantity=10)
    courses = courses_factory(_quantity=5)
    response = client.get("/api/v1/courses/")
    assert response.status_code == 200
    data = response.json()
    assert

@pytest.mark.django_db
def test_filter_list_courses_id(client, courses_factory, students_factory):
    pass

@pytest.mark.django_db
def test_filter_list_courses_name(client, courses_factory, students_factory):
    pass

@pytest.mark.django_db
def test_create_course(client, courses_factory, students_factory):
    pass

@pytest.mark.django_db
def test_update_course(client, courses_factory, students_factory):
    pass

@pytest.mark.django_db
def test_delete_course(client, courses_factory, students_factory):
    pass



