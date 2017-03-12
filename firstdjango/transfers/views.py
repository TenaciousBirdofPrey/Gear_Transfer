from django.shortcuts import render
from django.http import Http404

from transfers.models import Hotels

# Create your views here.
def index(request):
    hotels = Hotels.objects.all()
    return render(request,'transfers/index.html',{
        'hotels':hotels,
    })