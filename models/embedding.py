import pandas as pd
import boto3
import faiss
import numpy as np
from langchain.embeddings import BedrockEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import Bedrock
from PIL import Image
import base64
import json
import matplotlib.pyplot as plt
import cv2
from tqdm import tqdm  # For progress bar
import os
from concurrent.futures import ThreadPoolExecutor
from config import Config

session = boto3.Session(
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name=Config.AWS_REGION_NAME
)

bedrock_runtime = session.client('bedrock-runtime')

bedrock_embeddings = BedrockEmbeddings(client=bedrock_runtime,model_id='amazon.titan-embed-text-v2:0')