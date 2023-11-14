# tests/test_example.py
from django.test import TestCase
from yourapp.models import YourModel

class YourModelTests(TestCase):
    def test_something(self):
        # Your test code here
        obj = YourModel.objects.create(name='example')
        self.assertEqual(obj.name, 'example')
