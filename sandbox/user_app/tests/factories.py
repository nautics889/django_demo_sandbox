import factory

from user_app import models


class SandyUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.SandyUser

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    #TODO: override factory's create method to provide hashing
    password = factory.Faker('password')
