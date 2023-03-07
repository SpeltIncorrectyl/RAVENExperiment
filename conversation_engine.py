class ConversationEngine:
    def __init__(self, chat_engine, primer):
        self.chat_engine = chat_engine
        role_primer = {"role" : "system", "content" : primer}
        self.messages = [role_primer]
    
    def speak(self, message):
        self.messages.append(message)

    def respond(self, context):
        response = self.chat_engine.chat(context + self.messages)
        self.messages.append(response)
        return response