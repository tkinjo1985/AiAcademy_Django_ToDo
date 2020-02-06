from django.db import models


class ToDo(models.Model):

    class Meta:
        db_table = 'todo'

    todo_name = models.CharField(max_length=200)
    todo_content = models.CharField(max_length=1000)
    todo_done_flag = models.IntegerField(default=0)
    todo_create_date = models.TextField()
    todo_done_date = models.TextField()
