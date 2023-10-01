from django.db import models

# Create your models here.
class status(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    Bulb_Issue= models.CharField(max_length=10)
    Curr_Leak= models.CharField(max_length=10)
    Brok_Wire=models.CharField(max_length=10)
    No_Sgnl= models.CharField(max_length=10)

    def __str__(self):
        return (f"{self.Bulb_Issue}")