import json
import numpy as np
import os
import pickle
import joblib
import onnxruntime
import time
from azureml.core.model import Model
from azureml.monitoring import ModelDataCollector
from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType

def init():
    global model, scaler, input_name, label_name, inputs_dc, prediction_dc
    

    scaler_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'scaler/1/scaler.pkl')
    # deserialize the model file back into a sklearn model
    scaler = joblib.load(scaler_path)
    
    model_onnx = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'support-vector-classifier/1/svc.onnx')
    # print(os.listdir(model_onnx))
    model = onnxruntime.InferenceSession(model_onnx, None)
    input_name = model.get_inputs()[0].name
    label_name = model.get_outputs()[0].name
    
    # variables to monitor model input and output data
    inputs_dc = ModelDataCollector("Support vector classifier model", designation="inputs", feature_names=["feat1", "feat2", "feat3", "feat4", "feat5", "feat6", "feat7"])
    prediction_dc = ModelDataCollector("Support vector classifier model", designation="predictions", feature_names=["weatherprediction"])

    
@input_schema('data', NumpyParameterType(np.array([[34.927778, 0.24, 7.3899, 83, 16.1000, 1016.51, 1]])))
@output_schema(NumpyParameterType(np.array([0])))
def run(data):
                try: 
                    data = scaler.fit_transform(data.reshape(1, 7))
                    inputs_dc.collect(data)
                    
                    # model inference
                    result = model.run([label_name], {input_name: data.astype(np.float32)})[0]
                    # this call is saving model output data into Azure Blob
                    prediction_dc.collect(result)

                 
                except Exception as e:   
                    result = 'error'
                    prediction_dc.collect(result)
                    
                return result.tolist()    