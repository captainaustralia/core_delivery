import pytest
from django.urls import reverse

from core_delivery.users.models import DefaultUser


@pytest.mark.django_db
class TestCRUDUserCase(object):
    def test_create(self, client):
        data = {
            "email": "physrow@gmail.com",
            "first_name": "Alexander",
            "last_name": "Alekseev",
            "phone": "+79094502061",
            "password": "somethingstrong",
        }

        url = reverse("users-list")

        response = client.post(path=url, data=data, format="json")
        new_object: DefaultUser = DefaultUser.objects.last()
        data.pop("password")

        assert response.status_code == 201, "User must be created"
        assert new_object, "Object must be in db"

        for key, value in data.items():
            assert data[key] == new_object.__getattribute__(key)

    def test_get_list_user(self, client, default_user):
        url = reverse("users-list")

        response = client.get(path=url, format="json")
        response_data = response.json()[0]
        user_obj = DefaultUser.objects.last()

        assert response.status_code == 200, "Get must be return 1 object"
        assert user_obj, "After user factory must be created 1 object"

        for k, v in response_data.items():
            assert str(v) == str(
                default_user.__getattribute__(k)
            ), "All attrs must be eq"

    def test_get_detail_user(self, client, default_user):
        url = reverse("users-detail", args={f"{default_user.uuid}"})

        response = client.get(path=url, format="json")

        assert response.status_code == 200

    def test_delete_user(self, client, default_user):
        url = reverse("users-detail", args={f"{default_user.uuid}"})

        response = client.delete(path=url)

        assert response.status_code == 403, "User must be auth"

    def test_patch_user(self, client, default_user):
        url = reverse("users-detail", args={f"{default_user.uuid}"})

        response = client.patch(path=url, data={"email": "abcd@mail.com"})

        assert response.status_code == 403, "User must be auth"
