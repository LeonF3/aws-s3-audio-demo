# 🎙️ Audio to S3 Demo

This simple Python script demonstrates how to upload a local audio file to an Amazon S3 bucket and retrieve a public URL.

## 📦 Tech Stack
- Python 3
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (AWS SDK for Python)
- [python-dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables

---

## ⚙️ Setup

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/aws-s3-audio-demo.git
cd aws-s3-audio-demo
```

### 2. Install Dependencies
```bash
pip install boto3 python-dotenv
```

### 3. Create Your `.env` File
Rename `.env.example` to `.env` and add your AWS credentials:
```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-2
S3_BUCKET_NAME=your_bucket_name
```

### 4. Add Your Audio File
Place your `.mp4` audio file in the root directory and rename it to `sample_audio.mp4` (or update the script accordingly).

### 5. Run the Script
```bash
python audio_to_s3_demo.py
```

---

## ✅ Output
If successful, the script will print a public S3 URL like:
```
https://your_bucket_name.s3.us-east-2.amazonaws.com/demo/audio/sample_audio.mp4
```

## 🛡 Notes
- Ensure your S3 bucket permissions allow public reads or adjust ACL settings as needed.
- This is a demo and not meant for production use without proper security reviews.

---

## 📄 License
This project is open-source and available under the MIT License.

---

Built by [Leon Franklin](https://www.linkedin.com/in/leon-m-franklin-iii-813950206/) ✊🏾
