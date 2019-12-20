from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/',blank = True,null = True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

    # def pub_date_pretty(self):
    #     return self.pub_date.strftime('%b %e %Y')
