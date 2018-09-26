from django.db import models
import datetime as dt
# Create your models here.


class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()



class tags(models.Model):
    name = models.CharField(max_length =30)




class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_image = models.ImageField(upload_to = 'images/')

    @classmethod
    def today_gallary(cls):
        today = dt.date.today()
        gallary = cls.objects.filter(name = today)
        return gallary