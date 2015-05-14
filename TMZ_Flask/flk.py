from flask import Flask
from flask import render_template
#from models import db
from flask_sqlalchemy import SQLAlchemy
from alchemyapi import AlchemyAPI
from collections import defaultdict

 
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbgood'

db = SQLAlchemy(app)
       
class Entities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer)
    text = db.Column(db.String)
    e_type = db.Column(db.String)
    relevance = db.Column(db.Float)
    sentiment = db.Column(db.String)
    sentiment_score = db.Column(db.Float)

    def __init__(self, article_id, text, e_type, relevance, sentiment, sentiment_score):
        self.article_id = article_id
        self.text = text
        self.e_type = e_type
        self.relevance = relevance
        self.sentiment = sentiment
        self.sentiment_score = sentiment_score

class Cooccurrences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity1 = db.Column(db.String)
    entity2 = db.Column(db.String)
    count = db.Column(db.Integer)

    def __init__(self, entity1, entity2, count):
        self.entity1 = entity1
        self.entity2 = entity2
        self.count = count
 
@app.route("/")
def hello():
    user = {'nickname': 'Miguel'}  # fake user
 
 
    return render_template('index.html',
                           title='Home',
                           user=user)
    #return "Hello World!"
 
#@app.route('/signup', methods=['POST'])
@app.route('/getentities')
def getentities():
         
    #####Get Alchemy Response######
    demo_urls = ['http://www.nhl.com/ice/news.htm?id=758474&navid=nhl:topheads','http://www.nhl.com/gamecenter/en/recap?id=2014030227&navid=nhl:topheads']
    for article_id,demo_url in enumerate(demo_urls):
        # Create the AlchemyAPI Object
        alchemyapi = AlchemyAPI()
        response = alchemyapi.text('url', demo_url)
            
        #Article text
        if response['status'] == 'OK':
            footer_line_start = "NHL.com is the official web site of the National Hockey League" 
            demo_text = response['text'].encode('utf-8') #save text here and make text calls instead of url calls later on
            demo_text = demo_text.split(footer_line_start)[0] 
            
        #Perform entity extraction
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
                e = Entities(article_id,entity_text, entity_type, entity_relevance,entity_sentiment,entity_score)
                db.session.add(e)
                db.session.commit()

    
    return "fsfsadf"    
     
     
      
@app.route('/message/<article_id>')
def message(article_id):
    entities = Entities.query.filter_by(article_id = article_id).all()
    return render_template('message.html', title='Home', entities = entities)

@app.route('/calculate_cooccurrences')
def calculate_cooccurrences():
    #default dict enters value in dictionary if it doesn't exist instead of return an error
    #it also looks like we have a nested dictionary here
    num_articles = 2
    matrix = defaultdict(lambda : defaultdict(int))
    for article_id in range(num_articles): 
        entities = Entities.query.filter_by(article_id = article_id).all()
        for i in range(len(entities)):
            for j in range(i,len(entities)):
                entity1, entity2 = [entities[i].text,entities[j].text]
                matrix[entity1][entity2] +=1
                matrix[entity2][entity1] +=1

                
    #Store the co-occurence matrix in the db
    for entity1 in matrix.iterkeys():
        entity2 = matrix[entity1].keys()[0]
        cooccurrence_count = matrix[entity1].values()[0]
        c = Cooccurrences(entity1,entity2,cooccurrence_count) 
        db.session.add(c)
        db.session.commit()            
    
    return "Co-occurrences calculated"

@app.route('/get_cooccurrences')
def get_cooccurrences():
    cooccurences = Cooccurrences.query.all()
    return render_template('message.html', title='Home', entities = cooccurences)
 
#calculate_cooccurrences() 

test = Cooccurrences.query.all()
for hope in test:
    print(hope.entity1)
    print(hope.entity2)
    print(hope.count)

#when debugging, comment out the line below 
#if __name__ == "__main__":
#    app.run()


