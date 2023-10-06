from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

# Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            promoted = int(request.form.get('promoted')),
            review = float(request.form.get('review')),
            projects = int(request.form.get('projects')),
            salary = int(request.form.get('salary')),
            tenure = float(request.form.get('tenure')),
            satisfaction = float(request.form.get('satisfaction')),
            bonus = int(request.form.get('bonus')),
            avg_hrs_month = float(request.form.get('avg_hrs_month'))
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df.info())

        pred_pipeline = PredictPipeline()
        result = pred_pipeline.predict(pred_df)
        if result[0].tolist() == 0:
            return render_template('home.html', result="stay")
        elif result[0].tolist() == 1:
            return render_template('home.html', result="left")
        return render_template('home.html', result=result[0])
        
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)