#!/usr/bin/env python

#API key 0d8339f022963cd369800291fc27389a008dcc04

from __future__ import print_function
from alchemyapi import AlchemyAPI
import json


demo_url = 'http://www.nhl.com/ice/news.htm?id=758474&navid=nhl:topheads'
#demo_html = '<html><head><title>Python Demo | AlchemyAPI</title></head><body><h1>Did you know that AlchemyAPI works on HTML?</h1><p>Well, you do now.</p></body></html>'
#image_url = 'http://demo1.alchemyapi.com/images/vision/football.jpg'
                                             
# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()


print('############################################')
print('#   Title Extraction Example               #')
print('############################################')
#print('Processing url: ', demo_url)


response = alchemyapi.title('url', demo_url)

if response['status'] == 'OK':
    #print('## Response Object ##')
    #print(json.dumps(response, indent=4))

    print('title: ', response['title'].encode('utf-8'))
    print('')
else:
    print('Error in title extraction call: ', response['statusInfo'])

print('')
print('############################################')
print('#   Text Extraction Example                #')
print('############################################')

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


print('')
print('')
print('############################################')
print('#   Entity Extraction Example              #')
print('############################################')

response = alchemyapi.entities('text', demo_text, {'sentiment': 1}) #can replace with 'text', demo_text

if response['status'] == 'OK':
    #print('## Response Object ##')
    #print(json.dumps(response, indent=4))

    print('')
    for entity in response['entities']:
        print('text: ', entity['text'].encode('utf-8'))
        print('type: ', entity['type'])
        print('relevance: ', entity['relevance'])
        print('sentiment: ', entity['sentiment']['type'])
        if 'score' in entity['sentiment']:
            print('sentiment score: ' + entity['sentiment']['score'])
        print('')
else:
    print('Error in entity extraction call: ', response['statusInfo'])


print('')
print('############################################')
print('#   Keyword Extraction Example             #')
print('############################################')

