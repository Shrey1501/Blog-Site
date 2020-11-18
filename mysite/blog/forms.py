from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
# "editable medium-editor-textarea" class is used to edit the content in the text area while writing a post or comment. It can be used to make the text bold, italic, underline, and can be converted to h1, h2 and so on....
    class Meta():
        model = Post
        fields = ('author','title','text')
        widgets = {
        'title': forms.TextInput(attrs={'class':'textinputclass'}),
        'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')
        widgets = {
        'author': forms.TextInput(attrs={'class':'textinputclass'}),
        'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea'})

        }
