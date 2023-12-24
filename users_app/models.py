from django.db import models


class User(models.Model):
    """
        This model is used to store user data.
    """
    email = models.EmailField(primary_key=True)
    profiles = models.ManyToManyField('Profile', related_name='users')
    favorites = models.ManyToManyField('Profile', related_name='favorited_by')


class Profile(models.Model):
    """
        This model is used to store profile data.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