response = alchemyapi.keywords('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':
    #print('## Response Object ##')
    #print(json.dumps(response, indent=4))

    print('')
    print('## Keywords ##')
    for keyword in response['keywords']:
        print('text: ', keyword['text'].encode('utf-8'))
        print('relevance: ', keyword['relevance'])
        print('sentiment: ', keyword['sentiment']['type'])
        if 'score' in keyword['sentiment']:
            print('sentiment score: ' + keyword['sentiment']['score'])
        print('')
else:
    print('Error in keyword extaction call: ', response['statusInfo'])



print('')
print('############################################')
print('#   Concept Tagging Example                #')
print('############################################')


response = alchemyapi.concepts('text', demo_text)

if response['status'] == 'OK':
    #print('## Object ##')
    #print(json.dumps(response, indent=4))

    print('')
    print('## Concepts ##')
    for concept in response['concepts']:
        print('text: ', concept['text'])
        print('relevance: ', concept['relevance'])
        print('')
else:
    print('Error in concept tagging call: ', response['statusInfo'])


print('')
print('############################################')
print('#   Sentiment Analysis Example             #')
print('############################################')

response = alchemyapi.sentiment('text', demo_text)

if response['status'] == 'OK':
    #print('## Response Object ##')
    #print(json.dumps(response, indent=4))

    print('')
    print('## Document Sentiment ##')
    print('type: ', response['docSentiment']['type'])

    if 'score' in response['docSentiment']:
        print('score: ', response['docSentiment']['score'])
else:
    print('Error in sentiment analysis call: ', response['statusInfo'])


print('')
print('############################################')
print('#   Targeted Sentiment Analysis Example    #')
print('############################################')

response = alchemyapi.sentiment_targeted('text', demo_text, 'National Hockey League') #INVESTIGATE

if response['status'] == 'OK':
    #print('## Response Object ##')
    #print(json.dumps(response, indent=4))

    print('')
    print('## Targeted Sentiment ##')
    print('type: ', response['docSentiment']['type'])

    if 'score' in response['docSentiment']:
        print('score: ', response['docSentiment']['score'])
else:
    print('Error in targeted sentiment analysis call: ',
          response['statusInfo'])


print('')
print('############################################')
print('#   Author Extraction Example              #')
print('############################################')

response = alchemyapi.author('text', demo_text)

if response['status'] == 'OK':
    #print('## Response Object ##')
    #print(json.dumps(response, indent=4))


    print('author: ', response['author'].encode('utf-8'))
    print('')
else:
    print('Error in author extraction call: ', response['statusInfo'])


# print('')
# print('')
# print('')
# print('############################################')
# print('#   Language Detection Example             #')
# print('############################################')
# print('')
# print('')
# 
# print('Processing text: ', demo_url)
# print('')
# 
# response = alchemyapi.language('text', demo_text)
# 
# if response['status'] == 'OK':
#     #print('## Response Object ##')
#     #print(json.dumps(response, indent=4))
# 
#     print('')
#     print('## Language ##')
#     print('language: ', response['language'])
#     print('iso-639-1: ', response['iso-639-1'])
#     print('native speakers: ', response['native-speakers'])
#     print('')
# else:
#     print('Error in language detection call: ', response['statusInfo'])


print('')
print('############################################')
print('#   Relation Extraction Example            #')
print('############################################')

response = alchemyapi.relations('text', demo_text)

if response['status'] == 'OK':
    #print('## Object ##')
    #print(json.dumps(response, indent=4))

    print('')
    for relation in response['relations']:
        if 'subject' in relation:
            print('Subject: ', relation['subject']['text'].encode('utf-8'))

        if 'action' in relation:
            print('Action: ', relation['action']['text'].encode('utf-8'))

        if 'object' in relation:
            print('Object: ', relation['object']['text'].encode('utf-8'))

        print('')
else:
    print('Error in relation extaction call: ', response['statusInfo'])


print('')
print('############################################')
print('#   Text Categorization Example            #')
print('############################################')

response = alchemyapi.category('text', demo_text)

if response['status'] == 'OK':
    #print('## Response Object ##')
    #print(json.dumps(response, indent=4))

    print('')
    print('## Category ##')
    print('text: ', response['category'])
    print('score: ', response['score'])
    print('')
else:
    print('Error in text categorization call: ', response['statusInfo'])


# print('')
# print('')
# print('')
# print('############################################')
# print('#   Feed Detection Example                 #')
# print('############################################')
# print('')
# print('')
# 
# print('Processing url: ', demo_url)
# print('')
# 
# response = alchemyapi.feeds('text', demo_text)
# 
# if response['status'] == 'OK':
#     #print('## Response Object ##')
#     #print(json.dumps(response, indent=4))
# 
#     print('')
#     print('## Feeds ##')
#     for feed in response['feeds']:
#         print('feed: ', feed['feed'])
# else:
#     print('Error in feed detection call: ', response['statusInfo'])
# 
# print('')
# print('')


# print('')
# print('')
# print('')
# print('############################################')
# print('#   Microformats Parsing Example           #')
# print('############################################')
# print('')
# print('')
# 
# print('Processing url: ', demo_url)
# print('')
# 
# response = alchemyapi.microformats('text', demo_text)
# 
# if response['status'] == 'OK':
#     #print('## Response Object ##')
#     #print(json.dumps(response, indent=4))
# 
#     print('')
#     print('## Microformats ##')
#     for microformat in response['microformats']:
#         print('Field: ', microformat['field'].encode('utf-8'))
#         print('Data: ', microformat['data'])
#         print('')
# 
# else:
#     print('Error in microformats parsing call: ', response['statusInfo'])
# 
# print('')
# print('')


# print('')
# print('')
# print('')
# print('############################################')
# print('#   Image Extraction Example               #')
# print('############################################')
# print('')
# print('')
# 
# print('Processing url: ', demo_url)
# print('')
# 
# response = alchemyapi.imageExtraction('text', demo_text)
# 
# if response['status'] == 'OK':
#     #print('## Response Object ##')
#     #print(json.dumps(response, indent=4))
# 
#     print('')
#     print('## Image ##')
#     print('Image: ', response['image'])
#     print('')
# 
# else:
#     print('Error in image extraction call: ', response['statusInfo'])
# 
# print('')
# print('')
# 
# 
# print('')
# print('')
# print('')
# print('############################################')
# print('#   Image tagging Example                  #')
# print('############################################')
# print('')
# print('')
# 
# print('Processing url: ', image_url)
# print('')
# 
# response = alchemyapi.imageTagging('url', image_url)
# 
# if response['status'] == 'OK':
#     #print('## Response Object ##')
#     #print(json.dumps(response, indent=4))
# 
#     print('')
#     print('## Keywords ##')
#     for keyword in response['imageKeywords']:
#         print(keyword['text'], ' : ', keyword['score'])
#     print('')
# else:
#     print('Error in image tagging call: ', response['statusInfo'])
# 
# print('')
# print('')


print('')
print('############################################')
print('#   Taxonomy  Example                      #')
print('############################################')

response = alchemyapi.taxonomy('text', demo_text)

if response['status'] == 'OK':
    #print('## Response Object ##')
    #print(json.dumps(response, indent=4))

    print('')
    print('## Categories ##')
    for category in response['taxonomy']:
        print(category['label'], ' : ', category['score'])
    print('')

else:
    print('Error in taxonomy call: ', response['statusInfo'])


# print('')
# print('')
# print('############################################')
# print('#   Combined  Example                      #')
# print('############################################')
# print('')
# print('')
# 
# print('Processing text: ', demo_url)
# print('')
# 
# response = alchemyapi.combined('text', demo_text)
# 
# if response['status'] == 'OK':
#     #print('## Response Object ##')
#     #print(json.dumps(response, indent=4))
# 
#     print('')
# 
#     print('## Keywords ##')
#     for keyword in response['keywords']:
#         print(keyword['text'], ' : ', keyword['relevance'])
#     print('')
# 
#     print('## Concepts ##')
#     for concept in response['concepts']:
#         print(concept['text'], ' : ', concept['relevance'])
#     print('')
# 
#     print('## Entities ##')
#     for entity in response['entities']:
#         print(entity['type'], ' : ', entity['text'], ', ', entity['relevance'])
#     print(' ')
# 
# else:
#     print('Error in combined call: ', response['statusInfo'])
# 
# print('')
# print('')
