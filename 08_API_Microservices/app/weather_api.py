import uvicorn
from fastapi import FastAPI
from variables import WeatherVariables
import numpy
import pickle
import pandas as pd
import onnxruntime as rt

# Create app object 
app = FastAPI()

# Load model scalar
pickle_in = open("artifacts/model-scaler.pkl", "rb")
scaler = pickle.load(pickle_in)

# Load the model
sess = rt.InferenceSession("artifacts/svc.onnx")
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name

# API Endpoints
@app.get('/')
def index():
    return {'Hello': 'Welcome to weather prediction service, access the api docs and test the API at http://0.0.0.0/docs.'}


@app.post('/predict')
def predict_weather(data: WeatherVariables):
    data = data.dict()

    # fetch input data using data varaibles
    temp_c = data['temp_c']
    humidity = data['humidity']
    wind_speed_kmph = data['wind_speed_kmph']
    wind_bearing_degree = data['wind_bearing_degree']
    visibility_km = data['visibility_km']
    pressure_millibars = data['pressure_millibars']
    current_weather_condition = data['current_weather_condition']

    data_to_pred = numpy.array([[temp_c, humidity, wind_speed_kmph, wind_bearing_degree,
                                 visibility_km, pressure_millibars, current_weather_condition]])

    # Scale input data
    data_to_pred = scaler.fit_transform(data_to_pred.reshape(1, 7))

    # Model inference
    prediction = sess.run(
        [label_name], {input_name: data_to_pred.astype(numpy.float32)})[0]

    if(prediction[0] > 0.5):
        prediction = "Rain"
    else:
        prediction = "No_Rain"
    return {
        'prediction': prediction
    }
