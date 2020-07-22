from django.test import TestCase


class UnitTestCase(TestCase):

    def test_case_connection(self):
        response = self.client.get('/deck/')
        assert response.status_code == 200

    def test_case_json(self):
        response = self.client.get('/deck/')
        self.assertContains(response, "ace")
        self.assertContains(response, "spades")
