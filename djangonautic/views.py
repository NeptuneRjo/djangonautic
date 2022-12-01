from django.http import HttpResponse


def home_page(request):
    return HttpResponse('home')


def about(request):
    return HttpResponse('about')
