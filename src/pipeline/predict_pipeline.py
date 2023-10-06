import sys
import numpy as np
import pandas as pd
import pickle

from src.exception import CustomException

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self, features):
        model = pickle.load(open('src/pipeline/RFC_Model.sav', 'rb'))
        preprocessor = pickle.load(open('src/pipeline/scaler.sav', 'rb'))
        data_scaled = preprocessor.transform(features)
        pred = model.predict(data_scaled)
        return pred

class CustomData:
    def __init__(self, promoted: int, review: float, projects: int, salary: int, 
                 tenure: float, satisfaction: float, bonus: int, avg_hrs_month: float):
        self.promoted = promoted
        self.review = review
        self.projecs = projects
        self.salary = salary
        self.tenure = tenure
        self.satisfaction = satisfaction
        self.bonus = bonus
        self.avg_hrs_month = avg_hrs_month

    def get_data_as_data_frame(self):
        input_dict = {
            "promoted": [self.promoted],
            "review": [self.review],
            "projects": [self.projecs],
            "salary": [self.salary],
            "tenure": [self.tenure],
            "satisfaction": [self.satisfaction],
            "bonus": [self.bonus],
            "avg_hrs_month": [self.avg_hrs_month]
        }
        
        return pd.DataFrame(input_dict)

import os
print(os.getcwd())