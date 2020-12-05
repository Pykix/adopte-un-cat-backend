# import requests
import os
import django
from users.models import User
from django_seed import Seed
from datingcat import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datingcat.settings')
django.setup()

seeder = Seed.seeder()
seeder.add_entity(User, 25, {
    "email": lambda x: seeder.faker.email()
})
seeder.execute()

# def client():
#     # credentials = {
#     #     "username": "bonjour",
#     #     "email": "testtest@email.fr",
#     #     "password1": "adminadmin",
#     #     "password2": "adminadmin",
#     # }
#
#     token_h = "Token 5c833afa0c6e903a6586b8a613270056ea3158ce"
#     headers = {"Authorization": token_h}
#
#     response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)
#     print("Status code: ", response.status_code)
#     response_data = response.json()
#     print(response_data)
#
#
# if __name__ == "__main__":
#     client()
