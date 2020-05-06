from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import os


def upload_and_edit(instance, filename):
    ext = os.path.splitext(filename)[-1]
    return 'image/{user}/{pk}{ext}'.format(user=instance.user, pk=instance.pk, ext=ext)


class Images(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to=upload_and_edit)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    details = models.TextField(default='N/A', max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image_details', kwargs={'pk': self.pk})


class Comment(models.Model):
    comment = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Images, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
