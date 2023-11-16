from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.response import Response

class MenuTest(TestCase):
    def test_get_items(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Dish1", price=10, inventory=20)
        Menu.objects.create(title="Dish2", price=15, inventory=25)

    def test_get_all_items(self):
        serializer = MenuSerializer(Menu.objects.all())
        return Response(serializer.data)
        