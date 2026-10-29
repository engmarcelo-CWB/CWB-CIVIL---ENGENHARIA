"""Textos padrão por tipo de vistoria. Usados quando o JSON não traz o campo correspondente.

Os textos são genéricos de propósito: o perito deve adaptá-los ao caso sempre que houver
informação específica (o JSON tem precedência sobre tudo que está aqui).
"""

TIPOS = {
    "obra_inacabada": {
        "titulo": "LAUDO TÉCNICO DE VISTORIA DE OBRA NÃO CONCLUÍDA",
        "especie": "Vistoria de constatação e de análise comparativa de conformidade (ABNT NBR 13752:2024)",
        "objetivo": (
            "Constatar o estágio físico da obra, verificar a conformidade dos serviços executados com os "
            "projetos, memoriais, contrato e normas técnicas aplicáveis, quantificar os serviços executados "
            "e aceitos, os executados com vícios (a refazer) e os não executados, e estimar o percentual "
            "de obra executada e o custo para sua conclusão."
        ),
        "metodologia": [
            "Anamnese e análise da documentação disponibilizada (contrato, projetos, memoriais, cronograma, medições).",
            "Vistoria técnica presencial, sensorial, com registro fotográfico sistemático e anotações in loco.",
            "Levantamento quantitativo dos serviços por unidade padronizada, separando executado aceito, executado com vício e não executado.",
            "Classificação das não conformidades quanto à origem e à natureza (ABNT NBR 13752:2024).",
            "Confronto entre o avanço físico verificado e o previsto/medido.",
            "Orçamentação dos serviços com base em tabela de custos referencial, com cálculo do percentual executado aceito e dos custos de refazimento e de conclusão.",
        ],
        "pressupostos": [
            "A vistoria foi visual e sensorial, sem ensaios destrutivos ou tecnológicos, salvo quando indicado.",
            "Serviços executados em desacordo com projeto, memorial ou norma não foram considerados executados para fins do percentual aceito; seu custo de refazimento foi orçado separadamente.",
            "Elementos ocultos (embutidos, enterrados ou cobertos) foram avaliados pelos indícios visíveis; sua conformidade plena depende de prospecção.",
            "As quantidades e informações documentais fornecidas pelo solicitante foram consideradas verídicas, sem prejuízo das verificações por amostragem feitas na vistoria.",
            "Os custos referem-se à data-base da tabela referencial indicada e devem ser atualizados se o laudo for usado em data posterior.",
        ],
        "normas": [
            ("ABNT NBR 13752:2024", "Perícias de engenharia na construção civil"),
            ("ABNT NBR 12721", "Avaliação de custos unitários de construção para incorporação imobiliária"),
        ],
    },
    "patologias": {
        "titulo": "LAUDO TÉCNICO PERICIAL DE MANIFESTAÇÕES PATOLÓGICAS",
        "especie": "Vistoria de causalidade, com constatação e análise comparativa de conformidade (ABNT NBR 13752:2024)",
        "objetivo": (
            "Identificar e descrever as manifestações patológicas existentes no imóvel, investigar seus "
            "mecanismos e origens, estabelecer o nexo causal, classificar as anomalias quanto à origem e à "
            "natureza, indicar as medidas corretivas e estimar o custo dos reparos."
        ),
        "metodologia": [
            "Anamnese: histórico da edificação, surgimento e evolução das manifestações, reformas e manutenções realizadas.",
            "Análise da documentação técnica disponibilizada.",
            "Vistoria técnica presencial com registro fotográfico e descrição de cada manifestação (tipo, configuração, extensão, atividade).",
            "Análise comparativa de conformidade com projetos, memoriais, normas de execução e de desempenho.",
            "Formulação e verificação de hipóteses de causa, com descarte das incompatíveis com as evidências (análise de causalidade).",
            "Classificação quanto à origem e à natureza; indicação da terapia e orçamentação dos reparos.",
        ],
        "pressupostos": [
            "O diagnóstico baseia-se nas evidências disponíveis na data da vistoria; onde a evidência visual não permite conclusão, o laudo indica a investigação complementar necessária.",
            "A expressão \"causa provável\" indica hipótese compatível com as evidências, não confirmada por ensaio; \"causa determinada\" indica confirmação por evidência direta.",
            "A atribuição de responsabilidade jurídica não é objeto deste laudo; indica-se a origem técnica das anomalias.",
            "Os custos referem-se à data-base da tabela referencial indicada.",
        ],
        "normas": [
            ("ABNT NBR 13752:2024", "Perícias de engenharia na construção civil"),
            ("ABNT NBR 15575 (partes 1 a 6)", "Edificações habitacionais — Desempenho"),
            ("ABNT NBR 17170:2022", "Edificações — Garantias — Prazos recomendados e diretrizes"),
        ],
    },
    "inspecao_predial": {
        "titulo": "LAUDO DE INSPEÇÃO PREDIAL",
        "especie": "Inspeção predial (ABNT NBR 16747:2020 e Norma de Inspeção Predial IBAPE Nacional 2025)",
        "objetivo": (
            "Avaliar as condições técnicas, de uso, de operação, de manutenção e de funcionalidade da "
            "edificação e de seus sistemas, identificar anomalias e falhas, classificá-las quanto à origem, "
            "organizar as recomendações técnicas em patamares de prioridade e avaliar a manutenção e o uso."
        ),
        "metodologia": [
            "Anamnese, levantamento de dados e documentos.",
            "Análise dos documentos disponibilizados.",
            "Vistoria sistêmica da edificação, predominantemente sensorial, com testes simples de acionamento quando cabível.",
            "Classificação da origem das anomalias e falhas.",
            "Recomendações técnicas.",
            "Organização das recomendações em patamares de prioridade.",
            "Avaliação da manutenção.",
            "Avaliação do uso.",
            "Redação e emissão do laudo.",
        ],
        "pressupostos": [
            "A inspeção predial é predominantemente sensorial e não contempla ensaios tecnológicos ou prospecções; quando necessários, são indicados como recomendação.",
            "A inspeção predial não se destina ao recebimento de obra, à apuração de nexo causal ou à certificação da edificação.",
            "Foram inspecionados os sistemas e áreas acessíveis na data da vistoria; os não inspecionados estão relacionados com o respectivo motivo.",
        ],
        "normas": [
            ("ABNT NBR 16747:2020", "Inspeção predial — Diretrizes, conceitos, terminologia e procedimento"),
            ("Norma de Inspeção Predial IBAPE Nacional (2025)", "Metodologia de inspeção predial"),
            ("ABNT NBR 5674", "Manutenção de edificações — Requisitos para o sistema de gestão de manutenção"),
            ("ABNT NBR 14037", "Diretrizes para elaboração de manuais de uso, operação e manutenção das edificações"),
        ],
    },
    "recebimento_obra": {
        "titulo": "LAUDO TÉCNICO DE VISTORIA DE RECEBIMENTO DE OBRA",
        "especie": "Vistoria de constatação e de análise comparativa de conformidade (ABNT NBR 13752:2024)",
        "objetivo": (
            "Verificar, por ocasião da entrega, a conformidade da obra com o contratado (projetos, memorial "
            "descritivo, material publicitário e normas técnicas), registrar pendências, vícios aparentes e "
            "indícios de vícios ocultos, quantificar e orçar as correções e subsidiar a decisão de recebimento."
        ),
        "metodologia": [
            "Análise da documentação de entrega (contrato, memorial descritivo, projetos, manual do proprietário, termo de garantia).",
            "Vistoria sistemática por ambiente e por sistema, com registro fotográfico.",
            "Testes funcionais simples (esquadrias, instalações elétricas e hidráulicas, escoamento, estanqueidade quando cabível) e verificações de prumo, nível e planeza.",
            "Análise comparativa de conformidade com memorial, projetos e normas, inclusive requisitos verificáveis da ABNT NBR 15575.",
            "Classificação, quantificação e orçamentação das pendências e vícios.",
        ],
        "pressupostos": [
            "A vistoria de recebimento é visual e funcional; vícios ocultos podem manifestar-se posteriormente e estão cobertos pelos prazos de garantia aplicáveis.",
            "A decisão de receber, receber com ressalvas ou não receber a obra cabe ao contratante; este laudo fornece subsídio técnico.",
            "Os custos referem-se à data-base da tabela referencial indicada.",
        ],
        "normas": [
            ("ABNT NBR 13752:2024", "Perícias de engenharia na construção civil"),
            ("ABNT NBR 15575 (partes 1 a 6)", "Edificações habitacionais — Desempenho"),
            ("ABNT NBR 17170:2022", "Edificações — Garantias — Prazos recomendados e diretrizes"),
            ("ABNT NBR 14037", "Diretrizes para elaboração de manuais de uso, operação e manutenção das edificações"),
        ],
    },
}

