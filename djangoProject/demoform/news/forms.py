from attr import attr
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','time_created',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'tieude123'}),
            'content': forms.Textarea(attrs={'class': 'noidung204000'})
        }


class SendEmail(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'tieude'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'baohung', 'id':'noidung'}))
    cc = forms.BooleanField(required=False)