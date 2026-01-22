from sqlalchemy.orm import Session
from datetime import date
from src.database.models import Matricula


def cadastrar(db: Session, aluno_id: int, curso_id: int, data_matricula: date, status: str):
    matricula = Matricula(
        aluno_id=aluno_id,
        curso_id=curso_id,
        data_matricula=data_matricula,
        status=status
    )
    db.add(matricula)
    db.commit()
    db.refresh(matricula)
    return matricula


def obter_todos(db: Session):
    matriculas = db.query(Matricula).all()
    return matriculas


def obter_por_id(db: Session, id: int):
    matricula = db.query(Matricula).filter(Matricula.id == id).first()
    return matricula


def apagar(db: Session, id: int):
    matricula = db.query(Matricula).filter(Matricula.id == id).first()
    if not matricula:
        return 0
    db.delete(matricula)
    db.commit()
    return 1


def editar(db: Session, id: int, aluno_id: int, curso_id: int, data_matricula: date, status: str):
    matricula = db.query(Matricula).filter(Matricula.id == id).first()
    if not matricula:
        return 0
    matricula.aluno_id = aluno_id
    matricula.curso_id = curso_id
    matricula.data_matricula = data_matricula
    matricula.status = status
    db.commit()
    return 1