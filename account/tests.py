from django.test import TestCase, SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)


class LoginRequiredDashboardViewTests(SimpleTestCase):
    def test_redirection(self):
        login_url = reverse('login')
        url = reverse('dashboard')
        response = self.client.get(url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(
                             login_url=login_url, url=url))
