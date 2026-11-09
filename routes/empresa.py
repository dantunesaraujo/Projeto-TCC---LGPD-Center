# =========================
# empresa.py
# cadastro da empresa
# =========================

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Empresa
from schemas import EmpresaCreate


router = APIRouter()


# cria sessão com o banco
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# =========================
# SALVAR EMPRESA
# =========================

@router.post("/empresa")
def salvar_empresa(
    data: EmpresaCreate,
    db: Session = Depends(get_db)
):

    # procura uma empresa já cadastrada
    empresa = db.query(Empresa).first()

    # atualiza caso já exista
    if empresa:

        empresa.nome = data.nome
        empresa.cnpj = data.cnpj
        empresa.responsavel = data.responsavel
        empresa.email = data.email

    # cria caso ainda não exista
    else:

        empresa = Empresa(
            nome=data.nome,
            cnpj=data.cnpj,
            responsavel=data.responsavel,
            email=data.email
        )

        db.add(empresa)

    # salva alterações
    db.commit()

    return {
        "msg": "empresa salva com sucesso"
    }


# =========================
# BUSCAR EMPRESA
# =========================

@router.get("/empresa/dados")
def pegar_empresa(
    db: Session = Depends(get_db)
):

    empresa = db.query(Empresa).first()

    # caso não exista cadastro
    if not empresa:

        return {
            "nome": "",
            "cnpj": "",
            "responsavel": "",
            "email": ""
        }

    # retorna os dados cadastrados
    return {
        "nome": empresa.nome,
        "cnpj": empresa.cnpj,
        "responsavel": empresa.responsavel,
        "email": empresa.email
    }