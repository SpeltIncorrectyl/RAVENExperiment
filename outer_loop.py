class OuterLoop:
    def __init__(self, conversation_engine):
        self.conversation_engine = conversation_engine
        
    def speak(self, message):
        self.conversation_engine.speak(message)

    def respond(self):
        return self.conversation_engine.respond("The User is looking to develop AI technology.")