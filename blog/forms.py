from django import forms

from .models import Post,Post1

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','imagen',)


class Post1Form(forms.ModelForm):

    class Meta:
        model = Post1
        fields = ('title','limite_a','limite_b','imagen',)
