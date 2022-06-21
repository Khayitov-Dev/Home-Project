from django import forms
from .models import HomePlaceSale,Comment
from .snippets import choices



class HomeCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter title'}))
    categories = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categories separated by comma. Example: chinese,thai'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    location = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Location'}))
    price = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Price'}))
    vat = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Vat in %'}))
    taste = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=choices)
    persons = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}), choices=choices)
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = HomePlaceSale
        fields = ['title','image','categories','location','price','vat','taste','persons','details']
