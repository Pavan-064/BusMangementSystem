from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from .models import User

class UserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username, password=password)
            return user
        except User.DoesNotExist:
            return None

    
