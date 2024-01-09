import os
from openai import OpenAI

def call_gpt_2(sentence):
    def initialize_openai():
        OpenAI.api_key = os.getenv("OPENAI_API_KEY")
        return OpenAI()

    def get_openai_instructions():
        return "Classify sentences as being about five key topics from the economy: credit conditions, household spending, inflation, investment, and labor market conditions. Respond with a json object with a key for each topic with a value of 1 or 0."

    def get_openai_examples():
        example_credit_conditions = "Higher interest rates continued to dampen loan demand, and several bankers reported that delinquencies edged up for specific loan categories."
        example_household_spending = "Consumer spending was down, and general merchandisers reported discretionary goods spending declined, a trend they were hopeful would reverse with the holiday shopping season."
        example_inflation = "Many contacts in manufacturing and freight said they were holding prices steady or, alternatively, reducing them to stay competitive, even in cases in which costs were increasing."
        example_investment = "A contact in Southern California noted that capital markets and investment activities have rebounded in recent months, especially in the sustainability and clean technology areas."
        example_labor_market = "Several financial services firms restructured staffing to gain efficiencies, including limiting hiring to revenue-generating roles and reducing staff in underperforming product or market areas."
        response_credit_conditions = "{'credit_conditions': 1, 'household_spending': 0, 'inflation': 0, 'investment': 0, 'labor_market': 0}"
        response_household_spending = "{'credit_conditions': 0, 'household_spending': 1, 'inflation': 0, 'investment': 0, 'labor_market': 0}"
        response_inflation = "{'credit_conditions': 0, 'household_spending': 0, 'inflation': 1, 'investment': 0, 'labor_market': 0}"
        response_investment = "{'credit_conditions': 0, 'household_spending': 0, 'inflation': 0, 'investment': 1, 'labor_market': 0}"
        response_labor_market = "{'credit_conditions': 0, 'household_spending': 0, 'inflation': 0, 'investment': 0, 'labor_market': 1}"
        return example_credit_conditions, example_household_spending, example_inflation, example_investment, example_labor_market, response_credit_conditions, response_household_spending, response_inflation, response_investment, response_labor_market

    def generate_openai_completion(client, sentence):
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

    client = initialize_openai()
    return generate_openai_completion(client, sentence)
