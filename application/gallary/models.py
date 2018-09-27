from django.db import models


# my models .
class Location(models.Model):
    name = models.CharField(max_length =60)
        
    def __str__(self):
        return self.name

    def save_location(self):
        self.save()


class Category(models.Model):
    name = models.CharField(max_length =60)
        
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()


class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category =  models.ForeignKey(Category)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()


    @classmethod
    def search_by_name(cls,search_term):
        gallary = cls.objects.filter(name__icontains=search_term)
        return gallary

    @classmethod
    def get_image_by_id(cls,id):
        gallary = cls.objects.get(pk=id)
        return gallary


    @classmethod
    def search_by_category(cls,search_term):
        gallary = cls.objects.filter(category__icontains=search_term)
        return gallary


    @classmethod
    def search_by_location(cls,search_term):
        gallary = cls.objects.filter(location__icontains=search_term)
        return gallary






