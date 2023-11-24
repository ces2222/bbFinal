import os
from openai import OpenAI

def call_gpt(sentence):
    def initialize_openai():
        OpenAI.api_key = os.getenv("OPENAI_API_KEY")
        return OpenAI()

    def get_openai_instructions():
        return "Your role is to classify sentences as either being about the manufacturing sector of the economy or not. You will respond with a JSON object with a key of manufacturing with a value of 1 or 0."

    def get_openai_examples():
        positive_example = "Manufacturing activity was robust, though demand for certain discretionary products slowed."
        negative_example = "Leisure travel activity softened, but business and convention bookings continued to improve."
        positive_example_response = "{'manufacturing': 1}"
        negative_example_response = "{'manufacturing': 0}"
        return positive_example, negative_example, positive_example_response, negative_example_response

    def generate_openai_completion(client, sentence):
        instructions = get_openai_instructions()
        positive_example, negative_example, positive_example_response, negative_example_response = get_openai_examples()

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

    client = initialize_openai()
    return generate_openai_completion(client, sentence)
