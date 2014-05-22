from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Contact(models.Model):
    
    # Python data types mapping to the databases and also the validation rules
    
    first_name = models.CharField(
        max_length=255, 
        #label = 'Your Name', 
        #initial = 'Shubham',
        #help_text = '255 charcaters max.',
        validators = [RegexValidator(r'^[a-zA-Z_]+$', 'Enter a valid FirstName')]
    )
    
    last_name = models.CharField(        
        max_length = 255,
        #label = 'Your LastName',
        #initial = 'Utwal',
        #help_text = '255 charcaters max.',
        validators = [RegexValidator(r'^[a-zA-Z]+$', 'Enter a valid LastName')]
    )
    
    email = models.EmailField(
        max_length = 100,
        #initial = 'foo@example.com',
        #label = 'Your Email-id',
        #help_text = '100 characters max.'
    )
    
    #Method : String representation of object
    
    def __str__(self): 
        return self.first_name + " " + self.last_name 