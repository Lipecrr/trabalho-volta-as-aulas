from datetime import date
from pydantic import BaseModel


class AlunoCriar(BaseModel):
    nome: str
    telefone: str
    data_nascimento = date


class AlunoEditar(BaseModel):
    nome: str
    telefone: str
    data_nascimento: date


class ProfessorCriar(BaseModel):
    nome: str
    telefone: str
    data_nascimento: date
    especialidade: str


class ProfessorEditar(BaseModel):
    nome: str
    telefone: str
    data_nascimento: date
    especialidade: str


class CursoCriar(BaseModel):
    titulo: str
    descricao: str
    professor_id: int
    carga_horaria: float
    ativo: bool


class CursoEditar(BaseModel):
    titulo: str
    descricao: str
    professor_id: int
    carga_horaria: float
    ativo: bool


class ModuloCriar(BaseModel):
    curso_id: int
    titulo: str
    

class ModuloEditar(BaseModel):
    curso_id: int
    titulo: str


class AulaCriar(BaseModel):
    modulo_id: int
    titulo: str
    descricao: str
    tipo: str


class AulaEditar(BaseModel):
    modulo_id: int
    titulo: str
    descricao: str
    tipo: str


class MatriculaCriar(BaseModel):
    aluno_id: int
    curso_id: int
    data_matricula: date
    status: str


class MatriculaEditar(BaseModel):
    aluno_id: int
    curso_id: int
    data_matricula: date
    status: str


class ProgressoCriar(BaseModel):
    matricula_id: int
    aula_id: int
    concluido: bool
    data_concusao: date


class ProgressoEditar(BaseModel):
    matricula_id: int
    aula_id: int
    concluido: bool
    data_concusao: date


class AvaliacaoCriar(BaseModel):
    curso_id: int
    aluno_id: int
    nota: float
    comentario: str


class AvaliacaoEditar(BaseModel):
    curso_id: int
    aluno_id: int
    nota: float
    comentario: str


class CertificadoCriar(BaseModel):
    matricula_id: int
    data_emissao: date
    codico_validacao: str


class CertificadoEditar(BaseModel):
    matricula_id: int
    data_emissao: date
    codico_validacao: str