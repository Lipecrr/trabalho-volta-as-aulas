from sqlalchemy import Column, Date, Double, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    senha = Column(String(50), nullable=False)
    tipo = Column(String(20), nullable=False)

    aluno = relationship("Aluno", back_populates="usuario")
    professor = relationship("Professor", back_populates="usuario")


class Aluno(Base):
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    cpf = Column(String(14))
    telefone = Column(String(20))
    data_nascimento = Column(Date)

    usuario = relationship("Usuario", back_populates="aluno")
    matricula = relationship("Matricula", back_populates="aluno")


class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    especialidade = Column(String(20))
    
    usuario = relationship("Usuario", back_populates="professor")
    cursos = relationship("Curso", back_populates="professor")


class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(500))
    professor_id = Column(Integer, ForeignKey("professores.id"))
    carga_horaria = Column(Integer)
    ativo = Column(Boolean, default=True)

    professor = relationship("Professor", back_populates="cursos")
    modulos = relationship("Modulo", back_populates="curso")
    matriculas = relationship("Matricula", back_populates="curso")
    avaliacoes = relationship("Avaliacao", back_populates="curso")


class Modulo(Base):
    __tablename__ = "modulos"

    id = Column(Integer, primary_key=True)
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=False)
    titulo = Column(String(100), nullable=False)
    ordem = Column(Integer)

    curso = relationship("Curso", back_populates="modulos")
    aulas = relationship("Aula", back_populates="modulo")


class Aula(Base):
    __tablename__ = "aulas"

    id = Column(Integer, primary_key=True)
    modulo_id = Column(Integer, ForeignKey("modulos.id"), nullable=False)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(500))
    tipo = Column(String(20))
    url_conteudo = Column(String(255))

    modulo = relationship("Modulo", back_populates="aulas")
    progressos = relationship("Progresso", back_populates="aula")


class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=False)
    data_matricula = Column(Date)
    status = Column(String(20))

    aluno = relationship("Aluno", back_populates="matriculas")
    curso = relationship("Curso", back_populates="matriculas")
    progressos = relationship("Progresso", back_populates="matricula")
    certificado = relationship("Certificado", back_populates="matricula", uselist=False)


class Progresso(Base):
    __tablename__ = "progressos"

    id = Column(Integer, primary_key=True)
    matricula_id = Column(Integer, ForeignKey("matriculas.id"))
    aula_id = Column(Integer, ForeignKey("aulas.id"))
    concluido = Column(Boolean, default=False)
    data_conclusao = Column(Date)

    matricula = relationship("Matricula", back_populates="progressos")
    aula = relationship("Aula", back_populates="progressos")


class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id = Column(Integer, primary_key=True)
    curso_id = Column(Integer, ForeignKey("cursos.id"))
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    nota = Column(Integer)
    comentario = Column(String(500))

    curso = relationship("Curso", back_populates="avaliacoes")


class Certificado(Base):
    __tablename__ = "certificados"

    id = Column(Integer, primary_key=True)
    matricula_id = Column(Integer, ForeignKey("matriculas.id"), unique=True)
    data_emissao = Column(Date)
    codigo_validacao = Column(String(100), unique=True)

    matricula = relationship("Matricula", back_populates="certificado")