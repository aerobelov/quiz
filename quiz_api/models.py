from django.db import models
from django.contrib.auth.models import User
import datetime

class QuizParticipant(models.Model):
    """
    CUSTOM USER MODEL
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_number = models.IntegerField()

    def __str__(self):
        return f'{self.user}/{self.user_number}'

class Question_set(models.Model):
    """
    QUESTION SET MODEL
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    start_date = models.DateField(default=datetime.date.today(), editable=False)
    end_date = models.DateField()

    def __str__(self):
        return self.title

class Question_type(models.Model):
    """
    QUESTION TYPE MODEL
    """
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Question(models.Model):
    """
    QUESTION MODEL
    """
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey("Question_type", on_delete=models.CASCADE)
    set = models.ForeignKey("Question_set", on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

class Answer_option(models.Model):
    """
    ANSWER OPTION MODEL
    """
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class Answer(models.Model):
    """
    ANSWER MODEL
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(QuizParticipant, on_delete=models.CASCADE)
    question = models.ForeignKey("Question", on_delete=models.CASCADE, default=1)
    option = models.ForeignKey("Answer_option", on_delete=models.CASCADE)
    text_option = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.question}/{self.option}'


"""
LAST QUESTION RETRIEVER
"""
def last():
    return Question.objects.last()
