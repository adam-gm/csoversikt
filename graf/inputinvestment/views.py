from django.shortcuts import render

#Lage "views" her
def input(request):
    return render(request, 'input.html')