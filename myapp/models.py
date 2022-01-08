
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    image=models.ImageField(upload_to="uploads", default="images/noimage.png")

    
class Talk(models.Model):
    talk=models.CharField(max_length=140)
    time=models.DateTimeField(auto_now_add=True)
    talk_from=models.ForeignKey(User, on_delete=models.CASCADE, related_name="talk_from")
    talk_to=models.ForeignKey(User, on_delete=models.CASCADE, related_name="talk_to")
    def __str__(self):
        return "{}>>{}".format(self.talk_from, self.talk_to)