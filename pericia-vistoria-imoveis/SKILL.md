---
name: pericia-vistoria-imoveis
description: Elabora laudos periciais de vistoria de imóveis e obras (NBR 13752:2024, NBR 16747, IBAPE 2025) — analisa fotos e relatos, classifica anomalias com prioridade e grau de risco, indica correções e normas, orça por custos referenciais (CUB, SINAPI, SICRO, SETOP, SMOP, DER), calcula % de obra executada e custos a refazer/executar, e gera laudo em Word e planilha em Excel. Atende qualquer sistema construtivo (convencional, alvenaria estrutural, pré-moldado, metálico, steel frame, wood frame, modular, containers) e obras públicas em retomada/repactuação. Use sempre que o usuário falar em laudo, perícia, vistoria de obra, obra inacabada ou paralisada, avanço físico, patologias, vícios, fissuras, infiltração, inspeção predial, recebimento de obra, entrega de chaves, quesitos ou orçamento de reparos, mesmo sem dizer "laudo".
---

# Perícia e vistoria de imóveis

Esta skill conduz o engenheiro do início ao fim de um laudo de vistoria: coleta dos dados, análise técnica das constatações, orçamento dos serviços e emissão de dois documentos — o **laudo em Word (.docx)** e a **planilha de quantitativos e custos em Excel (.xlsx)**.

O laudo é um documento técnico assinado por profissional habilitado e pode ir parar num processo judicial. Por isso a regra que orienta tudo abaixo é: **cada afirmação do laudo precisa estar apoiada no que foi visto, informado ou medido, e cada número precisa ter fonte.** Quando faltar dado, pergunte ou deixe explícito como pendência — nunca preencha com valor plausível inventado.

## Os quatro tipos de vistoria

| Tipo (`tipo` no JSON) | Quando usar | Espécie de vistoria (NBR 13752:2024) |
|---|---|---|
| `obra_inacabada` | Obra paralisada, rescisão contratual, troca de construtora, financiamento interrompido | Constatação + análise comparativa de conformidade |
| `patologias` | Manifestações patológicas, vícios construtivos, infiltrações, fissuras; apurar causa e responsabilidade | Causalidade (inclui constatação e conformidade) |
| `inspecao_predial` | Edificação em uso; avaliar conservação, manutenção e uso | NBR 16747:2020 + Norma de Inspeção Predial IBAPE (2025) |
| `recebimento_obra` | Entrega de chaves, recebimento provisório/definitivo, vistoria de entrega | Constatação + análise comparativa de conformidade |

Se o pedido misturar finalidades (ex.: recebimento com vícios graves cuja causa precisa ser apurada), escolha o tipo principal e trate o restante como capítulo adicional, dizendo isso ao usuário. A inspeção predial não serve para recebimento de obra nem para apurar nexo causal — se pedirem isso numa inspeção predial, explique e sugira o tipo adequado.

Antes de começar a análise, leia `references/tipos-de-vistoria.md` na seção do tipo escolhido (escopo, método e conteúdo mínimo) e `references/estrutura-e-qualidade.md` (ordem das seções e critérios de qualidade extraídos de laudos reais de referência, com os erros que eles cometeram e que este laudo não pode repetir).

## O sistema construtivo muda a vistoria

Identifique o sistema construtivo logo no início (`imovel.sistema_construtivo_tipo`) e leia a seção correspondente de `references/sistemas-construtivos.md`. Em sistemas industrializados (steel frame, wood frame, modular, pré-moldado, painéis), a referência de conformidade inclui a norma do sistema, a DATec/Diretriz SINAT quando houver, o projeto do sistema e o manual do fabricante; os pontos críticos são outros (ancoragens, contraventamentos, membranas, juntas entre módulos, ligações), boa parte fica oculta após o fechamento, e as tabelas de pesos por etapa da obra convencional não servem sem adaptação. Obras mistas usam as seções de cada parte.

## Fluxo de trabalho

### 1. Identificar o tipo e coletar os dados

Leia `references/roteiro-coleta.md` e peça ao usuário, de forma organizada e em poucas mensagens (agrupe as perguntas, não faça uma por vez):

