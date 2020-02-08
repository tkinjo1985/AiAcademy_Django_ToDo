import datetime

from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView

from .forms import NewCreateTodo
from .models import ToDo


class Index(TemplateView):
    template_name = 'todo/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 未完了ToDoの取得
        context["in_progress_todo"] = ToDo.objects.filter(
            is_done=False).filter(is_hidden=False).order_by('-id')
        # 完了済ToDoの取得
        context["done_todo"] = ToDo.objects.filter(
            is_done=True).filter(is_hidden=False).order_by('create_date')
        return context


class New(FormView):
    template_name = 'todo/new.html'
    form_class = NewCreateTodo
    success_url = reverse_lazy('todo:index')

    def form_valid(self, form):
        new_todo_name = form.cleaned_data['todo_name']
        new_todo_content = form.cleaned_data['todo_content']
        # モデルへ保存
        todo = ToDo(name=new_todo_name,
                    content=new_todo_content,
                    create_date=datetime.date.today())
        todo.save()

        return super().form_valid(form)


class Detail(FormView):
    template_name = 'todo/detail.html'
    form_class = NewCreateTodo
    success_url = reverse_lazy('todo:index')

    def get(self, request, todo_id):
        # モデルからレコードを取得
        todo_name = ToDo.objects.get(id=todo_id).name
        todo_content = ToDo.objects.get(id=todo_id).content

        # 取得したレコードをフォームの初期値として設定
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
            edit_todo_name = new_todo['todo_name']
            edit_todo_content = new_todo['todo_content']

            # 更新するレコードを取得
            old_todo = ToDo.objects.get(id=todo_id)

            # フォームから取得した内容でレコードを更新して保存
            old_todo.name = edit_todo_name
            old_todo.content = edit_todo_content
            old_todo.save()

            # indexページへリダイレクト
            return redirect(reverse('todo:index'))


class Done(View):

    def get(self, request, todo_id):
        # モデルからレコードを取得
        todo = ToDo.objects.get(id=todo_id)

        #　現在時刻(ToDo完了時刻)と完了フラグを設定し保存
        todo.done_date = datetime.date.today()
        todo.is_done = True
        todo.save()

        return redirect(reverse('todo:index'))


class Delete(View):

    def get(self, request, todo_id):
        # モデルからレコードを取得し非表示に設定
        todo = ToDo.objects.get(id=todo_id)
        todo.is_hidden = True
        todo.save()

        return redirect(reverse('todo:index'))
