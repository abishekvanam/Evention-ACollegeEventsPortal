import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text=models.CharField(max_length=300)
    question_pub_date = models.DateTimeField('date published',default='0')
    asked_by=models.CharField(max_length=100)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
#    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text=models.CharField(max_length=500)
    question_id_of_answer=models.IntegerField(default=0)
    answer_pub_date=models.DateTimeField('date published',default='0')
    answered_by=models.CharField(max_length=100)
    #votes=models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text




