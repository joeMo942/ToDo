from django.db import models

class task(models.Model):
    task = models.CharField(max_length=200)
    iscompleted=models.BooleanField(default=False)
    craeted_at=models.DateTimeField(auto_now_add=True)
    changed_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task