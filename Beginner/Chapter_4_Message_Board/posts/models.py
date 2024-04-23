from django.db import models

# Create your models here.
class Post(models.Model):
    # Stores text type within the database.
    text = models.TextField()

    # Add this str function to change Posts title.
    def __str__(self):
        return self.text[:50]