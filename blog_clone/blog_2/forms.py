from django import forms
from .models import Post,Comments


class PostForm(forms.ModelForm):

    class Meta():
        model=Post
        fields=('title','text','author')

        widgets={
            'title' : forms.TextInput(attrs={'class':'textinputclass'}),
            'text' :  forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):


    class Meta():
        model=Comments
        fields=('text','author')

        widgets={
            'author' :  forms.TextInput(attrs={'class':'textinputclass'}),
            'text' :    forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }
