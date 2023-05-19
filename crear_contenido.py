import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENIA_API_KEY")

openai.api_key = api_key


def crear_contenido(tema, tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Por favor escribe un articulo corsto sobre el tema: {tema}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()


def resumir_texto(texto, tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Por favor resume el siguiente texto: {texto}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperatura=temperatura
    )
    return respuesta.choices[0].text.strip()


tema = input(
    "Elije un tema para tu articulo: "
)

tokens = int(input("Cuantos tokens maximos quieres que tenga tu articulo: "))
temperatura = int(input("Del 1 al 10, que tan creativo quieres que sea tu articulo")) / 10
articulo_creado = crear_contenido(tema, tokens, temperatura)
print(articulo_creado)

