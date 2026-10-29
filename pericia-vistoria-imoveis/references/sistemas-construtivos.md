# Sistemas construtivos — o que muda na vistoria

O sistema construtivo define **o que é referência de conformidade**, **onde estão os pontos críticos** e **como a obra se divide em etapas**. Identifique-o antes da análise (campo `imovel.sistema_construtivo_tipo`) e leia só a seção correspondente. Obras mistas (ex.: térreo convencional + pavimento superior em LSF) usam as seções de cada parte.

Sumário: [Regra geral para sistemas industrializados](#regra-geral-para-sistemas-industrializados) · [Convencional](#convencional--concreto-armado--alvenaria-de-vedação) · [Alvenaria estrutural](#alvenaria-estrutural) · [Paredes de concreto](#paredes-de-concreto-moldadas-no-local) · [Pré-moldado](#pré-moldado--pré-fabricado-de-concreto) · [Estrutura metálica / galpões](#estrutura-metálica-e-galpões) · [Light steel frame](#light-steel-framing-lsf) · [Light wood frame](#light-wood-framing-lwf) · [Modular volumétrico](#construção-modular-volumétrica-off-site-e-containers) · [Painéis e outros](#painéis-monolíticos-sanduíche-icf-clt-e-outros)

## Regra geral para sistemas industrializados

1. **Referência de conformidade em camadas**: norma ABNT específica do sistema (quando existe) → NBR 15575 (desempenho, para habitacionais) → **DATec** do produto e **Diretriz SINAT** (Sistema Nacional de Avaliações Técnicas, no âmbito do PBQP-H) para sistemas inovadores → projeto executivo e **manual técnico do fabricante/sistemista** → contrato e memorial.
2. **Peça sempre**: projeto estrutural do sistema com ART, memorial do fabricante, DATec (se houver; verifique validade e se o produto usado é o avaliado), registros de recebimento dos componentes, procedimentos de montagem e, no modular, os relatórios de inspeção de fábrica.
3. **Componente fora do especificado** (perfil de espessura diferente, chapa de outro tipo, membrana omitida) é não conformidade mesmo sem sintoma — o desempenho do sistema depende do conjunto avaliado. Registre especificado × executado.
4. **Grande parte do que importa fica oculta** depois do fechamento (ancoragens, contraventamentos, barreiras, isolantes). Na obra inacabada isso é uma oportunidade: fotografe o que ainda está aberto. Na obra concluída, indique prospecções pontuais (abertura de chapa, termografia, boroscópio) em vez de presumir.
5. **Exposição às intempéries** pesa mais: chapas de OSB, madeira, isolantes e perfis expostos em obra paralisada degradam rápido e frequentemente precisam ser substituídos, não apenas concluídos — isso vai para `qtd_refazer`.
6. **Pesos por etapa**: as tabelas de `custos-referenciais.md` foram feitas para obra convencional. Em sistemas industrializados, use o orçamento/cronograma do fornecedor ou do contrato; se não houver, declare a estimativa e explique a adaptação.

---

## Convencional — concreto armado + alvenaria de vedação

**Normas**: NBR 6118 (projeto), NBR 14931 (execução), NBR 12655 (concreto), NBR 8545 (alvenaria de vedação), NBR 15270 (blocos cerâmicos), NBR 13749 (revestimentos de argamassa), NBR 6122 (fundações).

**Pontos de vistoria**: dimensões de pilares/vigas × projeto (trena; cite a prancha), cobrimento, ninhos de concretagem, armaduras expostas e oxidadas, pilares/vigas/lajes não executados, vergas e contravergas, encunhamento, amarração alvenaria-pilar, impermeabilização de baldrame, prumo e planeza.

**Patologias típicas**: fissura a 45° em cantos de vãos (verga/contraverga), fissura horizontal no topo da alvenaria (encunhamento/deformação de viga), fissura vertical na interface pilar-alvenaria (amarração), umidade ascensional (baldrame sem impermeabilização), corrosão de armaduras (cobrimento insuficiente, ninhos), recalque diferencial.

## Alvenaria estrutural

**Normas**: NBR 16868 partes 1 a 3 (2020), NBR 6136 (blocos de concreto), NBR 15270 (blocos cerâmicos).

**Pontos de vistoria**: paredes estruturais **não podem ser rasgadas, cortadas ou removidas** — verifique rasgos horizontais para instalações, aberturas não previstas, demolições em reformas (NBR 16280); grauteamento e armaduras nos pontos indicados no projeto; cinta de respaldo; juntas de controle; modulação dos blocos.

**Patologias típicas**: fissuras por rasgos de instalações, fissuras na última laje (movimentação térmica da laje de cobertura sem junta deslizante), fissuras em cantos de aberturas sem verga armada. **Remoção de parede estrutural é prioridade 1** até verificação por projetista.

## Paredes de concreto moldadas no local

**Normas**: NBR 16055 (paredes de concreto); referência histórica: Diretriz SINAT nº 001.

**Pontos de vistoria**: espessura das paredes, cobrimento das telas, posição de eletrodutos embutidos (concentração de tubulação reduz seção), juntas de concretagem, falhas de adensamento sob aberturas, nichos de concretagem nas cotas inferiores.

**Patologias típicas**: fissuras de retração em cantos de aberturas, infiltração por juntas frias, bicheiras. Reparos não podem comprometer a seção estrutural — paredes de concreto são estruturais.

## Pré-moldado / pré-fabricado de concreto

**Normas**: NBR 9062 (projeto e execução de estruturas de concreto pré-moldado), NBR 6118, NBR 14861 (lajes alveolares — verificar ano).

**Pontos de vistoria**: ligações (consolos, chumbadores, aparelhos de apoio de neoprene, grauteamento de cálices), comprimento de apoio de vigas e lajes, fissuras em consolos e dentes Gerber, juntas entre painéis (selante), danos de transporte e montagem (lascamentos, armaduras expostas).

**Patologias típicas**: fissura em consolo/dente Gerber (prioridade 1), ruptura de aparelho de apoio, infiltração pelas juntas de painéis de fachada, corrosão de insertos metálicos.

## Estrutura metálica e galpões

**Normas**: NBR 8800 (estruturas de aço e mistas), NBR 14762 (perfis formados a frio), NBR 6123 (vento), NBR 14514 / NBR 14513 (telhas de aço — verificar), NBR 16239 (perfis tubulares — verificar).

**Pontos de vistoria**: perfis e espessuras × projeto, **ligações** (parafusadas × soldadas conforme projeto; qualidade de solda; parafusos faltantes), contraventamentos e tirantes (presença, tensionamento, posição de projeto), chumbadores e placas de base (grauteamento, porcas), proteção anticorrosiva (pintura, galvanização), terças e correntes, calhas e condutores, telhas faltantes ou mal fixadas.

**Patologias típicas**: corrosão em bases e ligações, contraventamento ausente ou frouxo, flambagem local, deformações por sobrecarga, infiltração por fixação de telhas, calhas subdimensionadas. A Quadra FNDE de referência mostra o padrão: arcos, espaçadores, mãos-francesas e contraventamentos executados em desacordo com o projeto — cada divergência é registrada com o elemento e a prancha, e a conclusão pede **verificação estrutural por projetista** (não "risco mínimo").

## Light steel framing (LSF)

**Normas**: ABNT NBR 16970 partes 1 (desempenho), 2 (projeto estrutural) e 3 (verificar ano), NBR 14762 (perfis formados a frio), NBR 15253 (perfis de aço formados a frio com revestimento metálico para painéis estruturais — verificar), NBR 15575; Diretriz SINAT para LSF e DATec do sistemista, quando aplicável.

**Documentos a pedir**: projeto estrutural do LSF (painéis, guias, montantes, vergas, contraventamentos), especificação de perfis (espessura e revestimento de zinco), chapas de fechamento (OSB, cimentícia, gesso), membrana hidrófuga/barreira de vento, isolante, detalhes de ancoragem na fundação.

**Pontos de vistoria**:
- ancoragem dos painéis à fundação (chumbadores/parabolts e hold-downs nos pontos de projeto) e estanqueidade da base (painel sobre radier/viga com fita de vedação e nível);
- montantes no espaçamento de projeto (usualmente modulação de 400 ou 600 mm), vergas e ombreiras nas aberturas, contraventamento (fitas em X tensionadas ou chapa estrutural);
- espessura dos perfis e integridade do revestimento metálico (cortes, furos fora das regiões permitidas, ferrugem branca/vermelha);
- membrana hidrófuga contínua e com transpasse; chapas externas com juntas tratadas; chapas OSB protegidas da umidade;
- isolante preenchendo as cavidades; fitas e selantes em juntas e esquadrias;
- distância do piso externo à base dos painéis (respingo) e caimento.

**Patologias típicas**: fissuras nas juntas de chapas (tratamento inadequado, falta de junta de movimentação), infiltração por esquadrias e pela base, inchamento/apodrecimento de OSB por umidade, corrosão de perfis em contato com umidade ou solo, som "oco" e vibração por fixação insuficiente, pontes térmicas e condensação.

**Obra paralisada**: OSB e perfis expostos — avalie umidade e corrosão; chapa OSB inchada vai para refazer.

## Light wood framing (LWF)

**Normas**: ABNT NBR 16936 (Edificações em light wood frame, 2023 — verificar), NBR 7190 (estruturas de madeira, 2022), NBR 15575; Diretriz SINAT nº 005 (light wood framing) e DATec do sistemista.

**Pontos de vistoria**: madeira tratada (autoclave) com comprovação da classe de tratamento; separação física entre madeira e fundação (barreira de umidade, soleira tratada); ancoragens; membrana hidrófuga; ventilação de beirais e fachadas; proteção contra cupins.

**Patologias típicas**: apodrecimento por umidade na base e em áreas molhadas, ataque de cupins, empenamento, fissuras em juntas de chapas, infiltração por esquadrias.

## Construção modular volumétrica, off-site e containers

Não há norma ABNT específica para construção modular volumétrica — a **NBR 15873 trata de coordenação modular** (compatibilização dimensional), não de módulos volumétricos; não a cite como "norma da construção modular". A referência é o sistema estrutural de cada módulo (LSF, estrutura metálica, concreto, madeira) + NBR 15575 + DATec (quando houver) + projeto e manual do fabricante. Containers marítimos adaptados também não têm norma ABNT própria: avalie como estrutura metálica, com atenção ao conforto térmico e acústico (NBR 15575-4/-5, NBR 15220) e à corrosão.

**Divida a análise em duas partes**:
1. **Módulos (fábrica)**: integridade estrutural, danos de transporte e içamento (amassamentos, fissuras em chapas, empenamento), acabamentos, instalações embutidas, documentação de inspeção de fábrica.
2. **Canteiro**: fundação (nível e locação dos apoios — tolerâncias do fabricante), apoio e fixação dos módulos, **ligações entre módulos** (estruturais e de instalações), **juntas entre módulos** (vedação de cobertura e fachada — principal fonte de infiltração), cobertura complementar, rampas e acessos.

**Pontos de vistoria**: desnível entre módulos, frestas e selantes nas juntas, rufos de junta na cobertura, continuidade das instalações elétricas e hidráulicas entre módulos (conexões acessíveis para manutenção), aterramento das estruturas metálicas, ventilação sob módulos elevados, corrosão na base.

**Obra inacabada / % executado**: separe **módulos fabricados e entregues** (valor de fábrica) de **serviços de canteiro** (fundação, montagem, ligações, acabamentos de junta, ligações às redes). Módulo fabricado mas não entregue ou não instalado é "material não incorporado" (seção própria), não % executado. Peça o contrato com o fabricante: ele costuma ter cronograma de pagamento por marcos (projeto, fabricação, transporte, montagem) que serve de peso por etapa.

## Painéis monolíticos, sanduíche, ICF, CLT e outros

- **Painéis de EPS com argamassa armada (monolíticos)**: verifique espessura da argamassa projetada, cobrimento da tela, fissuras; exija DATec/projeto do sistemista.
- **Painéis sanduíche (termoacústicos)**: fixações, selagem das juntas, corrosão de bordas.
- **ICF (fôrmas de EPS preenchidas com concreto)**: falhas de concretagem não visíveis — indique prospecção; proteção do EPS externo.
- **CLT / MLC (madeira engenheirada)**: NBR 7190; umidade, proteção de topos e base, ligações metálicas.
- **Drywall (vedação interna)**: NBR 15758; montantes, fixação, reforços para cargas suspensas, chapa RU em áreas molhadas, tratamento de juntas.

Para qualquer sistema não listado: identifique o sistemista, peça DATec/manual e projeto, e trate como "sistema inovador" — a conformidade é com o documento técnico do sistema, e a ausência dele deve constar como documento não disponibilizado.
