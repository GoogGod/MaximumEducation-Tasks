from django.shortcuts import render
from .models import Advertisement
# Create your views here.

def example(request):
    advertisements = Advertisement.objects.all()
    context = {"advertisements": advertisements}
    return render(request, "index.html", context)

def top_sellers(request):
    return render(request, "top-sellers.html")