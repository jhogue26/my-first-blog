from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, this is my Django assignment!</h1>")

def post_list(request):
    return HttpResponse("<h1>Post List</h1>")