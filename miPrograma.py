import os
import openai
import spacy  # modelo de procesamiento de la imagen
from dotenv import load_dotenv

# cargar las variables en nuestro /.env
load_dotenv()

api_key = os.getenv('OPENIA_API_KEY')

openai.api_key = api_key
# Preparar Peticion
modelo = "text-davinci-002"
prompt = "Cuenta una historia breve"

#  Enviar Peticion
respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=1,
    # temperature=1,  # entre mayor el valor se pone mas creativo,
    max_tokens=50,  # abreviacion de respuesta

)
# # recorrido de un arreglo o tupla
# for idx, opcion in enumerate(respuesta.choices):
#     texto_generado = opcion.text.strip()
#     print(f"Respuesta {idx+1}: {texto_generado}\n")

texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)

print("*****")

# Procesar informacion en espaniol
modelo_spacy = spacy.load("es_core_news_md")

analisis = modelo_spacy(texto_generado)
# Los tokens son palabras y signos de putntuacion, o entre mesclado
# for token in analisis:
#     print(token.text, token.pos_, token.head.text)


# for ent in analisis.ents:
#     print(ent.text, ent.label_)

ubicacion = None
for ent in analisis.ents:
    if ent.label_ == "LOC":
        ubicacion = ent
        break

if ubicacion:
    prompt2 = f"Dime mas acerca de {ubicacion}"
    repuesta2 = openai.Completion.create(
        engine=modelo,
        prompt=prompt2,
        n=1,
        max_tokens=100
    )
    print(repuesta2.choices[0].text.strip())
