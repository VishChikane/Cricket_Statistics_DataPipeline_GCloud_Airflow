from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "learning-gcp-vish"
    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bkt-bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://bkt-cricket-project-dataflow-metadata/udf.js",
        "JSONPath": "gs://bkt-cricket-project-dataflow-metadata/icc_odi_batsman_ranking.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "cloud-etl-project-446709:cricket_dataset.icc_odi_batsman_ranking",
        "inputFilePattern": "gs://bkt-cricket-stat-project/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://bkt-cricket-project-dataflow-metadata",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
