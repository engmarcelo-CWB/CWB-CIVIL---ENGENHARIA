# Formato do `laudo.json`

Entrada única de `scripts/gerar_documentos.py`. Nomes de campo exatos; campos não usados podem ser omitidos. Um exemplo completo e válido está em `assets/exemplo_laudo.json` — copie e adapte.

**Textos longos** (descrições, análise, conclusão): parágrafos separados por linha em branco (`\n\n`); linhas iniciadas por `- ` viram marcadores; `**texto**` sai em negrito.

**Números**: use número JSON (`12.5`), não texto. Percentuais e BDI como fração (`0.25`) — valores acima de 1 são lidos como porcentagem (25 → 25%).

**Datas**: `"AAAA-MM-DD"` (saem como dd/mm/aaaa ou por extenso).

## Campos de topo

| Campo | Obrig. | Descrição |
|---|---|---|
| `tipo` | sim | `obra_inacabada`, `patologias`, `inspecao_predial` ou `recebimento_obra` |
| `numero_laudo` | sim | Ex.: `"2026-015"` (vira parte do nome dos arquivos) |
| `data_emissao` | sim | `"2026-10-29"` |
| `local_emissao` | | Ex.: `"Tijucas do Sul/PR"` |
| `titulo` | | Substitui o título padrão do tipo |
| `perito` | | Sobrescreve campos de `assets/perito_padrao.json`. Normalmente só `{"art": "..."}` |
| `solicitante` | sim | `{nome, documento, qualidade, endereco, contato}` |
| `proprietario` | | `{nome, documento, endereco}` |
| `processo` | | `{numero, juizo, comarca, partes}` |
| `objeto` | | Texto; padrão: "Imóvel situado em …" |
| `objetivo` | | Texto; padrão do tipo |
| `finalidade` | | Ex.: "Instruir ação de rescisão contratual" |
| `pressupostos` | | Lista de textos, somados aos padrões do tipo |
| `normas` | | Lista de strings ou `{norma, titulo}`, somadas às normas padrão do tipo e às citadas nas anomalias |
| `metodologia` | | Lista de etapas; substitui a padrão do tipo |
| `imovel` | sim | Ver abaixo |
| `documentos` | | Lista `{documento, situacao, observacao}`; `situacao`: `analisado`, `nao_disponibilizado`, `nao_existente`, `parcial` |
| `analise_documental` | | Texto |
| `vistoria` | | Ver abaixo |
| `constatacoes_gerais` | | Texto antes do quadro de anomalias (ex.: estágio geral da obra) |
| `checklist` | | Só recebimento: lista `{ambiente, sistema, item, situacao, anomalia}`; `situacao`: `conforme`, `nao_conforme`, `nao_verificado`, `nao_se_aplica` |
| `anomalias` | | Ver abaixo |
| `analise` | | Texto da análise técnica geral |
| `avaliacao_manutencao`, `avaliacao_uso` | inspeção predial | Textos |
| `periodicidade_proxima_inspecao` | | Texto |
| `parecer_recebimento` | recebimento | Texto: aceite / aceite com ressalvas / não aceite e por quê |
| `base_custos` | se houver custos | Ver abaixo |
| `servicos` | | Orçamento discriminado (método A) |
| `etapas` | | Pesos por etapa (método B) |
| `materiais_nao_incorporados` | | Lista `{descricao, unidade, quantidade, estado, valor_unitario, observacao}` |
| `recomendacoes_gerais` | | Lista de textos |
| `quesitos` | | Lista `{parte, numero, pergunta, resposta}` |
| `conclusao` | sim (na prática) | Texto |
| `anexos` | | Lista de textos (planilha e relatório fotográfico são incluídos automaticamente) |
| `fotos_gerais` | | Lista `{arquivo, legenda}` — vão para o anexo de relatório fotográfico |

## Campos acrescentados a partir dos laudos de referência

