# Tipos de vistoria — escopo, método e conteúdo do laudo

Sumário: [Base comum](#base-comum-nbr-137522024) · [Obra inacabada](#1-obra-inacabada-obra-não-concluída) · [Patologias construtivas](#2-patologias-construtivas-vícios-construtivos) · [Inspeção predial](#3-inspeção-predial) · [Recebimento de obra](#4-recebimento-de-obra--entrega-de-chaves)

## Base comum (NBR 13752:2024)

A ABNT NBR 13752:2024 (Perícias de engenharia na construção civil), publicada em outubro de 2024, substituiu a versão de 1996. Ela trata a **vistoria** como espécie de perícia com três finalidades, que se acumulam:

1. **Constatação** — descreve o estado do bem: tipologia, padrão, idade, estado de conservação, anomalias, manifestações patológicas, falhas, avanço físico. Não determina causas, responsabilidades nem soluções.
2. **Análise comparativa de conformidade** — confronta o que existe com projetos, memoriais, normas técnicas, legislação, manuais, dados de fabricantes, contratos e material publicitário.
3. **Causalidade** — investiga a existência ou não de nexo causal, com método investigativo; pode revelar responsabilidades técnicas e consequências. Sempre usa as duas anteriores.

Entre as aplicações expressamente previstas estão as **obras não concluídas** e a **entrega e recebimento de obra**.

**Conteúdo mínimo comum a todo laudo de vistoria** (constatação):
- identificação do solicitante e do objeto;
- objetivo e finalidade;
- pressupostos, ressalvas e condicionantes;
- data(s) da vistoria;
- descrição técnica detalhada;
- relatório fotográfico;
- local e data do laudo;
- assinatura e identificação do perito (registro no conselho);
- relação de anexos.

Na vistoria **de conformidade**, acrescente: documentos considerados, procedimentos adotados e descrição das não conformidades com o referencial confrontado. Fora a simples constatação, o laudo deve **citar as referências técnicas** que fundamentam a análise.

Toda ocorrência registrada deve ter **características físicas, localização precisa e extensão**.

Inclua sempre a ART do laudo (campo `art` em `perito`).

---

## 1. Obra inacabada (obra não concluída)

**Definição prática**: obra interrompida antes de cumprir integralmente o objeto contratado, sem recebimento formal (parcial ou definitivo).

**Objetivo típico**: determinar o estágio físico real, separar o que foi executado corretamente (aceito) do que foi executado com vício (refazer) e do que não foi executado; quantificar e valorar cada parcela; subsidiar rescisão, acerto de contas, retomada por outro executor, liberação de financiamento ou ação judicial.

**Método**:
1. Anamnese: contrato, aditivos, projetos, memoriais, cronograma físico-financeiro, boletins de medição, pagamentos, diário de obra, notificações, motivos da paralisação.
2. Vistoria presencial com registro fotográfico sistemático (ambiente por ambiente, fachadas, cobertura) e croquis.
3. Levantamento quantitativo por serviço, em unidades padronizadas (m², m³, m, un, kg, pt).
4. Classificação das não conformidades quanto à origem e à natureza.
5. Análise cruzada: avanço físico verificado × declarado/medido × pago; materiais entregues e não incorporados (estocados na obra) — registre separadamente, com estado de conservação.
6. Custos: valor do executado aceito, custo de refazer (demolição + reexecução + descarte), custo para concluir.
7. Riscos da paralisação: exposição de armaduras, infiltração em estrutura sem cobertura, furto, deterioração de materiais — e serviços de proteção imediata.

**Seções específicas do laudo**: estágio físico por etapa; quadro de quantidades (previsto / aceito / refazer / não executado); % executado aceito; confronto com medições e pagamentos (se fornecidos); materiais não incorporados; custo para conclusão; recomendações de proteção.

**Obra pública para retomada/repactuação** (UBS, escolas, quadras, CRAS, convênios): acrescente os dados do programa (`programa`), o confronto do % informado no sistema do órgão com o verificado, a situação das restrições já registradas e a conclusão sobre a viabilidade de conclusão e a necessidade de planilha de repactuação — ver `estrutura-e-qualidade.md`, seção 3. Obra abandonada costuma ter um encadeamento causal claro (cobertura inacabada → infiltração → danos em forros, revestimentos, portas e instalações; abandono → vandalismo e furto de fiação, disjuntores, louças, vidros): descreva-o na análise, porque ele define a ordem da retomada (proteger e cobrir primeiro).

**Atenção**: o "% executado" do laudo é o **aceito tecnicamente**. Serviço executado com vício não conta como executado — entra como refazer. Deixe isso explícito no texto.

---

## 2. Patologias construtivas (vícios construtivos)

**Objetivo típico**: identificar e descrever as manifestações patológicas, apurar o mecanismo e a origem (nexo causal), indicar a terapia (correção) e o custo, e responder quesitos sobre responsabilidade técnica.

**Método** (vistoria de causalidade):
1. Anamnese: idade da edificação, data do surgimento e evolução de cada sintoma, reformas feitas (NBR 16280), manutenções (NBR 5674), uso, eventos externos (obra vizinha, chuva intensa, vazamento).
2. Constatação detalhada de cada manifestação: tipo, configuração, dimensão, extensão, atividade (ativa/estabilizada), umidade.
3. Conformidade: confronto com projeto, memorial, normas de execução e de desempenho (NBR 15575 para habitacionais), manual do proprietário.
4. Diagnóstico: formular hipóteses de causa, testar cada uma contra as evidências, descartar as incompatíveis. Quando a evidência visual não basta, indicar ensaio específico em vez de concluir.
5. Classificação (origem e natureza) e prazo de garantia aplicável (NBR 17170 como referência técnica).
6. Terapia: procedimento de reparo em sequência e serviços orçamentários.

**Seções específicas do laudo**: para cada manifestação — sintoma, mecanismo, hipóteses consideradas, causa provável ou determinada, origem, natureza, nexo causal, terapia, custo. Quadro-resumo de nexo causal.

**Atenção**: diferencie "causa determinada" (confirmada por evidência/ensaio) de "causa provável" (compatível com as evidências). Não conclua por responsabilidade jurídica; aponte a origem técnica (projeto, material, execução, uso, manutenção, terceiros, envelhecimento natural).

---

## 3. Inspeção predial

**Base**: ABNT NBR 16747:2020 (Inspeção predial — diretrizes, conceitos, terminologia e procedimento) e a Norma de Inspeção Predial do IBAPE Nacional (2025), que detalha a metodologia. Considera a edificação **em uso**, avaliando segurança, habitabilidade e sustentabilidade (durabilidade e manutenibilidade).

**Não é**: recebimento de obra, apuração de nexo causal (cabe à NBR 13752), certificação, nem substitui as inspeções periódicas do plano de manutenção.

**Método (sequência normativa)**:
1. Anamnese, levantamento de dados e documentos
2. Análise dos documentos
3. Vistoria sistêmica (predominantemente sensorial; testes simples de acionamento são admitidos; ensaios ficam como recomendação)
4. Classificação da origem das anomalias e falhas
5. Recomendações técnicas
6. Organização em patamares de prioridade (1, 2, 3)
7. Avaliação da manutenção
8. Avaliação do uso (regular ou irregular)
9. Redação e emissão do laudo

**Conteúdo mínimo do laudo**:
a) identificação do contratante e do responsável legal;
b) descrição técnica do empreendimento;
c) datas das vistorias e equipe;
d) metodologia;
e) documentos solicitados e disponibilizados;
f) análise da documentação;
g) sistemas inspecionados e não inspecionados (com motivo);
h) anomalias, falhas e não conformidades, com fotos;
i) classificação quanto à origem;
j) recomendações de ação;
k) organização por prioridade;
l) avaliação da manutenção e do uso;
m) conclusões, com periodicidade da próxima inspeção quando houver legislação aplicável;
n) data de emissão;
o) assinatura e registro no conselho;
p) ART/RRT.

