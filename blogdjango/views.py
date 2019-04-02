from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Let`s Rock!</h1>')
