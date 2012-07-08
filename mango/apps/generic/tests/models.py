from django.test import TestCase
from django.contrib.auth.models import User

from generic.models import UserProfile


class UserProfileTest(TestCase):
    def test_profile_creation(self):
        """
        Test that when a user is created, there's an equivalent UserProfile.
        """
        self.assertEqual(UserProfile.objects.count(), 0)
        user = User.objects.create_user('marconi',
                                        'marconi@djangomango.com',
                                        'supersecure')
        self.failUnless(user.get_profile())
        self.assertEqual(UserProfile.objects.count(), 1)
