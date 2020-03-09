from datetime import timezone
from django.db import models
from accounts.models import CustomUser


class ToDo(models.Model):

    class Meta:
        db_table = 'todo'

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name='投稿ユーザ')
    name = models.CharField(max_length=200, verbose_name='ToDo名')
    content = models.CharField(max_length=10000, verbose_name='ToDo内容')
    create_date = models.DateTimeField(auto_now_add=True)
    done_date = models.DateTimeField(null=True)
    is_done = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