1. **Dados da obra/imóvel** — localização, matrícula, proprietário e solicitante, áreas, tipologia, padrão, sistema construtivo, pavimentos, idade, projetos, memoriais, contrato, cronograma, medições, alvarás, manual do proprietário, ART/RRT de projeto e execução.
2. **Dados da vistoria** — data(s), condições (tempo, iluminação, acesso), acompanhantes, sistemas que não puderam ser vistoriados.
3. **Fotos da obra** — peça os arquivos originais (o EXIF traz data e coordenadas, que o gerador põe na legenda como prova), cada uma com o local (cômodo/pavimento/fachada) e, quando possível, uma referência de escala; mais uma imagem de satélite com o lote e, se houver, fotos de fiscalizações anteriores com a fonte.
4. **Relato textual** de tudo que foi constatado, item por item.
5. **Quantitativos** — para cada serviço: quantidade prevista em projeto/contrato, quantidade executada e aceitável, quantidade executada com vício (a refazer) e, por diferença, a não executada. Exemplos: nº de janelas e dimensões, m² de piso, m² de reboco, m de rodapé, pontos elétricos.
6. **Base de custos** — pergunte sempre qual tabela usar (SINAPI, SICRO, SETOP, SMOP, DER-PR, ORSE etc.), UF, mês de referência, se é desonerada ou não e o BDI. Peça que o usuário **anexe a planilha da tabela do mês** (ver passo 3). Para obra inacabada, pergunte também o projeto-padrão do CUB e a área equivalente (NBR 12721).
7. **Processo judicial** (se houver) — número, vara, comarca, partes e quesitos.
8. **Obra pública/financiada** (se for o caso) — órgão, programa e norma a atender, instrumento, ID no sistema (SIMEC, CNES, Transferegov), valor pactuado, prazo, datas, % físico informado e restrições já registradas.

Os dados do perito vêm de `assets/perito_padrao.json` (CWB Civil, Eng. Marcelo de Lima Ferreira). Use-os sem perguntar, a menos que o usuário indique outro responsável técnico. Confirme apenas o número da ART do laudo, que muda a cada trabalho.

Se o usuário já trouxer tudo na primeira mensagem, não repita perguntas: confira o que falta e peça só isso.

### 2. Analisar fotos e relatos

Comece pelo **quadro de situação por sistema** (`situacao_sistemas`): para cada sistema da obra — fundações, estrutura, vedações, cobertura, esquadrias, revestimentos, pisos, pintura, instalações hidráulicas, sanitárias, pluviais, elétricas, lógica, SPDA, incêndio, serviços externos — diga se está concluído, concluído com vícios, parcial, não executado ou danificado. Esse quadro organiza o laudo inteiro: a descrição detalhada é agrupada por esses mesmos sistemas.

Depois, para cada constatação, examine a foto junto com o relato e registre uma anomalia com:

- **Localização** precisa e **sistema** (estrutura, vedação, revestimento, cobertura, impermeabilização, esquadrias, instalações etc.).
- **Descrição técnica** do que se vê: tipo, dimensão aproximada, extensão, padrão (ex.: "fissura inclinada a ~45° partindo do canto superior da janela, abertura estimada < 1 mm").
- **Mecanismo provável** e **origem** (endógena, exógena, funcional, uso/operação/manutenção) e **natureza** (vício aparente, vício oculto, defeito, avaria, mutilação etc.). Use as definições de `references/classificacao-anomalias.md`.
- **Prioridade** (1, 2 ou 3) com a justificativa — obrigatória na inspeção predial, útil nos demais tipos. O laudo mostra também o **grau de risco** correspondente (crítico, regular, mínimo), terminologia que órgãos públicos ainda pedem.
- **Especificado × executado** quando a anomalia é divergência de projeto: valores com unidade e a prancha/item de referência (ex.: "V13 especificada 15 × 30 cm (EST-03), executada 8,5 × 24 cm, medida com trena").
- **Requisito normativo** não atendido: norma e o que ela exige, consultando `references/normas-por-sistema.md`.
- **Correção recomendada**: sequência executiva do reparo (remoção, tratamento, reexecução, proteção), e os **serviços orçamentários** que a representam, com quantidade.
- **Ensaios ou investigações complementares** quando a foto e o relato não bastam para concluir (ex.: pacometria, esclerometria, extração de testemunho, prova de carga, teste de estanqueidade, termografia, sondagem).

