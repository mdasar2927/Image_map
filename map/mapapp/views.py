from django.shortcuts import render

# Create your views here.
def map(request):
    return render(request,"map.html")
def apj(request):
    return render(request,"apj.html")
def island(request):
    return render(request,"island.html")
def pamban(request):
    return render(request,"pamban.html")
def temple(request):
    return render(request,"temple.html")
def water(request):
    return render(request,"water.html")