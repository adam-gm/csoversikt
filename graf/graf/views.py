from django.shortcuts import render
from graf.investment import lastInnLagretData

#Lage "views" her
def index(request):
    return render(request, 'index.html', 'index2.html')

def getSavedInvestments(request):
    data  = lastInnLagretData()
    return render(request, 'index3.html', {'data': data})