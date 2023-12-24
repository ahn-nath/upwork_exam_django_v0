from rest_framework import serializers

from users_app.models import Users, Profiles


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = '__all__'
