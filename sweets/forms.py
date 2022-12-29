from django.forms import ModelForm, Textarea
from .models import Cart
from django import forms


class CartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['quantityInGrams'].widget.attrs.update(
                            {'class': 'form-control'})

    class Meta:
        model = Cart
        fields = ['quantityInGrams']    
        widgets = {
            'quantityInGrams': Textarea(attrs={'rows': 1}),
        }