Seja honesto com os limites da evidência. Uma foto mostra o sintoma, nem sempre a causa. Quando a causa for inferida, escreva "indica", "é compatível com", "provável" — e diga o que confirmaria. Não afirme abertura de fissura, prumo, espessura ou resistência que não tenham sido medidos; se o usuário não mediu, a anomalia é descrita como estimada visualmente.

**Sobre as normas** — cite a norma, o ano da versão e o requisito em si. Só cite número de item/seção se ele constar da referência que você consultou; número de item inventado desmoraliza o laudo. As versões em `references/normas-por-sistema.md` foram conferidas em outubro de 2026; se houver acesso à web e passar tempo desde então, confira a versão vigente no catálogo da ABNT antes de citar, e registre a data da conferência em `premissas`.

Por fim, defina a **classificação global** (`grau_risco_global`), coerente com a pior anomalia: com qualquer item de prioridade 1, o global não pode ser mínimo nem satisfatório. Elemento estrutural ausente ou em desacordo com o projeto pede verificação estrutural por projetista habilitado e prioridade 1 até essa verificação. Na análise, encadeie causas e efeitos (ex.: cobertura inacabada → infiltrações → danos em forros, portas e instalações), porque isso define a ordem dos reparos.

Mostre ao usuário a lista de anomalias analisadas (tabela curta) e peça confirmação ou correções antes de orçar. É mais barato corrigir a interpretação aqui do que depois do laudo pronto.

### 3. Levantar custos unitários

Leia `references/custos-referenciais.md`. Em resumo:

- Com a planilha da tabela anexada, use o script de busca para achar código, descrição, unidade e preço:
  ```bash
  python scripts/buscar_precos.py <tabela.xlsx> "palavras chave" [--uf PR] [--limite 15]
  python scripts/buscar_precos.py <tabela.xlsx> --codigo 87878 [--uf PR]
  ```
  Escolha a composição cuja descrição corresponde ao serviço real (material, espessura, traço, dimensão) e anote código e fonte. Se houver dúvida entre composições, mostre as opções ao usuário.
- O CUB do mês vem do site do Sinduscon do estado (CUB-PR: sindusconpr.com.br). Busque na web e registre mês e projeto-padrão.
- Sem tabela anexada e sem preço informado, **deixe `preco_unitario` vazio (`null`)**. A planilha sai com a célula destacada em amarelo para preenchimento, e o laudo indica que o valor depende da tabela. Não use preço de memória.
- Serviço sem composição na tabela oficial: use cotação ou composição própria, marcando a fonte como "Cotação" ou "Composição própria" e explicando em `premissas`.

Serviços a refazer custam a **remoção/demolição** do que foi mal executado (com transporte e descarte quando relevante) **mais a reexecução**. Por isso, cada serviço com `qtd_refazer` pode ter um bloco `demolicao` com sua própria composição.

### 4. Calcular

Dois métodos, usados conforme os dados disponíveis (podem coexistir no mesmo laudo):

- **Orçamento discriminado** (preferencial, quando há quantitativos): para cada serviço, valor previsto = qtd prevista × PU; valor executado aceito = qtd aceita × PU; refazer = qtd refazer × (PU + PU demolição); a executar = qtd não executada × PU. **% executado aceito = Σ valor aceito ÷ Σ valor previsto.**
- **Pesos por etapa** (quando não há orçamento detalhado): valor global = CUB × área equivalente (ou orçamento contratual); % executado = Σ (peso da etapa × % executado da etapa). Use os pesos do cronograma físico-financeiro contratual quando existir; na falta dele, as tabelas indicativas de `references/custos-referenciais.md` (residencial normal, galpão, residencial alto padrão — campo `etapas.modelo`) precisam ser declaradas como tal no laudo.

