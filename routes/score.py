from fastapi import APIRouter
from database import SessionLocal
from models import Resposta
from routes.perguntas import perguntas, perguntas_por_area

router = APIRouter()


# ============================================================
# CONFIGURAÇÕES
# ============================================================

# Junta todas as perguntas do sistema.
TODAS_AS_PERGUNTAS = perguntas + perguntas_por_area


# ============================================================
# PONTUAÇÃO
# ============================================================

def pontos_resposta(resposta):
    # Atende vale 1 ponto.
    if resposta == "atende":
        return 1

    # Atende parcialmente vale meio ponto.
    if resposta == "parcial":
        return 0.5

    # Não atende vale zero.
    if resposta == "nao":
        return 0

    # N/A não recebe ponto.
    return 0


# ============================================================
# CLASSIFICAÇÃO DE ATENDIMENTO
# ============================================================

def classificar_atendimento(indice):
    if indice <= 25:
        return "Baixo atendimento"

    if indice <= 50:
        return "Atendimento limitado"

    if indice <= 75:
        return "Atendimento intermediário"

    return "Atendimento elevado"


# ============================================================
# CLASSIFICAÇÃO DE RISCO
# ============================================================

def classificar_risco(indice):
    if indice < 40:
        return "alto risco"

    if indice < 70:
        return "risco médio"

    return "baixo risco"


# ============================================================
# DESCRIÇÃO DO RESULTADO
# ============================================================

def gerar_descricao(indice):
    if indice <= 25:
        return (
            "O nível de atendimento à LGPD é baixo. "
            "Existem lacunas relevantes que devem ser priorizadas."
        )

    if indice <= 50:
        return (
            "O nível de atendimento à LGPD é limitado. "
            "Existem pontos importantes que precisam de correção."
        )

    if indice <= 75:
        return (
            "O nível de atendimento à LGPD é intermediário. "
            "Existem controles implantados, mas ainda há oportunidades de melhoria."
        )

    return (
        "O nível de atendimento à LGPD é elevado. "
        "Os controles avaliados apresentam bom nível de atendimento."
    )


# ============================================================
# MAPA DE RESPOSTAS
# ============================================================

def buscar_respostas_map():
    db = SessionLocal()

    try:
        respostas = db.query(Resposta).all()

        resultado = {}

        for item in respostas:
            resultado[item.pergunta_id] = item.resposta

        return resultado

    finally:
        db.close()


# ============================================================
# CÁLCULO DO ÍNDICE
# ============================================================

def calcular_indice(lista_perguntas, respostas_map):
    # Pontuação obtida pelas respostas válidas.
    pontuacao_obtida = 0.0

    # Quantidade de perguntas respondidas com:
    # Atende, Parcial ou Não atende.
    respondidas = 0

    # Quantidade de perguntas marcadas como N/A.
    nao_aplicaveis = 0

    # Quantidade de perguntas sem resposta.
    pendentes = 0

    for pergunta in lista_perguntas:
        pergunta_id = pergunta["id"]

        resposta = respostas_map.get(pergunta_id)

        # Pergunta ainda não respondida.
        # Não entra no cálculo do índice.
        if resposta is None:
            pendentes += 1
            continue

        # N/A não entra na pontuação.
        # Também não entra no denominador.
        if resposta == "nao_aplicavel":
            nao_aplicaveis += 1
            continue

        # Resposta válida.
        respondidas += 1
        pontuacao_obtida += pontos_resposta(resposta)

    # O máximo possível considera somente as perguntas
    # que realmente receberam uma resposta válida.
    pontuacao_maxima = respondidas

    if pontuacao_maxima > 0:
        indice = round(
            (pontuacao_obtida / pontuacao_maxima) * 100,
            2
        )
    else:
        indice = 0

    return {
        "indice": indice,
        "pontuacao_obtida": round(pontuacao_obtida, 2),
        "pontuacao_maxima": pontuacao_maxima,
        "respondidas": respondidas,
        "nao_aplicaveis": nao_aplicaveis,
        "pendentes": pendentes
    }


# ============================================================
# NORMALIZAÇÃO DE ÁREA
# ============================================================

def normalizar_area(area):
    valor = str(area or "").strip().lower()

    if valor in [
        "rh",
        "recursos humanos",
        "recursos humanos (rh)"
    ]:
        return "rh"

    if valor in [
        "juridico",
        "jurídico",
        "juridico / compliance",
        "jurídico / compliance"
    ]:
        return "juridico"

    if valor in [
        "ti",
        "tecnologia",
        "segurança da informação",
        "seguranca da informacao",
        "segurança da informação / ti",
        "seguranca da informacao / ti"
    ]:
        return "ti"

    if valor == "financeiro":
        return "financeiro"

    if valor in [
        "atendimento",
        "comercial",
        "atendimento / comercial"
    ]:
        return "atendimento"

    return valor