ORIGEM = {
    "endogena_projeto": "Endógena — projeto",
    "endogena_material": "Endógena — material",
    "endogena_execucao": "Endógena — execução",
    "exogena": "Exógena",
    "funcional": "Funcional",
    "uso_manutencao": "Uso, operação ou manutenção",
    "indeterminada": "Indeterminada (requer investigação)",
}

NATUREZA = {
    "vicio_aparente": "Vício aparente",
    "vicio_oculto": "Vício oculto",
    "defeito": "Defeito",
    "avaria": "Avaria",
    "mutilacao": "Mutilação",
    "deterioracao": "Deterioração",
    "envelhecimento_natural": "Envelhecimento natural",
    "vicio_informacao": "Vício de informação técnica",
    "nao_executado": "Serviço não executado",
    "nao_conformidade": "Não conformidade",
}

PRIORIDADE = {
    1: "Prioridade 1 — ação urgente (saúde, segurança, funcionalidade ou perda de vida útil)",
    2: "Prioridade 2 — funcionalidade parcialmente comprometida",
    3: "Prioridade 3 — ação planejada / manutenção",
}

SITUACAO_DOC = {
    "analisado": "Analisado",
    "nao_disponibilizado": "Solicitado e não disponibilizado",
    "nao_existente": "Inexistente",
    "parcial": "Disponibilizado parcialmente",
}

