from google.cloud import storage

csv_filename = 'batsmen_rankings.csv'
bucket_name = 'bkt-cricket-stat-project'
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
destination_blob_name = f'{csv_filename}'  # The path to store in GCS

blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(csv_filename)

print(f"File {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")
