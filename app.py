import pandas as pd
import google.generativeai as genai

pergunta = ""
genai.configure(api_key="")

df = pd.read_excel("kpi013d.xlsx")
df_csv = df.to_csv("kpi013d.csv", index=False)

file = genai.upload_file(path="kpi013d.csv", display_name="Arquivo CSV", mime_type="text/csv")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=genai.GenerationConfig(
        temperature=0.0,
        top_k=0.1,
        top_p=0.1,
        #max_output_tokens=8096,
        response_mime_type="text/plain"
    ),
    system_instruction="Se comporte como uma analista de dados financeiros\nResponda sempre em portugues do Brasil\nResponda de forma objetiva",
)

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                file,
            ],
        },        
    ]
)

chat_session.send_message

response = chat_session.send_message("Descreva este relatório em portugues do Brasil e me liste possíveis análises que posso fazer com ele")
print(response.text)

while pergunta != "sair": 

    pergunta = input("Digite sua pergunta: ")
    if pergunta == "sair":
        break

    response = chat_session.send_message(pergunta)
    print(response.text)

