from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello world')


def func(request):
    return HttpResponse('salom')
