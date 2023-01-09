from django.forms import ModelForm, Textarea, NumberInput
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
        labels = {
            'quantityInGrams': ('Quantity in Grams')
        }  
        widgets = {
            'quantityInGrams': NumberInput(attrs={'rows': 1}),
        }


class GiftWrapForm(forms.Form):
    option = forms.BooleanField(required=True, label="Add gift wrapping for £1?")
    message = forms.CharField(max_length=200,widget=forms.Textarea(attrs={"rows":"2"}))
 