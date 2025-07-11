import os
from openai import OpenAI

# Retrieve the API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)

while True:
    user_input = input("\n You: ")

    if user_input.lower() in ["exit", "quit", "q"]:
        print("👋 Goodbye!")
        break

    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal::BZnAK2Ts",
        messages=[
            {"role": "user", "content": user_input}
        ],
        temperature=0.9,
        frequency_penalty=0.5,    
        presence_penalty=0.3  
    )

    print("\n🤖 Bot:", response.choices[0].message.content.strip())
