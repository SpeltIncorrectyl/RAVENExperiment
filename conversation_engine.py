class ConversationEngine:
    def __init__(self, chat_engine, primer):
        self.chat_engine = chat_engine
        role_primer = {"role" : "system", "content" : primer}
        self.messages = [role_primer]
    
    def speak(self, message):
        role_message = {"role" : "user", "content" : message}
        self.messages.append(role_message)

    def respond(self, _context):
        response = self.chat_engine.chat(self.messages)
        self.messages.append(response)
        return response.content