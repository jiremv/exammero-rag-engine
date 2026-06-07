from ollama import chat

response = chat(
    model="llama3",
    format="json",
    messages=[
        {
            "role": "user",
            "content": "Genera un JSON con nombre y edad"
        }
    ]
)

print(response["message"]["content"])
