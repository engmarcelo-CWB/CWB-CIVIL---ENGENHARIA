# Custos referenciais e métodos de cálculo

Sumário: [Bases de custo](#1-bases-de-custo) · [Buscando preços na planilha](#2-buscando-preços-na-planilha-da-tabela) · [Desoneração e BDI](#3-desoneração-e-bdi) · [Método A — orçamento discriminado](#4-método-a--orçamento-discriminado) · [Método B — pesos por etapa](#5-método-b--pesos-por-etapa-sobre-o-cub-ou-orçamento-global) · [Serviços a refazer](#6-serviços-a-refazer) · [Regras de ouro](#7-regras-de-ouro)

## 1. Bases de custo

As tabelas mudam todo mês (ou trimestre) e são grandes demais para ficar embutidas na skill. **Pergunte sempre qual base usar** e peça a planilha do mês.

| Base | Abrangência | Onde obter | Observações |
|---|---|---|---|
| **SINAPI** (Caixa/IBGE) | Edificações e infraestrutura, todas as UFs | caixa.gov.br/sinapi → downloads por UF e mês | Referência obrigatória para recursos federais (Decreto 7.983/2013). Publicado com e sem desoneração. Preço por UF; o arquivo pode trazer várias UFs em colunas |
| **SICRO** (DNIT) | Obras rodoviárias e de infraestrutura | gov.br/dnit → Custos e pagamentos → SICRO | Por UF; periodicidade definida pelo DNIT |
| **CUB/m²** (Sinduscons) | Custo global por m² de projeto-padrão (NBR 12721) | No PR: sindusconpr.com.br/economia/cub-pr (mensal) | Não é preço de serviço; serve para valor global (método B) |
| **SETOP / tabela do Governo de MG** | Edificações e infraestrutura em MG | portal do Governo de MG (verificar nome atual da tabela) | Usada em MG e às vezes como referência complementar |
| **SMOP** (Prefeitura de Curitiba) | Edificações, infraestrutura e mão de obra em Curitiba | curitiba.pr.gov.br → Tabela de Custos SMOP | Arquivos em .xlsx/PDF, com versões com e sem desoneração; confira se há tabela mais recente que a disponível |
| **DER-PR** | Obras rodoviárias no PR | der.pr.gov.br → tabela de preços | |
| ORSE (SE), SEINFRA (CE), SIURB e CPOS (SP), outras | Regionais | sites dos órgãos | Usar quando o usuário indicar |
| TCPO (Pini) | Composições (índices de consumo) | Publicação comercial | Para montar composição própria |
| Cotação de mercado | Itens sem composição oficial | 3 cotações, quando possível | Registrar fornecedor e data em `premissas` |
| Orçamento contratual | Preços pactuados entre as partes | Contrato | Em acerto de contas contratual, costuma ser a base mais adequada — pergunte |

Registre no laudo e na planilha: base, UF, mês de referência, regime (desonerado/não desonerado), BDI e data de consulta.

## 2. Buscando preços na planilha da tabela

```bash
# busca por palavras (todas precisam aparecer na descrição; acentos e caixa ignorados)
python scripts/buscar_precos.py SINAPI_2026_09.xlsx "piso ceramico 60x60" --uf PR
# busca por código
python scripts/buscar_precos.py SINAPI_2026_09.xlsx --codigo 87263 --uf PR
# ver como o script entendeu o arquivo (abas, linha de cabeçalho, colunas)
python scripts/buscar_precos.py SINAPI_2026_09.xlsx --diagnostico
```

O script procura, em cada aba, a linha de cabeçalho com colunas de código, descrição, unidade e preço/custo. Com `--uf`, ele usa a coluna cujo título é a sigla da UF (formato com várias UFs lado a lado). Se o diagnóstico mostrar que ele escolheu a coluna errada, use `--col-preco "<título>"` (ou `--aba`, `--col-codigo`, `--col-descricao`, `--col-unidade`).

Na escolha da composição, confira: material e especificação, dimensão/espessura, inclusão ou não de material (algumas composições são só mão de obra), unidade. Na dúvida entre duas, mostre ambas ao usuário.

## 3. Desoneração e BDI

- **Desonerado × não desonerado**: muda os encargos sociais da mão de obra. Use o regime que o usuário indicar e não misture regimes no mesmo orçamento.
- **BDI**: em perícia de imóvel particular, aplique o BDI que o usuário indicar (ou nenhum, se ele pedir custo direto). Para obras públicas, referência usual: Acórdão TCU 2622/2013 — para construção de edifícios, faixa de 20,34% (1º quartil) a 25,00% (3º quartil), média 22,12% (confira no acórdão antes de citar). O BDI vai em `base_custos.bdi` como fração (0,25 = 25%).
- A planilha mostra preço sem BDI, BDI e preço com BDI em colunas separadas, com fórmula.

## 4. Método A — orçamento discriminado

Para cada serviço `i`:

| Grandeza | Fórmula |
|---|---|
| Qtd. não executada | `max(prevista − aceita − refazer, 0)` |
| PU com BDI | `PU × (1 + BDI)` |
| Valor previsto | `prevista × PU_bdi` |
| Valor executado aceito | `aceita × PU_bdi` |
| Custo de refazer | `refazer × (PU + PU_demolição) × (1 + BDI)` (+ descarte, se lançado como serviço próprio) |
| Custo a executar | `não executada × PU_bdi` |
| Custo para concluir | `refazer + a executar` |

**% executado aceito = Σ valor aceito ÷ Σ valor previsto.**

Também é útil o **% executado bruto** (aceito + com vício) ÷ previsto, para comparar com o que o executor mediu — a diferença é o que foi feito e não pode ser aceito.

Serviços sem preço entram com quantidade, mas ficam fora dos totais — o script avisa e a planilha destaca a célula. O % executado só é confiável quando todos os serviços relevantes têm preço.

## 5. Método B — pesos por etapa sobre o CUB ou orçamento global

Use quando não há quantitativos por serviço, ou como verificação do método A.

1. **Valor global**: orçamento contratual, se houver; senão `CUB/m² × área equivalente` (NBR 12721), declarando projeto-padrão e mês. Lembre que o CUB **não inclui**: fundações especiais (estacas, tubulões, paredes-diafragma, rebaixamento de lençol), elevadores, equipamentos (bombas, aquecedores, ar-condicionado etc.), obras complementares (urbanização, ajardinamento, ligações de serviços públicos), projetos, impostos e taxas, remuneração do construtor e do incorporador. Se esses itens existirem na obra, orce-os à parte (campo `valor_global_adicional`).
2. **Pesos**: use o cronograma físico-financeiro do contrato. Sem ele, os pesos abaixo são **indicativos** para residência unifamiliar térrea, padrão normal, estrutura de concreto armado com alvenaria de vedação — ajuste à obra e declare no laudo que são estimativa do perito.

| Etapa | Peso indicativo |
|---|---|
| Serviços preliminares e canteiro | 2% |
| Fundações (rasas) | 6% |
| Estrutura (concreto armado) | 15% |
| Alvenaria e vedações | 8% |
| Cobertura (estrutura, telhas, rufos, calhas) | 7% |
| Impermeabilização | 2% |
| Instalações hidrossanitárias | 7% |
| Instalações elétricas | 6% |
| Revestimentos de parede (chapisco, reboco, azulejo) | 12% |
| Forros | 2% |
| Pisos (contrapiso, revestimento, rodapé, soleiras) | 10% |
| Esquadrias (portas, janelas, ferragens) | 9% |
| Vidros | 2% |
| Louças, metais e acessórios | 3% |
| Pintura | 7% |
| Serviços complementares e limpeza final | 2% |
| **Total** | **100%** |

Sobrado: aumentar estrutura e escada (~+3%) reduzindo fundações proporcionalmente. Na dúvida, pergunte ao usuário.

**Outras tabelas indicativas** (usadas em laudos de referência — também embutidas no script, pelo campo `etapas.modelo`):

| Etapa | `residencial_normal` (acima) | `galpao` ¹ | `residencial_alto` ² |
|---|---|---|---|
| Projetos | — | — | 0,7% |
| Serviços preliminares | 2,0% | 1,8% | 3,0% |
| Movimento de terra | — | 0,2% | 1,0% |
| Fundações especiais/profundas | — | 4,0% | — |
| Fundações / infraestrutura | 6,0% | 3,0% | 7,5% |
| Estrutura / superestrutura | 15,0% | 6,0% | 18,8% |
| Alvenaria e vedações | 8,0% | 3,1% | 6,0% |
| Esquadrias | 9,0% | 9,5% | 4,0% |
| Cobertura | 7,0% | 20,0% | 0,6% |
| Instalações hidrossanitárias | 7,0% | 5,3% | 12,0% |
| Instalações elétricas | 6,0% | 6,0% | 4,3% |
| Impermeabilização (e isolação térmica) | 2,0% | 1,1% | 9,0% |
| Revestimentos (paredes, pisos, forros) ³ | 24,0% | 9,3% | 24,0% |
| Vidros | 2,0% | 0,4% | 3,4% |
| Louças, metais e acessórios | 3,0% | — | — |
| Pintura | 7,0% | 7,0% | 4,2% |
| Serviços complementares e limpeza | 2,0% | 23,3% | 1,5% |
| **Total** | 100% | 100% | 100% |

¹ Galpão industrial com estrutura de concreto e cobertura metálica, de laudo judicial de avaliação (método evolutivo, CUB R8-N) — note o peso de serviços complementares (pátios, pavimentação, redes externas).
² Residência padrão alto/fino em concreto e alvenaria, com piscina, baseada em tabela de incidência PINI usada em laudo judicial (cobertura em laje, por isso o peso baixo).
³ Em `residencial_normal`, soma de revestimentos de parede (12%), forros (2%) e pisos (10%), que o script mantém como linhas separadas.

Para sistemas industrializados (LSF, modular, pré-moldado etc.) nenhuma destas tabelas é adequada sem adaptação — veja `sistemas-construtivos.md`.

Com `etapas.modelo`, basta informar em `itens` a etapa e o percentual executado; o peso é preenchido pela tabela (por nome da etapa) e a origem dos pesos é declarada automaticamente. Pesos informados no item prevalecem.

3. **% executado** de cada etapa: informado pelo usuário com base na vistoria (somente a parcela aceita). **% global = Σ (peso × % etapa)**; valor executado = valor global × % global.

## 6. Serviços a refazer

O custo de refazer inclui, conforme o caso:
- demolição/remoção do serviço mal executado (composição de demolição ou remoção);
- carga, transporte e descarte de entulho (caçamba);
- reexecução do serviço (mesma composição do serviço novo);
- serviços associados danificados no reparo (ex.: refazer pintura após reparo de reboco; recompor impermeabilização sob piso removido).

Lance a demolição no bloco `demolicao` do serviço quando for 1:1 com ele; lance como serviço separado (com `qtd_prevista = 0` e `qtd_refazer` = quantidade) quando for um item agregado, como transporte de entulho. Serviços associados entram como serviços próprios.

## 7. Regras de ouro

- Preço sem fonte não entra no laudo. Sem tabela, deixe `null` e avise.
- Uma base por orçamento; se precisar complementar (item inexistente no SINAPI), identifique a fonte item a item.
- Mês de referência explícito; se o laudo for usado meses depois, recomende atualização pelo índice (INCC ou SINAPI) — não atualize por conta própria sem pedido.
- Materiais entregues e não incorporados à obra vão em seção própria, sem entrar no % executado.
