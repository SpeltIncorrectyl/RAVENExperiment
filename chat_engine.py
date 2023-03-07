import openai

class ChatEngine:
    def __init__(self, api_key):
        self.api_key = api_key

    def chat(self, messages):
        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages   
        )
        return response.choices[0].message