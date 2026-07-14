from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

from config import *

credentials = Credentials(
    url=URL,
    api_key=API_KEY
)

model = ModelInference(
    model_id=MODEL_ID,
    credentials=credentials,
    project_id=PROJECT_ID
)

def generate_plan(prompt):

    response = model.generate_text(prompt=prompt)

    return response
