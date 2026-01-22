from sqlalchemy.orm import Session
from datetime import date
from src.database.models import Curso

def cadastrar(
    db: Session, 
    titulo: str, 
    descricao: str, 
    professor_id: int, 
    carga_horaria: float,
    ativo: bool):
    curso = Curso(
        titulo=titulo,
        descricao=descricao,
        professor_id=professor_id,
        carga_horaria=carga_horaria,
        ativo=ativo)
    db.add(curso)
    db.commit()
    db.refresh(curso)
    return curso


def obter_todos(db: Session):
    cursos = db.query(Curso).all()
    return cursos


def obter_por_id(db: Session, id: int):
    curso = db.query(Curso).filter(Curso.id == id).first()
    return curso


def apagar(db: Session, id: int):
    curso = db.query(Curso).filter(Curso.id == id).first()
    if not curso:
        return 0
    db.delete(curso)
    db.commit()
    return 1


def editar(db: Session, 
    id: int, 
    titulo: str, 
    descricao: str, 
    professor_id: int, 
    carga_horaria: float,
    ativo: bool):
    curso = db.query(Curso).filter(Curso.id == id).first()
    if not curso:
        return 0
    curso.titulo = titulo
    curso.descricao = descricao
    curso.professor_id = professor_id
    curso.carga_horaria = carga_horaria
    curso.ativo = ativo

    db.commit()
    return 1