from django.db import models

class User(models.Model):
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=20)
    # voice_print_id = models.PositiveIntegerField() ※ここは将来的に実装する(2024/1/28MEMO)
    # curren_counselor_id = models.PositiveIntegerField() ※ここは将来的に実装する(2024/1/28MEMO)

    class Meta:
        app_label = 'crud'

    def __str__(self):
        return self.email