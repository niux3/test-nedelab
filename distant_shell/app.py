import os
import json
from fastapi import FastAPI, HTTPException, status, Request, Depends
from auth import AuthHandler

def is_token_correct(token: str):
    with open("creds.json", "r") as f:
        return token == json.load(f)["token"]

auth_handler = AuthHandler()
app = FastAPI()

@app.post('/login')
def login(password: str):
    token = None
    with open("creds.json", "r") as f:
        token = json.load(f)["token"]
    if password != token:
        raise HTTPException(status_code=401, detail="Vous n'avez pas les droits")
    token = auth_handler.encode_token(password)
    return {'token': token}


@app.post("/exec")
def execute_shell(cmd: str, password: str):
    os.system(cmd)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", port=8000, log_level="info")
