import os
import django

# Setting the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

# Setup Django
django.setup()

# Import modules after setting up Django
import random
from faker import Faker
from first_app.models import AccessRecord, Webpage, Topic

# FAKE POP SCRIPT
fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    topic = random.choice(topics)
    t = Topic.objects.get_or_create(top_name=topic)[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # Get the topic for the entry
        top = add_topic()

        # Create fake data for that entry
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Ensure unique URL
        unique = False
        while not unique:
            fake_url = fakegen.url()
            if not Webpage.objects.filter(url=fake_url).exists():
                unique = True

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake access record for the web page that is created
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populating completed!')
