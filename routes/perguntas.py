# =========================
# perguntas.py
# perguntas do sistema
# =========================

from fastapi import APIRouter


router = APIRouter()


# ============================================================
# PERGUNTAS GERAIS
# ============================================================

perguntas = [

    {
        "id": 1,
        "area": "Geral",
        "slug": "geral",
        "categoria": "Governança",
        "texto": "Há uma política ou norma de proteção de dados pessoais que trate da finalidade do tratamento; da transparência relacionada à coleta e ao manuseio; da estrutura de proteção de dados; de regras para tomada de decisões em temas de privacidade; e de critérios para aceitação de riscos?"
    },

    {
        "id": 2,
        "area": "Geral",
        "slug": "geral",
        "categoria": "Controle Administrativo",
        "texto": "Existe um canal de comunicação ativo, seguro e público para o recebimento e resposta a solicitações, reclamações e demais questionamentos dos titulares de dados pessoais sobre a forma de tratamento de dados pessoais realizado pela empresa?"
    },

    {
        "id": 3,
        "area": "Geral",
        "slug": "geral",
        "categoria": "Governança",
        "texto": "A empresa possui uma área de Privacidade e Proteção de Dados Pessoais ou um Encarregado pelo Tratamento de Dados Pessoais (DPO) formalmente designado?"
    },

    {
        "id": 4,
        "area": "Geral",
        "slug": "geral",
        "categoria": "Governança",
        "texto": "Há um inventário completo e atualizado de dados pessoais, contendo os agentes de tratamento, a descrição do fluxo (uso, coleta, armazenamento, compartilhamento e eliminação), finalidades, bases legais, categorias de dados e medidas de segurança?"
    },

    {
        "id": 5,
        "area": "Geral",
        "slug": "geral",
        "categoria": "Controle Administrativo",
        "texto": "A empresa possui um aviso de privacidade externo para fornecer aos titulares de dados pessoais informações claras e facilmente acessíveis sobre suas práticas de tratamento de dados, sobre como os dados são protegidos, além das informações de contato do Encarregado de Tratamento de Dados (DPO)?"
    },

    {
        "id": 6,
        "area": "Geral",
        "slug": "geral",
        "categoria": "Controle Administrativo",
        "texto": "É implementada e mantida uma estratégia abrangente de treinamento, educação e conscientização, destinada a garantir que todos os colaboradores compreendam suas responsabilidades e os procedimentos relacionados ao uso e à proteção de dados pessoais?"
    },

    {
        "id": 7,
        "area": "Geral",
        "slug": "geral",
        "categoria": "Governança",
        "texto": "A empresa possui um processo definido para elaboração de Relatório de Impacto à Proteção de Dados Pessoais (RIPD) para atividades de tratamento consideradas de alto risco aos titulares?"
    },

    {
        "id": 8,
        "area": "Geral",
        "slug": "geral",
        "categoria": "Controle Técnico",
        "texto": "A empresa possui uma equipe dedicada à resposta a incidentes de segurança envolvendo dados pessoais, além de um plano de resposta formalizado e comunicado a todas as áreas envolvidas nos processos de detecção, resposta e recuperação?"
    },

    {
        "id": 9,
        "area": "Geral",
        "slug": "geral",
        "categoria": "Controle Administrativo",
        "texto": "As medidas para uso e proteção de dados pessoais são monitoradas e auditadas para assegurar que as operações que envolvem o tratamento de dados pessoais estejam em conformidade com o disposto em leis e regulamentações aplicáveis?"
    },

    {
        "id": 10,
        "area": "Geral",
        "slug": "geral",
        "categoria": "Governança",
        "texto": "A empresa possui mapeadas as transferências internacionais de dados pessoais realizadas em suas operações, incluindo os países de destino e as organizações ou provedores envolvidos, bem como salvaguardas adequadas para essa transferência?"
    }
]


# ============================================================
# PERGUNTAS POR ÁREA
# ============================================================

