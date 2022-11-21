from azureml.core import Environment, Experiment, Workspace
from azureml.core.model import InferenceConfig, Model
from azureml.core.webservice import LocalWebservice


# enter details of your AzureML workspace
ws = Workspace(subscription_id = "921b1060-fc07-42c5-8bad-c255bbf99a42", resource_group = "rgrg", workspace_name = "mlws")

# model = run.register_model(model_name = 'diabetes_model', model_path = 'best_estimator/model.pkl')
model = Model(workspace=ws, name='redbrakeqrwl9fj3', version=1)

env = Environment.from_conda_specification('env24', "../json/conda.yml")

env.register(ws)

inference_config = InferenceConfig(
    environment=env,
    source_directory=".",
    entry_script="./score.py",
)

deployment_config = LocalWebservice.deploy_configuration(port=6789)

service = Model.deploy(
    workspace = ws,
    name = 'deployment24',
    models = [model],
    inference_config = inference_config,
    deployment_config = deployment_config,
    overwrite=True)
    
service.wait_for_deployment(show_output=True)


