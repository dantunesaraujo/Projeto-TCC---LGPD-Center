# =========================
# schemas.py
# validação dos dados
# recebidos pela API
# =========================

from typing import Literal
from pydantic import BaseModel, EmailStr


# tipos de resposta permitidos
RespostaTipo = Literal[
    "atende",
    "parcial",
    "nao",
    "nao_aplicavel"
]


# =========================
# LOGIN
# =========================

class UserCreate(BaseModel):
    email: EmailStr
    senha: str


# =========================
# EMPRESA
# =========================

class EmpresaCreate(BaseModel):
    nome: str
    cnpj: str
    responsavel: str
    email: EmailStr


# =========================
# RESPOSTA
# =========================

class RespostaCreate(BaseModel):
    pergunta_id: int
    resposta: RespostaTipo