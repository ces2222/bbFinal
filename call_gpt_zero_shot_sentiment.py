import os
from openai import OpenAI

def initialize_openai():
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI()

def get_openai_instructions():
        return "Create a sentiment score for sentences about the economy. Output is JSON with a key for each major topic with a value between -1 (most negative) and 1 (most positive).}"

def generate_openai_completion(client, sentence, instructions):
    instructions = get_openai_instructions()
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": sentence}
        ],
        seed=1985,
        response_format={ "type": "json_object" }
        )
        
    return completion

def call_gpt_zero_sentiment(sentence):
    client = initialize_openai()
    instructions = get_openai_instructions()
    return generate_openai_completion(client, sentence, instructions)
