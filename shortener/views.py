from django.shortcuts import render,get_object_or_404,redirect

from .models import Url

def root(request,url_hash):
    url = get_object_or_404(Url,url_hash=url_hash)
    url.clicked()
    return redirect(url.full_url)


