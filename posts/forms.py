from django import forms

from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content', 'create_user', 'post']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['create_user'].required = False
        self.fields['post'].required = False
