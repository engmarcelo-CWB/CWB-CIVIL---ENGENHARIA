# Classificação de anomalias, falhas e não conformidades

## 1. Termos (ABNT NBR 13752:2024, seção 3 — redação resumida)

| Termo | Sentido |
|---|---|
| Anomalia | Irregularidade ou desvio em relação a um padrão ou regra |
| Anomalia endógena | Originada no projeto, na especificação de materiais ou na execução |
| Anomalia exógena | Originada de fatores externos à edificação ou causada por terceiros |
| Anomalia funcional | Decorrente do fim da vida útil, decrepitude ou obsolescência |
| Manifestação patológica | Irregularidade que se manifesta no produto por falha de projeto, fabricação, instalação, execução, uso ou manutenção (exclui o envelhecimento natural) |
| Envelhecimento natural | Perda de desempenho com o tempo, mesmo com uso e manutenção adequados |
| Decrepitude | Desgaste pelo envelhecimento natural em uso e manutenção normais |
| Deterioração | Desgaste precoce da construção ou de suas partes |
| Falha | Ocorrência que prejudica o uso; desempenho abaixo do exigido |
| Vício | Anomalia ou falha que prejudica o desempenho ou torna o produto inadequado à finalidade |
| Vício aparente | Visível e facilmente constatável por qualquer pessoa |
| Vício oculto | Não aparente; verificável só por profissional técnico ou que se manifesta com o tempo |
| Vício construtivo | Vício com origem em projeto, especificação de materiais ou execução |
| Vício de informação técnica | Falta ou deficiência de informação nos manuais e documentos entregues ao usuário |
| Defeito | Anomalia ou falha que afeta solidez e segurança, ou ameaça a saúde e a segurança do usuário |
| Avaria | Estrago físico causado por agente externo |
| Mutilação | Retirada de sistemas, elementos ou componentes originalmente existentes |
| Dano | Prejuízo causado a alguém por vícios, defeitos, avarias, mutilação ou deterioração |
| Conformidade | Atendimento a requisito ou padrão (não conformidade: o não atendimento) |
| Vida útil / VUP | Período em que a construção cumpre sua finalidade com manutenção adequada / estimativa teórica de projeto |
| Prazo de garantia | Período em que o fornecedor responde por falhas originadas na concepção ou produção (não se confunde com vida útil) |

Use esses termos com esse sentido no laudo. "Defeito" é palavra forte: reserve para o que afeta solidez/segurança ou a saúde do usuário.

## 2. Origem — campo `origem` no JSON

| Valor | Quando |
|---|---|
| `endogena_projeto` | Erro ou omissão de projeto (ex.: falta de junta de dilatação, detalhe de rufo inexistente) |
| `endogena_material` | Material inadequado ou fora de especificação |
| `endogena_execucao` | Execução em desacordo com projeto ou boas práticas (ex.: ausência de verga/contraverga, cura inadequada, caimento invertido) |
| `exogena` | Fator externo ou terceiros (obra vizinha, impacto de veículo, vazamento de unidade vizinha, evento climático extremo) |
| `funcional` | Fim de vida útil, decrepitude, obsolescência |
| `uso_manutencao` | Uso, operação ou manutenção inadequados (falta de limpeza de calhas, sobrecarga, reforma sem projeto) |
| `indeterminada` | Evidências insuficientes — diga o ensaio/investigação necessário |

Quando a origem for mista (ex.: execução deficiente agravada por falta de manutenção), escolha a predominante e explique a concorrência na análise.

Na **inspeção predial**, a classificação usual (IBAPE 2025) é: anomalia endógena (construtiva), exógena, funcional, e falha de uso, operação ou manutenção — mapeie para os valores acima.

## 3. Natureza — campo `natureza`

`vicio_aparente`, `vicio_oculto`, `defeito`, `avaria`, `mutilacao`, `deterioracao`, `envelhecimento_natural`, `vicio_informacao`, `nao_executado` (pendência de obra), `nao_conformidade` (diverge de projeto/memorial/norma sem ainda ser vício funcional).

## 4. Prioridade — campo `prioridade`

Patamares da Norma de Inspeção Predial IBAPE (2025), compatíveis com a NBR 16747:

| Prioridade | Critério | Prazo de ação sugerido* |
|---|---|---|
| **1** | Perda de desempenho que compromete saúde, segurança ou funcionalidade com risco de paralisação; ou causa perda de vida útil, aumento expressivo de custo ou risco ambiental | Imediato / curto prazo |
| **2** | Funcionalidade parcialmente comprometida, sem prejuízo à operação e sem afetar saúde ou segurança | Médio prazo |
| **3** | Ações que podem ser planejadas, sem comprometer vida útil ou durabilidade | Planejado / manutenção |

