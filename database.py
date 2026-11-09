# =========================
# database.py
# conexão com banco SQLite - Projeto LGPD
# =========================

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# arquivo onde os dados do Projeto LGPD serão armazenados
DATABASE_URL = "sqlite:///./projeto_lgpd.db"


# cria a conexão principal com o banco
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# cria sessões para consultar e alterar os dados
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# base utilizada pelos models
Base = declarative_base()