import os
from openai import OpenAI

def call_gpt(sentence):
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI()
    instructions = "Your role is to classify sentences as either being about the manufacturing sector of the economy or not. You will respond with a json object with a key of manufacturing with a value of 1 or 0."
    positive_example = "Manufacturing activity was robust, though demand for certain discretionary products slowed."
    negative_example = "Leisure travel activity softened, but business and convention bookings continued to improve."
    positive_example_response = "{'manufacturing': 1}"
    negative_example_response = "{'manufacturing': 0}"
    sentence = "Nonfinancial services firms generally reported moderate growth and solid demand but some expressed uncertainty about the future."

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": positive_example},
            {"role": "assistant", "content": positive_example_response},
            {"role": "user", "content": negative_example},
            {"role": "assistant", "content": negative_example_response},
            {"role": "user", "content": sentence}
        ])
    return completion.choices[0].message