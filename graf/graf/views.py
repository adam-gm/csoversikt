from django.shortcuts import render

#Lage "views" her
def index(request):
    return render(request, 'index.html')


