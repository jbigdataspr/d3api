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
from django.views.generic.base import RedirectView
from d3e.views import home_view, rrect_view, burst_view, ttip_view, ttip2_view, \
	 piechart_view, d3dbar_view, relig_view, bar2_view, bar3_view, \
	 raindrop_view, debts_view, barcharts_view, tmp_view, \
	 heatmap_view, globtemp_view, realine_view, contour1_view, \
	 contour2_view, contour3_view, contour4_view, howard_view, md_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('d3/', home_view, name='d3 home'),
    path('d3/pie/', piechart_view, name='piechart'),
    path('d3/roundedrect/', rrect_view, name='RoundedRectangles'),
    path('d3/sunburst/', burst_view, name='sunburst'),
    path('d3/raindrop/', raindrop_view, name='raindrop'),
    path('d3/debts', debts_view, name='debts'),
    path('d3/bar/', barcharts_view, name = 'barcharts'),
	path('d3/bar2/', bar2_view, name = 'bar2'),
	path('d3/bar3/', bar3_view, name = 'bar3'),
	path('d3/d3dbar/', d3dbar_view, name = 'd3dBar'),
	path('d3/ttip/', ttip_view, name = 'tooltips'),
	path('d3/ttip2/', ttip2_view, name = 'tooltips2'),
	path('d3/howard/', howard_view, name = 'howard_tooltips2'),
	path('d3/md/', md_view, name = 'md_tooltips2'),
	path('d3/religions/', relig_view, name = 'religions'),
	path('d3/heatmap/', heatmap_view, name = 'heatmap'),
	path('d3/globtemp/', globtemp_view, name = 'heatmap'),
	path('d3/realine/', realine_view, name = 'RealTime'),
	path('d3/contour1/', contour1_view, name = 'contour1'),
	path('d3/contour2/', contour2_view, name = 'contour2'),
	path('d3/contour3/', contour3_view, name = 'contour3'),
	path('d3/contour4/', contour4_view, name = 'contour4'),
    path('d3/tmp/', tmp_view, name='tmp'),
	path('', RedirectView.as_view(url='d3/', permanent=False), name='index'),
]
