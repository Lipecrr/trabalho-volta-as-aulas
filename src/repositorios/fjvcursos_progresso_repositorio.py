from sqlalchemy.orm import Session
from datetime import date
from src.database.models import Progresso

def cadastrar(db: Session,
    matricula_id: int,
    aula_id: int,
    concluido: bool,
    data_conclusao: date):
    progresso = Progresso(
        matricula_id=matricula_id,
        aula_id=aula_id,
        concluido=concluido,
        data_conclusao=data_conclusao
    )
    db.add(progresso)
    db.commit()
    db.refresh(progresso)
    return progresso


def obter_todos(db:Session):
    progressos = db.query(Progresso).all()
    return progressos


def obter_por_id(db:Session, id: int):
    progresso = db.query(Progresso).filter(Progresso.id == id).first()
    return progresso


def apagar(db:Session, id: int):
    progresso = db.query(Progresso).filter(Progresso.id == id).first()
    if not progresso:
        return 0
    db.delete(progresso)
    db.commit()
    return 1


def editar(db: Session,
    id: int,
    matricula_id: int,
    aula_id: int,
    concluido: bool,
    data_conclusao: date):
    progresso = db.query(Progresso).filter(Progresso.id == id).first()
    if not progresso:
        return 0
    progresso.matricula_id = matricula_id
    progresso.aula_id = aula_id
    progresso.concluido = concluido
    progresso.data_conclusao = data_conclusao