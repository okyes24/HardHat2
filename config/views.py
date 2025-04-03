from django.shortcuts import render


def  main(request):
    return render(request, "main.html")

def  top(request):
    return render(request, "top.html")

def  bottom(request):
    return render(request, "bottom.html")