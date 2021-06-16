from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


class Topic(models.Model):
   topic_name = models.CharField(max_length=50)

   def __str__(self):
        return self.topic_name

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=False)
    question=models.CharField(max_length=600)

    option1 = models.CharField(max_length=200, null=True, blank=True)
    option2 = models.CharField(max_length=200, null=True, blank=True)
    option3 = models.CharField(max_length=200, null=True, blank=True)
    option4 = models.CharField(max_length=200, null=True, blank=True)
    option5 = models.CharField(max_length=200, null=True, blank=True)

    # Вопросы в которых нужно быбрать картинку
    picture1 = models.ImageField(upload_to='static/questions-picture', null=True, blank=True)
    picture2 = models.ImageField(upload_to='static/questions-picture', null=True, blank=True)
    picture3 = models.ImageField(upload_to='static/questions-picture', null=True, blank=True)
    picture4 = models.ImageField(upload_to='static/questions-picture', null=True, blank=True)
    picture5 = models.ImageField(upload_to='static/questions-picture', null=True, blank=True)

    #Вопросы в которых должны вводить данные
    entry = models.CharField(max_length=200, null=True, blank=True)
    entry_answer = models.CharField(max_length=200, null=True, blank=True)

    my_choices=(('Option1','Option1'),
         ('Option2','Option2'),
         ('Option3','Option3'),
         ('Option4','Option4'),
         ('Option5','Option5'),
         ('Picture1','Picture1'),
         ('Picture2','Picture2'),
         ('Picture3','Picture3'),
         ('Picture4','Picture4'),
         ('Picture5','Picture5'),
         ('Entry_answer','Entry_answer'))


    answer = MultiSelectField(choices=my_choices,
                                 max_choices=4,
                                 max_length=200, null=False, default=False)

    def __str__(self):
        template = '{0.id} || {0.topic} || {0.question}'
        return template.format(self)


class Result(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    exam = models.ForeignKey(Topic,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
