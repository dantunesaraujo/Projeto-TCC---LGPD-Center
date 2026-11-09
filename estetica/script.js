/**
 * =====================================================================
 * LGPD Center - Script Principal de Controle e Renderização (v3.5)
 * =====================================================================
 */

const PERGUNTAS = [
    { id: 1, area: "Geral", categoria: "🟢 Controle Administrativo", texto: "Há uma política ou norma de proteção de dados pessoais que trate da finalidade do tratamento; da transparência relacionada à coleta e ao manuseio; da estrutura de proteção de dados; de regras para tomada de decisões em temas de privacidade; e de critérios para aceitação de riscos?" },
    { id: 2, area: "Geral", categoria: "🟢 Controle Administrativo", texto: "Existe um canal de comunicação ativo, seguro e público para o recebimento e resposta a solicitações, reclamações e demais questionamentos dos titulares de dados pessoais sobre a forma de tratamento de dados pessoais realizado pela empresa?" },
    { id: 3, area: "Geral", categoria: "🟢 Controle Administrativo", texto: "A empresa possui uma área de Privacidade e Proteção de Dados Pessoais ou um Encarregado pelo Tratamento de Dados Pessoais (DPO) formalmente designado?" },
    { id: 4, area: "Geral", categoria: "🟢 Controle Administrativo", texto: "Há um inventário completo e atualizado de dados pessoais, contendo os agentes de tratamento, a descrição do fluxo (uso, coleta, armazenamento, compartilhamento e eliminação), finalidades, bases legais, categorias de dados e medidas de segurança?" },
    { id: 5, area: "Geral", categoria: "🟢 Controle Administrativo", texto: "A empresa possui um aviso de privacidade externo para fornecer aos titulares de dados pessoais informações claras e facilmente acessíveis sobre suas práticas de tratamento de dados, sobre como os dados são protegidos, além das informações de contato do Encarregado de Tratamento de Dados (DPO)?" },
    { id: 6, area: "Geral", categoria: "🟢 Controle Administrativo", texto: "É implementada e mantida uma estratégia abrangente de treinamento, educação e conscientização, destinada a garantir que todos os colaboradores compreendam suas responsabilidades e os procedimentos relacionados ao uso e à proteção de dados pessoais?" },
    { id: 7, area: "Geral", categoria: "🟢 Controle Administrativo", texto: "A empresa possui um processo definido para elaboração de Relatório de Impacto à Proteção de Dados Pessoais (RIPD) para atividades de tratamento consideradas de alto risco aos titulares?" },
    { id: 8, area: "Geral", categoria: "🔵 Controle Técnico", texto: "A empresa possui uma equipe dedicada à resposta a incidentes de segurança envolvendo dados pessoais, além de um plano de resposta formalizado e comunicado a todas as áreas envolvidas nos processos de detecção, resposta e recuperação?" },
    { id: 9, area: "Geral", categoria: "🟢 Controle Administrativo", texto: "As medidas para uso e proteção de dados pessoais são monitoradas e auditadas para assegurar que as operações que envolvem o tratamento de dados pessoais estejam em conformidade com o disposto em leis e regulamentações aplicáveis?" },
    { id: 10, area: "Geral", categoria: "🟢 Controle Administrativo", texto: "A empresa possui mapeadas as transferências internacionais de dados pessoais realizadas em suas operações, incluindo os países de destino e as organizações ou provedores envolvidos, bem como salvaguardas adequadas para essa transferência?" },

    { id: 11, area: "Recursos Humanos (RH)", categoria: "🔵 Controle Técnico", texto: "A empresa realiza o tratamento de dados pessoais e sensíveis dos colaboradores com medidas de segurança adequadas (ex: criptografia, controle de acesso e segmentação de ambientes)?" },
    { id: 12, area: "Recursos Humanos (RH)", categoria: "🟢 Controle Administrativo", texto: "Os dados dos colaboradores são utilizados apenas para finalidades legítimas e específicas (ex: folha de pagamento, benefícios, obrigações legais), sem uso indevido ou excessivo?" },
    { id: 13, area: "Recursos Humanos (RH)", categoria: "🟢 Controle Administrativo", texto: "Existe política definida para armazenamento, retenção e descarte de dados dos colaboradores?" },
    { id: 14, area: "Recursos Humanos (RH)", categoria: "🔵 Controle Técnico", texto: "O acesso aos dados pessoais dos colaboradores é restrito aos profissionais autorizados, de acordo com suas funções e responsabilidades?" },

    { id: 15, area: "Segurança da Informação / TI", categoria: "🔵 Controle Técnico", texto: "A empresa adota medidas técnicas de segurança (como criptografia, controle de acesso e backups) para proteção de dados pessoais?" },
    { id: 16, area: "Segurança da Informação / TI", categoria: "🔵 Controle Técnico", texto: "Existe monitoramento contínuo e mecanismos para prevenção de acessos não autorizados aos sistemas?" },
    { id: 17, area: "Segurança da Informação / TI", categoria: "🔵 Controle Técnico", texto: "A organização possui uma política de gestão de identidades e senhas (ex: autenticação, controle de usuários)?" },
    { id: 18, area: "Segurança da Informação / TI", categoria: "🔵 Controle Técnico", texto: "A empresa realiza testes periódicos para identificar vulnerabilidades nos sistemas, aplicações e dispositivos que armazenam ou processam dados pessoais?" },

    { id: 19, area: "Financeiro", categoria: "🔵 Controle Técnico", texto: "Os dados financeiros e bancários são tratados com níveis de confidencialidade?" },
    { id: 20, area: "Financeiro", categoria: "🟢 Controle Administrativo", texto: "A empresa valida se os dados financeiros coletados são estritamente necessários para a finalidade do processo financeiro, evitando coleta excessiva de informações?" },
    { id: 21, area: "Financeiro", categoria: "🟢 Controle Administrativo", texto: "Existem regras claras para o compartilhamento de dados financeiros com bancos, contadores e instituições financeiras, garantindo conformidade com a LGPD?" },

    { id: 22, area: "Atendimento / Comercial", categoria: "🟢 Controle Administrativo", texto: "A empresa informa de forma clara ao cliente a finalidade da coleta de seus dados pessoais?" },
    { id: 23, area: "Atendimento / Comercial", categoria: "🟢 Controle Administrativo", texto: "A empresa registra e gerencia o consentimento do cliente para uso de seus dados, garantindo possibilidade de revogação quando aplicável?" },
    { id: 24, area: "Atendimento / Comercial", categoria: "🟢 Controle Administrativo", texto: "Os dados coletados são utilizados apenas para as finalidades informadas ao titular?" }
];

