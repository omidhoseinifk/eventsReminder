from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import datetime


class Events(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(
        ('content'), config_name='default')
    update_date_time = models.DateTimeField(
        ('create date'), auto_now_add=True, auto_now=False)
    create_date_time = models.DateTimeField(
        ('update date'), auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title
        pass

    def date_time(self):
        print(datetime.datetime.now().strftime('%A, %Y-%m-%d, %H:%M'))
