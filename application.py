from flask import Flask, request,render_template,jasonify
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline

application = Flask(__name__)

app = application


@app.route('/')

def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')

    else:
        data = CustomData(
            
        )