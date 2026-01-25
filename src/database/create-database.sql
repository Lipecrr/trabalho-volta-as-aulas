create database fjvcursos;
use fjvcursos;

CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    telefone VARCHAR(20),
    data_nascimento DATE
);

CREATE TABLE professores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    telefone VARCHAR(20),
    data_nascimento DATE,
    especialidade VARCHAR(20)
);

CREATE TABLE cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descricao VARCHAR(500),
    professor_id INT,
    carga_horaria INT,
    ativo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (professor_id) REFERENCES professores(id)
);

CREATE TABLE modulos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    curso_id INT NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

CREATE TABLE aulas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modulo_id INT NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    descricao VARCHAR(500),
    tipo VARCHAR(20),
    FOREIGN KEY (modulo_id) REFERENCES modulos(id)
);

CREATE TABLE matriculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT NOT NULL,
    curso_id INT NOT NULL,
    data_matricula DATE,
    status VARCHAR(20),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

CREATE TABLE progressos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    matricula_id INT,
    aula_id INT,
    concluido BOOLEAN DEFAULT FALSE,
    data_conclusao DATE,
    FOREIGN KEY (matricula_id) REFERENCES matriculas(id),
    FOREIGN KEY (aula_id) REFERENCES aulas(id)
);

CREATE TABLE avaliacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    curso_id INT,
    aluno_id INT,
    nota INT,
    comentario VARCHAR(500),
    FOREIGN KEY (curso_id) REFERENCES cursos(id),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
);

CREATE TABLE certificados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT UNIQUE,
    matricula_id INT UNIQUE,
    data_emissao DATE,
    codigo_validacao VARCHAR(100) UNIQUE,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (matricula_id) REFERENCES matriculas(id)
);

