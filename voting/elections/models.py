from django.db import models

# Create your models here.
class Election(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    
    
    def __str__(self):
        return self.title


class Candidate(models.Model):
    name=models.CharField(max_length=100)
    election=models.ForeignKey(Election,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
from django.contrib.auth.models import User

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} voted for {self.candidate.name}"