**Documentos típicos a solicitar**: projetos legais e executivos (as built), habite-se, AVCB/CLCB (Corpo de Bombeiros), manual de uso, operação e manutenção (NBR 14037), plano e registros de manutenção (NBR 5674), laudos anteriores, contratos de manutenção (elevadores, bombas, SPDA, gás), relatórios de inspeção de SPDA, limpeza de reservatórios, potabilidade, laudos de reformas (NBR 16280). Verifique se o município tem lei de inspeção predial obrigatória e cite-a se houver.

**Avaliação da manutenção**: classifique o plano de manutenção (existe? é cumprido? há registros?) e o estado geral. **Avaliação do uso**: regular (conforme projeto) ou irregular (sobrecarga, alteração de uso, intervenções sem projeto).

---

## 4. Recebimento de obra / entrega de chaves

**Objetivo típico**: verificar, no ato da entrega, se a obra corresponde ao contratado (projeto, memorial descritivo, material publicitário, normas), registrar pendências e vícios aparentes e documentar o estado da unidade/edificação para fins de garantia.

**Método**:
1. Documentos: contrato, memorial descritivo, projetos, material de venda, manual do proprietário (NBR 14037), termo de garantia, habite-se, ligações definitivas.
2. Vistoria sistemática por ambiente e por sistema, com testes funcionais simples: abertura e vedação de esquadrias, funcionamento de tomadas/interruptores/disjuntores, escoamento de ralos e caimentos, estanqueidade de box e sacadas (teste de lâmina d'água quando cabível), pressão e vazamentos em pontos hidráulicos, prumo, nível e planeza (com régua e nível quando disponíveis), som cavo em revestimentos cerâmicos (percussão), acabamento de pintura.
3. Conformidade com memorial (marca, modelo, especificação) e com a NBR 15575 nos requisitos verificáveis em vistoria.
4. Registro: lista de pendências classificada (vício aparente × indício de vício oculto; prioridade), quantificada e orçada.

**Seções específicas do laudo**: checklist por ambiente/sistema (conforme / não conforme / não verificado), quadro de pendências com custo, recomendação de aceite (com ou sem ressalvas) ou de não aceite, prazos de garantia de referência (NBR 17170) e prazo legal para reclamação de vícios aparentes como informação.

**Atenção**: o laudo pode recomendar aceite com ressalvas, listando o que deve ser corrigido e em que prazo. A decisão de receber ou não é do contratante.
