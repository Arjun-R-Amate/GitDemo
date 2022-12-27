from django.db import models

# Create your models here.
class book_add(models.Model):
    author = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.author
    
    class Meta:
        db_table = "Book"