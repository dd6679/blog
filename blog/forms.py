from django import forms


class PostForm(forms.Form):
    title = forms.CharField()
    post_text = forms.CharField(widget=forms.Textarea)
    public = forms.BooleanField()