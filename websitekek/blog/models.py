from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        #curr date
        self.published_date = timezone.now()
        # renew database
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})


class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse_('post_list')



    def __str__(self):
        return self.text
