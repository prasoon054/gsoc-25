from minio import Minio
from minio.error import S3Error

# Connect to local MinIO
client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)
bucket_name = "testbucket"

# Create a bucket if it doesn't exist
if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)
    print(f"Bucket '{bucket_name}' created.")
else:
    print(f"Bucket '{bucket_name}' already exists.")

# Upload a file
file_path = "example.txt"
with open(file_path, "w") as f:
    f.write("Hello from MinIO!")

client.fput_object(bucket_name, "example.txt", file_path)
print("File uploaded.")

# List files in the bucket
print("Listing objects:")
for obj in client.list_objects(bucket_name):
    print(obj.object_name)
