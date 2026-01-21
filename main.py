from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.post("/api/v1/alunos", tags=["Alunos"])
# def cadastrar_aluno(aluno: AlunoCriar, db: Session = Depends(get_db)):
#     # aluno = 