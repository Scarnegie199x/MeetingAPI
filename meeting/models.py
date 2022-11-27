from django.db import models
from django.contrib.auth import get_user_model




class Meeting(models.Model):
    title = models.CharField(max_length=255)
    #created_by = models.ForeignKey(get_user_model(),
                                #on_delete=models.CASCADE,
                                #)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title[:50]


class Topic(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    problem = models.TextField(blank=True)
    resolution = models.TextField()
    meeting = models.ForeignKey(Meeting,
                              on_delete=models.CASCADE,
                              related_name="Meeting",
                              )
    #attachments = FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.title[:50]