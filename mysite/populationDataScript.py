'''
This script is going to populate
the database tables automatically
using Faker library which generates
Fake data.
'''

# The following code will set defaul working environment
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# The following code will setup djangoproject
import django
django.setup()

# The following code will generate FAKE data
from faker import Faker
import random
from home.models import Topic, WebPage, AccessRecords

fakeDataGenerator = Faker()
topics = ['Ethical Hacking', 'Web App Testing', 'Bug Bounty', 'CTFs', 'Python']

def addTopics():
    t = Topic.objects.get_or_create(topicName=random.choice(topics))[0]
    t.save()
    return t

def populateData(N=5):
    for entry in range(N):
        
        topicEntry = addTopics()

        fakeURL = fakeDataGenerator.url()
        fakeDate = fakeDataGenerator.date()
        fakeName = fakeDataGenerator.company()

        webPageEntry = WebPage.objects.get_or_create(topic=topicEntry, url=fakeURL, name=fakeName)[0]

        accessRecordEntry = AccessRecords.objects.get_or_create(name=webPageEntry, date=fakeDate)[0]

if __name__ == '__main__':
    print('Populating Data Using Automated Script')
    populateData(20)
    print('Population Data is Complete!')
