from sqlalchemy.orm import Session
from datetime import date
from src.database.models import Modulo


def cadastrar(db: Session, curso_id: int, titulo: str):
    modulo = Modulo(
        curso_id=curso_id,
        titulo=titulo)
    db.add(modulo)
    db.commit()
    db.refresh(modulo)
    return modulo


def obter_todos(db: Session):
    modulos = db.query(Modulo).all()
    return modulos


def obter_por_id(db: Session, id: int):
    modulo = db.query(Modulo).filter(Modulo.id == id).first()
    return modulo


def apagar(db: Session, id: int):
    modulo = db.query(Modulo).filter(Modulo.id == id).first()
    if not modulo:
        return 0
    db.delete(modulo)
    db.commit()
    return 1


def editar(db: Session, id: int, curso_id: int, titulo: str):
    modulo = db.query(Modulo).filter(Modulo.id == id).first()
    if not modulo:
        return 0
    modulo.curso_id=curso_id,
    titulo=titulo
    db.commit()
    return 1