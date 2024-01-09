import os
from openai import OpenAI

def initialize_openai():
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI()

def get_openai_instructions():
        return "Classify sentences as being about five key topics from the economy: credit conditions, household spending, inflation, investment, and labor market conditions. Respond with a json object with a key for each topic with a value of 1 or 0."

def get_openai_examples():
    example_credit_conditions = "Higher interest rates continued to dampen loan demand, and several bankers reported delinquencies edged up."
    example_household_spending = "Consumer spending was down, and general merchandisers reported discretionary goods spending declined."
    example_inflation = "Many contacts in manufacturing and freight said they were holding prices steady or reducing them to stay competitive."
    example_investment = "A contact noted capital markets and investment activities have rebounded in recent months."
    example_labor_market = "Several financial services firms restructured staffing to gain efficiencies, including limiting hiring and reducing staff."
    response_credit_conditions = "{'credit_conditions': 1, 'household_spending': 0, 'inflation': 0, 'investment': 0, 'labor_market': 0}"
    response_household_spending = "{'credit_conditions': 0, 'household_spending': 1, 'inflation': 0, 'investment': 0, 'labor_market': 0}"
    response_inflation = "{'credit_conditions': 0, 'household_spending': 0, 'inflation': 1, 'investment': 0, 'labor_market': 0}"
    response_investment = "{'credit_conditions': 0, 'household_spending': 0, 'inflation': 0, 'investment': 1, 'labor_market': 0}"
    response_labor_market = "{'credit_conditions': 0, 'household_spending': 0, 'inflation': 0, 'investment': 0, 'labor_market': 1}"
    return example_credit_conditions, example_household_spending, example_inflation, example_investment, example_labor_market, response_credit_conditions, response_household_spending, response_inflation, response_investment, response_labor_market

def generate_openai_completion(client, sentence, instructions, examples):
    instructions = get_openai_instructions()
    example_credit_conditions, example_household_spending, example_inflation, example_investment, example_labor_market, response_credit_conditions, response_household_spending, response_inflation, response_investment, response_labor_market = get_openai_examples()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": example_credit_conditions},
            {"role": "assistant", "content": response_credit_conditions},
            {"role": "user", "content": example_household_spending},
            {"role": "assistant", "content": response_household_spending},
            {"role": "user", "content": example_inflation},
            {"role": "assistant", "content": response_inflation},
            {"role": "user", "content": example_investment},
            {"role": "assistant", "content": response_investment},
            {"role": "user", "content": example_labor_market},
            {"role": "assistant", "content": response_labor_market},
            {"role": "user", "content": sentence}
        ])

    return completion

def call_gpt(sentence):
    client = initialize_openai()
    instructions = get_openai_instructions()
    examples = get_openai_examples()
    return generate_openai_completion(client, sentence, instructions, examples)
