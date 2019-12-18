from django.test import TestCase

from django.test import Client
from django.urls import reverse


class PageViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_about(self):
        resp = self.client.get(reverse('about'))

        self.assertEqual(
            resp.status_code, 200
        )

    def test_privacy(self):
        resp = self.client.get(reverse('privacy_policy'))

        self.assertEqual(
            resp.status_code, 200
        )

    def test_terms(self):
        resp = self.client.get(reverse('terms'))

        self.assertEqual(
            resp.status_code, 200
        )

    def test_cookies(self):
        resp = self.client.get(reverse('cookies_policy'))

        self.assertEqual(
            resp.status_code, 200
        )

