import os
from openai import OpenAI

class ChatGPT:
    def __init__(self):
        token = os.getenv("CHATGPT_TOKEN")
        self.client = OpenAI(api_key=token)
    
    def test(self):
        stream = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "what is machine learning?"}],
            stream=True,
        ) # TODO: gotta pay first
        for part in stream:
            print(part.choices[0].delta.content or "")
        breakpoint()

if __name__ == "__main__":
    chatbot = ChatGPT()
    chatbot.test()
