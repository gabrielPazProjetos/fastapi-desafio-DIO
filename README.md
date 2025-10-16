
fastapi-DIO
Projeto de API bancária simples desenvolvido com FastAPI, como parte dos estudos da DIO.
Endpoints disponíveis
Cadastro
POST /cadastro
Cria um novo usuário.
{
  "nome": "Lucas",
  "email": "Lucas@teste.com",
  "senha": "123"
}


Login
POST /login
Autentica o usuário.
{
  "email": "Lucas@teste.com",
  "senha": "123"
}


Extrato
GET /extrato?email=Lucas@teste.com
Retorna o saldo do usuário.
Testes com curl
Os testes abaixo foram realizados via terminal usando curl:
# Cadastro
curl -X POST http://127.0.0.1:8000/cadastro -H "Content-Type: application/json" -d "{\"nome\":\"Lucas\",\"email\":\"Lucas@teste.com\",\"senha\":\"123\"}"

# Login
curl -X POST http://127.0.0.1:8000/login -H "Content-Type: application/json" -d "{\"email\":\"Lucas@teste.com\",\"senha\":\"123\"}"

# Extrato
curl http://127.0.0.1:8000/extrato?email=Lucas@teste.com

Print dos testes
Estrutura do projeto
fastapi-DIO/
├── main.py
├── README.md
├── testes/
│   └── comandos_curl.txt
├── imagens/
│   └── terminal_testes.png




