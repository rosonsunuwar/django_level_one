import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()
# import random
from second_app.models import Users
from faker import Faker
fakegen = Faker()
def populate():
    for _ in range(10):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
    
    use = Users.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]
if __name__ == '__main__':
    print("Populating....!")
    populate()
    print("Populating Complete!")