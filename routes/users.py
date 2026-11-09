# =========================
# users.py - Projeto LGPD
# login e criação de usuário
# =========================

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import User
from schemas import UserCreate


router = APIRouter()


# cria uma sessão com o banco
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# =========================
# LOGIN
# =========================

@router.post("/login")
def login(data: UserCreate, db: Session = Depends(get_db)):

    # procura usuário pelo email
    user = db.query(User).filter(
        User.email == data.email
    ).first()

    # se usuário existir, verifica a senha
    if user:

        if user.senha == data.senha:
            return {
                "msg": "login ok"
            }

        return {
            "erro": "senha incorreta"
        }

    # se não existir, cria um novo usuário
    # essa lógica facilita o uso da versão MVP
    novo_user = User(
        email=data.email,
        senha=data.senha
    )

    db.add(novo_user)
    db.commit()

    return {
        "msg": "usuario criado e login ok"
    }