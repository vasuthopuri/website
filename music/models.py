from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Model
from django.utils import timezone


class Post(models.Model):
    post_title = models.CharField(max_length=250)
    post_description = models.TextField()
    post_author = models.ForeignKey(User, default=1)
    post_image = models.URLField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'post'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.post_title
