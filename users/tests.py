from django.test import TestCase

import users
from users.models import Profile

# Create your tests here.
    # Profile object can be created with all required fields
def test_create_profile_with_all_required_fields(self):
    user = users.objects.create(username='test_user')
    profile = Profile.objects.create(user=user)
    assert profile.user == user
    assert profile.name is None
    assert profile.email is None
    assert profile.profile_image is None
    assert profile.username is None
    assert profile.id is not None