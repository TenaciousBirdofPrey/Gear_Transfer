from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.http import HttpResponseRedirect


from transfers.models import Transfers
from django.core.serializers import serialize

from .forms import TransfersForm



#Create your views here.
def index(request):
	#sends hotel database to map
    transfers = Transfers.objects.all()
    form = TransfersForm()
    return render(request,'transfers/index.html',{
        'transfers': transfers, 'form': form,
    })

def post_transfers(request):
	form = TransfersForm(request.POST)
	if form.is_valid():
		transfer = Transfers(
			from_loc = form.cleaned_data['from_loc'],
			to_loc = form.cleaned_data['to_loc'],
			item = form.cleaned_data['item'],
			drop_date = form.cleaned_data['drop_date'],
			pick_date = form.cleaned_data['pick_date'],
			)
		transfer.save()

	return HttpResponseRedirect('/')

