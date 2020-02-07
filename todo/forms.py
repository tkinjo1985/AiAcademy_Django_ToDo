from django import forms


class NewCreateTodo(forms.Form):
    todo_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'ToDo名を入力してください。'}), label='ToDo名')
    todo_content = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'ToDoの内容を入力してください。'}), label='内容',)