SITUACAO_CHECK = {
    "conforme": "Conforme",
    "nao_conforme": "Não conforme",
    "nao_verificado": "Não verificado",
    "nao_se_aplica": "Não se aplica",
}

GRAU_RISCO = {
    "critico": "Crítico",
    "regular": "Regular",
    "minimo": "Mínimo",
    "satisfatorio": "Satisfatório",
}
PRIORIDADE_PARA_GRAU = {1: "critico", 2: "regular", 3: "minimo"}
ORDEM_GRAU = {"satisfatorio": 0, "minimo": 1, "regular": 2, "critico": 3}

SITUACAO_SISTEMA = {
    "concluido": "Concluído",
    "concluido_com_vicios": "Concluído com vícios",
    "parcial": "Executado parcialmente",
    "nao_executado": "Não executado",
    "danificado": "Executado e danificado",
    "nao_se_aplica": "Não se aplica",
}

# Sistemas construtivos: rótulo e normas que entram automaticamente nas referências do laudo.
# Anos só onde conferidos; os demais sem ano (confirmar no Catálogo ABNT antes de acrescentar).
SISTEMAS = {
    "convencional": ("Estrutura de concreto armado moldada in loco com alvenaria de vedação",
                     [("ABNT NBR 6118:2023", "Projeto de estruturas de concreto"),
                      ("ABNT NBR 14931", "Execução de estruturas de concreto"),
                      ("ABNT NBR 8545", "Execução de alvenaria sem função estrutural de tijolos e blocos cerâmicos")]),
    "alvenaria_estrutural": ("Alvenaria estrutural",
                             [("ABNT NBR 16868:2020 (partes 1 a 3)", "Alvenaria estrutural")]),
    "paredes_concreto": ("Paredes de concreto moldadas no local",
                         [("ABNT NBR 16055", "Parede de concreto moldada no local para a construção de edificações")]),
    "pre_moldado": ("Estrutura pré-moldada / pré-fabricada de concreto",
                    [("ABNT NBR 9062", "Projeto e execução de estruturas de concreto pré-moldado"),
                     ("ABNT NBR 6118:2023", "Projeto de estruturas de concreto")]),
    "estrutura_metalica": ("Estrutura metálica",
                           [("ABNT NBR 8800", "Projeto de estruturas de aço e de estruturas mistas de aço e concreto de edifícios"),
                            ("ABNT NBR 14762", "Dimensionamento de estruturas de aço constituídas por perfis formados a frio"),
                            ("ABNT NBR 6123", "Forças devidas ao vento em edificações")]),
    "steel_frame": ("Light steel framing (LSF)",
                    [("ABNT NBR 16970 (partes 1 a 3)", "Light steel framing — sistemas construtivos estruturados em perfis leves de aço formados a frio, com fechamentos em chapas delgadas"),
                     ("ABNT NBR 14762", "Dimensionamento de estruturas de aço constituídas por perfis formados a frio"),
                     ("DATec / Diretriz SINAT aplicável", "Avaliação técnica do sistema (PBQP-H), quando houver")]),
    "wood_frame": ("Light wood framing (LWF)",
                   [("ABNT NBR 16936", "Edificações em light wood frame"),
                    ("ABNT NBR 7190:2022", "Projeto de estruturas de madeira"),
                    ("DATec / Diretriz SINAT aplicável", "Avaliação técnica do sistema (PBQP-H), quando houver")]),
    "modular": ("Construção modular volumétrica (off-site)",
                [("Projeto e manual técnico do fabricante dos módulos", "Referência de conformidade do sistema"),
                 ("DATec / Diretriz SINAT aplicável", "Avaliação técnica do sistema (PBQP-H), quando houver")]),
    "container": ("Módulos em containers adaptados",
                  [("ABNT NBR 8800", "Projeto de estruturas de aço e de estruturas mistas de aço e concreto de edifícios"),
                   ("ABNT NBR 15220", "Desempenho térmico de edificações")]),
    "paineis": ("Sistema em painéis (monolíticos, sanduíche ou similares)",
                [("DATec / Diretriz SINAT aplicável", "Avaliação técnica do sistema (PBQP-H), quando houver")]),
    "misto": ("Sistema misto", []),
    "outro": ("Outro sistema", []),
}

