from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, "index.html", {})


def d3e_view(request):
    return render(request, "piechart.html", {})

def rrect_view(request):
    return render(request, "roundedRect.html", {})

def burst_view(request):
    return render(request, "sunburst.html", {})

def raindrop_view(request):
    return render(request, "raindrop.html", {})

def debts_view(request):
    return render(request, "debts.html", {})


def bar_view(request):
    return render(request, "barcharts.html", {})

def tmp_view(request):
    return render(request, "temp.html", {})