from django.shortcuts import render


# Create your views here.
def home(request):
    context = {"app": "my new app"}
    return render(request, "app/home.html", context)
