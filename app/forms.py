from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail', 
        'Category', 'main_cat')

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'col-lg-12',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('content', )        


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'col-lg-12',
        'placeholder': 'Type your comment',
        'id': 'message',
        'rows': '6'
    }))