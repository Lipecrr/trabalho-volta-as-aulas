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
    

#Curso
@app.post("/api/v1/cursos", tags=["Cursos"])
def cadastrar_curso(curso: CursoCriar, db: Session = Depends(get_db)):
    curso = fjvcursos_curso_repositorio.cadastrar(
        db,
        curso.titulo,
        curso.descricao,
        curso.professor_id, 
        curso.carga_horaria,
        curso.ativo
    )
    return curso


@app.get("/api/v1/cursos", tags=["Cursos"])
def listar_cursos(db: Session = Depends(get_db)):
    cursos = fjvcursos_curso_repositorio.obter_todos(db)
    return cursos


@app.delete("/api/v1/cursos/{id}", tags=["Cursos"])
def apagar_curso(id: int, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_curso_repositorio.apagar(db, id)
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return {"status":"ok"}


@app.put("/api/v1/cursos/{id}", tags=["Cursos"])
def editar_curso(id: int, curso: CursoEditar, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_curso_repositorio.editar(
        db,
        id,
        curso.titulo,
        curso.descricao,
        curso.professor_id, 
        curso.carga_horaria,
        curso.ativo
    )
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return {"status": "ok"}


@app.get("/api/v1/cursos/{id}", tags=["Cursos"])
def listar_curso(id:int, db: Session = Depends(get_db)):
    curso = fjvcursos_curso_repositorio.obter_por_id(db, id)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso

    
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


@app.delete("/api/v1/professores/{id}", tags=["Professores"])
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



## Modulo
@app.post("/api/v1/modulos", tags=["Modulos"])
def cadastrar_modulo(modulo: ModuloCriar, db: Session = Depends(get_db)):
    modulo = fjvcursos_modulo_repositorio.cadastrar(
        db,
        modulo.curso_id,
        modulo.titulo
    )
    return modulo


@app.get("/api/v1/modulos", tags=["Modulos"])
def listar_modulos(db: Session = Depends(get_db)):
    modulos = fjvcursos_modulo_repositorio.obter_todos(db)
    return modulos


@app.delete("/api/v1/modulos/{id}", tags=["Modulos"])
def apagar_modulo(id: int, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_modulo_repositorio.apagar(db, id)
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Modulo não encontrado")
    return {"status:", "ok"}


@app.put("/api/v1/modulos/{id}", tags=["Modulos"])
def editar_modulo(id: int, modulo: ModuloEditar, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_modulo_repositorio.editar(
        db,
        id,
        modulo.curso_id,
        modulo.titulo,
    )
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Modulo não encontrado")
    return {"status": "ok"}


