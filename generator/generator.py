import random
from faker import Faker
from generator.data import NewUser

"""Faker generator of user info for sign up process"""

faker_en = Faker('En')
fake = Faker()
Faker.seed()


def generated_new_user():
    yield NewUser(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
    )
