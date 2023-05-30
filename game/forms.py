from django import forms

class EntryForm(forms.Form):
    your_guess = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z]+', 'title':'Enter Characters Only '}))
