from django import forms


class UrlForm(forms.Form):
    url = forms.CharField(label='первичный взнос', max_length=100, required=False)
    second = forms.CharField(label='ставка', max_length=100, required=False)
    term = forms.CharField(label='сумма', max_length=100, required=False)

