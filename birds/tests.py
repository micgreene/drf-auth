from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Bird
'''
Steps for Manual Authentications Testing Using Httpie:

- 1) run a POST request using valid log-in credentials:
   http POST :8000/api/token/ username=admin password=admin

- 2) This returns an access and a refresh token

- 3) Copy the access token.

- 4) Test auth by now running an api request using the bearer token:
   http :8000/api/appname/ 'Authorization: Bearer <copied token>'

- 5) This should return the contents of our database list in JSON format.

- 6) An incorrect token should return an access request denied message
'''


class BirdTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_bird = Bird.objects.create(name='Eagle', owner=testuser1,description='Bird of prey.')
        test_bird.save()

    def test_birds_model(self):
        bird = Bird.objects.get(id=1)
        actual_owner = str(bird.owner)
        actual_name = str(bird.name)
        actual_description = str(bird.description)
        self.assertEqual(actual_owner,'testuser')
        self.assertEqual(actual_name, 'Eagle')
        self.assertEqual(actual_description,'Bird of prey.')
