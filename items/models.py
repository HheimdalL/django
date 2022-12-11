from django.db import models
import uuid
from user.models import CustomUser
from django.urls import reverse

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    name = models.CharField(max_length=120,)
    description = models.TextField(max_length=1024,)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    image = models.ImageField(upload_to='images/',)
    
    acart = models.ManyToManyField(CustomUser, through='Cart')
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('detail_item', args=[str(self.id)])
  
class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    quantity = models.PositiveIntegerField()
