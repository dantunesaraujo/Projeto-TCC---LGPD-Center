# =========================
# models.py
# estrutura das tabelas
# do banco de dados
# =========================

from sqlalchemy import Column, Integer, String
from database import Base


# =========================
# USUÁRIOS
# =========================

class User(Base):
    __tablename__ = "users"

    # identificador único
    id = Column(Integer, primary_key=True, index=True)

    # email utilizado no login
    email = Column(String, unique=True, index=True, nullable=False)

    # senha do usuário
    senha = Column(String, nullable=False)


# =========================
# EMPRESA
# =========================

class Empresa(Base):
    __tablename__ = "empresas"

    # identificador único
    id = Column(Integer, primary_key=True, index=True)

    # nome da empresa
    nome = Column(String, nullable=False)

    # CNPJ
    cnpj = Column(String, nullable=False)

    # responsável pela LGPD
    responsavel = Column(String, nullable=True)

    # email de contato
    email = Column(String, nullable=True)


# =========================
# RESPOSTAS
# =========================

class Resposta(Base):
    __tablename__ = "respostas"

    # identificador único da resposta
    id = Column(Integer, primary_key=True, index=True)

    # identifica qual pergunta foi respondida
    pergunta_id = Column(Integer, unique=True, index=True, nullable=False)

    # resposta escolhida pelo usuário
    #
    # valores utilizados:
    # atende
    # parcial
    # nao
    # nao_aplicavel
    resposta = Column(String, nullable=False)