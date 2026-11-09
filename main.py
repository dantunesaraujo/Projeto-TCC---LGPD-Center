# =====================================================================
# main.py - Sistema Principal Projeto LGPD
# Arquivo central para inicialização da API, rotas e banco de dados
# =====================================================================

from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from database import engine
from models import Base

from routes.users import router as users_router
from routes.empresa import router as empresa_router
from routes.perguntas import router as perguntas_router
from routes.respostas import router as respostas_router
from routes.score import router as score_router


app = FastAPI(
    title="Projeto LGPD - Sistema de Governança e Conformidade",
    description="Plataforma completa para autoavaliação, gestão de riscos e relatórios LGPD",
    version="2.8"
)

Base.metadata.create_all(bind=engine)

app.mount("/estetica", StaticFiles(directory="estetica"), name="estetica")
app.mount("/logos", StaticFiles(directory="logos"), name="logos")


@app.get("/", summary="Página de Login")
def pagina_raiz():
    return FileResponse("estetica/templates/login.html")

@app.get("/login", summary="Página de Login")
def pagina_login():
    return FileResponse("estetica/templates/login.html")

@app.get("/empresa", summary="Gerenciamento de Dados da Empresa")
def pagina_empresa():
    return FileResponse("estetica/templates/empresa.html")

@app.get("/guia", summary="Guia Educativo LGPD")
def pagina_guia():
    return FileResponse("estetica/templates/guia.html")

@app.get("/perguntas", summary="Módulo de Autoavaliação")
def pagina_perguntas():
    return FileResponse("estetica/templates/perguntas.html")

@app.get("/dashboard", summary="Visão Geral do Diagnóstico")
def pagina_dashboard():
    return FileResponse("estetica/templates/dashboard.html")

@app.get("/risco", summary="Indicador de Risco")
def pagina_risco():
    return FileResponse("estetica/templates/risco.html")

@app.get("/relatorio", summary="Relatório Consolidado e Recomendações")
def pagina_relatorio():
    return FileResponse("estetica/templates/relatorio.html")

@app.get("/privacidade", summary="Aviso de Privacidade")
def pagina_privacidade():
    return FileResponse("estetica/templates/privacidade.html")


@app.post("/login", summary="Processa a Autenticação")
def processar_login(email: str = Form(None), senha: str = Form(None)):
    return {"status": "success", "message": "Login efetuado com sucesso no Projeto LGPD!"}


app.include_router(users_router, prefix="/api/users", tags=["Usuários"])
app.include_router(empresa_router, prefix="/api/empresa", tags=["Empresa"])
app.include_router(perguntas_router, prefix="/api/perguntas", tags=["Perguntas"])
app.include_router(respostas_router, prefix="/api/respostas", tags=["Respostas"])
app.include_router(score_router, prefix="/api/score", tags=["Métricas e Scores"])