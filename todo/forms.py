from django import forms

from .models import ToDo


class NewCreateTodo(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = ("name", "content")

    content = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'ToDoの内容を入力してください。'}), label='内容',)

    def __init__(self, *args, **kwargs):
        super(NewCreateTodo, self).__init__(*args, **kwargs)
        self.fields["name"].label = 'ToDo名'
        self.fields["name"].widget.attrs = {'placeholder': 'ToDo名を入力してください。'}
