from ollama import chat

response = chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": "¿Qué es un peatón?"
        }
    ]
)

print(
    response["message"]["content"]
)
