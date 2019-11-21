from django.shortcuts import render

# Create your views here.



def flower_home_view(request):
    return render(request, "codeflower_index.html", {})