from chat_engine import ChatEngine
from conversation_engine import ConversationEngine
from outer_loop import OuterLoop

apikey = ""
with open("openaiapikey.txt") as apikey_file:
    apikey = apikey_file.read()

prompt = ""
with open("conversation.prompt") as prompt_file:
    prompt = prompt_file.read()

chat_engine = ChatEngine(apikey)
conversation_engine = ConversationEngine(chat_engine, prompt)
outer_loop = OuterLoop(conversation_engine)

while True:
    message = input("User: ")
    outer_loop.speak(message)
    response = outer_loop.respond()
    print(f"RAVEN: {response}")