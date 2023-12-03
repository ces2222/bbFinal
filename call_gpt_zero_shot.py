import os
from openai import OpenAI

def initialize_openai():
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI()

def get_openai_instructions():
        return "Classify sentences as being about five key topics from the economy: credit conditions, household spending, inflation, investment, and labor market conditions. Respond with a json object with a key for each topic with a value of 1 or 0."

def generate_openai_completion(client, sentence, instructions):
    instructions = get_openai_instructions()
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": sentence}
        ])

    return completion

def call_gpt_zero(sentence):
    client = initialize_openai()
    instructions = get_openai_instructions()
    return generate_openai_completion(client, sentence, instructions)
