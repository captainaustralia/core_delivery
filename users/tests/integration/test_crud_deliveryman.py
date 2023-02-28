from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from core_delivery.factories import DefaultUserFactory
from core_delivery.users.models import DeliveryMan


class TestApi(APITestCase):
    databases = ("default",)

    def setUp(self):
        self.url = reverse("deliveryman-list")
        self.user = DefaultUserFactory()
        self.client.force_authenticate(user=self.user)

    def test_create_deliveryman(self):
        response = self.client.post(path=self.url, data={}, format="json")

        delivery_man_obj = DeliveryMan.objects.last()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.user, delivery_man_obj.user)
