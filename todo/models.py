from django.db import models


class ToDo(models.Model):

    class Meta:
        db_table = 'todo'

    name = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    is_done = models.BooleanField(default=False)
    create_date = models.TextField()
    done_date = models.TextField()
    is_hidden = models.BooleanField(default=False)
