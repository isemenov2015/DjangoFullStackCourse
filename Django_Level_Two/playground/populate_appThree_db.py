import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'playground.settings')

import django
django.setup()

#FAKE POP SCRIPT
import random
from appThree.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', "Marketplace", "News", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate_urls(N = 5):
    for entry in range(N):
        #get the topic for the entry
        topic = add_topic()

        #make fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #Create new webpage entry
        webpg = Webpage.objects.get_or_create(topic = topic, url = fake_url, name = fake_name)[0]

        #create a fake access record for the Webpage
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

def populate_users(N = 5):
    for entry in range(N):
        fname = fakegen.name().split(' ')
        fake_name = fname[0]
        fake_surname = fname[1]
        fake_email = fakegen.email()
        usr = User.objects.get_or_create(name = fake_name, surname = fake_surname, email = fake_email)[0]

if __name__ == "__main__":
    print("Populating script...")
    populate_urls(20)
    populate_users(10)
    print("Populating complete")
