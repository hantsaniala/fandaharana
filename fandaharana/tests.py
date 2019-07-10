from django.test import TestCase
from django.urls import reverse, resolve

from .views import home, month  #: 16, 39
from .models import Person, Public  #: 21_22, 23


class TestHome(TestCase):
    def test_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_resolve_view(self):
        view = resolve('/')
        self.assertEqual(view.func, home)


class MonthTests(TestCase):
    def setUp(self):
        john = Person.objects.create(last_name='Doe', first_name='John')
        alice = Person.objects.create(last_name='Noa', first_name='Alice')
        Public.objects.create(
            date='2012-12-12',
            hour_1='15:00:00',
            hour_2='17:00:00',
            place='Eftrano',
            person_1=john,
            person_2=alice, )

        self.url = reverse('month', kwargs={'month_num': 12, 'year_num': 2012})
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_resolve_view(self):
        view = resolve('/volana/12-2012')
        self.assertEquals(view.func, month)

    def test_contain_event(self):
        self.assertContains(self.response, 'John - Alice')
        self.assertContains(self.response, '15H - 17H')
        self.assertContains(self.response, 'Alarobia 12')


class MonthErrorTests(TestCase):
    def setUp(self):
        self.url = reverse('month',
                           kwargs={'month_num': 16, 'year_num': 2012})
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 404)
