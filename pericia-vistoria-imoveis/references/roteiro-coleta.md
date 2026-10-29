# Roteiro de coleta de dados

Use este roteiro para pedir as informações ao usuário. Agrupe tudo em uma ou duas mensagens; pule o que ele já informou. Marque como **(obrigatório)** só o que impede o laudo de sair.

## Bloco A — Identificação

- Número do laudo (se não houver, proponha `AAAA-NNN`) **(obrigatório)**
- Solicitante / contratante: nome, CPF/CNPJ, contato **(obrigatório)**
- Proprietário (se diferente do solicitante)
- Processo judicial ou arbitral: nº, vara/câmara, comarca, partes, quesitos (anexar)
- ART do laudo (pode ficar para depois)

## Bloco B — Imóvel e obra

- Endereço completo, município/UF, coordenadas (opcional) **(obrigatório)**
- Matrícula e cartório; inscrição imobiliária
- Tipologia (residência unifamiliar, sobrado, edifício, galpão, sala comercial…) e padrão (baixo/normal/alto)
- Sistema construtivo (concreto armado + alvenaria de vedação, alvenaria estrutural, paredes de concreto, pré-moldado, estrutura metálica, steel frame, wood frame, modular volumétrico, containers, painéis…) **(obrigatório)** — em sistemas industrializados, pergunte também o fabricante/sistemista e se há DATec, projeto do sistema e manual de montagem (ver `sistemas-construtivos.md`)
- Obra pública ou financiada: órgão/programa, instrumento (convênio, termo de compromisso, contrato), ID no sistema (SIMEC, CNES, Transferegov), valor pactuado, prazo, datas, % físico informado e restrições já registradas pelo órgão; norma do programa a que o laudo deve atender
- Nº de pavimentos, área do terreno, área construída, área privativa/equivalente (NBR 12721)
- Idade / data do habite-se / data de início e de paralisação da obra
- Construtora/executor e responsável técnico (ART/RRT de execução)
- Características relevantes: fundação, cobertura, esquadrias, revestimentos, instalações especiais

## Bloco C — Documentos disponíveis

Pergunte quais existem e peça os relevantes ao tipo:
- Projetos (arquitetônico, estrutural, fundações, hidrossanitário, elétrico, PPCI) e memorial descritivo
- Contrato, aditivos, orçamento contratual, cronograma físico-financeiro, boletins de medição, comprovantes de pagamento
- Diário de obra, notificações, atas
- Alvará, habite-se, AVCB
- Manual de uso, operação e manutenção; plano e registros de manutenção
- Laudos e relatórios anteriores

Registre também os documentos **pedidos e não disponibilizados** — o laudo precisa dizer isso.

## Bloco D — Vistoria

- Data(s) e horário; condições do tempo (chuva recente muda o diagnóstico de umidade)
- Quem acompanhou
- Instrumentos usados (trena, nível, prumo, fissurômetro, higrômetro, termovisor…)
- Sistemas ou áreas não vistoriados e o motivo
- **Fotos**: uma ou mais por constatação, com o local identificado (ex.: "Foto 07 – Banheiro social – parede do box"). Fotos gerais das fachadas e de cada ambiente ajudam a caracterização. Peça os **arquivos originais** (não prints do WhatsApp, que apagam data e GPS do EXIF) — de preferência de câmera com localização ligada ou app de foto georreferenciada. Inclua uma imagem de satélite com o lote destacado e, se houver, prints do sistema do órgão (SIMEC etc.) e fotos de fiscalizações anteriores (com a fonte).
- **Medidas** do que diverge do projeto (seção de pilares e vigas, vãos, espessuras, aberturas de fissuras) com o instrumento usado.
- **Relato textual** de cada constatação: o que é, onde, extensão/dimensão, desde quando (se souber), se piora com chuva/uso.

## Bloco E — Quantitativos (obra inacabada e recebimento; patologias quando houver orçamento de reparo)

Peça uma lista de serviços com, para cada um:

| Serviço | Unidade | Qtd. prevista (projeto/contrato) | Qtd. executada sem vício | Qtd. executada com vício (refazer) |
|---|---|---|---|---|
| Janela de alumínio de correr 1,20 × 1,20 m | un | 8 | 5 | 1 |
| Piso cerâmico 60 × 60 | m² | 95,0 | 40,0 | 12,0 |
| Reboco interno | m² | 320,0 | 210,0 | 0 |

A quantidade não executada é calculada por diferença. Se o usuário tiver só percentuais por etapa ("estrutura 100%, alvenaria 80%, reboco 30%…"), use o método de pesos por etapa.

Se ele tiver o orçamento contratual em planilha, peça o arquivo: os quantitativos previstos e até os preços contratados podem sair de lá.

## Bloco F — Base de custos

Pergunte sempre (não há tabela padrão):
- Tabela: SINAPI, SICRO, SETOP-MG, SMOP (Curitiba), DER-PR, ORSE, SEINFRA-CE, outra, ou orçamento contratual
- UF e mês de referência
- Desonerada ou não desonerada
- BDI a aplicar (ou "sem BDI")
- Para obra inacabada pelo método de etapas: CUB do estado, projeto-padrão (ex.: R1-N) e mês; área equivalente
- **Anexar a planilha da tabela do mês** — sem ela, os preços ficam em aberto

## Mensagem modelo

> Para elaborar o laudo de **[tipo]** preciso dos dados abaixo. Pode mandar tudo de uma vez, na ordem que preferir:
> 1. Identificação: solicitante, proprietário, nº do processo (se houver) e quesitos.
> 2. Imóvel: endereço, matrícula, áreas, tipologia, padrão, sistema construtivo, pavimentos, idade.
> 3. Documentos que você tem (projetos, memorial, contrato, cronograma, medições, manual…).
> 4. Vistoria: data, condições, quem acompanhou, o que não pôde ser vistoriado.
> 5. Fotos, cada uma com o local, e o relato de cada constatação.
> 6. Quantidades por serviço: previsto, executado sem vício e executado com vício.
> 7. Base de custos: tabela, UF, mês, desoneração, BDI — e a planilha da tabela anexada.
