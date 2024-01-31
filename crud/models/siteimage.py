from django.db import models

class SiteImage(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='media/images/')

    class Meta:
        app_label = 'crud'

    def __str__(self):
        return self.title