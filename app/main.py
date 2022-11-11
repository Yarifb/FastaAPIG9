from fastapi import FastAPI

app = FastAPI()

@app.get("/saludo")
async def root():
    return {"message": "Hola MisionTIC 2022"}

@app.get("/usuarios/{user_id}")
async def read_user(user_id: str): # rn lugar de str va int
    return {"user_id": user_id}

cursos = [{"curso": "Fundamento de Programacion"}, {"curso": "Programacion Basica"}, {"curso": "Desarrollo de Software"}, {"curso": "Desarrollo de Apps Web"}]

@app.get("/cursos/")
async def read_item(skip: int = 0, limit: int = 10):
    return cursos[skip : skip + limit]
