from django.shortcuts import render

# Create your views here.
def index(request):
    user = request.user
    return render(request, "pages/index1.html")

# def register(request):
#     return render(request, "register.html")