# ============================================================
# RESULTADO POR ÁREA
# ============================================================

def gerar_resultados_areas(respostas_map):
    areas = [
        ("rh", "Recursos Humanos (RH)"),
        ("juridico", "Jurídico / Compliance"),
        ("ti", "Segurança da Informação / TI"),
        ("financeiro", "Financeiro"),
        ("atendimento", "Atendimento / Comercial")
    ]

    resultados = []

    for slug, nome in areas:
        # Pega somente as perguntas da área.
        lista_area = [
            pergunta
            for pergunta in perguntas_por_area
            if normalizar_area(pergunta.get("area")) == slug
        ]

        dados = calcular_indice(
            lista_area,
            respostas_map
        )

        indice = dados["indice"]

        resultados.append({
            "nome": nome,
            "area": nome,
            "slug": slug,
            "indice": indice,
            "percentual": indice,
            "classificacao": classificar_atendimento(indice),
            "pontuacao_obtida": dados["pontuacao_obtida"],
            "pontuacao_maxima": dados["pontuacao_maxima"],
            "respondidas": dados["respondidas"],
            "nao_aplicaveis": dados["nao_aplicaveis"],
            "pendentes": dados["pendentes"],
            "total": len(lista_area)
        })

    return resultados


# ============================================================
# RESULTADO POR CATEGORIA
# ============================================================

def gerar_resultados_categorias(respostas_map):
    categorias = [
        "Controle Técnico",
        "Controle Administrativo",
        "Governança"
    ]

    resultados = []

    for categoria in categorias:
        # Seleciona todas as perguntas pertencentes
        # à categoria, independente da área.
        lista_categoria = [
            pergunta
            for pergunta in TODAS_AS_PERGUNTAS
            if pergunta.get("categoria") == categoria
        ]

        dados = calcular_indice(
            lista_categoria,
            respostas_map
        )

        indice = dados["indice"]

        resultados.append({
            "categoria": categoria,
            "indice": indice,
            "percentual": indice,
            "classificacao": classificar_atendimento(indice),
            "pontuacao_obtida": dados["pontuacao_obtida"],
            "pontuacao_maxima": dados["pontuacao_maxima"],
            "respondidas": dados["respondidas"],
            "nao_aplicaveis": dados["nao_aplicaveis"],
            "pendentes": dados["pendentes"],
            "total": len(lista_categoria)
        })

    return resultados


# ============================================================
# DISTRIBUIÇÃO DAS RESPOSTAS
# ============================================================

def gerar_distribuicao(respostas_map):
    contagem = {
        "atende": 0,
        "parcial": 0,
        "nao": 0,
        "nao_aplicavel": 0
    }

    for pergunta in TODAS_AS_PERGUNTAS:
        pergunta_id = pergunta["id"]

        resposta = respostas_map.get(pergunta_id)

        if resposta in contagem:
            contagem[resposta] += 1

    total_respondidas = sum(contagem.values())

    def percentual(valor):
        if total_respondidas == 0:
            return 0

        return round(
            (valor / total_respondidas) * 100,
            2
        )

    return {
        "itens": [
            {
                "nome": "Atende",
                "quantidade": contagem["atende"],
                "percentual": percentual(contagem["atende"])
            },
            {
                "nome": "Atende parcialmente",
                "quantidade": contagem["parcial"],
                "percentual": percentual(contagem["parcial"])
            },
            {
                "nome": "Não atende",
                "quantidade": contagem["nao"],
                "percentual": percentual(contagem["nao"])
            },
            {
                "nome": "Não aplicável (N/A)",
                "quantidade": contagem["nao_aplicavel"],
                "percentual": percentual(contagem["nao_aplicavel"])
            }
        ],
        "atende": {
            "quantidade": contagem["atende"],
            "percentual": percentual(contagem["atende"])
        },
        "parcial": {
            "quantidade": contagem["parcial"],
            "percentual": percentual(contagem["parcial"])
        },
        "nao": {
            "quantidade": contagem["nao"],
            "percentual": percentual(contagem["nao"])
        },
        "nao_aplicavel": {
            "quantidade": contagem["nao_aplicavel"],
            "percentual": percentual(contagem["nao_aplicavel"])
        },
        "total": total_respondidas
    }


