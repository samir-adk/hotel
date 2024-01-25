from resturant.models import Book
from django.forms import ModelForm,Textarea
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields=['arrival_date','departure_time','room','no_guests','phone','message']
		widgets = { 
        'arrival_date': DateInput(), 
        'departure_time':DateInput(),
        'message':Textarea(attrs={'cols':10,'rows':10})
            }


class FrontBook(ModelForm):
	class Meta:
		model=Book
		fields=['arrival_date','departure_time','no_guests','phone','message']
		widgets = { 
	    'arrival_date': DateInput(), 
	    'departure_time':DateInput(),
	    'message':Textarea(attrs={'cols':10,'rows':10})
	        }


