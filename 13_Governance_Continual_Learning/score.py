import json
import numpy as np
import os
import pickle
import joblib
import onnxruntime
import logging
import time
from azureml.core.model import Model
from applicationinsights import TelemetryClient
from azureml.monitoring import ModelDataCollector
from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType


def init():
    global model, scaler, input_name, label_name, inputs_dc, prediction_dc, tc
    
    # Add your telemetry key
    tc = TelemetryClient('xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx')
    scaler_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'scaler/1/scaler.pkl')
    # deserialize the model file back into a sklearn model
    
    try:
        scaler = joblib.load(scaler_path)
    except Exception as e:
        tc.track_event('FileNotFoundException', {'error_message': str(e)}, {'FileNotFoundError': 101})
        tc.flush()

    model_onnx = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'support-vector-classifier/1/svc.onnx')
    
    try:
        model = onnxruntime.InferenceSession(model_onnx, None)
    except Exception as e:
        tc.track_event('FileNotFoundException', {'error_message': str(e)}, {'FileNotFoundError': 101})
        tc.flush()

    input_name = model.get_inputs()[0].name
    label_name = model.get_outputs()[0].name
    
    # variables to monitor model input and output data
    inputs_dc = ModelDataCollector("Support vector classifier model", designation="inputs", feature_names=["Temperature_C", "Humidity", "Wind_speed_kmph", "Wind_bearing_degrees", "Visibility_km", "Pressure_millibars", "Current_weather_condition"])
    prediction_dc = ModelDataCollector("Support vector classifier model", designation="predictions", feature_names=["Future_weather_condition"])

    
@input_schema('data', NumpyParameterType(np.array([[34.927778, 0.24, 7.3899, 83, 16.1000, 1016.51, 1]])))
@output_schema(NumpyParameterType(np.array([0])))
def run(data):

            try:              
                inputs_dc.collect(data)
            except Exception as e:
                tc.track_event('ValueNotFoundException', {'error_message': str(e)}, {'ValueError': 201})
                tc.flush()


            try:
                # scale data
                data = scaler.transform(data)
            except Exception as e: 
                tc.track_event('ScalingException', {'error_message': str(e)}, {'ScalingError': 301})     
                tc.flush()  


            try:        
                # model inference
                result = model.run([label_name], {input_name: data.astype(np.float32)})[2]
                 # this call is saving model output data into Azure Blob
                prediction_dc.collect(result)
                if result == 0:
                    output = "Rain"                 
                else: 
                    output = "No Rain"
                return output
            except Exception as e:
                    tc.track_event('InferenceException', {'error_message': str(e)}, {'InferenceError': 401})
                    tc.flush()
                    output = 'error'
                    return output 