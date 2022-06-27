from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import AbstractUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: AbstractUser):
        token = super().get_token(user)

        # Add custom claims
        token['admin'] = user.is_admin
        token['name'] = user.get_full_name()
        # ...

        return token
