from chat_engine import ChatEngine
from conversation_engine import ConversationEngine
from code_engine import CodeEngine

apikey = ""
with open("openaiapikey.txt") as apikey_file:
    apikey = apikey_file.read()

prompt = ""
with open("conversation.prompt") as prompt_file:
    prompt = prompt_file.read()

chat_engine = ChatEngine(apikey)

conversation_engine = ConversationEngine(chat_engine, prompt)

code_engine = CodeEngine(conversation_engine)

while True:
    message = input("User: ")
    code_engine.speak(message)
    response = code_engine.respond()
    print(f"RAVEN: {response}")