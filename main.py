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


## Aluno
@app.post("/api/v1/alunos", tags=["Alunos"])
def cadastrar_aluno(aluno: AlunoCriar, db: Session = Depends(get_db)):
    aluno = fjvcursos_aluno_repositorio.cadastrar(
        db,
        aluno.nome,
        aluno.telefone,
        aluno.data_nascimento
    )
    return aluno


@app.get("/api/v1/alunos", tags=["Alunos"])
def listar_cliente(db: Session = Depends(get_db)):
    alunos = fjvcursos_aluno_repositorio.obter_todos(db)
    return alunos


@app.delete("/api/v1/alunos/{id}", tags=["Alunos"])
def apagar_aluno(id: int, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_aluno_repositorio.apagar(db, id)
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"status": "ok"}


@app.put("/api/v1/alunos/{id}", tags=["Alunos"])
def editar_aluno(id: int, aluno: AlunoEditar, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_aluno_repositorio.editar(
        db, id, aluno.nome, aluno.telefone,aluno.data_nascimento,
    )
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"status": "ok"}


@app.get("/api/v1/alunos/{id}", tags=["Alunos"])
def listar_aluno(id: int, db: Session = Depends(get_db)):
    aluno = fjvcursos_aluno_repositorio.obter_por_id(db, id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno
    


## Professor
@app.post("/api/v1/professores", tags=["Professores"])
def cadastrar_professor(professor: ProfessorCriar, db: Session = Depends(get_db)):
    professor = fjvcursos_professor_repositorio.cadastrar(
        db,
        professor.nome,
        professor.telefone,
        professor.data_nascimento,
        professor.especialidade,
    )
    return professor


@app.get("/api/v1/professores", tags=["Professores"])
def listar_professores(db: Session = Depends(get_db)):
    professores = fjvcursos_professor_repositorio.obter_todos(db)
    return professores


@app.delete("api/v1/professores/{id}", tags=["Professores"])
def apagar_professor(id: int, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_professor_repositorio.apagar(db, id)
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Professor não encotrado")
    return {"status": "ok"}


@app.put("/api/v1/professores/{id}", tags=["Professores"])
def editar_professor(id: int, professor: ProfessorEditar, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_professor_repositorio.editar(
        db, id, professor.nome, professor.telefone, professor.data_nascimento, professor.especialidade,
    )
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return {"status": "ok"}


@app.get("/api/v1/professores/{id}", tags=["Professores"])
def listar_professor(id: int, db: Session = Depends(get_db)):
    professor = fjvcursos_professor_repositorio.obter_por_id(db, id)
    if not professor:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return professor


