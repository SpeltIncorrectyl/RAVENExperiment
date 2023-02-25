import openai

class CompletionEngine:
    def __init__(self, apikey):
        self.apikey = apikey

    def complete(prompt, temperature):
        openai.api_key = self.apikey
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=temperature,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].text