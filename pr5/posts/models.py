from django.db import models
# zxc pasw
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]