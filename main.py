from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Please set it in .env")

# use API_KEY here (DO NOT print it)
from groq import Groq

client = Groq(api_key=API_KEY)

print("🤖 Groq Streaming Chatbot (type 'exit' to quit)\n")

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]


while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    print("Bot: ", end="", flush=True)

    # STREAMING RESPONSE
    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
        stream=True,  # 👈 enables streaming
    )

    bot_reply = ""

    for chunk in stream:
        content = chunk.choices[0].delta.content or ""
        print(content, end="", flush=True)
        bot_reply += content

    print("\n")

    messages.append({"role": "assistant", "content": bot_reply})
