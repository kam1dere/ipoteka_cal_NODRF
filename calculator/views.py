from django.shortcuts import render, redirect
from .forms import UrlForm


def my_view(request):
    if request.method == 'GET':
        form = UrlForm(request.POST)
        if form.is_valid():
            name = form.newURL
            return redirect('')
