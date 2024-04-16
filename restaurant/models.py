from django.db import models

# Create your models here.
class Booking(models.Model):
    id= models.IntegerField(max_length=11, primary_key=True)
    name = models.CharField(max_length=255)
    booking_date = models.DateField()
    no_of_guests = models.IntegerField(max_length=6)


    def __str__(self): 
        return self.name


# Add code to create Menu model
class Menu(models.Model):
   id= models.IntegerField(max_length=11, primary_key=True)
   title = models.CharField(max_length=255) 
   price = models.DecimalField(decimal_places=2, max_digits=10) 
   inventory = models.IntegerField(max_length=5) 

   def __str__(self):
      return self.title