function obterRespostas() {
    try {
        return JSON.parse(localStorage.getItem("lgpd_respostas") || "{}");
    } catch (e) {
        return {};
    }
}

function responder(id, valor) {
    let respostas = obterRespostas();
    respostas[id] = valor;
    localStorage.setItem("lgpd_respostas", JSON.stringify(respostas));
    atualizarProgressoLocal();
}

function carregarPerguntasPorArea() {
    let selectArea = document.getElementById("select-area");
    if (!selectArea) return;

    let areaSelecionada = selectArea.value;
    let mapa = obterRespostas();
    let filtradas = areaSelecionada === "Todas" 
        ? PERGUNTAS 
        : PERGUNTAS.filter(p => p.area === areaSelecionada);

    renderizarPerguntas(filtradas, mapa);
}

function renderizarPerguntas(perguntas, mapa) {
    let html = "";
    perguntas.forEach((pergunta, index) => {
        let valorAtual = mapa[pergunta.id] || "";
        html += `
            <div class="card-pergunta">
                <div class="pergunta-topo">
                    <div class="pergunta-topo-esq">
                        <span class="badge-pergunta">Pergunta ${index + 1}</span>
                        <span class="badge-area">${pergunta.area}</span>
                    </div>
                    <span class="badge-categoria">${pergunta.categoria}</span>
                </div>
                <p>${pergunta.texto}</p>
                <select onchange="responder(${pergunta.id}, this.value)">
                    <option value="" ${valorAtual === "" ? "selected" : ""}>Selecione uma resposta...</option>
                    <option value="atende" ${valorAtual === "atende" ? "selected" : ""}>Atende</option>
                    <option value="parcial" ${valorAtual === "parcial" ? "selected" : ""}>Atende parcialmente</option>
                    <option value="nao" ${valorAtual === "nao" ? "selected" : ""}>Não atende</option>
                    <option value="nao_aplicavel" ${valorAtual === "nao_aplicavel" ? "selected" : ""}>Não aplicável (N/A)</option>
                </select>
            </div>
        `;
    });

    let div = document.getElementById("perguntas");
    if (div) div.innerHTML = html;
    atualizarProgressoLocal();
}

