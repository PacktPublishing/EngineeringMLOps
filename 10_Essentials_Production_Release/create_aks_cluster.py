import numpy as np
import azureml.core
from azureml.core import Workspace
from azureml.core.model import Model
from azureml.core.compute import ComputeTarget
from azureml.core.compute_target import ComputeTargetException
from azureml.core.compute import AksCompute, ComputeTarget

ws = Workspace.from_config()
print(ws.name, ws.resource_group, ws.location, sep = '\n')

# Choose a name for your AKS cluster
aks_name = 'prod-aks' 

# Verify that cluster does not exist already
try:
    aks_target = ComputeTarget(workspace=ws, name=aks_name)
    print('Found existing cluster, use it.')
except ComputeTargetException:
    # Use the default configuration (can also provide parameters to customize)
    prov_config = AksCompute.provisioning_configuration()

    # Create the cluster
    aks_target = ComputeTarget.create(workspace = ws, 
                                    name = aks_name, 
                                    provisioning_configuration = prov_config)

if aks_target.get_status() != "Succeeded":
    aks_target.wait_for_completion(show_output=True)