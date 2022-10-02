from fastapi import FastAPI

import pandas as pd

# uvicorn FastApi:app --reload
# uvicorn main:app --reload --host 0.0.0.0
# para iniciar o projeto    


app = FastAPI()

one_hot_enc = pd.read_pickle('one_hot_encoder.pkl')
modelo = pd.read_pickle('modelo_treinado.pkl')
scaler = pd.read_pickle('scaler.pkl')
# http://127.0.0.1:8000/modelo/v1=30&v2=5000&v3=Alugado&v4=5&v5=Reforma&v6=5&v7=10000&v8=8.8&v9=0&v10=0.5&v11=2
# http://127.0.0.1:8000/modelo/v1=50&v2=100000&v3=Alugado&v4=10&v5=Reforma&v6=1&v7=30000&v8=10.0&v9=0.3&v10=0&v11=20

@app.get('/modelo/v1={idade}&v2={renda}&v3={imovel}&v4={tempo_trabalhado}&v5={motivo_emprestimo}&v6={nota_emprestimo}&v7={total_emprestado}&v8={taxa_juros}&v9={renda_alocada}&v10={devedora}&v11={relacionamento_bancario}')
def previsao_modelo(idade, renda, imovel, tempo_trabalhado, 
                    motivo_emprestimo, nota_emprestimo, total_emprestado,
                    taxa_juros, devedora, renda_alocada, relacionamento_bancario):
    
    dados = {
        'idade': [float(idade)],
        'renda': [float(renda)],
        'imovel': [imovel],
        'tempo_trabalhado': [float(tempo_trabalhado)],
        'motivo_emprestimo': [motivo_emprestimo],
        'nota_emprestimo': [nota_emprestimo],
        'total_emprestado': [float(total_emprestado)],
        'taxa_juros': [float(taxa_juros)],
        'renda_alocada': [float(renda_alocada)],
        'devedora': [float(devedora)],
        'relacionamento_bancario': [float(relacionamento_bancario)]
    }

    dados = pd.DataFrame(dados)
    print(dados)

    dados = one_hot_enc.transform(dados)
    dados_transformados = pd.DataFrame(dados, columns=one_hot_enc.get_feature_names_out())

    dados_transformados = scaler.transform(dados_transformados)
    dados_transformados = pd.DataFrame(dados_transformados, columns = one_hot_enc.get_feature_names_out())
    return {'result': modelo.predict(dados_transformados)[0],
            'probability_0': modelo.predict_proba(dados_transformados).tolist()[0][0],
            'probability_1': modelo.predict_proba(dados_transformados).tolist()[0][1],
            }
    
    
    



#@app.get("/quem_eh_vitoria")
#async def root():
#    return {"message": "A vitória é o amor da minha vida, a poposa mais linda deste universo"}