# ============================================================
# PLANO DE AÇÃO
# ============================================================

def gerar_plano_acao(resultados_categorias):
    recomendacoes = {
        "Governança": [
            "Definir ou fortalecer responsabilidades relacionadas à proteção de dados.",
            "Revisar processos de governança, avaliação de riscos e tomada de decisões.",
            "Formalizar controles, responsabilidades e evidências de conformidade."
        ],

        "Controle Administrativo": [
            "Revisar políticas, procedimentos e regras internas relacionados ao tratamento de dados.",
            "Formalizar processos de retenção, descarte, treinamento e atendimento aos titulares.",
            "Criar um cronograma para correção das principais lacunas administrativas."
        ],

        "Controle Técnico": [
            "Revisar os controles de acesso e proteção dos sistemas.",
            "Fortalecer criptografia, backups, monitoramento e prevenção de acessos não autorizados.",
            "Criar um plano de correção para os principais controles técnicos identificados."
        ]
    }

    # Menor índice recebe maior prioridade.
    ordenados = sorted(
        resultados_categorias,
        key=lambda item: item["indice"]
    )

    plano = []

    for posicao, item in enumerate(ordenados, start=1):
        categoria = item["categoria"]

        plano.append({
            "prioridade": f"{posicao}ª Prioridade",
            "categoria": categoria,
            "indice": item["indice"],
            "percentual": item["indice"],
            "classificacao": item["classificacao"],
            "acoes": recomendacoes.get(
                categoria,
                []
            )
        })

    return plano


# ============================================================
# RESULTADO GERAL
# ============================================================

def gerar_resultado_geral(respostas_map):
    dados = calcular_indice(
        TODAS_AS_PERGUNTAS,
        respostas_map
    )

    indice = dados["indice"]

    return {
        "indice": indice,
        "score": indice,
        "percentual": indice,

        "classificacao": classificar_atendimento(
            indice
        ),

        "status": classificar_atendimento(
            indice
        ),

        "descricao": gerar_descricao(
            indice
        ),

        "risco": classificar_risco(
            indice
        ),

        "pontuacao_obtida": dados["pontuacao_obtida"],
        "pontuacao_maxima": dados["pontuacao_maxima"],

        "respondidas": dados["respondidas"],
        "nao_aplicaveis": dados["nao_aplicaveis"],
        "pendentes": dados["pendentes"],

        "total": len(
            TODAS_AS_PERGUNTAS
        ),
        "total_perguntas": len(
            TODAS_AS_PERGUNTAS
        )
    }


# ============================================================
# ENDPOINTS
# ============================================================

@router.get("/score")
def score():
    respostas_map = buscar_respostas_map()
    return gerar_resultado_geral(respostas_map)


@router.get("/score-areas")
def score_areas():
    respostas_map = buscar_respostas_map()
    return {
        "areas": gerar_resultados_areas(respostas_map)
    }


@router.get("/score-categorias")
def score_categorias():
    respostas_map = buscar_respostas_map()
    return {
        "categorias": gerar_resultados_categorias(respostas_map)
    }


@router.get("/distribuicao-respostas")
def distribuicao_respostas():
    respostas_map = buscar_respostas_map()
    return gerar_distribuicao(respostas_map)


@router.get("/plano-acao")
def plano_acao():
    respostas_map = buscar_respostas_map()
    categorias = gerar_resultados_categorias(respostas_map)
    return {
        "plano": gerar_plano_acao(categorias)
    }


@router.get("/dashboard-dados")
def dashboard_dados():
    respostas_map = buscar_respostas_map()

    geral = gerar_resultado_geral(respostas_map)
    areas = gerar_resultados_areas(respostas_map)
    categorias = gerar_resultados_categorias(respostas_map)
    distribuicao = gerar_distribuicao(respostas_map)
    plano = gerar_plano_acao(categorias)

    return {
        "geral": geral,
        "areas": areas,
        "categorias": categorias,
        "distribuicao": distribuicao,
        "plano_acao": plano
    }


@router.get("/relatorio-dados")
def relatorio_dados():
    respostas_map = buscar_respostas_map()

    geral = gerar_resultado_geral(respostas_map)
    areas = gerar_resultados_areas(respostas_map)
    categorias = gerar_resultados_categorias(respostas_map)
    distribuicao = gerar_distribuicao(respostas_map)
    plano = gerar_plano_acao(categorias)

    return {
        "geral": geral,
        "areas": areas,
        "categorias": categorias,
        "distribuicao": distribuicao,
        "plano_acao": plano
    }