\*O prazo é sugestão do perito; a norma define os patamares, não prazos fixos. Se quiser explicitar, use o campo `prazo` da anomalia.

Em vistorias que não são inspeção predial, a prioridade continua útil para ordenar as recomendações.

### Grau de risco (terminologia ainda pedida por órgãos públicos)

Muitos contratantes — prefeituras e programas federais de retomada de obras — pedem a classificação por **grau de risco** (crítico, regular/médio, mínimo), da versão anterior da norma IBAPE. A versão de 2025 usa patamares de prioridade. Para atender aos dois, cada anomalia recebe a prioridade e o laudo mostra o grau correspondente (campo `grau_risco`, preenchido automaticamente se omitido):

| Prioridade (IBAPE 2025) | Grau de risco (terminologia anterior) | Impacto |
|---|---|---|
| 1 | Crítico | Irrecuperável sem ação imediata — saúde, segurança, meio ambiente, perda excessiva de desempenho, paralisação |
| 2 | Regular (médio) | Parcialmente recuperável — perda parcial de desempenho e funcionalidade, deterioração precoce |
| 3 | Mínimo | Recuperável — pequenas perdas, estética, atividade programável |

**Classificação global** (`grau_risco_global`: `critico`, `regular`, `minimo`): reflete a anomalia mais grave ainda não tratada. Um único item crítico torna o global crítico, a menos que a conclusão explique por que ele é localizado e isolável (ex.: escorado/interditado) — e mesmo assim o global não cai para mínimo. "Satisfatório" só cabe quando não há anomalias relevantes. O script avisa quando o global informado é mais brando que a pior anomalia. Para desempate dentro de um patamar, pode-se usar a matriz GUT (Gravidade × Urgência × Tendência, notas 1 a 5) — campo opcional `gut`.

## 5. Prazos de referência (informativo, não conclusivo)

- **ABNT NBR 17170:2022** — Edificações — Garantias — Prazos recomendados e diretrizes. Use a tabela da norma para o prazo de garantia recomendado de cada sistema; cite como referência técnica.
- **Código Civil, art. 618** — empreiteiro responde por 5 anos pela solidez e segurança da obra; a ação deve ser proposta em 180 dias do aparecimento do vício.
- **CDC, art. 26** — prazo para reclamar de vício aparente: 90 dias para bens duráveis, contados da entrega; para vício oculto, a contagem começa quando o vício fica evidenciado.
- **CDC, art. 27** — 5 anos para reparação de danos por fato do produto/serviço.

O perito informa esses marcos; enquadrar o caso concreto é decisão jurídica.

## 6. Fissuras

Registre: configuração (inclinada ~45°, vertical, horizontal, mapeada, em escada), localização em relação a aberturas e elementos estruturais, **abertura** (medida com fissurômetro/cartão, campo `abertura_mm`; se estimada, diga), extensão, se atravessa o reboco/bloco, e atividade (ativa ou estabilizada — só afirme se houve monitoramento com selo/gesso ou medições em datas diferentes). A nomenclatura por abertura (fissura, trinca, rachadura, fenda) varia entre autores — declare o critério adotado e sua fonte.

Leitura típica da configuração (hipóteses a confirmar): 45° em cantos de vãos → falta de verga/contraverga; 45° convergindo para um ponto da base → recalque diferencial; horizontal no topo da parede → deformação da viga/laje ou encunhamento; vertical na junção com pilar → falta de amarração; mapeada no reboco → retração da argamassa; horizontal na última fiada sob laje de cobertura → movimentação térmica da laje.

## 7. Escrevendo a anomalia — padrão

> **A-07 — Banheiro social, parede do box (Foto 12).** Destacamento do revestimento cerâmico 30×60 em área aproximada de 1,2 m², com placas soltas ao toque e som cavo à percussão em toda a parede. No verso das placas destacadas observa-se argamassa colante com pouca área de contato (cordões não esmagados), compatível com assentamento sem dupla colagem para placas desse formato. **Origem:** endógena (execução). **Natureza:** vício construtivo, aparente. **Requisito:** ABNT NBR 13754 (revestimento de paredes internas com placas cerâmicas e argamassa colante) — assentamento com preenchimento adequado do tardoz e aderência ao substrato; recomendações do fabricante da argamassa e da placa quanto à dupla colagem. **Prioridade 2.** **Correção:** remoção do revestimento da parede, limpeza do substrato, verificação da impermeabilização do box, reassentamento com argamassa AC-II/AC-III e dupla colagem, rejuntamento. Serviços: itens 5.3 (remoção) e 5.4 (revestimento).
