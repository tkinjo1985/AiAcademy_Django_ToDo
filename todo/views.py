import datetime

from django.shortcuts import get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NewCreateTodo
from .models import ToDo


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'todo/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 未完了ToDoの取得
        context["in_progress_todo"] = ToDo.objects.filter(
            is_done=False, is_hidden=False).order_by('-id')
        # 完了済ToDoの取得
        context["done_todo"] = ToDo.objects.filter(
            is_done=True, is_hidden=False).order_by('create_date')

        return context


class New(LoginRequiredMixin, CreateView):
    template_name = 'todo/new.html'
    form_class = NewCreateTodo
    success_url = reverse_lazy('todo:index')

    #　新規ToDoの作成
    def form_valid(self, form):
        new_todo = form.save(commit=False)
        new_todo.create_date = datetime.date.today()
        new_todo.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class Detail(LoginRequiredMixin, FormView):
    template_name = 'todo/detail.html'
    form_class = NewCreateTodo
    success_url = reverse_lazy('todo:index')

    # 保存済ToDoをFormの初期値に設定
    def get_initial(self):
        initial = super().get_initial()
        todo_id = self.kwargs["todo_id"]
        todo = get_object_or_404(ToDo, pk=todo_id)
        initial = {
            'name': todo.name,
            'content': todo.content,
        }

        return initial

    # ToDoの更新
    def form_valid(self, form):
        todo_id = self.kwargs["todo_id"]
        old_todo = get_object_or_404(ToDo, pk=todo_id)
        new_todo = NewCreateTodo(self.request.POST, instance=old_todo)
        new_todo.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class Done(LoginRequiredMixin, View):

    def get(self, request, todo_id):
        # モデルからレコードを取得
        todo = get_object_or_404(ToDo, pk=todo_id)

        #　現在時刻(ToDo完了時刻)と完了フラグを設定し保存
        todo.done_date = datetime.date.today()
        todo.is_done = True
        todo.save()

        return redirect(reverse('todo:index'))


class Delete(LoginRequiredMixin, View):

    def get(self, request, todo_id):
        # モデルからレコードを取得し非表示に設定
        todo = get_object_or_404(ToDo, pk=todo_id)
        todo.is_hidden = True
        todo.save()

        return redirect(reverse('todo:index'))
