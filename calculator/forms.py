from django import forms


class UrlForm(forms.Form):
    url = forms.CharField(label='Введи ЮРЛ', max_length=100)

    def newURL(self):
        new_url = self.cleaned_data['url']
        return new_url
