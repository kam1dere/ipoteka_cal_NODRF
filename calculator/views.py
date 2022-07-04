from django.shortcuts import render, redirect
from .forms import UrlForm


def my_view(request):
    if request.method == 'GET':
        form = UrlForm(request.GET)
        return render(request, 'redir.html', {'form': form})
