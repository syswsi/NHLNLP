from django.db import models

class Entities(models.Model): #when I looked at SQL life file, it had an id column. So when using model API, I had to set id before any other arguments
    text = models.TextField()
    type = models.TextField()
    relevance = models.FloatField()
    sentiment = models.CharField(max_length = 15)
    sentiment_score = models.FloatField()

    def __str__(self):             
        return self.text
