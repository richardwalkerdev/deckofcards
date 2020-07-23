"""This module adds unit tests for this app"""
from django.test import TestCase


class UnitTestCase(TestCase):
    """Simple unit tests"""
    def test_case_connection(self):
        """Test that the service is healthy via HTTP status"""
        response = self.client.get('/deck/')
        assert response.status_code == 200

    def test_case_json(self):
        """Test the response includes the ace of spades"""
        response = self.client.get('/deck/')
        self.assertContains(response, "ace")
        self.assertContains(response, "spades")
        self.assertContains(response, "joker")
