from django import forms

class NameForm(forms.Form):
    postlink = forms.CharField(label='enter post url', max_length=100)