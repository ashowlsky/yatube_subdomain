from django import forms
from posts.models import Post, Group

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group',)

    def clean_text(self):
        data = self.cleaned_data['text']
        if data == '':
            raise forms.ValidationError('error error')
        return data