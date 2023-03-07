import re
import subprocess

class CodeEngine:
    def __init__(self, conversation_engine):
        self.conversation_engine = conversation_engine
        self.conversation_engine.speak({"role" : "user", "content" : "Print 'Hello World' to the console."})
        self.conversation_engine.speak({"role" : "assistant", "content" : "Sure! I will print this to the console. \n```\n <<print('Hello World')\n```"})
        self.conversation_engine.speak({"role" : "assistant", "content" : "Result: Hello World"})

    def speak(self, message):
        role_message = {"role" : "user", "content" : message}
        self.conversation_engine.speak(role_message)

    def respond(self):
        response = self.conversation_engine.respond([]).content
        for code in self.get_code(response):
            result = subprocess.run(["python", "-c", code], capture_output=True, text=True).stdout
            formatted_result = f"Result: {result}"
            print(formatted_result)
            message = {"role" : "assistant", "content" : formatted_result}
            self.conversation_engine.speak(message)
        return response
    
    def get_code(_self, message):
        return re.findall(r'```\n(.*)\n```', message, flags=re.DOTALL)