from django import forms

from .models import Comments, User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content', 'create_user', 'post']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['create_user'].required = False
        self.fields['post'].required = False


class UserForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField(required=False)
    desc = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'avatar', 'desc']