perguntas_por_area = [

    # =========================
    # RH
    # =========================

    {
        "id": 101,
        "area": "Recursos Humanos (RH)",
        "slug": "rh",
        "categoria": "Controle Técnico",
        "texto": "A empresa realiza o tratamento de dados pessoais e sensíveis dos colaboradores com medidas de segurança adequadas (ex: criptografia, controle de acesso e segmentação de ambientes)?"
    },

    {
        "id": 102,
        "area": "Recursos Humanos (RH)",
        "slug": "rh",
        "categoria": "Controle Administrativo",
        "texto": "Os dados dos colaboradores são utilizados apenas para finalidades legítimas e específicas (ex: folha de pagamento, benefícios, obrigações legais), sem uso indevido ou excessivo?"
    },

    {
        "id": 103,
        "area": "Recursos Humanos (RH)",
        "slug": "rh",
        "categoria": "Controle Administrativo",
        "texto": "Existe política definida para armazenamento, retenção e descarte de dados dos colaboradores?"
    },


    # =========================
    # JURÍDICO / COMPLIANCE
    # =========================

    {
        "id": 201,
        "area": "Jurídico / Compliance",
        "slug": "juridico",
        "categoria": "Controle Administrativo",
        "texto": "Os contratos com terceiros (fornecedores, parceiros, prestadores de serviço) possuem cláusulas específicas de proteção de dados e privacidade conforme a LGPD?"
    },

    {
        "id": 202,
        "area": "Jurídico / Compliance",
        "slug": "juridico",
        "categoria": "Governança",
        "texto": "A empresa define formalmente, nos contratos, os papéis de controlador e operador de dados pessoais nas relações com terceiros?"
    },

    {
        "id": 203,
        "area": "Jurídico / Compliance",
        "slug": "juridico",
        "categoria": "Governança",
        "texto": "A empresa realiza revisão jurídica periódica dos contratos, termos e acordos de confidencialidade (NDA) firmados com terceiros, incluindo a elaboração de aditivos contratuais quando necessário, para garantir conformidade contínua com a LGPD?"
    },


    # =========================
    # TI
    # =========================

    {
        "id": 301,
        "area": "Segurança da Informação / TI",
        "slug": "ti",
        "categoria": "Controle Técnico",
        "texto": "A empresa adota medidas técnicas de segurança (como criptografia, controle de acesso e backups) para proteção de dados pessoais?"
    },

    {
        "id": 302,
        "area": "Segurança da Informação / TI",
        "slug": "ti",
        "categoria": "Controle Técnico",
        "texto": "Existe monitoramento contínuo e mecanismos para prevenção de acessos não autorizados aos sistemas?"
    },

    {
        "id": 303,
        "area": "Segurança da Informação / TI",
        "slug": "ti",
        "categoria": "Controle Técnico",
        "texto": "A organização possui uma política de gestão de identidades e senhas (ex: autenticação, controle de usuários)?"
    },


    # =========================
    # FINANCEIRO
    # =========================

    {
        "id": 401,
        "area": "Financeiro",
        "slug": "financeiro",
        "categoria": "Controle Administrativo",
        "texto": "Os dados financeiros e bancários são tratados com níveis de confidencialidade?"
    },

    {
        "id": 402,
        "area": "Financeiro",
        "slug": "financeiro",
        "categoria": "Controle Administrativo",
        "texto": "A empresa valida se os dados financeiros coletados são estritamente necessários para a finalidade do processo financeiro, evitando coleta excessiva de informações?"
    },

    {
        "id": 403,
        "area": "Financeiro",
        "slug": "financeiro",
        "categoria": "Governança",
        "texto": "Existem regras claras para o compartilhamento de dados financeiros com bancos, contadores e instituições financeiras, garantindo conformidade com a LGPD?"
    },


    # =========================
    # ATENDIMENTO / COMERCIAL
    # =========================

    {
        "id": 501,
        "area": "Atendimento / Comercial",
        "slug": "atendimento",
        "categoria": "Controle Administrativo",
        "texto": "A empresa informa de forma clara ao cliente a finalidade da coleta de seus dados pessoais?"
    },

    {
        "id": 502,
        "area": "Atendimento / Comercial",
        "slug": "atendimento",
        "categoria": "Controle Administrativo",
        "texto": "A empresa registra e gerencia o consentimento do cliente para uso de seus dados, garantindo possibilidade de revogação quando aplicável?"
    },

    {
        "id": 503,
        "area": "Atendimento / Comercial",
        "slug": "atendimento",
        "categoria": "Governança",
        "texto": "Os dados coletados são utilizados apenas para as finalidades informadas ao titular?"
    }
]


# ============================================================
# ROTA DAS PERGUNTAS GERAIS
# ============================================================

@router.get("/perguntas")
def listar_perguntas_gerais():
    return perguntas


# ============================================================
# ROTA DAS PERGUNTAS POR ÁREA
# ============================================================

@router.get("/perguntas-areas")
def listar_perguntas_por_area():
    return perguntas_por_area


# ============================================================
# LISTA DE ÁREAS
# ============================================================

@router.get("/areas")
def listar_areas():

    return [
        {
            "slug": "geral",
            "nome": "Avaliação Geral"
        },
        {
            "slug": "rh",
            "nome": "Recursos Humanos (RH)"
        },
        {
            "slug": "juridico",
            "nome": "Jurídico / Compliance"
        },
        {
            "slug": "ti",
            "nome": "Segurança da Informação / TI"
        },
        {
            "slug": "financeiro",
            "nome": "Financeiro"
        },
        {
            "slug": "atendimento",
            "nome": "Atendimento / Comercial"
        }
    ]