from django import forms


class PostForm(forms.Form):
    title = forms.CharField()
    photo = forms.ImageField()