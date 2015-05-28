# TMZHater
Letting you figure out how much hate your favorite celeb gets on TMZ.

# Getting Started:

You will need to install the following:

Sign up for your account on the Alchemy Website: http://www.alchemyapi.com/api/register.html
Download Eclipse: https://eclipse.org/
Download Pydev from the Eclipse Marketplace

# Running the final project 

0) Install Flask (pip install Flask)and SQl-Alchemy (pip install flask-sqlalchemy) (AlchemyAPI package and API key is include with the sample code)
1) Run create_db.py to create the database
2) In command prompt, enter python flk.py to start the web server
3) Go to http://127.0.0.1:5000/extract_entities to perform NER / SA and http://127.0.0.1:5000/extract_entities to view the results
4) Go to http://127.0.0.1:5000/calculate_cooccurrences to calculate how often two entities occur together
5) Go to http://127.0.0.1:5000/retrieve_cooccurrences to view the results

# Explain NLP & NER here
What is NLP -> Watch this video: https://class.coursera.org/nlp/lecture/ 
What is IE / NER -> Watch this video: https://class.coursera.org/nlp/lecture/61
What is Alchemy API?
	-> A library that performs a bunch of NLP tasks for you



# flask tutorial

Flask is a web framework that makes it every easy to set up a web app using python
Flask has three main components
1) Models -> how the data will be stored in the database
2) Routing -> the python function that will exected when a URL is accessed
3) Templates -> how information is displayed on the web page

###1 Model definition ####
We will be using a database to store certain data and retrieve it later
In flask, each database table corresponds to a model class
In this project, we will have two database models: Entities and Occurences
The Entities model stores the named entities extract from the articles using alchemy API 
The occurences model stores the co-occurrence matrix between the entities
The co-occurrence matrix simply holds how often each possible pair of entities occurs together in the same article 
Once we have defined our models in the main flk.py, we need to create another file that will actually create the database from the model definition

###2 Routing ####
Flask maps each url path to a python function 
@app.route('/url_path')
def some_function():
{}

This means that when someone accesses the page http://YourWebsite/url_path, that the function some_function() is called
In our case, we will use these functions to perform various NLP calculations and API calls


###3 Templates ###
TO DO -> Explain templates


#Other resources 
http://flask.pocoo.org/docs/0.10/quickstart/





