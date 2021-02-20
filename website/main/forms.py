from django import forms

class CarPredictForm(forms.Form):
    Year=forms.IntegerField()
    Present_Price=forms.IntegerField()
    Owner=forms.IntegerField()
    Fuel_Type_Petrol=forms.ChoiceField()
    Seller_Type_Individual=forms.ChoiceField()
    Transmission_Manual=forms.ChoiceField()
