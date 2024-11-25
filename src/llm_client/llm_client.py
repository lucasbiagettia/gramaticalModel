from fireworks.client import Fireworks
from pydantic import BaseModel

class FireworksClient():
    def __init__(self, api_key: str, model: str):
        self.model = model
        self.client = Fireworks(api_key=api_key)

    def send_message(self, prompt: str, response_model: BaseModel):
        response = self.client.chat.completions.create(
            model=self.model,
            response_format={
                "type": "json_object", 
                "schema": response_model.model_json_schema()
            },
            messages=[{
                "role": "user",
                "content": prompt
            }],
            temperature=0.1
        )
        return response.choices[0].message.content