from django import forms


class NewCreateTodo(forms.Form):
    todo_name = forms.CharField(
        widget=forms.TextInput, label='ToDo名')
    todo_content = forms.CharField(widget=forms.Textarea, label='ToDoの内容')
