from django.db import models
from django import forms



# Create your models here.


class Person(models.Model): 
    registration_number = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()   
    cellphone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    friends= models.ManyToManyField('self',)
    is_online = models.BooleanField(default=False)
    faculty= models.ForeignKey('Faculty',on_delete=models.DO_NOTHING,default=None,null=True)
    def __str__(self) :
        return self.first_name +' '+ self.last_name
    person_type='generic'
    


class Faculty(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=6)
    def __str__(self):
        return self.name

class Campus(models.Model) :
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    def __str__(self) :
        return self.name
        

class Job(models.Model) :
    title = models.CharField(max_length=10)
    def __str__(self):
        return self.title
    
    

class Cursus(models.Model):
    title = models.CharField(max_length=10)
    def __str__(self):

        return self.title
    
class Employee(Person):

    office = models.CharField(max_length=20)
    campus = models.ForeignKey('Campus', on_delete=models.DO_NOTHING)
    job = models.ForeignKey('Job',on_delete=models.DO_NOTHING)
    person_type='employee'

class Student (Person):
    cursus = models.ForeignKey('Cursus',on_delete=models.DO_NOTHING)
    year = models.CharField(max_length=1)
    person_type='student'

class Message(models.Model):
    author = models.ForeignKey('Person',on_delete=models.DO_NOTHING) 
    content = models.TextField()
    publication_date = models.DateField()
    publication_time = models.DateTimeField(auto_now=True)
    def __str__(self) :
        if len(self.content)>20:
            return self.content[:19]+"..."
        else:
            return self.content


class Invitation(models.Model):
    sender = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='sent_invitations')
    recipient = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='received_invitations')
    date_sent = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Invitation de {self.sender} à {self.recipient}'

    
    
     

    



    



 




