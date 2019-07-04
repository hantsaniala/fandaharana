from django.test import TestCase
from django.urls import reverse, resolve

from .views import home


class TestHome(TestCase):
    def test_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_resolve_view(self):
        view = resolve('/')
        self.assertEqual(view.func, home)
