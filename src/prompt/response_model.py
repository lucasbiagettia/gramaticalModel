from pydantic import BaseModel

class SentenceWithErrors(BaseModel):
    correct_sentence: str
    incorrect: str
    explanation: str
