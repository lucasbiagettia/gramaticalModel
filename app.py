from src.llm_client.llm_client import FireworksClient
from src.prompt.prompt_provider import get_errors_generator_prompt, get_errors_generator_prompt_with_error_type
from src.prompt.response_model import SentenceWithErrors
from dotenv import load_dotenv
import os

load_dotenv()
FIREWORKS_API_KEY = os.getenv('FIREWORKS_API_KEY')
MODEL_NAME = os.getenv('MODEL_NAME')

fireworks_client = FireworksClient(api_key=FIREWORKS_API_KEY, model=MODEL_NAME)

text = '''
Precisamente, la negociación se iniciará mientras permanece vigente la "posición común" -la política unilateral impuesta por la UE hacia Cuba en 1996 a propuesta del Gobierno del conservador español de José María Aznar-, una "garantía" exigida por varios Estados miembros para mantener la misma política hacia La Habana en el caso de que las conversaciones no den los resultados esperados.
'''

prompt = get_errors_generator_prompt_with_error_type(text)
print(prompt)



response = fireworks_client.send_message(prompt, SentenceWithErrors)
print(response)

