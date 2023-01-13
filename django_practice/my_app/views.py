from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect

# Create your views here.

article = {
    'sports':'Sports stection page',
    'weather':'Weather time page',
    'finance':'Be rich page <b><b><h1>Hey yooooo</h1>',
    'joy':'Im great!!!!!'
}


def simple_view(request):
    return render(request, 'my_app/example.html')