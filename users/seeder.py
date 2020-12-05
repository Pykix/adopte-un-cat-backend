from users.models import User
from django_seed import Seed

seeder = Seed.seeder()
seeder.add_entity(User, 25, {
    "email": lambda x: seeder.faker.email()
})
seeder.execute()
