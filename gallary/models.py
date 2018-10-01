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


    # getting the images by name
    @classmethod
    def search_image_by_name(cls,search_term):
        gallary = cls.objects.filter(name__icontains=search_term)
        return gallary


    #filtering the images and returning by  it's id
    @classmethod
    def get_image_by_id(cls,id):
        gallary = cls.objects.get(pk=id)
        return gallary

    #filtering the images and returning the image by category
    @classmethod
    def search_image_by_category(cls,search_term):
        gallary = cls.objects.filter(category__name__icontains=search_term)
        return gallary

    #filtering the images and returning the image category
    @classmethod
    def filter_image_by_location(cls,search_term):
        gallary = cls.objects.filter(location__name__icotains=search_term)
        return gallary

    
    #updating the image for a specific image id
    @classmethod
    def update_image(cls, id):
        gallary=cls.objects.filter(id=id).update(id=id)
        return gallary
        
    

    #delleting a specific image
    @classmethod
    def delete_image_by_id(cls, id):
        gallary = cls.objects.filter(pk=id)
        gallary.delete()
