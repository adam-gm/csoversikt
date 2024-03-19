from django.shortcuts import render
import investment

#Lage "views" her
def index(request):
    return render(request, 'index.html')

def getSavedInvestments(request):
    data  = investment.lastInnLagretData()
    return render(request, 'index3.html', {'data': data})