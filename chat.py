import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_APIM_MODEL_ENDPOINT")
#endpoint = os.getenv("AZURE_AI_FOUNDRY_MODEL_ENDPOINT")
deployment_name = os.getenv("MODEL_DEPLOYMENT_NAME")
print(f"endpoint: {endpoint}, model_deployment: {deployment_name}")
client = ChatCompletionsClient(endpoint=endpoint, credential=DefaultAzureCredential(), credential_scopes=["https://cognitiveservices.azure.com/.default"])

response = client.complete(
  messages=[UserMessage(content="Capital of France?")],
  max_tokens=100,
  model = deployment_name,
)

print(response)
