from django.apps import AppConfig
#import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from django.http import HttpResponse
#from .models import Prediction
model = pickle.load(open('main/random_forest_regression_model.pkl', 'rb'))

class MainConfig(AppConfig):

    #print(prediction.year)
    name = 'main'

    #print(input2.year)
