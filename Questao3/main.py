from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",  
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


URL = "https://jsonplaceholder.typicode.com/posts"

@app.get('/get-all-posts')
async def get_all():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()        
        return data
    else:
        return 'Falha na solicitação:', response.status_code


@app.get('/get-post/{id}')
async def get_post_by_id(id:int):
    response = requests.get(f'{URL}/{id}')
    if response.status_code == 200:
        data = response.json()        
        return data
    else:
        return 'Falha na solicitação:', response.status_code
    
@app.post('/create-post')
async def create_post(id:int, titulo: str, completado: bool):
    
    data = {
        'userId': id,
        'title': titulo,
        'completed': completado
    }
    response = requests.post(URL, json=data)
    if response.status_code == 201:
        return 'Solicitação POST bem-sucedida! Nova tarefa criada. Dados inseridos :', response.json()
        
    else:
        return 'Falha na solicitação POST:', response.status_code
    

@app.get('/como-eu-faria-autenticação')
async def text_autenticacao():
    #       COMO EU UTILIZARIA NA PRÁTICA
    # import requests
    # TOKEN_DE_ACESSO = 'exemplo_token'
    # url = 'https://endpointexemplo/'
    # headers = {
    #     'Authorization': f'Bearer {TOKEN_DE_ACESSO}'
    # }
    # response = requests.get(url, headers=headers)
    return "Eu criaria uma variável constante para armazenar o token de acesso e o utilizaria no cabeçalho de autorização (Authorization) ao fazer uma solicitação para a URL."

    
