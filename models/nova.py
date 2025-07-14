import boto3
import json
import base64
from config import Config

session = boto3.Session(
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name=Config.AWS_REGION_NAME
)

bedrock_runtime = session.client('bedrock-runtime')

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def invoke_model_api(image_path, image_format, prompt_text):
    encoded_image = image_to_base64(image_path)
    
    kwargs = {
        "modelId": "us.amazon.nova-lite-v1:0",
        "contentType": "application/json",
        "accept": "application/json",
        "body": json.dumps({
            "inferenceConfig":{
                "max_new_tokens": 800,
                "top_p": 0.9, 
                "top_k": 15, 
                "temperature": 0.54
            },
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "image": {
                                "format": image_format,
                                "source": {"bytes": encoded_image},
                            }
                        },
                        {
                            "text": prompt_text,
                        }
                    ]
                }
            ]
        })
    }

    response = bedrock_runtime.invoke_model(**kwargs)
    generated_text = json.loads(response['body'].read().decode('utf-8'))
    return generated_text['output']['message']['content'][0]['text']