| Campo | Descrição |
|---|---|
| `subtitulo` | Linha abaixo do título na capa (ex.: "Retomada e conclusão das obras da UBS Tipo 1 — Comunidade X") |
| `programa` | Obra pública/financiada — ver abaixo |
| `situacao_sistemas` | Lista `{sistema, situacao, descricao}`; `situacao`: `concluido`, `concluido_com_vicios`, `parcial`, `nao_executado`, `danificado`, `nao_se_aplica`. Use os **mesmos nomes de sistema** do campo `sistema` das anomalias — a descrição detalhada é agrupada por eles |
| `agrupar_por_sistema` | `true` (padrão) agrupa a descrição detalhada por sistema |
| `grau_risco_global` | `critico`, `regular`, `minimo` ou `satisfatorio` |
| `justificativa_grau_global` | Texto curto que fundamenta a classificação global |
| `nivel_inspecao` | Texto (ex.: "vistoria sensorial, sem ensaios — equivalente ao nível 1 da norma IBAPE anterior") |
| `criterio_fissuras` | Critério de nomenclatura por abertura adotado e sua fonte |
| `fotos_exif` | `true` (padrão) põe data e coordenadas do EXIF na legenda das fotos |
| `coautores` | Lista de outros signatários `{nome, titulo, registro, registros_adicionais}` |

### `programa` (obras públicas, convênios, repactuação)

```json
{"orgao": "FNDE / Ministério da Educação", "norma_referencia": "norma do programa indicada pelo solicitante",
 "instrumento": "Termo de compromisso nº ...", "id_sistema": "ID SIMEC 30946", "objeto": "...",
 "executor": "...", "contrato": "...", "valor_pactuado": 407955.11, "prazo": "746 dias",
 "data_inicio": "2014-12-05", "data_paralisacao": "2017-03-01",
 "percentual_informado": 44.82, "fonte_percentual": "SIMEC — última vistoria da instituição",
 "situacao": "Inacabada", "historico": "texto",
 "imagem_sistema": {"arquivo": "fotos/simec.png", "legenda": "Painel do SIMEC", "fonte": "SIMEC"},
 "restricoes": [{"codigo": "258943", "descricao": "Fundações executadas em desconformidade", "situacao": "Persiste"}],
 "explicacao_diferenca": "texto explicando a diferença entre o % informado e o apurado"}
```

### Novos campos em `anomalias[]`

| Campo | Descrição |
|---|---|
| `grau_risco` | Opcional; se omitido, deriva da prioridade (1 crítico, 2 regular, 3 mínimo) |
| `especificado` / `executado` | Especificado em projeto/memorial × executado/medido, com unidades |
| `referencia_projeto` | Prancha ou item do memorial (ex.: "EST-02/11") |
| `abertura_mm` | Abertura de fissura medida |

### Novos campos em fotos (`{arquivo, legenda, ...}`)

`data` e `coordenadas` (sobrescrevem o EXIF), `fonte` (ex.: "pasta de acompanhamento da obra"), `grupo` (só em `fotos_gerais`: agrupa o relatório fotográfico, ex.: "Registros do terreno", "Cobertura").

## `imovel`

`endereco` (obrig.), `municipio_uf`, `matricula`, `inscricao`, `coordenadas`, `tipologia`, `padrao`, **`sistema_construtivo_tipo`** (`convencional`, `alvenaria_estrutural`, `paredes_concreto`, `pre_moldado`, `estrutura_metalica`, `steel_frame`, `wood_frame`, `modular`, `container`, `paineis`, `misto`, `outro` — acrescenta as normas do sistema às referências), `sistema_construtivo` (texto livre; se omitido usa o rótulo do tipo), `fabricante_sistema`, `pavimentos`, `area_terreno`, `area_construida`, `area_privativa`, `area_equivalente` (números em m²), `idade`, `executor`, `responsavel_tecnico_execucao`, `servicos_publicos`, `imagem_localizacao` (`{arquivo, legenda, fonte}` — imagem de satélite com o lote), `descricao` (texto), `caracteristicas` (lista `{item, descricao}`, ex.: `{"item": "Cobertura", "descricao": "Telha cerâmica sobre estrutura de madeira"}`).

## `vistoria`

`datas` (lista de datas), `condicoes`, `acompanhantes` (lista), `informacoes_colhidas` (texto: o que acompanhantes e responsáveis informaram — anamnese), `instrumentos` (lista), `sistemas_inspecionados` (lista de textos), `sistemas_nao_inspecionados` (lista `{sistema, motivo}`).

## `anomalias[]`