function atualizarProgressoLocal() {
    let respostas = obterRespostas();
    let total = PERGUNTAS.length;
    let respondidas = Object.keys(respostas).filter(k => respostas[k] !== "").length;
    let el = document.getElementById("progresso-texto");
    if (el) el.innerText = `${respondidas} de ${total} respondidas`;
}

function calcularMétricas() {
    let respostas = obterRespostas();
    let porArea = {};

    let catAdminAtrib = 0, catAdminPoss = 0;
    let catTecAtrib = 0, catTecPoss = 0;

    PERGUNTAS.forEach(p => {
        if (!porArea[p.area]) {
            porArea[p.area] = { atribuidos: 0, possiveis: 0, total: 0, respondidas: 0 };
        }
        porArea[p.area].total += 1;

        let v = respostas[p.id];
        if (v && v !== "") {
            porArea[p.area].respondidas += 1;
        }

        let peso = 0;
        let poss = 1;
        if (v === "atende") { peso = 1; }
        else if (v === "parcial") { peso = 0.5; }
        else if (v === "nao") { peso = 0; }
        else { poss = 0; }

        if (poss > 0) {
            if (p.categoria.includes("Administrativo")) {
                catAdminAtrib += peso;
                catAdminPoss += 1;
            } else {
                catTecAtrib += peso;
                catTecPoss += 1;
            }
        }
    });

    let indiceAdmin = catAdminPoss > 0 ? (catAdminAtrib / catAdminPoss) * 100 : 0;
    let indiceTec = catTecPoss > 0 ? (catTecAtrib / catTecPoss) * 100 : 0;

    let blocosAtivos = 0;
    let somaBlocos = 0;
    if (catAdminPoss > 0) { somaBlocos += indiceAdmin; blocosAtivos++; }
    if (catTecPoss > 0) { somaBlocos += indiceTec; blocosAtivos++; }
    
    let indiceGeral = blocosAtivos > 0 ? (somaBlocos / blocosAtivos).toFixed(1) : 0;

    let resultadoAreas = {};
    for (let area in porArea) {
        let pArea = PERGUNTAS.filter(x => x.area === area);
        let atrA = 0, possA = 0;
        pArea.forEach(x => {
            let v = respostas[x.id];
            if (v === "atende") { atrA += 1; possA += 1; }
            else if (v === "parcial") { atrA += 0.5; possA += 1; }
            else if (v === "nao") { possA += 1; }
        });
        resultadoAreas[area] = {
            indice: possA > 0 ? ((atrA / possA) * 100).toFixed(1) : 0,
            respondidas: porArea[area].respondidas,
            total: porArea[area].total
        };
    }

    let respondidasTotal = Object.keys(respostas).filter(k => respostas[k] !== "").length;

    return { 
        indice: parseFloat(indiceGeral), 
        indiceAdmin: parseFloat(indiceAdmin),
        indiceTec: parseFloat(indiceTec),
        respondidas: respondidasTotal, 
        total: PERGUNTAS.length,
        areas: resultadoAreas 
    };
}

