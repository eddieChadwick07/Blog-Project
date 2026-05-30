from django.db import models

class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

