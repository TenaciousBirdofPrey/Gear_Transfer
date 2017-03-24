from django import forms


class TransfersForm (forms.Form):
	from_loc = forms.CharField(max_length = 10, label = "Transfer From")
	to_loc = forms.CharField(max_length = 10, label = "Transfer To")
	item = forms.CharField(max_length = 20, label = "Item")
	drop_date= forms.DateField( label = "Delivery Date",widget = forms.SelectDateWidget )