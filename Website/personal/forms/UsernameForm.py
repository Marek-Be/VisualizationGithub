from django import forms

class NameForm(forms.Form):
    post = forms.CharField(label='5523', max_length=100)