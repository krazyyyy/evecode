from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass


class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.name}"

class Agent(models.Model):
    name = models.CharField(max_length=64)
    agent_img = models.CharField(max_length=500, default="N/a")
    def __str__(self):
        return f"{self.name}"

class Properties(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="broker")
    name = models.CharField(max_length=100)
    location = models.TextField(max_length=100)
    size = models.IntegerField()
    water = models.BooleanField()
    lugage = models.BooleanField()
    bed_room = models.IntegerField()
    bath_room = models.IntegerField()
    garage = models.IntegerField()
    year = models.IntegerField()
    pur_ch = [
        ('Sale', 'sale'),
        ('rent', 'rent'),
        ('buy', 'buy')
    ]
    purpose = models.CharField(max_length=5, choices=pur_ch, default="buy")
    price = models.IntegerField(default=0)
    house = models.CharField(max_length=500, default="N/a")
    description = models.TextField(max_length=1000, default="This is a Fantastic House To Live")
    stories = models.IntegerField(default=2)
    floor = models.IntegerField(default="0")
    cat = [
        ('RES', 'Residences'),
        ('OFF', 'Office'),
        ('COM', 'Commercial'),
        ('BUL', 'Building'),
        ('STO', 'STORAGE')
    ]
    category = models.CharField(max_length=100,choices=cat, default="Residences")

    def __str__(self):
        return f"{self.name} at {self.location}"         


class Reviews(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE, related_name='reviewer', default=1)
    name = models.CharField(max_length=50)
    review = models.TextField(max_length=500)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class Blog(models.Model):
    # timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=74)
    img = models.CharField(max_length=500, default="N/a")
    img_2 = models.CharField(max_length=500, default="N/a")
    context = models.TextField(max_length=3000)
    context_2 = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=52)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}"