function carregarVisaoGeral() {
    let m = calcularMétricas();
    let totalPerguntas = PERGUNTAS.length;
    let porcentagemProgresso = totalPerguntas > 0 ? ((m.respondidas / totalPerguntas) * 100).toFixed(0) : 0;

    let elProgresso = document.getElementById("progresso-total-num");
    if (elProgresso) elProgresso.innerText = `${porcentagemProgresso}% (${m.respondidas}/${totalPerguntas})`;

    let elPontuacao = document.getElementById("pontuacao-num");
    if (elPontuacao) {
        elPontuacao.innerText = `${m.indice}%`;
        let v = m.indice;
        if (v <= 25) elPontuacao.style.color = "#ef4444";
        else if (v <= 50) elPontuacao.style.color = "#f97316";
        else if (v <= 75) elPontuacao.style.color = "#eab308";
        else elPontuacao.style.color = "#22c55e";
    }

    let containerAreas = document.getElementById("pontuacao-por-area");
    if (containerAreas) {
        let html = "";
        for (let area in m.areas) {
            let info = m.areas[area];
            html += `
                <div class="area-progress-item">
                    <div class="area-progress-header">
                        <span><strong>${area}</strong></span>
                        <span>${info.indice}% (${info.respondidas}/${info.total})</span>
                    </div>
                    <div class="area-progress-bar-bg">
                        <div class="area-progress-bar-fill" style="width: ${info.indice}%;"></div>
                    </div>
                </div>
            `;
        }
        containerAreas.innerHTML = html;
    }
}

function gerarGrafico() {
    let canvas = document.getElementById("grafico");
    if (!canvas) return;

    let rect = canvas.getBoundingClientRect();
    let dpr = window.devicePixelRatio || 1;

    let alturaCSS = 80;

    canvas.width = rect.width * dpr;
    canvas.height = alturaCSS * dpr;
    
    canvas.style.width = rect.width + "px";
    canvas.style.height = alturaCSS + "px";

    let ctx = canvas.getContext("2d");
    ctx.scale(dpr, dpr);

    let larguraCSS = rect.width;
    let métricas = calcularMétricas();
    let valor = métricas.indice;

    ctx.clearRect(0, 0, larguraCSS, alturaCSS);
    ctx.fillStyle = "#0f172a";
    ctx.fillRect(0, 0, larguraCSS, alturaCSS);

    if (valor <= 25) ctx.fillStyle = "#ef4444";
    else if (valor <= 50) ctx.fillStyle = "#f97316";
    else if (valor <= 75) ctx.fillStyle = "#eab308";
    else ctx.fillStyle = "#22c55e";

    ctx.fillRect(0, 0, (valor / 100) * larguraCSS, alturaCSS);
    
    ctx.fillStyle = "#ffffff";
    ctx.font = "bold 22px Montserrat, sans-serif";
    ctx.textBaseline = "middle";
    ctx.fillText(`Índice Geral de Conformidade: ${valor}%`, 24, alturaCSS / 2);
}

