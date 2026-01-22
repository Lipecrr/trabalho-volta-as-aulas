from sqlalchemy.orm import Session
from datetime import date
from src.database.models import Avaliacao


def cadastrar(db: Session, curso_id: int, aluno_id: int, nota: float, comentario: str):
    avaliacao = Avaliacao(
        curso_id=curso_id,
        aluno_id=aluno_id,
        nota=nota,
        comentario=comentario)
    db.add(avaliacao)
    db.commit()
    db.refresh(avaliacao)
    return avaliacao


def obter_todos(db: Session):
    avaliacoes = db.query(Avaliacao).all()
    return avaliacoes


def obter_por_id(db: Session, id: int):
    avaliacao = db.query(Avaliacao).filter(Avaliacao.id == id).first()
    return avaliacao


def apagar(db: Session, id: int):
    avaliacao = db.query(Avaliacao).filter(Avaliacao.id == id).first()
    if not avaliacao:
        return 0
    db.delete(avaliacao)
    db.commit()
    return 1


def editar(db: Session, id: int, curso_id: int, aluno_id: int, nota: float, comentario: str):
    avaliacao = db.query(Avaliacao).filter(Avaliacao.id == id).first()
    if not avaliacao:
        return 0
    avaliacao.curso_id = curso_id
    avaliacao.aluno_id = aluno_id
    avaliacao.nota = nota
    avaliacao.comentario = comentario
    db.commit()
    return 1