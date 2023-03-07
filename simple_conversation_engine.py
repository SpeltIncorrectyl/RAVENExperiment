class SimpleConversationEngine:
    def __init__(self, completion_engine, conversation_prompt):
        self.completion_engine = completion_engine
        self.conversation_prompt = conversation_prompt
        self.messages = []

    def speak(self, message):
        self.messages.append(f"User: {message}")

    def respond(self, context):
        messages = ""
        for message in self.messages:
            messages += f"{message}\n"
        messages = messages[:-1]
        prompt = self.conversation_prompt.replace("<<Conversation>>", messages)
        prompt = prompt.replace("<<Context>>", context)
        response = self.completion_engine.complete(prompt, 0.5)
        self.messages.append(f"RAVEN: {response}")
        return response