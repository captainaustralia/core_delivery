import pytest
from django.urls import reverse

from core_delivery.users.models import DefaultUser

data = {
    "email": "physrow@gmail.com",
    "first_name": "Alexander",
    "last_name": "Alekseev",
    "phone": "+79094502061",
    "password": "somethingstrong"
}


@pytest.mark.django_db
class TestCRUDUserCase(object):

    def test_create(self, client):
        url = reverse("users-list")

        response = client.post(path=url,
                               data=data,
                               format="json")
        new_object: DefaultUser = DefaultUser.objects.last()
        data.pop("password")

        assert response.status_code == 201
        assert new_object

        for key, value in data.items():
            assert data[key] == new_object.__getattribute__(key)

    def test_get_list_user(self, client, default_user):
        url = reverse("users-list")

        response = client.get(
            path=url,
            format="json"
        )
        response_data = response.json()[0]
        user_obj = DefaultUser.objects.last()

        assert response.status_code == 200
        assert user_obj

        for k, v in response_data.items():
            assert str(v) == str(default_user.__getattribute__(k))

    def test_get_detail_user(self, client, default_user):
        url = reverse("users-detail", args={f"{default_user.uuid}"})

        response = client.get(path=url, format="json")

        assert response.status_code == 200

    def test_delete_user(self, client, default_user):
        url = reverse("users-detail", args={f"{default_user.uuid}"})

        response = client.delete(path=url)

        assert response.status_code == 403

    def test_patch_user(self, client, default_user):
        url = reverse("users-detail", args={f"{default_user.uuid}"})

        response = client.patch(path=url, data={"email": "abcd@mail.com"})

        assert response.status_code == 403
