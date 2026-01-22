from sqlalchemy.orm import Session
from src.database.models import Aula

def cadastrar(db: Session,
    modulo_id: int,
    titulo: str,
    descricao: str,
    tipo: str):
    aula=Aula(
        modulo_id=modulo_id,
        titulo=titulo,
        descricao=descricao,
        tipo=tipo)
    db.add(aula)
    db.commit()
    db.refresh(aula)
    return aula


def obter_todos(db: Session):
    aulas = db.query(Aula).all()
    return aulas


def obter_por_id(db:Session, id: int):
    aula = db.query(Aula).filter(Aula.id == id).first()
    return aula


def apagar(db: Session, id: int):
    aula = db.query(Aula).filter(Aula.id == id).first()
    if not aula:
        return 0
    db.delete(aula)
    db.commit()
    return 1


def editar(db: Session,
    id: int,
    modulo_id: int,
    titulo: str,
    descricao: str,
    tipo: str):
    aula = db.query(Aula).filter(Aula.id == id).first()
    if not aula:
        return 0
    aula.modulo_id=modulo_id
    aula.titulo=titulo
    aula.descricao=descricao
    aula.tipo=tipo

    db.commit()
    return 1