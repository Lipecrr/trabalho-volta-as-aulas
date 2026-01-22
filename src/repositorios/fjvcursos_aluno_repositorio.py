from sqlalchemy.orm import Session
from datetime import date
from src.database.models import Aluno

def cadastrar(db: Session, nome: str, telefone: str, data_nascimento: date):
    aluno = Aluno(
        nome=nome,
        telefone=telefone,
        data_nascimento=data_nascimento)
    db.add(aluno)
    db.commit()
    db.refresh(aluno)
    return aluno


def obter_todos(db: Session):
    alunos = db.query(Aluno).all()
    return alunos


def obter_por_id(db: Session, id: int):
    aluno = db.query(Aluno).filter(Aluno.id == id).first()
    return aluno


def apagar(db: Session, id: int):
    aluno = db.query(Aluno).filter(Aluno.id == id).first()
    if not aluno:
        return 0
    db.delete(aluno)
    db.commit()
    return 1


def editar(db: Session, id: int, nome: str, telefone: str, data_nascimento: date):
    aluno = db.query(Aluno).filter(Aluno.id == id).first()
    if not aluno:
        return 0
    aluno.nome = nome
    aluno.telefone = telefone
    aluno.data_nascimento = data_nascimento
    db.commit()
    return 1

