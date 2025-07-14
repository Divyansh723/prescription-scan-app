import boto3
import json
import base64
from config import Config

session = boto3.Session(
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name='us-east-1'  # Replace with your desired region
)

bedrock_runtime = session.client('bedrock-runtime')

def invoke_model_api_for_text( prompt_text):
    kwargs = {
        "modelId": "amazon.titan-text-premier-v1:0",
        "contentType": "application/json",
        "accept": "application/json",
        "body": json.dumps({
            "inputText": prompt_text,
            "textGenerationConfig": {
                "maxTokenCount": 1000,
                "temperature": 0.67,
                # "top_p": 0.9,
            }
        })
    }
    response = bedrock_runtime.invoke_model(**kwargs)
    generated_text = json.loads(response['body'].read().decode('utf-8'))
    return generated_text["results"][0]["outputText"]

def main():
    prompt_text = "Translate 'Hello, how are you?' to French."
    result = invoke_model_api_for_text(prompt_text)
    print("Translated Text:", result)

if __name__ == "__main__":
    main()