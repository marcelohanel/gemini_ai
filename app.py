import pandas as pd
import google.generativeai as genai

pergunta = ""
df = pd.read_excel("Vendas.xlsx")
#df = df.drop(["Código Venda", "Quantidade", "Valor Unitário"], axis=1)
df_text = df.to_string(index=False)

genai.configure(api_key="")

#for m in genai.list_models():
#  if 'generateContent' in m.supported_generation_methods:
#    print(m.name)

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=genai.GenerationConfig(
        temperature=0.0,
    ),
    system_instruction="Se comporte como uma analista de dados financeiros\nSeja sempre objetivo nas respostas\nResponda sempre em portugues do Brasil",
)

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                df_text,
            ],
        },        
    ]
)
response = chat_session.send_message("Descreva este relatório em portugues do Brasil")
print(response.text)


#print(df_text)
#print()
#print()

while pergunta != "sair": 
    pergunta = input("Digite sua pergunta: ")
    if pergunta == "sair":
        break

    response = chat_session.send_message(pergunta)
    print(response.text)

