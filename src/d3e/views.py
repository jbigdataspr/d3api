from django.shortcuts import render

def home_view(request):
    return render(request, "index.html", {})

def piechart_view(request):
    return render(request, "piechart.html", {})

def rrect_view(request):
    return render(request, "roundedRect.html", {})

def burst_view(request):
    return render(request, "sunburst.html", {})

def raindrop_view(request):
    return render(request, "raindrop.html", {})

def debts_view(request):
    return render(request, "debts.html", {})

def barcharts_view(request):
    return render(request, "barcharts.html", {})

def d3dbar_view(request):
	return render(request, "d3dbar.html", {})

def relig_view(request):
	return render(request, "religions.html", {})

def bar2_view(request):
	return render(request, "bar2.html", {})

def bar3_view(request):
	return render(request, "bar3.html", {})

def ttip_view(request):
	return render(request, "tooltip.html", {})

def ttip2_view(request):
	return render(request, "tooltip2.html", {})

def heatmap_view(request):
	return render(request, "heatmap.html", {})

def globtemp_view(request):
	return render(request, "globtemp.html", {})

def realine_view(request):
    return render(request, "realine.html", {})

def contour1_view(request):
    return render(request, "contour1.html", {})

def contour2_view(request):
    return render(request, "contour2.html", {})

def contour3_view(request):
    return render(request, "contour3.html", {})

def contour4_view(request):
    return render(request, "contour4.html", {})

def tmp_view(request):
    return render(request, "temp.html", {})

def howard_view(request):
	return render(request, "howard.html", {})

def md_view(request):
	return render(request, "md.html", {})