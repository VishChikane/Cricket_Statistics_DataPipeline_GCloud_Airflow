# Function to upload file to GCS bucket
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    # Set environment variable for Google Cloud credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cloud-etl-project-446709-fa37b207b9e4.json"

    # Initialize a GCS client
    storage_client = storage.Client()
    
    # Get the GCS bucket
    bucket = storage_client.bucket(bucket_name)
    
    # Create a new blob and upload the file
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    
    print(f"File {source_file_name} uploaded to {destination_blob_name} in bucket {bucket_name}.")

# GCS bucket details
bucket_name = 'bkt-dev-employee-data'
source_file_name = 'employee_data.csv'
destination_blob_name = 'employee_data.csv'

# Upload the file to GCS bucket
upload_to_gcs(bucket_name, source_file_name, destination_blob_name)