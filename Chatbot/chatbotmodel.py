from openai import OpenAI

client = OpenAI(api_key="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")

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
