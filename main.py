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
def listar_alunos(db: Session = Depends(get_db)):
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


@app.get("/api/v1/modulos/{id}", tags=["Modulos"])
def listar_modulo(id: int, db: Session = Depends(get_db)):
    modulo = fjvcursos_modulo_repositorio.obter_por_id(db, id)
    if not modulo:
        raise HTTPException(status_code=404, detail="Modulo não encontrado")
    return modulo

## Aula
@app.post("/api/v1/aulas", tags=["Aulas"])
def cadastar_aula(aula: AulaCriar, db: Session = Depends(get_db)):
    aula = fjvcursos_aula_repositorio.cadastrar(
        db,
        aula.modulo_id,
        aula.titulo,
        aula.descricao,
        aula.tipo,
    )
    return aula


@app.get("/api/v1/aulas", tags=["Aulas"])
def listar_aulas(db: Session = Depends(get_db)):
    aulas = fjvcursos_aula_repositorio.obter_todos(db)
    return aulas


@app.delete("/api/v1/aulas/{id}", tags=["Aulas"])
def apagar_aula(id: int, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_aula_repositorio.apagar(db, id)
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Aula não encontrado")
    return {"status:", "ok"}


@app.put("/api/v1/aulas/{id}", tags=["Aulas"])
def editar_modulo(id: int, aula: AulaEditar, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_aula_repositorio.editar(
        db,
        id,
        aula.modulo_id,
        aula.titulo,
        aula.descricao,
        aula.tipo,
    )
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Aula não encontrado")
    return {"status": "ok"}


@app.get("/api/v1/aulas/{id}", tags=["Aulas"])
def listar_aula(id: int, db: Session = Depends(get_db)):
    aula = fjvcursos_aula_repositorio.obter_por_id(db, id)
    if not aula:
        raise HTTPException(status_code=404, detail="Aula não encontrado")
    return aula

## Matricula
@app.post("/api/v1/matriculas", tags=["Matriculas"])
def cadastrar_matricula(matricula: MatriculaCriar, db: Session = Depends(get_db)):
    matricula = fjvcursos_matricula_repositorio.cadastrar(
        db,
        matricula.aluno_id,
        matricula.curso_id,
        matricula.data_matricula,
        matricula.status,
    )
    return matricula


@app.get("/api/v1/matriculas", tags=["Matriculas"])
def listar_matriculas(db: Session = Depends(get_db)):
    matriculas = fjvcursos_matricula_repositorio.obter_todos(db)
    return matriculas


@app.delete("/api/v1/matriculas/{id}", tags=["Matriculas"])
def apagar_matricula(id: int, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_matricula_repositorio.apagar(db, id)
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Matricula não encontrado")
    return {"status:", "ok"}


@app.put("/api/v1/matriculas/{id}", tags=["Matriculas"])
def editar_matricula(id: int, matricula: MatriculaEditar, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_matricula_repositorio.editar(
        db,
        id,
        matricula.aluno_id,
        matricula.curso_id,
        matricula.data_matricula,
        matricula.status,
    )
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Matricula não encontrado")
    return {"status": "ok"}


@app.get("/api/v1/matriculas/{id}", tags=["Matriculas"])
def listar_matricula(id: int, db: Session = Depends(get_db)):
    matricula = fjvcursos_matricula_repositorio.obter_por_id(db, id)
    if not matricula:
        raise HTTPException(status_code=404, detail="Matricula não encontrado")
    return matricula


## Progresso
@app.post("/api/v1/progressos", tags=["Progressos"])
def cadastar_progresso(progresso: ProgressoCriar, db: Session = Depends(get_db)):
    progresso = fjvcursos_progresso_repositorio.cadastrar(
        db,
        progresso.matricula_id,
        progresso.aula_id,
        progresso.concluido,
        progresso.data_concusao,    
    )
    return progresso


@app.get("/api/v1/progressos", tags=["Progressos"])
def listar_progressos(db: Session = Depends(get_db)):
    progressos = fjvcursos_matricula_repositorio.obter_todos(db)
    return progressos


@app.delete("/api/v1/progressos/{id}", tags=["Progressos"])
def apagar_progresso(id: int, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_progresso_repositorio.apagar(db, id)
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Progresso não encontrado")
    return {"status:", "ok"}


@app.put("/api/v1/progressos/{id}", tags=["Progressos"])
def editar_progresso(id: int, progresso: ProgressoEditar, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_progresso_repositorio.editar(
        db,
        id,
        progresso.matricula_id,
        progresso.aula_id,
        progresso.concluido,
        progresso.data_concusao,
    )
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Progresso não encontrado")
    return {"status": "ok"}


@app.get("/api/v1/progresso/{id}", tags=["Progresso"])
def listar_progresso(id: int, db: Session = Depends(get_db)):
    progresso = fjvcursos_progresso_repositorio.obter_por_id(db, id)
    if not progresso:
        raise HTTPException(status_code=404, detail="Progresso não encontrado")
    return progresso


## Avaliacao
@app.post("/api/v1/avaliacao", tags=["Avaliacoes"])
def cadastrar_avaliacao(avaliacao: AvaliacaoCriar, db: Session = Depends(get_db)):
    avaliacao = fjvcursos_avaliacao_repositorio.cadastrar(
        db,
        avaliacao.curso_id,
        avaliacao.aluno_id,
        avaliacao.nota,
        avaliacao.comentario,
    )
    return avaliacao


@app.get("/api/v1/avaliacoes", tags=["Avaliacoes"])
def listar_avaliacoes(db: Session = Depends(get_db)):
    avaliacoes = fjvcursos_avaliacao_repositorio.obter_todos(db)
    return avaliacoes


@app.delete("/api/v1/avaliacoes/{id}", tags=["Avaliacoes"])
def apagar_avaliacao(id: int, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_avaliacao_repositorio.apagar(db, id)
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Avaliacao não encontrado")
    return {"status:", "ok"}


@app.put("/api/v1/avaliacoes/{id}", tags=["Avaliacoes"])
def editar_avaliacao(id: int, avaliacao: AvaliacaoEditar, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_avaliacao_repositorio.editar(
        db,
        id,
        avaliacao.curso_id,
        avaliacao.aluno_id,
        avaliacao.nota,
        avaliacao.comentario,
    )
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Avaliação não encontrado")
    return {"status": "ok"}


@app.get("/api/v1/avaliacao/{id}", tags=["Avaliação"])
def listar_avaliacao(id: int, db: Session = Depends(get_db)):
    avaliacao = fjvcursos_avaliacao_repositorio.obter_por_id(db, id)
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrado")
    return avaliacao


## Certificado
@app.post("/api/v1/certificado", tags=["Certificados"])
def cadastrar_certificado(certificado: CertificadoCriar, db: Session = Depends(get_db)):
    certificado = fjvcursos_certificado_repositorio.cadastrar(
        db,
        certificado.aluno_id,
        certificado.matricula_id,
        certificado.data_emissao,
        certificado.codico_validacao,
    )
    return certificado


@app.get("/api/v1/certificados", tags=["Certificados"])
def listar_certificados(db: Session = Depends(get_db)):
    certificados = fjvcursos_certificado_repositorio.obter_todos(db)
    return certificados


@app.delete("/api/v1/certificados/{id}", tags=["Certificados"])
def apagar_certificado(id: int, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_certificado_repositorio.apagar(db, id)
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Certificado não encontrado")
    return {"status:", "ok"}


@app.put("/api/v1/certificados/{id}", tags=["Certificados"])
def editar_certificado(id: int, certificado: CertificadoCriar, db: Session = Depends(get_db)):
    linhas_afetadas = fjvcursos_certificado_repositorio.editar(
        db,
        id,
        certificado.aluno_id,
        certificado.matricula_id,
        certificado.data_emissao,
        certificado.codico_validacao,
    )
    if not linhas_afetadas:
        raise HTTPException(status_code=404, detail="Certificado não encontrado")
    return {"status": "ok"}