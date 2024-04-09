from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from fastapi import Depends, HTTPException,status
from database import get_db
from sqlalchemy.orm import Session
from database import engine
from models import Users, Users_Request
import models

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


models.Base.metadata.create_all(bind=engine)


db_dependency = Annotated[Session, Depends(get_db)]


@app.get('/get-user', status_code=status.HTTP_200_OK,
        summary='Retorna todos os usuário',
        description='Retorna todos os usuário ou uma lista vazia.')
async def get_all_users(db: db_dependency):
    if db.query(Users).all() == []:
        return "Banco de dados vazio!"
    else:
        return db.query(Users).all()


@app.get('/get-user/{id}',status_code=status.HTTP_200_OK,
        summary='Retorna um usuário',
        description='Retorna um usuário baseado no parametro id')
async def get_user_by_id (db: db_dependency, id: int):
    if db.query(Users).all() == []:
        return "Banco de dados vazio!"
    User_model = db.query(Users).filter(Users.id == id).first()
    if User_model is not None:
        return User_model
    raise HTTPException(status_code=404, detail='Usuario não encontrado')

@app.post('/create-user',        
        status_code=status.HTTP_200_OK,
        summary='Cria um usuário',
        description='Cria um usuário atravez do username e o email passados no JSON')
async def create_user (db: db_dependency, Users_request: Users_Request):
    User_model = Users(**Users_request.model_dump())
    if len(User_model.email) < 15:
        raise HTTPException(status_code=400, detail="""O endereço de e-mail deve ter mais de 15 caracteres.""")
    elif "@" not in User_model.email:
        raise HTTPException(status_code=400, detail="""O endereço de e-mail deve ter "@".""")
    elif ".com" not in User_model.email:
        raise HTTPException(status_code=400, detail="""O endereço de e-mail deve ter ".com".""")
    elif db.query(Users).filter(Users.email == User_model.email).first() is not None and db.query(Users).filter(Users.username == User_model.username).first() is not None:
        raise HTTPException(status_code=400, detail="""Este usuario já foi criado!""")
    else:
        db.add(User_model)
        db.commit()

    return f"""Usuario : {User_model.username} com o email {User_model.email} foi criado com sucesso!"""



