"""d3vz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from d3e.views import d3e_view, home_view, rrect_view, burst_view, raindrop_view, debts_view, bar_view, tmp_view
from codeflower.views import flower_home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('d3/', home_view, name='d3 home'),
    path('d3/piechart', d3e_view, name='d3e'),
    path('d3/roundedrect', rrect_view, name='RoundedRectangles'),
    path('d3/sunburst', burst_view, name='sunburst'),
    path('d3/raindrop', raindrop_view, name='raindrop'),
    path('d3/debts', debts_view, name='debts'),
    path('d3/bar', bar_view, name='barcharts'),
    path('d3/tmp', tmp_view, name='barcharts'),
    path('flower/', flower_home_view, name='CodeFlower'),
]
