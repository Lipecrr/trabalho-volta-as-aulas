from sqlalchemy.orm import Session
from datetime import date
from src.database.models import Certificado


def cadastrar(db: Session, aluno_id: int, matricula_id: int, data_emissao: date, codigo_validacao: str):
    certificado = Certificado(
        aluno_id=aluno_id,
        matricula_id=matricula_id,
        data_emissao=data_emissao,
        codigo_validacao=codigo_validacao)
    db.add(certificado)
    db.commit()
    db.refresh(certificado)
    return certificado


def obter_todos(db: Session):
    certificados = db.query(Certificado).all()
    return certificados


def obter_por_id(db: Session, id: int):
    certificado = db.query(Certificado).filter(Certificado.id == id).first()
    return certificado


def apagar(db: Session, id: int):
    certificado = db.query(Certificado).filter(Certificado.id == id).first()
    if not certificado:
        return 0
    db.delete(certificado)
    db.commit()
    return 1


def editar(db: Session, id: int, aluno_id: int, matricula_id: int, data_emissao: date, codigo_validacao: str):
    certificado = db.query(Certificado).filter(Certificado.id == id).first()
    if not certificado:
        return 0
    certificado.aluno_id = aluno_id
    certificado.matricula_id = matricula_id
    certificado.data_emissao = data_emissao
    certificado.codigo_validacao = codigo_validacao