from django import forms


class TransfersForm (forms.Form):
	from_loc = forms.CharField(max_length = 10)
	to_loc = forms.CharField(max_length = 10)
	item = forms.CharField(max_length = 20)