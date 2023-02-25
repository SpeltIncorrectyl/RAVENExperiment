from completion_engine import CompletionEngine
from conversation_engine import ConversationEngine
from outer_loop import OuterLoop

apikey = ""
with open("openaiapikey.txt") as apikey_file:
    apikey = apikey_file.read()

prompt = ""
with open("conversation.prompt") as prompt_file:
    prompt = prompt_file.read()

completition_engine = CompletionEngine(apikey)
conversation_engine = ConversationEngine(completition_engine, prompt)
outer_loop = OuterLoop(conversation_engine)

while True:
    message = input("User: ")
    outer_loop.speak(message)
    response = outer_loop.respond()
    print(f"RAVEN: {response}")