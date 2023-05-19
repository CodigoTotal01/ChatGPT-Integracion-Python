import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENIA_API_KEY")

openai.api_key = api_key

preguntas_anteriores = []
respuestas_anteriores = []


def preguntar_chat_gpt(prompt, modelo="text-davinci-002"):
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=150,
        temperature=0.5
    )

    return respuesta.choices[0].text.strip()


# No mantinee el contexto de la s conversaciones

print("Bienvenido a neustro chatbot basico. Escribe 'salir' cuando quieras terminar")
while True:
    conversacion_historica = ""
    ingreso_usuario = input("n\TU:")
    if ingreso_usuario.lower() == "salir":
        break
    # La función zip() combina dos o más iterables en una secuencia de tuplas
    for pregunta, respuesta in zip(preguntas_anteriores, respuestas_anteriores):
        conversacion_historica += f"El usuario pregunta: {pregunta}\n"
        conversacion_historica += f"ChatGPT responde: {respuesta}\n"

    prompt = f"EL usuario pregunta: {ingreso_usuario}\n"
    print(conversacion_historica)
    conversacion_historica += prompt
    respuesta_gpt = preguntar_chat_gpt(conversacion_historica)
    print(f"{respuesta_gpt}")

    preguntas_anteriores.append(ingreso_usuario)
    respuestas_anteriores.append(respuesta_gpt)
