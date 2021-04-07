from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    description=models.TextField()
    url=models.TextField()
    image=models.ImageField(upload_to="images/")
    icon=models.ImageField(upload_to="images/")
    votes=models.IntegerField(default=1)
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e %y")
    def summary(self):
        return self.description[:100]
