from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=2000, help_text='Write here your message!')
    source = models.CharField(max_length=50)

    def __str__(self):
        return self.name