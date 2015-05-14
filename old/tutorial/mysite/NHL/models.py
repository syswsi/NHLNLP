from django.db import models

class Entities(models.Model): #when I looked at SQL life file, it had an id column. So when using model API, I had to set id before any other arguments
    entity_text = models.TextField()
    entity_type = models.TextField()
    relevance = models.FloatField()
    sentiment = models.CharField(max_length = 15)
    sentiment_score = models.FloatField()
