from django.shortcuts import render
from django.http import HttpResponse
from .forms import CarPredictForm
from .models import Prediction
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler


def index (response):
	return render (response,"main/index.html",{})

def predict(request):
	if request.method=="POST":
		print(request.POST)
		Year= 2020 - int(request.POST['Year'])
		# prediction = Prediction.objects.create(year=y)
		# prediction.year=y
		# prediction.Present_Price=request.POST['Present_Price']
		# prediction.Kms_Driven=request.POST['Kms_Driven']
		# prediction.Owner=request.POST['Owner']
		# prediction.Fuel_Type_Petrol=request.POST['Fuel_Type_Petrol']
		# prediction.Transmission_Manual=request.POST['Transmission_Manual']
		# prediction.save()

		Present_Price=float(request.POST['Present_Price'])
		Kms_Driven=int(request.POST['Kms_Driven'])
		Owner=int(request.POST['Owner'])
		Fuel_Type_Petrol=str(request.POST['Fuel_Type_Petrol'])
		Seller_Type_Individual=str(request.POST['Seller_Type_Individual'])
		Transmission_Manual=str(request.POST['Transmission_Manual'])
		Kms_Driven2=np.log(Kms_Driven)
		model = pickle.load(open('main/random_forest_regression_model.pkl', 'rb'))
		Fuel_Type_Diesel = 0
		if Fuel_Type_Petrol == 'Petrol':
			Fuel_Type_Petrol = 1
			Fuel_Type_Diesel = 0
		else:
			Fuel_Type_Petrol = 0
			Fuel_Type_Diesel = 1
		if Seller_Type_Individual == 'Dealer':
			Seller_Type_Individual = 1
		else:
			Seller_Type_Individual = 0
		if Transmission_Manual == 'Manual':
			Transmission_Manual = 1
		else:
			Transmission_Manual = 0
		prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
		output=round(prediction[0],2)



		dict_variable={'Year':request.POST['Year'],'Present_Price':Present_Price,'Kms_Driven':Kms_Driven,'Owner':Owner,'Fuel_Type_Petrol':request.POST['Fuel_Type_Petrol'],
		'Seller_Type_Individual':request.POST['Seller_Type_Individual'],'Transmission_Manual':request.POST['Transmission_Manual'],'Output':output}
	return render(request,"main/predict_result.html",dict_variable)


# Create your views here.
