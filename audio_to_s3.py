# audio_to_s3_demo.py
"""
This script demonstrates how to upload a file to AWS S3 and return a public URL.

🔐 Make sure to create a .env file with your AWS credentials:
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
S3_BUCKET_NAME=
"""

import boto3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# Initialize S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def upload_file_to_s3(file_path, object_key):
    """
    Uploads a file to S3 and returns a public URL.

    :param file_path: Local path to file
    :param object_key: Desired S3 key (path inside the bucket)
    """
    try:
        s3.upload_file(
            file_path,
            S3_BUCKET_NAME,
            object_key,
            ExtraArgs={"ACL": "public-read"}  # Make file public
        )
        public_url = f"https://{S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{object_key}"
        print(f"✅ Uploaded successfully: {public_url}")
        return public_url
    except Exception as e:
        print(f"❌ Failed to upload: {e}")
        return None

if __name__ == "__main__":
    # Sample usage
    local_file = "sample_audio.mp4"
    s3_key = f"demo/audio/{local_file}"
    upload_file_to_s3(local_file, s3_key)
