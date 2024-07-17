import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student
from tests.students.fixture import client_api, courses_factory, students_factory

@pytest.mark.django_db
def test_get_first_course(client, courses_factory, students_factory):
    students = students_factory(_quantity=3)
    courses = courses_factory(_quantity=2)
    response = client.get("/api/v1/courses/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    assert data[0]['name'] == courses[0].name
    assert len(data[0]['students']) == courses[0].students.count()

@pytest.mark.django_db
def test_get_list_courses(client, courses_factory, students_factory):
    courses = courses_factory(_quantity=5)
    students = students_factory(_quantity=10)
    response = client.get("/api/v1/courses/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    list_courses = []
    for course in data:
        list_courses.append(Course(id=course["id"], name=course["name"]))
    assert list_courses == courses

@pytest.mark.django_db
def test_filter_list_courses_id(client, courses_factory):
    courses = courses_factory(_quantity=5)
    second_course_id = courses[1].id
    response = client.get(f"/api/v1/courses/{second_course_id}/")
    assert response.status_code == 200
    filter_course_id = Course.objects.filter(id=second_course_id).exists()
    assert response.json()['id'] == second_course_id
    assert filter_course_id
@pytest.mark.django_db
def test_filter_list_courses_name(client, courses_factory):
    courses = courses_factory(_quantity=5)
    five_course_name = courses[4].name
    response = client.get(f"/api/v1/courses/", {'name': five_course_name})
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['name'] == five_course_name

@pytest.mark.django_db
def test_create_course(client):
    data = {
        "name": "Обучение Django",
    }
    response = client.post("/api/v1/courses/", data)
    assert response.status_code == 201
    assert response.data['name'] == data['name']

@pytest.mark.django_db
def test_update_course(client, courses_factory):
    courses = courses_factory(_quantity=5)
    data = {
        "name": "Обучение Python",
    }
    first_course_id = courses[0].id
    response = client.patch(f"/api/v1/courses/{first_course_id}/", data, content_type='application/json')
    assert response.status_code == 200
    assert response.data['name'] == data['name']

@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    courses = courses_factory(_quantity=3)
    first_course_id = courses[0].id
    response = client.delete(f"/api/v1/courses/{first_course_id}/")
    assert response.status_code == 204
    deleted_course = Course.objects.filter(id=first_course_id).first()
    assert deleted_course is None