Nunca deixe o % executado sem apuração por falta de medições — estime pelo método de etapas e fundamente. Se o órgão ou o executor informaram um percentual (SIMEC, boletins), o laudo confronta os dois e explica a diferença.

Para obra finalizada (`recebimento_obra`) o raciocínio é o mesmo: o previsto é o contratado, o aceito é o que está conforme, o refazer são os vícios e o "não executado" são as pendências.

Os scripts fazem essas contas — você não precisa somar à mão. Mas confira se o resultado faz sentido (ex.: % executado acima de 100% indica quantidade lançada errada).

### 5. Gerar os documentos

1. Monte o arquivo `laudo.json` seguindo `references/formato-dados.md` (leia esse arquivo inteiro antes de montar o JSON — os nomes de campo são exatos). Os textos do laudo (objetivo, metodologia, descrição, análise, conclusão) você redige nos campos de texto; o script cuida de formatação, numeração, tabelas, fotos e totais.
2. Gere os dois arquivos:
   ```bash
   python scripts/gerar_documentos.py laudo.json --saida <pasta>
   ```
   Saem `Laudo_<numero>.docx` e `Planilha_<numero>.xlsx`. O script também imprime o resumo dos cálculos e avisa sobre preços faltando, fotos não encontradas, anomalias sem foto, não conformidades sem especificado × executado, inconsistências de quantidade e **classificação global incoerente** — trate cada aviso antes de entregar (corrija ou justifique no texto).
3. Verifique: converta o .docx para PDF (`soffice --headless --convert-to pdf`) e olhe algumas páginas como imagem (capa, uma anomalia com foto, a tabela de custos). Na planilha, se existir o recálculo da skill xlsx, rode-o para garantir zero erros de fórmula.
4. Entregue os dois arquivos ao usuário com um resumo curto: tipo de laudo, nº de anomalias por prioridade, % executado (quando houver) e totais a refazer/a executar. Liste o que ficou pendente (preços em aberto, ART, assinatura, ensaios recomendados).

## Cuidados que valem para todos os laudos

- **Linguagem**: técnica, impessoal, objetiva. Descreva antes de concluir. Evite adjetivos ("péssimo", "absurdo") e juízo sobre pessoas; aponte fatos, requisitos e consequências.
- **Responsabilidade**: em perícia judicial, a atribuição de responsabilidade cabe ao juiz; o perito aponta origem técnica, nexo causal e quem tinha o dever técnico, sem decidir o mérito jurídico. Prazos legais (CDC, Código Civil) podem ser mencionados como referência, não como conclusão jurídica.
- **Escopo**: diga o que não foi vistoriado e por quê. Vistoria visual não substitui ensaio; recomende-o quando for o caso.
- **Assinatura**: o laudo sai com campo de assinatura e de ART. O documento é uma minuta técnica até ser revisado e assinado pelo responsável — mencione isso na entrega.
- **Privacidade**: dados pessoais de partes (CPF, endereço) vão só onde o laudo exige.

## Arquivos de apoio

| Arquivo | Quando ler |
|---|---|
| `references/tipos-de-vistoria.md` | Sempre, na seção do tipo escolhido |
| `references/estrutura-e-qualidade.md` | Sempre: ordem das seções, critérios de qualidade e obras públicas |
| `references/sistemas-construtivos.md` | Sempre, na seção do sistema construtivo da obra |
| `references/roteiro-coleta.md` | Na coleta de dados (passo 1) |
| `references/classificacao-anomalias.md` | Ao classificar cada anomalia (passo 2) |
| `references/normas-por-sistema.md` | Ao indicar requisitos normativos (passo 2) |
| `references/custos-referenciais.md` | Antes de orçar e calcular (passos 3 e 4) |
| `references/formato-dados.md` | Antes de montar o `laudo.json` (passo 5) |
| `scripts/buscar_precos.py` | Busca de composições em planilha de tabela referencial |
| `scripts/gerar_documentos.py` | Gera o .docx e o .xlsx a partir do JSON |
| `assets/perito_padrao.json` | Dados padrão do perito e da empresa |
| `assets/exemplo_laudo.json` | Exemplo completo e válido de entrada |
