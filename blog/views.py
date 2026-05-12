from django.http import HttpResponse

def post_list(request):
    return HttpResponse("<h1>Post List</h1>")