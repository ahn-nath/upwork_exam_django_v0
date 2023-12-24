from django.db import models


class Users(models.Model):
    """
        This model is used to store user data.
    """
    email = models.EmailField(primary_key=True)
    user_profiles = models.ManyToManyField('Profiles', related_name='user_profiles', blank=True)
    user_favorites = models.ManyToManyField('Profiles', related_name='favorite_by', blank=True)

    def __str__(self):
        return self.email


class Profiles(models.Model):
    """
        This model is used to store profile data.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
