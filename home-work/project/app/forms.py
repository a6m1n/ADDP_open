from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    def save(self):
        Post.objects.create(title=self.cleaned_data['title'])

    class Meta:
        model = Post
        fields = ('title',)