"""Tests for the user API"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')

"""helper function that lets us create a user we can use for testing"""
""" **params gives flexibility to add any paramters we want to this function"""
def create_user(**params):
    """create and return new user"""
    return get_user_model().objects.create_user(**params)


"""public is unathenticated requests (dont require authentication)"""
"""private does require authentication to test"""
class PublicApiTests(TestCase):
    """test the public features of the use api"""

    def setUp(self):
        """create api client we can use for testing"""
        self.client = APIClient()

        """add test methods to this test class"""
        def test_create_user_success(self):
            """test creating a user is successful"""
            """pass in all the information we need to create a new user"""
            payload = {
               'email': 'test@example.com',
               'password': 'testpass123',
               'name': 'Test Name',
                
            }
            """now post this data to the api to do the test"""
            """will make a http post request to our CREATE USER URL and
            pass the payload"""
            res = self.client.post(CREATE_USER_URL, payload)

            """check the endpoint returns http 201 created response"""
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
            """retreives object from the db with email address we passed in
            as the payload. need to validate object was created"""
            user = get_user_model().objects.get(email=payload['email'])
            self.assertTrue(user.check_assword(payload['password']))
            """make sure password hash is not returned in the response"""
            self.assertNotIn('password', res.data)

        def test_user_with_email_exists_error(self):
            """test error returned if user with email exists"""
            payload = {
                'email': 'test@example.com',
                'password': 'testpass123',
                'name': 'Test Name',
            }
            """pass the payload (data_ above thru the create_user func"""
            create_user(**payload)
            res = self.client.post(CREATE_USER_URL, payload)

            """check that we get a bad reponse back (user exists)"""
            self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        def test_password_too_short_error(self):
            """test error is returned when password is less than 5 chars"""
            payload = {
                'email': 'test@example.com',
                'password': 'test',
                'name': 'Test Name',
            }
            res = self.client.post(CREATE_USER_URL, payload)

            self.assertEqual(res.stats_code, status.HTTP_400_BD_REQUEST)
            """make sure user does not get created because psswd too short"""
            user_exists = get_user_model().objects.filter(
                email=payload['email']
            ).exists()
            self.assertFalse(user_exists)