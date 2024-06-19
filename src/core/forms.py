from django import forms


class GenerationQuantityForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label="Quantity")