# Pesos indicativos por etapa (fração). Ver references/custos-referenciais.md para a origem.
PESOS_MODELOS = {
    "residencial_normal": {
        "_origem": "pesos indicativos do perito para residência unifamiliar padrão normal em concreto armado e alvenaria (sem cronograma contratual)",
        "Serviços preliminares": 0.02, "Fundações": 0.06, "Estrutura": 0.15, "Alvenaria e vedações": 0.08,
        "Cobertura": 0.07, "Impermeabilização": 0.02, "Instalações hidrossanitárias": 0.07,
        "Instalações elétricas": 0.06, "Revestimentos de parede": 0.12, "Forros": 0.02, "Pisos": 0.10,
        "Esquadrias": 0.09, "Vidros": 0.02, "Louças e metais": 0.03, "Pintura": 0.07,
        "Serviços complementares": 0.02,
    },
    "galpao": {
        "_origem": "pesos indicativos para galpão industrial (tabela de etapas usada em laudo judicial de avaliação pelo método evolutivo)",
        "Serviços preliminares": 0.018, "Movimento de terra": 0.002, "Fundações especiais": 0.04,
        "Infraestrutura": 0.03, "Superestrutura": 0.06, "Vedação": 0.031, "Esquadrias": 0.095,
        "Cobertura": 0.20, "Instalações hidráulicas": 0.053, "Instalações elétricas": 0.06,
        "Impermeabilização e isolação térmica": 0.011, "Revestimentos": 0.093, "Vidros": 0.004,
        "Pintura": 0.07, "Serviços complementares": 0.233,
    },
    "residencial_alto": {
        "_origem": "pesos indicativos para residência padrão alto, baseados em tabela de incidência por etapa (PINI) usada em laudo judicial",
        "Projetos": 0.007, "Serviços preliminares": 0.03, "Movimento de terra": 0.01, "Infraestrutura": 0.075,
        "Superestrutura": 0.188, "Vedação": 0.06, "Esquadrias": 0.04, "Cobertura": 0.006,
        "Instalações hidráulicas": 0.12, "Instalações elétricas": 0.043,
        "Impermeabilização e isolação térmica": 0.09, "Revestimentos": 0.24, "Vidros": 0.034,
        "Pintura": 0.042, "Serviços complementares": 0.015,
    },
}
