from flask import Flask, request,render_template,jasonify
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline

application = Flask(__name__)

app = application