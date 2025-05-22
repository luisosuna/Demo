from openai import OpenAI

client = OpenAI(api_key="")

while True:
    user_input = input("\n You: ")

    if user_input.lower() in ["exit", "quit", "q"]:
        print("👋 Goodbye!")
        break

    response = client.chat.completions.create(
        model="",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    print("\n🤖 Bot:", response.choices[0].message.content.strip())
