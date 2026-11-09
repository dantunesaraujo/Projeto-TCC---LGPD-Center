# =========================
# respostas.py
# armazenamento das respostas
# =========================

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Resposta
from schemas import RespostaCreate


router = APIRouter()


# cria sessão com o banco
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# ============================================================
# SALVAR OU ATUALIZAR RESPOSTA
# ============================================================

@router.post("/responder")
def responder(
    data: RespostaCreate,
    db: Session = Depends(get_db)
):

    # procura se a pergunta já possui resposta
    resposta_existente = db.query(Resposta).filter(
        Resposta.pergunta_id == data.pergunta_id
    ).first()

    # atualiza caso exista
    if resposta_existente:

        resposta_existente.resposta = data.resposta

    # cria caso seja a primeira resposta
    else:

        nova = Resposta(
            pergunta_id=data.pergunta_id,
            resposta=data.resposta
        )

        db.add(nova)

    db.commit()

    return {
        "msg": "resposta salva com sucesso"
    }


# ============================================================
# LISTAR TODAS AS RESPOSTAS
# ============================================================

@router.get("/respostas")
def listar_respostas(
    db: Session = Depends(get_db)
):

    respostas = db.query(Resposta).all()

    return [
        {
            "pergunta_id": resposta.pergunta_id,
            "resposta": resposta.resposta
        }
        for resposta in respostas
    ]


# ============================================================
# RESETAR TODAS AS RESPOSTAS
# ============================================================

@router.delete("/respostas")
def resetar_respostas(
    db: Session = Depends(get_db)
):

    db.query(Resposta).delete()
    db.commit()

    return {
        "msg": "todas respostas foram removidas"
    }


# ============================================================
# BUSCAR UMA RESPOSTA
# ============================================================

@router.get("/respostas/{pergunta_id}")
def buscar_resposta(
    pergunta_id: int,
    db: Session = Depends(get_db)
):

    resposta = db.query(Resposta).filter(
        Resposta.pergunta_id == pergunta_id
    ).first()

    if not resposta:
        return {
            "encontrado": False
        }

    return {
        "encontrado": True,
        "pergunta_id": resposta.pergunta_id,
        "resposta": resposta.resposta
    }