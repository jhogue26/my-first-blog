from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, this is my Django assignment!</h1>")