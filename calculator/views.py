from django.shortcuts import render, redirect
from .forms import UrlForm


def my_view(request):

    return redirect('/test/')



