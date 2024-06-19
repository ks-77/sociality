import requests
from django.core.files.base import ContentFile
from faker import Faker

from accounts.models import CustomUser

fake = Faker()


def generate_user():
    username = fake.user_name()
    email = fake.email()
    phone_number = fake.phone_number()
    name = fake.name()
    bio = fake.text(max_nb_chars=150)
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=60)
    gender = fake.random_element(["Male", "Female", "Other"])
    pronouns = fake.random_element(["He/Him", "She/Her", "They/Them"])
    links = fake.url()

    response = requests.get("https://thispersondoesnotexist.com/", stream=True)
    response.raise_for_status()
    image_name = f"{username}.jpg"
    image_content = ContentFile(response.content)

    user = CustomUser(
        username=username,
        email=email,
        phone_number=phone_number,
        name=name,
        bio=bio,
        date_of_birth=date_of_birth,
        gender=gender,
        pronouns=pronouns,
        links=links,
    )
    user.avatar.save(image_name, image_content, save=True)
    user.set_password("password")
    user.save()

    return user
