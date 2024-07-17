from django.shortcuts import render
# from pro_app.models import User
from pro_app.forms import NewUserForm

# Create your views here.

def index(request):
    my_dict = {"inserted": "This is the home Page"}
    return render(request, "pro_app/index.html", context=my_dict)

def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid:
            form.save(commit = True)
            return index(request)
        else:
            print("ERROR ON THE FORM")


    return render(request, "pro_app/users.html", {"form": form})
    