import pytest
from django.urls import reverse
from rest_framework import status

from users_app.models import Users
from users_app.serializers import UserSerializer


@pytest.mark.django_db
def test_list_users(client):
    """
        Ensure we can list all users.
        :param client:
        :return: list of users
    """
    # create a couple of users
    u1 = Users.objects.create(email="test2@test.com")
    u2 = Users.objects.create(email="test3@test.com")
    u1.save()
    u2.save()

    url = reverse('users-list')
    response = client.get(url)

    users = Users.objects.all()
    expected_data = UserSerializer(users, many=True).data

    # assertions
    assert response.status_code == status.HTTP_200_OK
    assert Users.objects.count() == 2
    assert response.data['results'] == expected_data


@pytest.mark.django_db
def test_create_user(client):
    """
        Ensure we can create a new user object.
        :param client:
        :return: status code 201
    """
    url = reverse('users-list')
    data = {
        "email": "new_user@creation.gmail.com"
    }
    response = client.post(url, data=data, format='json')

    # assertions
    assert response.status_code == status.HTTP_201_CREATED
    assert Users.objects.count() == 1
    assert Users.objects.get().email == 'new_user@creation.gmail.com'
