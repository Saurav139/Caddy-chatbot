import boto3
import json

# Hardcoded credentials for testing
aws_access_key = "AKIAYCZECK2KFJ4YKVTP"
aws_secret_key = "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"
region = "us-east-2"
model_id = "amazon.titan-embed-text-v2:0"

# Initialize the Bedrock client
client = boto3.client(
    "bedrock-runtime",
    region_name=region,
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

# Test payload
payload = {
    "inputText": "Hello, this is a test."
}

try:
    response = client.invoke_model(
        modelId=model_id,
        body=json.dumps(payload)
    )
    print(response)
except Exception as e:
    print(f"Error: {e}")
