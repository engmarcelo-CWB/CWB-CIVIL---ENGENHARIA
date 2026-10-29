# Estrutura do laudo e critérios de qualidade

Extraído da análise de laudos reais de referência (obras públicas inacabadas para retomada/repactuação — UBS, quadra escolar FNDE, CRAS; inspeção predial de edifício institucional; avaliações judiciais de imóveis inacabados) e combinado com a NBR 13752:2024, a NBR 16747:2020 e a Norma de Inspeção Predial IBAPE (2025).

## 1. Ordem das seções (o gerador segue esta ordem)

| # | Seção | Conteúdo essencial | Observado nos melhores exemplos |
|---|---|---|---|
| — | Capa | Título por tipo, objeto em uma frase, solicitante, endereço, responsável técnico, ART, local e data | Bloco à direita descrevendo o objeto ("Laudo técnico de vistoria realizado por profissional habilitado... do seguinte objeto...") |
| — | Sumário | Gerado automaticamente | Todos os laudos públicos têm |
| 1 | Identificação | Solicitante, proprietário, processo, responsável técnico | |
| 2 | Objeto, objetivo e finalidade | Inclui o enquadramento em programa/portaria quando for obra pública | "...atestar se o objeto está apto a aderir à Portaria/Resolução..." |
| 3 | Dados da obra / programa | Contrato ou convênio, ID no sistema (SIMEC, CNES, Transferegov), executor, valor pactuado, prazo, datas de início/paralisação, % físico informado | Quadra FNDE: tabela do SIMEC com ID, processo, termo, datas e % |
| 4 | Pressupostos, ressalvas e condicionantes | Inclui declaração de isenção (sem interesse no bem) e vistoria não destrutiva | CRAS: princípios e ressalvas éticas |
| 5 | Referências normativas | Só versões vigentes | — (vários exemplos citam NBR 13752/1996 e IBAPE 2012, já superadas) |
| 6 | Metodologia e critérios | Etapas do trabalho, nível de inspeção, critério de classificação (origem, natureza, prioridade/grau de risco), conceituação dos termos | Todos definem grau de risco antes de usá-lo |
| 7 | Documentação analisada | Tabela: documento, situação, observação | |
| 8 | Caracterização e localização | Endereço, coordenadas, **imagem de satélite**, tipologia, padrão, **sistema construtivo**, áreas, serviços públicos | Imagem Google Earth com o lote destacado |
| 9 | Vistoria | Datas, condições, acompanhantes (e o que informaram — anamnese), instrumentos, sistemas não vistoriados | CRM-PR: entrevista com o responsável pela manutenção |
| 10 | Constatações | **Situação por sistema** (quadro) → quadro-resumo das anomalias → descrição detalhada **agrupada por sistema**, cada anomalia com fotos | UBS Verdelândia: um item por sistema com situação, irregularidades, fotos e solução |
| 11 | Análise técnica | Encadeamento causal entre anomalias (ex.: cobertura inacabada → infiltração → danos em forros, revestimentos, portas, instalações), nexo causal, avaliação de manutenção/uso | UBS: "Resultados e discussões" |
| 12 | Quantificação e custos | Base de custos, % executado (com confronto ao % informado), refazer, a executar, materiais não incorporados | CRAS: % não executado e planilha de serviços remanescentes em anexo |
| 13 | Recomendações | Por prioridade; inclui medidas imediatas (proteção, limpeza, escoramento) e verificações (cálculo estrutural, ensaios) | |
| 14 | Quesitos | Se houver | |
| 15 | Conclusão | Resposta direta ao objetivo; classificação global coerente; viabilidade (ex.: "passível de conclusão após as correções") | |
| 16 | Encerramento | Nº de páginas **e de fotografias**, local, data, assinatura, registro, ART | CRM-PR: "composto por 27 folhas e 39 fotos" |
| — | Anexos | ART; planilha de quantitativos e custos (serviços remanescentes e a refazer); composições de custo; cronograma físico-financeiro atualizado; pranchas de projeto citadas; relatório fotográfico geral | CRAS: planilha, composições e cronograma atualizados |

