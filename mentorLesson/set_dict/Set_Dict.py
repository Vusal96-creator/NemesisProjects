from dotenv import load_dotenv

load_dotenv()

#set
#
# bos_set=set()
#
# seherler_list=["Bakı", "Gəncə", "Bakı", "Sumqayıt", "Gəncə"]
# #
# print(seherler_list)
# #
# seherler_set=set(seherler_list)
# print(seherler_set)

# istirak = ["Anar", "Günel", "Anar", "Nicat", "Günel", "Anar", "Fidan"]
#
# istirak_set=set(istirak)
# print(istirak_set)


# hobiler={"oxumaq","idman","musiqi","musiqi"}
# # hobiler.add("uzmek")
# # hobiler.add("musiqi")
# print(hobiler)

# hobiler.remove("uzmek")
# hobiler.discard("uzmek")
# print(hobiler)

# sinif_a={"Anar","Gunel","Nicat"}
# sinif_b={"Gunel","Fidan","Ramin"}
#
# birlik=sinif_a | sinif_b
# print(birlik)
#
# ortaq=sinif_a & sinif_b
# print(ortaq)
#
# yalniz_a=sinif_a - sinif_b
# print(yalniz_a)

telebe={
    "ad":"Vusal",
    "age": 20,
    "fakulte":"Informatika",
    "herbi_veziyyeti": True,
    "soyad":"Vusal"
}
# print(telebe)

import json

# json_metn=json.dumps(telebe)
# print(json_metn)

# print(telebe.keys())
# print(telebe.values())
# print(telebe.items())


# gelen_metn = '{"ad": "Murad", "yas": 25}'
#
# telebe=json.loads(gelen_metn)
# print(telebe)


from openai import OpenAI

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",  # Groq endpoint
)
#
# def ai_sorus(sual):
#     cavab = client.chat.completions.create(
#         model="openai/gpt-oss-120b",  # Groq modeli
#         messages=[{"role": "user", "content": sual}]
#     )
#     return cavab.choices[0].message.content
#
# netice = ai_sorus("JSON nedir ? Provide in azerbaijani ")
# print(netice)


import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",  # Groq endpoint
)

def ai_sorus(sual):
    cavab = client.chat.completions.create(
        model="openai/gpt-oss-120b",  # Groq modeli
        messages=[{"role": "user", "content": sual}]
    )
    return cavab.choices[0].message.content

netice = ai_sorus("JSON nedir ? Provide in azerbaijani ")
print(netice)
