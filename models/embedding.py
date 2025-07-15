import boto3
from langchain.embeddings import BedrockEmbeddings
import json
import base64
from config import Config

session = boto3.Session(
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name=Config.AWS_REGION_NAME
)

bedrock_runtime = session.client('bedrock-runtime')

bedrock_embeddings = BedrockEmbeddings(client=bedrock_runtime,model_id='amazon.titan-embed-text-v2:0')