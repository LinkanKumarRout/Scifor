from django.db import models

# Create your models here.
class AllBlogs(models.Model):
    text = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text