## 2. Critérios de qualidade (verifique antes de gerar)

1. **Normas vigentes** — nunca NBR 13752:1996, Norma IBAPE 2012 ou NBR 5674:1999 como base.
2. **Classificação global coerente com a pior anomalia.** Se há prioridade 1 / grau crítico, o global não pode ser "mínimo" nem "satisfatório". Elemento estrutural faltante ou em desacordo com o projeto exige recomendação de **verificação estrutural por projetista habilitado** e no mínimo prioridade 1 até essa verificação. Obra sem cobertura exposta a chuvas não é "satisfatória". (O script avisa quando detecta incoerência.)
3. **Toda anomalia tem**: local preciso, descrição técnica, extensão/quantidade, origem, natureza, prioridade/grau, requisito normativo ou de projeto, correção e foto. Se faltar algum item, pergunte.
4. **Não conformidade com projeto = especificado × executado**, com unidade e referência da prancha. Ex.: "V13 especificada 15 × 30 cm (EST-03), executada 8,5 × 24 cm (medida com trena)".
5. **Fissuras**: abertura medida (fissurômetro/cartão) ou declarada como estimada; configuração (inclinada, vertical, horizontal, mapeada); atividade (ativa/estabilizada, se monitorada). Informe o critério de nomenclatura adotado (ex.: fissura até 0,5 mm; trinca acima disso) e sua fonte — a nomenclatura varia entre autores.
6. **% executado sempre apurado.** Sem medições, use o método de etapas e declare a fonte dos pesos; nunca deixe "não foi possível apurar" sem estimativa fundamentada. Confronte com o % informado (SIMEC, boletins, executor) e explique diferenças.
7. **Causa × sintoma**: o laudo encadeia causas (a cobertura inacabada é a causa primária dos danos em forros, portas e revestimentos) — isso orienta a ordem dos reparos.
8. **Fotos como prova**: legenda que diz o quê, onde e por quê ("Figura 12 – Dormitório 2: fissura a 45° no canto superior da janela, abertura ~0,3 mm. Fonte: elaboração própria, 20/10/2026"). Prefira fotos com data e coordenadas (câmera com GPS); o gerador lê o EXIF e inclui data/coordenadas na legenda. Fotos de terceiros (pasta da obra, fiscalização anterior) levam a fonte.
9. **Separar fato de opinião**: constatação no presente do indicativo; inferência com "indica", "é compatível com"; recomendação no infinitivo ou com "recomenda-se".
10. **Terminologia correta**: "obra não concluída" (NBR 13752:2024), vício/defeito no sentido da norma; evite "patologia" para o sintoma — use "manifestação patológica".
11. **Escopo honesto**: sistemas não vistoriados e motivo; ensaios necessários indicados como recomendação.
12. **Serviços corretivos fora da planilha original**: em repactuação de obra pública, deixe explícito que os serviços de correção e recomposição não constavam da planilha pactuada e foram incluídos na planilha de retomada (padrão dos laudos de UBS).

## 3. Obras públicas — retomada e repactuação

Laudos para retomada de obras financiadas com recursos federais (FNDE/SIMEC, Ministério da Saúde/CNES, convênios no Transferegov) seguem o mesmo modelo, com:
- enquadramento do objetivo na norma do programa (lei, portaria ou resolução que o solicitante indicar — confirme a vigente; não presuma o número);
- dados da obra extraídos do sistema do órgão (ID, termo, valor, % informado) e comparação com o verificado;
- relação de restrições e inconformidades já registradas pelo órgão, indicando se persistem ou foram superadas;
- conclusão sobre a viabilidade técnica de conclusão e sobre a necessidade de planilha de repactuação;
- planilha de serviços remanescentes + serviços de recuperação, composições e cronograma físico-financeiro atualizado como anexos.

Use o bloco `programa` do JSON (ver `formato-dados.md`).
