from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    # our database model will only have a title, an author and the body
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(
        "auth.User",
        on_delete = models.CASCADE, # for all many-to-one relationships like FOREIGN KEY, it's important to have an on_delete option
    )
    body = models.TextField()

    def __str__(self):
        """method to provide a human-readable version of the model in the admin"""
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs = {"pk": self.pk})