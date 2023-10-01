from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from fastapi.responses import FileResponse

# Carregue o modelo de regressão Random Forest treinado
model_filename = 'random_forest_regression_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Crie uma aplicação FastAPI
app = FastAPI()

# Crie um modelo Pydantic para entrada de requisição
class Item(BaseModel):
    gender: str
    age: int  # Alterado para aceitar apenas inteiros
    annual_income: int  # Alterado para aceitar apenas inteiros

def preprocess_input(item: Item):
    # Verifique se 'gender' está em 'male' ou 'female' (case insensitive)
    if item.gender.lower() not in ['male', 'female']:
        raise HTTPException(status_code=400, detail="O valor 'gender' deve ser 'male' ou 'female'.")

    # Verifique se 'age' está entre 12 e 100 anos
    if not (12 <= item.age <= 100):
        raise HTTPException(status_code=400, detail="A idade deve estar entre 12 e 100 anos.")

    # Crie um DataFrame a partir dos dados de entrada
    data = pd.DataFrame([item.dict()])
    
    # Mapeie 'gender' para 1 para 'Masculino' e 0 para 'Feminino'
    data['Gender_Male'] = 1 if item.gender.lower() == 'male' else 0
    data['Gender_Female'] = 1 if item.gender.lower() == 'female' else 0
    
    # Remova a coluna 'gender' original
    data.drop(columns=['gender'], inplace=True)
    
    # Normalize 'age' e 'annual_income' usando min-max scaling
    scaler = MinMaxScaler()
    data[['Age', 'Income']] = scaler.fit_transform(data[['age', 'annual_income']])
    
    # Reordene as colunas para 'Age', 'Income', 'Gender_Female', 'Gender_Male'
    data = data[['Age', 'Income', 'Gender_Female', 'Gender_Male']]
    
    return data

# Defina a rota de previsão
@app.post("/predict/")
async def predict(item: Item):
    try:
        # Pré-processa os dados de entrada
        data = preprocess_input(item)
        
        # Faça previsões usando o modelo
        predictions = model.predict(data)
        
        # Supondo que o modelo retorne uma única previsão
        prediction = predictions[0]
        
        return {"prediction": prediction}
    except HTTPException as e:
        raise e  # Levanta exceção HTTP com a mensagem de erro adequada
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Serve the HTML file when the root URL is accessed
@app.get("/", response_class=FileResponse)
async def serve_ui():
    return "index.html"  # Replace with the actual path to y
