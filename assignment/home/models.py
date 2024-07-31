from django.db import models

Age_Bracket = (
    ('age1','0-10'),
    ('age2', '11-20'),
    ('age3','21-30'),
    ('age4','31-40'),
)

Messages = (
    ('msg1','Congratulations!'),
    ('msg2', 'Sorry'),
    ('msg3','Sad'),
    ('msg4','Enjoy'),
    ('msg4','Good Evening'),
    ('msg4','Good Morning'),
)


# Create your models here.
class User(models.Model):
    userName=models.CharField(max_length=30,unique=True)
    ageBracket=models.CharField(max_length=10,choices=Age_Bracket)

class Message(models.Model):
    userNames=[(user.userName, user.userName) for user in User.objects.all()]
    senderName=models.CharField(max_length=30,choices=userNames)
    ageBracket=models.CharField(max_length=10,choices=Age_Bracket)
    receiverName=models.CharField(max_length=30)
    message=models.CharField(max_length=20,choices=Messages)
    
