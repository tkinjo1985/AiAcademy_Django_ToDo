import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, UpdateView

from .forms import ToDoForm
from .models import ToDo

import json

from django.utils import timezone


class UserIdCheck(UserPassesTestMixin):
    """
    ログインユーザーとToDo所有ユーザーの適合チェック

    """

    def test_func(self):
        todo_id = self.kwargs["pk"]
        todo = get_object_or_404(ToDo, pk=todo_id)
        user_id = self.request.user.id

        return todo.user_id == user_id

    def handle_no_permission(self):
        return render(self.request, 'todo/no_permission.html')


class Index(LoginRequiredMixin, TemplateView):
    """
    Indexページ:
    未完了/完了済ToDoの表示
    """
    template_name = 'todo/index.html'

    def get_context_data(self, **kwargs):
        """
        未完了/完了済ToDを取得しTemplateの変数に追加

        Returns
        -------
        context : dic
        未完了/完了済ToD
        """
        user_id = self.request.user.id
        context = super().get_context_data(**kwargs)
        context["user_name"] = self.request.user.username
        # 未完了ToDoの取得
        context["in_progress_todo"] = ToDo.objects.filter(user_id=user_id,
                                                          is_done=False,
                                                          is_hidden=False).order_by('-id')
        # 完了済ToDoの取得
        context["done_todo"] = ToDo.objects.filter(user_id=user_id,
                                                   is_done=True,
                                                   is_hidden=False).order_by('create_date')

        return context


class New(LoginRequiredMixin, CreateView):
    """
    新規ToDo作成View:
    GETアクセス時はからのフォームを表示
    POSTアクセス時はform_validメソッドでToDo作成
    """
    form_class = ToDoForm
    template_name = 'todo/new.html'
    success_url = reverse_lazy('todo:index')

    def form_valid(self, form):
        """
        バリデーションに問題がなけれなToDoを保存
        """
        new_todo = form.save(commit=False)
        # ログイン中ユーザーをToDo所有ユーザーに設定
        new_todo.user_id = self.request.user.id
        new_todo.save()

        return super().form_valid(form)


class Update(LoginRequiredMixin, UserIdCheck, UpdateView):
    """
    ToDo更新View:
    GETアクセス時は登録済ToDoをフォームの初期値に設定
    バリデーションに問題がなければToDoを更新
    """
    model = ToDo
    field = ['name', 'content']
    form_class = ToDoForm
    template_name = 'todo/update.html'
    success_url = reverse_lazy('todo:index')

    def get_initial(self):
        """
        保存済ToDoをFormの初期値に設定

        Returns
        -------
        initial : dic
        保存済ToDo name: ToDo名
                  context: ToDoの内容
        """
        initial = super().get_initial()
        todo_id = self.kwargs["pk"]

        todo = get_object_or_404(ToDo, pk=todo_id)
        initial = {
            'name': todo.name,
            'content': todo.content,
        }
        return initial


class Done(LoginRequiredMixin, UserIdCheck, View):
    """
    ToDo完了処理View:
    """

    def get(self, request, pk):
        """
        ToDoを完了済ステータスに変更する

        Parameters
         ----------
        pk : int
        todoのid
        """
        # モデルからレコードを取得
        todo = get_object_or_404(ToDo, pk=pk)

        #　現在時刻(ToDo完了時刻)と完了フラグを設定し保存
        todo.done_date = timezone.now()
        todo.is_done = True
        todo.save()

        return redirect(reverse('todo:index'))


class Delete(LoginRequiredMixin, UserIdCheck, View):
    """
    ToDo削除処理View
    """

    def get(self, request, pk):
        """
        ToDoを削除(非表示に)する

        Parameters
         ----------
        pk : int
        todoのid
        """
        # モデルからレコードを取得し非表示に設定
        todo = get_object_or_404(ToDo, pk=pk)
        # 非表示フラグをTrueに設定
        todo.is_hidden = True
        todo.save()

        return redirect(reverse('todo:index'))
