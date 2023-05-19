import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENIA_API_KEY")

openai.api_key = api_key
def clasificar_texto(texto):
    categorias = [
        "arte",
        "ciencia",
        "deporte",
        "salud"
    ]
    prompt = f"Porfavor clasifica el siquiente texto '{texto}' en una de estas categorias: {','.join(categorias)}. La categoria es: "
    respuesta = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        max_tokens=50,
        temperature=0.5
    )

    return respuesta.choices[0].text.strip()

texto_para_clasificar = input("Ingrese un texto porfavor: ")
clasificacion = clasificar_texto(texto_para_clasificar)
print(clasificacion)
