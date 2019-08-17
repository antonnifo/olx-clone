from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):

    CONDITION_TYPE = (
        ("New","New"),
        ("Used for less than a Month","Used for less than a Month"),
        ("Used for less than  3 Months","Used for less than 3 Months"),
        ("Used for less than  6 Months","Used for less than 6 Months"),
        ("Used for more than  6 Months","Used for more than 6 Months")
        
    )
    
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    condition  = models.CharField(max_length=100, choices=CONDITION_TYPE)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    created = models.DateTimeField()
    
    def __str__(self):
        return self.name
    