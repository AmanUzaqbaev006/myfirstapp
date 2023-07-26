from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'first_name', 'text', 'time_one', 'time_two','time_on','time']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),

            
            
           
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'time_one': forms.TextInput(attrs={'class': 'form-control'}),
            'time_on': forms.TextInput(attrs={'class': 'form-control'}),
            'time_two': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.TextInput(attrs={'class': 'form-control'}),
        }




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }

