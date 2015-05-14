from __future__ import print_function
import os, sys
from alchemyapi import AlchemyAPI
from TMZ_Hate.models import Entities
import django

#Set up Django so we can store the Alchemy results in the db
djangoproject_home = "C:\Users\nick\Documents\GitHub\NHLNLP\TMZ"
sys.path.append(djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'TMZ.settings'
django.setup()

######Get Alchemy Response######
demo_url = 'http://www.nhl.com/ice/news.htm?id=758474&navid=nhl:topheads'
# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()
print('Extracting Text')
response = alchemyapi.text('url', demo_url)

if response['status'] == 'OK':
    #print('## Response Object ##')
    #print(json.dumps(response, indent=4))
    footer_line_start = "NHL.com is the official web site of the National Hockey League" 
    demo_text = response['text'].encode('utf-8') #save text here and make text calls instead of url calls later on
    demo_text = demo_text.split(footer_line_start)[0] 
    print('text: ', demo_text )
    print('')
else:
    print('Error in text extraction call: ', response['statusInfo'])

#Perform entity extraction
print('Extracting Entities')
response = alchemyapi.entities('text', demo_text, {'sentiment': 1}) #can replace with 'text', demo_text

if response['status'] == 'OK':
    for id,entity in enumerate(response['entities']):
        entity_text = entity['text'].encode('utf-8')
        entity_type = entity['type']
        entity_relevance =  entity['relevance']
        entity_sentiment = entity['sentiment']['type']
        if 'score' in entity['sentiment']:
            entity_score = entity['sentiment']['score']
        else:
            entity_score = 0 #it has no entity score if it is neutral so just give it a zero score for consistency in db

        #Store entities in db
        #TO DO -> Make the field implicit and autoincrement
        e = Entities(id,entity_text, entity_type, entity_relevance,entity_sentiment,entity_score)
        e.save()
else:
    print('Error in entity extraction call: ', response['statusInfo'])


###Read entities from db###
all_entities = Entities.objects.all()
for current_entity in all_entities:
    attributes = ['text','type','relevance','sentiment','sentiment_score']
    for attribute in attributes:
        print(current_entity.__getattribute__(attribute))
    print('')
    
    
#if entity not in all entities
#add it to all entities
#else, increment the occurance count, and updatewd sentiment average (by making use of occurence count)
