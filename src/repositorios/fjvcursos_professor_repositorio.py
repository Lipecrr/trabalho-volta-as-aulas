from sqlalchemy.orm import Session
from datetime import date
from src.database.models import Professor

def cadastrar(db: Session, nome: str, telefone: str, data_nascimento: date, especialidade: str):
    professor = Professor(
        nome=nome,
        telefone=telefone,
        data_nascimento=data_nascimento,
        especialidade=especialidade)
    db.add(professor)
    db.commit()
    db.refresh(professor)
    return professor


def obter_todos(db: Session):
    professores = db.query(Professor).all()
    return professores


def obter_por_id(db: Session, id: int):
    professor = db.query(Professor).filter(Professor.id == id).first()
    return professor


def apagar(db: Session, id: int):
    professor = db.query(Professor).filter(Professor.id == id).first()
    if not professor:
        return 0
    db.delete(professor)
    db.commit()
    return 1


def editar(db: Session, id: int, nome: str, telefone: str, data_nascimento: date, especialidade: str):
    professor = db.query(Professor).filter(Professor.id == id).first()
    if not professor:
        return 0
    professor.nome = nome
    professor.telefone = telefone
    professor.data_nascimento = data_nascimento
    professor.especialidade = especialidade
    db.commit()
    return 1