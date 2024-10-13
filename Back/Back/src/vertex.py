import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting
import json

from google.oauth2 import service_account
# Load the service account key file
#with open('D:\\Users\\dragn\\Escritorio\\Hackaton\\gcp-banorte-hackaton-team-38-ee1e96b2a6d6.json') as source:
#    info = json.load(source)

# Create credentials object
#credentials = service_account.Credentials.from_service_account_info(info)

# Now use these credentials with the Vertex AI client library
from google.cloud import aiplatform
#vertexai.init(credentials=credentials, project="gcp-banorte-hackaton-team-38")


def generate_investment_plan(text1, textsi_1):
    #vertexai.init(project="gcp-banorte-hackaton-team-38", location="us-central1", credentials="D:\\Users\\dragn\\Escritorio\\Hackaton\\gcp-banorte-hackaton-team-38-ee1e96b2a6d6.json")
    vertexai.init(location="us-central1", project="gcp-banorte-hackaton-team-38")

    model = GenerativeModel(
        "gemini-1.5-flash-002",
        system_instruction=[textsi_1]
    )

    generation_config = {
        "max_output_tokens": 8192,
        "temperature": 1,
        "top_p": 0.95,
    }

    safety_settings = [
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
    ]
    responses = model.generate_content(
        [text1],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )
    full_response = "".join([response.text for response in responses])
    print(full_response)
    return "full_response"
