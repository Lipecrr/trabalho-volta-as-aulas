from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from src.database.conexao import get_db
from classes import (
    AlunoCriar,
    AlunoEditar,
    ProfessorCriar,
    ProfessorEditar,
    CursoCriar,
    CursoEditar,
    ModuloCriar,
    ModuloEditar,
    AulaCriar,
    AulaEditar,
    MatriculaCriar,
    MatriculaEditar,
    ProgressoCriar,
    ProgressoEditar,
    AvaliacaoCriar,
    AvaliacaoEditar,
    CertificadoCriar,
    CertificadoEditar,
)
from src.repositorios import (
    fjvcursos_aluno_repositorio,
    fjvcursos_aula_repositorio,
    fjvcursos_avaliacao_repositorio,
    fjvcursos_certificado_repositorio,
    fjvcursos_curso_repositorio,
    fjvcursos_matricula_repositorio,
    fjvcursos_modulo_repositorio,
    fjvcursos_professor_repositorio,
    fjvcursos_progresso_repositorio
    )


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/v1/alunos", tags=["Alunos"])
def cadastrar_aluno(aluno: AlunoCriar, db: Session = Depends(get_db)):
    aluno = fjvcursos_aluno_repositorio.cadastrar(
        db,
        aluno.nome,
        aluno.telefone,
        aluno.data_nascimento
    )
    return aluno