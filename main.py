from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

usuarios = {}
saldos = {}

class Usuario(BaseModel):
    nome: str
    email: str
    senha: str

class Login(BaseModel):
    email: str
    senha: str

@app.get("/")
def home():
    return {"mensagem": "API funcionando!"}

@app.post("/cadastro")
def cadastrar(usuario: Usuario):
    usuarios[usuario.email] = usuario
    saldos[usuario.email] = 0
    return {"mensagem": "Usuário cadastrado com sucesso"}

@app.post("/login")
def login(dados: Login):
    usuario = usuarios.get(dados.email)
    if not usuario or usuario.senha != dados.senha:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"mensagem": f"Bem-vindo, {usuario.nome}"}

@app.get("/extrato")
def extrato(email: str):
    if email not in saldos:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"email": email, "saldo": saldos[email]}
