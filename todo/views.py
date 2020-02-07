import datetime

from django.shortcuts import redirect, render, reverse
from django.views import View
from django.views.generic import TemplateView

from .forms import NewCreateTodo
from .models import ToDo


class Index(TemplateView):
    template_name = 'todo/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["in_progress_todo"] = ToDo.objects.filter(
            todo_done_flag=0).order_by('-todo_create_date')
        context["done_todo"] = ToDo.objects.filter(
            todo_done_flag=1).order_by('-todo_create_date')
        return context


class New(View):

    def get(self, request):
        # ToDo新規追加のためのフォーム作成
        context = {
            'form': NewCreateTodo()
        }
        return render(request, 'todo/new.html', context)

    def post(self, request):
        new_todo = NewCreateTodo(request.POST)
        if not new_todo.is_valid():
            context = {
                'form': NewCreateTodo()
            }
            return render(request, 'todo/new.html', context)

        new_todo = new_todo.cleaned_data

        # フォームの入力内容を取得
        new_todo_name = new_todo['todo_name']
        new_todo_content = new_todo['todo_content']

        # モデルへ保存
        todo = ToDo(todo_name=new_todo_name,
                    todo_content=new_todo_content,
                    todo_create_date=datetime.date.today())
        todo.save()

        # indexページへリダイレクト
        return redirect(reverse('todo:index'))


class Detail(View):

    def get(self, request, todo_id):
        # モデルからデータを取得
        todo_name = ToDo.objects.get(id=todo_id).todo_name
        todo_content = ToDo.objects.get(id=todo_id).todo_content

        # 取得したデータをフォームの初期値として設定
        form_values = {
            'todo_name': todo_name,
            'todo_content': todo_content,
        }
        context = {
            'form': NewCreateTodo(initial=form_values)
        }
        return render(request, 'todo/detail.html', context)

    def post(self, request, todo_id):
        new_todo = NewCreateTodo(request.POST)
        if new_todo.is_valid():
            new_todo = new_todo.cleaned_data

            # フォームの入力内容を取得
            new_todo_name = new_todo['todo_name']
            new_todo_content = new_todo['todo_content']

            # 更新するデータを取得
            old_todo = ToDo.objects.get(id=todo_id)

            # フォームから取得した内容でデータを更新して保存
            old_todo.todo_name = new_todo_name
            old_todo.todo_content = new_todo_content
            old_todo.save()

            # indexページへリダイレクト
            return redirect(reverse('todo:index'))


class Done(View):

    def get(self, request, todo_id):
        # モデルからデータを取得
        todo = ToDo.objects.get(id=todo_id)

        #　現在時刻(ToDo完了時刻)とflagを設定し保存
        todo.todo_done_date = datetime.date.today()
        todo.todo_done_flag = 1
        todo.save()

        return redirect(reverse('todo:index'))
