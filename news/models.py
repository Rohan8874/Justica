from django.db import models

class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='news_images/')
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
