from django.test import TestCase

# Create your tests here.
from .models import Location, Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile

class LocationTestClass(TestCase):



    def setUp(self):
        self.test_location = Location(name = 'Shags')
        self.test_location.save()

    

    def test_instance(self):

        self.assertTrue(isinstance(self.test_location, Location))

    #Testing  if the user can save the image

    def test_save_method(self):
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    # Tear down method
    def tearDown(self):
        Location.objects.all().delete()

        # Testing if a user can delete an image

    def test_delete_location(self):
        self.test_location.delete()
        self.assertEqual(len(Location.objects.all()), 0)


class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):


        self.isebania = Location.objects.create(name="Isebania")
        self.travell= category.objects.create(name='travell')


        self.test_image = Image.objects.create(image='image_name',name='name_input',
                                description='I love testing my code',
                                location=self.isebania,
                                )







        self.test_image.save()

    def test_save_method(self):
        self.test_image.save()
        test_images = Image.objects.all()
        self.assertTrue(len(test_images) > 0)

    # Testing save method
    def test_save_image(self):
        self.assertEqual(len(Image.objects.all()), 1)

