import openai
import os
from dotenv import load_dotenv

load_dotenv("environment.env")
print(os.getenv("OPENAI_API_KEY"))


openai.api_key = os.getenv("OPENAI_API_KEY")

def detectar_nombre_o_apellido(palabra):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that can identify whether a given word is a first name or a surname."
            },
            {
                "role": "user",
                "content": f"Identify if {palabra} is a first name or a surname."
            }
        ]
    )

    
    respuesta = response['choices'][0]['message']['content'].strip().lower()
    
    if "first name" in respuesta:
        return "Nombre"
    elif "surname" in respuesta:
        return "Apellido"
    else:
        return "Indeterminado"

palabra = input("Introduce una palabra: ")
resultado = detectar_nombre_o_apellido(palabra)
print(f"La palabra '{palabra}' es un: {resultado}")
