import dagshub
import mlflow

mlflow.set_tracking_uri("https://dagshub.com/AJINKYA-TEMGIRE/Emotion_Detection.mlflow")
dagshub.init(repo_owner='AJINKYA-TEMGIRE', repo_name='Emotion_Detection', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)