function carregarRelatorioFinal() {
    let dadosEmpresa = JSON.parse(localStorage.getItem("lgpd_empresa") || "{}");
    
    if (document.getElementById("rel_nome")) document.getElementById("rel_nome").innerText = dadosEmpresa.nome || "Não informado";
    if (document.getElementById("rel_cnpj")) document.getElementById("rel_cnpj").innerText = dadosEmpresa.cnpj || "Não informado";
    if (document.getElementById("rel_responsavel")) document.getElementById("rel_responsavel").innerText = dadosEmpresa.responsavel || "Não informado";
    if (document.getElementById("rel_email")) document.getElementById("rel_email").innerText = dadosEmpresa.email || "Não informado";

    let m = calcularMétricas();
    let elIndiceGeral = document.getElementById("rel_indice_geral");
    if (elIndiceGeral) {
        elIndiceGeral.innerText = `${m.indice}%`;
        let v = m.indice;
        if (v <= 25) elIndiceGeral.style.color = "#ef4444";
        else if (v <= 50) elIndiceGeral.style.color = "#f97316";
        else if (v <= 75) elIndiceGeral.style.color = "#eab308";
        else elIndiceGeral.style.color = "#22c55e";
    }

    let tabelaAreas = document.getElementById("rel_tabela_areas");
    if (tabelaAreas) {
        let html = "";
        for (let area in m.areas) {
            let info = m.areas[area];
            html += `
                <tr style="border-bottom: 1px solid #334155;">
                    <td style="padding: 6px 10px;"><strong>${area}</strong></td>
                    <td style="padding: 6px 10px;">${info.respondidas} / ${info.total}</td>
                    <td style="padding: 6px 10px;"><span style="color: #38bdf8; font-weight: bold;">${info.indice}%</span></td>
                </tr>
            `;
        }
        tabelaAreas.innerHTML = html;
    }

    let containerPlanos = document.getElementById("rel_planos_acao");
    if (containerPlanos) {
        let recomendacoesHtml = "";
        let v = m.indice;
        let mesmoIndice = m.indiceAdmin === m.indiceTec;
        let focaAdmin = m.indiceAdmin <= m.indiceTec;

        if (v <= 25) {
            if (mesmoIndice) {
                recomendacoesHtml = `
                    <div style="padding: 12px; background-color: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; line-height: 1.5;">
                        <strong style="color: #f87171;">Nível Inicial - Administrativo e Técnico (Atenção Equivalente):</strong><br>
                        Com nível inicial de maturidade e pontuação idêntica entre os controles administrativos e técnicos, recomenda-se uma abordagem integrada. A empresa deve estabelecer os fundamentos da governança de dados pessoais, definindo responsabilidades, fluxos e diretrizes básicas de governança, paralelamente à implementação de medidas elementares de segurança da informação (como controle de senhas, restrição de acessos e cópias de segurança). Os esforços devem ser distribuídos igualmente entre organizar os processos internos e proteger os ativos tecnológicos contra riscos imediatos.
                    </div>`;
            } else if (focaAdmin) {
                recomendacoesHtml = `
                    <div style="padding: 12px; background-color: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; line-height: 1.5;">
                        <strong style="color: #f87171;">Nível Inicial - Administrativo:</strong><br>
                        Com nível inicial de maturidade, recomenda-se que a empresa estabeleça os fundamentos da governança de dados pessoais, definindo responsabilidades e diretrizes para orientar o tratamento das informações. Primeiramente, deve identificar quem será responsável por coordenar as atividades de proteção de dados e quais colaboradores participam dessas operações. Em seguida, deve documentar os principais processos de coleta, utilização, armazenamento e descarte de dados pessoais, identificando as finalidades e as necessidades de cada atividade. Com base nesse levantamento, devem ser elaboradas orientações internas sobre o tratamento adequado das informações, incluindo regras de confidencialidade e responsabilidades dos colaboradores. As diretrizes devem ser comunicadas aos envolvidos, acompanhadas de orientações básicas sobre a LGPD. Por fim, a empresa deve manter os documentos organizados e estabelecer uma rotina de revisão para garantir que as práticas adotadas permaneçam alinhadas às atividades realizadas.
                    </div>`;
            } else {
                recomendacoesHtml = `
                    <div style="padding: 12px; background-color: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; line-height: 1.5;">
                        <strong style="color: #f87171;">Nível Inicial - Técnico:</strong><br>
                        Com nível inicial de maturidade, recomenda-se que a empresa implemente medidas básicas de segurança da informação para reduzir os riscos de acesso não autorizado, perda ou exposição de dados pessoais. Inicialmente, deve identificar os computadores, dispositivos, sistemas e locais de armazenamento utilizados no tratamento dessas informações. Com base nesse levantamento, deve restringir o acesso aos dados conforme as necessidades de cada colaborador, eliminar contas desnecessárias e estabelecer requisitos mínimos para a criação de senhas. Também deve manter os sistemas operacionais e aplicativos atualizados, utilizar soluções de proteção contra códigos maliciosos e implementar rotinas de cópias de segurança dos dados importantes. A empresa deve definir quem será responsável pela manutenção desses controles e pela verificação das cópias de segurança. Por fim, deve realizar verificações periódicas para identificar falhas, corrigir configurações inadequadas e confirmar que as medidas implementadas continuam funcionando.
                    </div>`;
            }
        } else if (v <= 50) {
            if (mesmoIndice) {
                recomendacoesHtml = `
                    <div style="padding: 12px; background-color: rgba(249, 115, 22, 0.1); border: 1px solid rgba(249, 115, 22, 0.3); border-radius: 8px; line-height: 1.5;">
                        <strong style="color: #fb923c;">Nível Básico - Administrativo e Técnico (Atenção Equivalente):</strong><br>
                        Com nível básico de maturidade e índices equivalentes nas duas frentes, a organização deve atuar simultaneamente na formalização de seus processos administrativos (políticas, inventários e tratamento de solicitações) e no fortalecimento dos controles técnicos (gestão de acessos, autenticação e verificação de backups), garantindo que a evolução da governança ocorra em sintonia com a segurança dos sistemas.
                    </div>`;
            } else if (focaAdmin) {
                recomendacoesHtml = `
                    <div style="padding: 12px; background-color: rgba(249, 115, 22, 0.1); border: 1px solid rgba(249, 115, 22, 0.3); border-radius: 8px; line-height: 1.5;">
                        <strong style="color: #fb923c;">Nível Básico - Administrativo:</strong><br>
                        Com nível básico de maturidade, recomenda-se que a empresa formalize seus processos de proteção de dados, transformando as orientações existentes em procedimentos documentados e aplicáveis às atividades cotidianas. Para isso, deve revisar o levantamento dos dados pessoais tratados e identificar os processos que precisam de regras específicas, como atendimento a solicitação dos titulares, compartilhamento de informações, descarte de documentos e comunicação de incidentes. Em seguida, deve elaborar ou revisar políticas e procedimentos, definindo responsáveis, etapas de execução e critérios para registro das atividades. Também deve estabelecer um processo para identificar e avaliar riscos relacionados ao tratamento de dados pessoais, priorizando situações que possam ocasionar impactos relevantes. Os documentos devem ser aprovados pelos responsáveis pertinentes, disponibilizados aos colaboradores e acompanhados de orientações sobre sua aplicação. Por fim, a empresa deve estabelecer uma periodicidade de revisão e manter registros das atualizações realizadas, verificando se os procedimentos estão sendo efetivamente seguidos.
                    </div>`;
            } else {
                recomendacoesHtml = `
                    <div style="padding: 12px; background-color: rgba(249, 115, 22, 0.1); border: 1px solid rgba(249, 115, 22, 0.3); border-radius: 8px; line-height: 1.5;">
                        <strong style="color: #fb923c;">Nível Básico - Técnico:</strong><br>
                        Com nível básico de maturidade, recomenda-se que a empresa fortaleça os controles técnicos existentes para garantir que os dados pessoais sejam acessados apenas por usuários autorizados e permaneçam protegidos durante seu armazenamento e utilização. Inicialmente, deve levantar os sistemas, diretórios e aplicações que armazenam essas informações, identificando os usuários e os respectivos níveis de permissão. Em seguida, deve revisar os acessos concedidos, remover permissões excessivas e estabelecer um procedimento para conceder, alterar e revogar acessos conforme as mudanças de função ou o desligamento de colaboradores. Sempre que tecnicamente viável, deve implementar autenticação multifator nos sistemas que apresentem maior risco e manter registros de atividades relevantes. Também deve verificar a integridade das cópias de segurança por meio de testes de restauração e avaliar a existência de vulnerabilidades decorrentes de sistemas desatualizados ou configurações inadequadas. Os responsáveis técnicos devem documentar as correções realizadas e estabelecer revisões periódicas das permissões e dos controles implementados.
                    </div>`;
            }
        } else if (v <= 75) {
            if (mesmoIndice) {
                recomendacoesHtml = `
                    <div style="padding: 12px; background-color: rgba(234, 179, 8, 0.1); border: 1px solid rgba(234, 179, 8, 0.3); border-radius: 8px; line-height: 1.5;">
                        <strong style="color: #facc15;">Nível Intermediário - Administrativo e Técnico (Atenção Equivalente):</strong><br>
                        Com nível intermediário de maturidade e pontuação equivalente, a empresa deve estruturar de forma conjunta a gestão de riscos de governança (avaliação de fornecedores, planos de tratamento de riscos) e aprimorar os mecanismos técnicos de monitoramento (alertas de segurança, resposta a incidentes e testes de recuperação). Ambas as frentes demandam atenção balanceada para elevar o patamar de conformidade.
                    </div>`;
            } else if (focaAdmin) {
                recomendacoesHtml = `
                    <div style="padding: 12px; background-color: rgba(234, 179, 8, 0.1); border: 1px solid rgba(234, 179, 8, 0.3); border-radius: 8px; line-height: 1.5;">
                        <strong style="color: #facc15;">Nível Intermediário - Administrativo:</strong><br>
                        Com nível intermediário de maturidade, recomenda-se que a empresa aprimore sua governança por meio de um processo estruturado de gestão de riscos relacionados à proteção de dados pessoais. Inicialmente, deve revisar os riscos identificados nos processos de tratamento, considerando as ameaças, as vulnerabilidades, os impactos potenciais e os controles existentes. Com base nessa análise, deve estabelecer critérios de priorização e definir planos de tratamento para os riscos que demandem medidas adicionais. Cada ação deve possuir um responsável, um prazo de execução e um resultado esperado, permitindo acompanhar sua implementação. A empresa também deve estabelecer indicadores para monitorar aspectos como pendências de adequação, conclusão de ações corretivas e recorrência de incidentes. Quando pertinente, a avaliação deve abranger fornecedores que tenham acesso a dados pessoais ou participem de seu tratamento, considerando os riscos associados a essas relações. Periodicamente, os resultados devem ser apresentados aos responsáveis pela gestão, permitindo revisar prioridades, avaliar a efetividade das medidas adotadas e direcionar recursos para as lacunas mais relevantes.
                    </div>`;
            } else {
                recomendacoesHtml = `
                    <div style="padding: 12px; background-color: rgba(234, 179, 8, 0.1); border: 1px solid rgba(234, 179, 8, 0.3); border-radius: 8px; line-height: 1.5;">
                        <strong style="color: #facc15;">Nível Intermediário - Técnico:</strong><br>
                        Com nível intermediário de maturidade, recomenda-se que a empresa aprimore os mecanismos de monitoramento para identificar atividades suspeitas e responder de maneira estruturada a possíveis incidentes envolvendo dados pessoais. Primeiramente, deve identificar quais sistemas e ambientes são mais relevantes para a proteção dessas informações e verificar quais registros de atividades estão disponíveis. Em seguida, deve configurar mecanismos de registro e alertas para eventos prioritários, como tentativas de acesso indevido, alterações incomuns de permissões e transferências atípicas de informações, conforme os recursos tecnológicos disponíveis. Também deve definir critérios para analisar os alertas, registrar ocorrências e encaminhar situações suspeitas aos responsáveis pela segurança da informação. Paralelamente, deve testar os procedimentos de recuperação de dados e realizar exercícios para avaliar a capacidade de resposta a incidentes. Os resultados dos testes e das análises devem ser documentados, permitindo identificar falhas e estabelecer medidas corretivas. Por fim, a empresa deve acompanhar indicadores de efetividade, como recorrência de eventos, tempo de análise e conclusão das correções, utilizando essas informações para aprimorar continuamente os controles técnicos.
                    </div>`;
            }
        } else {
            if (mesmoIndice) {
                recomendacoesHtml = `
                    <div style="padding: 12px; background-color: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.3); border-radius: 8px; line-height: 1.5;">
                        <strong style="color: #4ade80;">Nível Avançado - Administrativo e Técnico (Atenção Equivalente):</strong><br>
                        Com nível avançado de maturidade e índices equivalentes, a organização demonstra excelência equilibrada. O foco deve ser a consolidação da melhoria contínua em ambas as esferas, combinando revisões periódicas da governança com ciclos de otimização tecnológica e testes avançados de segurança.
                    </div>`;
            } else if (focaAdmin) {
                recomendacoesHtml = `
                    <div style="padding: 12px; background-color: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.3); border-radius: 8px; line-height: 1.5;">
                        <strong style="color: #4ade80;">Nível Avançado - Administrativo:</strong><br>
                        Com nível avançado de maturidade, recomenda-se que a empresa consolide um processo de melhoria contínua da governança de dados, utilizando evidências para avaliar a efetividade dos controles e orientar decisões. Para isso, deve estabelecer ciclos periódicos de avaliação que considerem indicadores de desempenho, resultados de auditorias, incidentes registrados, mudanças nos processos e atualizações regulatórias relevantes. Com base nos resultados, deve identificar oportunidades de aprimoramento, priorizar iniciativas e estabelecer planos de ação com responsáveis, prazos e critérios de conclusão. Também deve avaliar se as políticas e os procedimentos continuam adequados às atividades realizadas, promovendo revisões sempre que forem identificadas mudanças relevantes ou deficiências nos controles. A participação das áreas envolvidas deve ser incentivada, com mecanismos para compartilhar aprendizados e fortalecer a cultura de proteção de dados. Adicionalmente, a empresa deve avaliar periodicamente a maturidade de seus processos e acompanhar a evolução dos indicadores estabelecidos. Os resultados devem subsidiar decisões de gestão, direcionar investimentos e demonstrar se as iniciativas implementadas estão produzindo melhorias sustentáveis.
                    </div>`;
            } else {
                recomendacoesHtml = `
                    <div style="padding: 12px; background-color: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.3); border-radius: 8px; line-height: 1.5;">
                        <strong style="color: #4ade80;">Nível Avançado - Técnico:</strong><br>
                        Com nível avançado de maturidade, recomenda-se que a empresa implemente um processo contínuo de avaliação e otimização dos controles técnicos, priorizando melhorias fundamentadas em riscos, evidências e resultados de testes. Inicialmente, deve analisar os indicadores de segurança, os registros de incidentes, as vulnerabilidades identificadas e a efetividade das medidas de proteção existentes. Com base nessa análise, deve selecionar os controles que necessitam de aprimoramento e avaliar alternativas tecnológicas compatíveis com suas necessidades e capacidades operacionais. Entre as possibilidades estão a automação de verificações de acesso, o aperfeiçoamento da detecção de comportamentos anômalos, o fortalecimento da prevenção contra a perda de dados e a ampliação da visibilidade sobre os ambientes de armazenamento e compartilhamento de informações. Antes de implementar mudanças relevantes, a empresa deve avaliar os riscos envolvidos e realizar testes para verificar se as soluções funcionam conforme o esperado. Após a implementação, deve monitorar os resultados, documentar as melhorias e corrigir eventuais falhas. Esse processo deve ser repetido periodicamente, garantindo que os controles acompanhem a evolução dos riscos, dos recursos tecnológicos e das necessidades do negócio.
                    </div>`;
            }
        }
        containerPlanos.innerHTML = recomendacoesHtml;
    }
}

