from django.http.response import HttpResponse


def home_view(resonse):
    return HttpResponse('Home \n\n <a href="app/sports/">Sports</a>\n<a href="app/finance/">Finance</a>')