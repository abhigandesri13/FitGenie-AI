import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FBEFJLmmFQFBsDyoPKgOkvq1G2o10at6dhEzO5Kfnogw")
PROJECT_ID = os.getenv("a0113ebe-fa2d-4b69-bc78-e1887f387d28")
URL = os.getenv("https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/18708a3e-47b3-41de-8e17-73acaabbffdc")

MODEL_ID = "ibm/granite-4-h-small"