function salvarEmpresa(event) {
    if (event) event.preventDefault();
    let dados = {
        nome: document.getElementById("emp_nome")?.value || "",
        cnpj: document.getElementById("emp_cnpj")?.value || "",
        responsavel: document.getElementById("emp_responsavel")?.value || "",
        email: document.getElementById("emp_email")?.value || ""
    };
    localStorage.setItem("lgpd_empresa", JSON.stringify(dados));
    alert("Dados da empresa armazenados com sucesso!");
}

function carregarEmpresa() {
    let dados = JSON.parse(localStorage.getItem("lgpd_empresa") || "{}");
    if (document.getElementById("emp_nome")) document.getElementById("emp_nome").value = dados.nome || "";
    if (document.getElementById("emp_cnpj")) document.getElementById("emp_cnpj").value = dados.cnpj || "";
    if (document.getElementById("emp_responsavel")) document.getElementById("emp_responsavel").value = dados.responsavel || "";
    if (document.getElementById("emp_email")) document.getElementById("emp_email").value = dados.email || "";
}

function login() {
    let email = document.getElementById("email")?.value;
    let senha = document.getElementById("senha")?.value;
    let erroEl = document.getElementById("erro");

    if (!email || !senha) {
        if (erroEl) erroEl.innerText = "Por favor, preencha o e-mail e a senha.";
        return;
    }

    let formData = new FormData();
    formData.append("email", email);
    formData.append("senha", senha);

    fetch("/login", { method: "POST", body: formData })
    .then(response => {
        if (response.ok) {
            window.location.href = "/empresa";
        } else {
            if (erroEl) erroEl.innerText = "Erro ao efetuar login.";
        }
    })
    .catch(() => {
        if (erroEl) erroEl.innerText = "Não foi possível conectar ao sistema.";
    });
}