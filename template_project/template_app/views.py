from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'text':"Hello world", 'number':100}
    return render(request, "template_app/index.html", my_dict)

def relative(request):
    return render(request, "template_app/relative_url_template.html")

def other(request):
    return render(request, "template_app/other.html")

def base(request):
    return render(request, "template_app/base.html")