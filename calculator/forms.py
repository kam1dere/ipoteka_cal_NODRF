from django import forms


class UrlForm(forms.Form):
    url = forms.CharField(label='Введи ЮРЛ', max_length=100)