| Campo | Descrição |
|---|---|
| `id` | Único. Ex.: `"A-01"` |
| `titulo` | Curto, aparece nos quadros. Ex.: "Fissuras a 45° nos cantos das janelas" |
| `local`, `sistema` | Onde e qual sistema |
| `descricao` | Descrição técnica detalhada (o que se vê, dimensões, extensão) |
| `causa` | Mecanismo e causa (provável ou determinada) |
| `causa_resumo`, `nexo_resumo` | Opcionais, para o quadro de nexo causal (patologias) |
| `nexo_causal` | Texto (patologias) |
| `origem` | `endogena_projeto`, `endogena_material`, `endogena_execucao`, `exogena`, `funcional`, `uso_manutencao`, `indeterminada` |
| `natureza` | `vicio_aparente`, `vicio_oculto`, `defeito`, `avaria`, `mutilacao`, `deterioracao`, `envelhecimento_natural`, `vicio_informacao`, `nao_executado`, `nao_conformidade` |
| `prioridade` | `1`, `2` ou `3` (número) |
| `prazo` | Texto opcional. Ex.: "imediato", "até 90 dias" |
| `normas` | Lista de textos: norma + requisito. Ex.: `"ABNT NBR 8545 — vergas e contravergas sobre e sob vãos de janelas"` |
| `recomendacao` | Correção em sequência executiva |
| `recomendacao_resumo` | Opcional, para o quadro de recomendações |
| `ensaios` | Lista de investigações complementares |
| `servicos` | Lista de `item` dos serviços que orçam a correção. Ex.: `["3.2", "3.3"]` |
| `fotos` | Lista `{arquivo, legenda}` |

## `base_custos`

```json
{"fonte": "SINAPI", "uf": "PR", "mes_referencia": "09/2026", "regime": "nao_desonerado",
 "bdi": 0.25, "data_consulta": "2026-10-29",
 "observacoes": ["Item 4.3 cotado em 3 fornecedores locais em 10/2026."]}
```
`regime`: `desonerado` ou `nao_desonerado`.

## `servicos[]` (método A)

```json
{"item": "4.1", "etapa": "Esquadrias", "fonte": "SINAPI", "codigo": "00000",
 "descricao": "Janela de alumínio de correr, 2 folhas, 1,20 x 1,20 m, com vidro",
 "unidade": "un", "qtd_prevista": 8, "qtd_aceita": 5, "qtd_refazer": 1,
 "preco_unitario": 1234.56,
 "demolicao": {"fonte": "SINAPI", "codigo": "00000", "descricao": "Remoção de janela", "unidade": "un", "preco_unitario": 45.00},
 "observacao": "Janela do dormitório 2 instalada fora de prumo"}
```

- `qtd_prevista`: projeto/contrato. Em `recebimento_obra`, o contratado.
- `qtd_aceita`: executada e conforme.
- `qtd_refazer`: executada com vício.
- A não executada é calculada. Não informe.
- `preco_unitario`: **sem BDI**, da tabela. `null` se ainda não houver — fica pendente.
- `demolicao`: opcional; PU sem BDI, mesma unidade do serviço (a quantidade é `qtd_refazer`).
- Item que só existe como correção (ex.: transporte de entulho, tratamento de fissura): `qtd_prevista: 0, qtd_aceita: 0, qtd_refazer: <qtd>`.
- `etapa`: agrupa no resumo; use nomes consistentes ("Revestimentos", não "Revestimento" num e "Revestimentos" noutro).

## `etapas` (método B)

```json
{"valor_global_base": "cub",
 "cub": {"projeto_padrao": "R1-N", "valor": 2738.93, "mes": "09/2026", "fonte": "Sinduscon-PR"},
 "area_equivalente": 142.5,
 "valor_contrato": null,
 "valor_global_adicional": 0,
 "pesos_origem": "indicativos do perito (residência unifamiliar padrão normal) — sem cronograma contratual",
 "itens": [{"etapa": "Fundações", "peso": 0.06, "percentual_executado": 1.0, "observacao": ""}]}
```
`valor_global_base`: `cub` (CUB × área + adicional) ou `contrato` (valor_contrato + adicional). `percentual_executado`: parcela **aceita** da etapa.

`modelo` (opcional): `residencial_normal`, `galpao` ou `residencial_alto`. Com ele, os itens podem trazer só `etapa` e `percentual_executado` — o peso vem da tabela (casando pelo nome da etapa), etapas do modelo não informadas entram com 0% e a origem dos pesos é declarada. Use os nomes de etapa da tabela em `custos-referenciais.md`.
