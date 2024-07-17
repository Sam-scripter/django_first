import os
import django

# setting the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro_two.settings')

# Setup Django
django.setup()

# Import modules after setting up django
import random
from faker import Faker
from pro_app.models import User

# FAKE POPULATION SCRIPT
fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        
        fake_last_name = fakegen.last_name()
        

        # Ensure unique first name and email
        unique_first_name = False
        unique_email = False

        while not unique_first_name:
            fake_first_name = fakegen.first_name()
            if not User.objects.filter(first_name = fake_first_name).exists():
                unique_first_name = True

        while not unique_email:
            fake_email = fakegen.email()
            if not User.objects.filter(email = fake_email).exists():
                unique_email = True

        # Create the user entry
        new_user = User.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, email = fake_email)[0]

if __name__ == '__main__':
    print('populating User')
    populate(20)
    print('population of users complete')


