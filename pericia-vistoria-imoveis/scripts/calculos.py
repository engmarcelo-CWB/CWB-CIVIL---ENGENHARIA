"""Cálculos de quantitativos e custos do laudo (espelham as fórmulas da planilha)."""

import unicodedata

from textos_padrao import ORDEM_GRAU, PESOS_MODELOS, PRIORIDADE_PARA_GRAU


def _norm(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    return " ".join(s.split())


def _peso_modelo(tabela, etapa):
    alvo = _norm(etapa)
    for nome, peso in tabela.items():
        if nome.startswith("_"):
            continue
        n = _norm(nome)
        if n == alvo or n.startswith(alvo) or alvo.startswith(n):
            return peso
    return None


def _num(v):
    if v is None or v == "":
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace("R$", "").replace(" ", "")
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def calcular(dados):
    """Retorna dict com linhas de serviço calculadas, totais, etapas e avisos."""
    avisos = []
    base = dados.get("base_custos") or {}
    bdi = _num(base.get("bdi")) or 0.0
    if bdi > 1:
        avisos.append(f"BDI informado como {bdi}; interpretado como {bdi}% (fração {bdi/100:.4f}).")
        bdi = bdi / 100.0

    linhas = []
    for s in dados.get("servicos") or []:
        prev = _num(s.get("qtd_prevista")) or 0.0
        aceita = _num(s.get("qtd_aceita")) or 0.0
        refazer = _num(s.get("qtd_refazer")) or 0.0
        pu = _num(s.get("preco_unitario"))
        dem = s.get("demolicao") or {}
        pu_dem = _num(dem.get("preco_unitario")) or 0.0
        nao_exec = max(prev - aceita - refazer, 0.0)
        item = str(s.get("item", "")).strip()
        if aceita + refazer > prev + 1e-9 and prev > 0:
            avisos.append(
                f"Serviço {item}: aceita ({aceita}) + refazer ({refazer}) excede a prevista ({prev}). Confira as quantidades."
            )
        if prev == 0 and refazer == 0 and aceita == 0:
            avisos.append(f"Serviço {item}: todas as quantidades são zero.")
        if pu is None:
            avisos.append(f"Serviço {item} ({s.get('descricao','')[:50]}): sem preço unitário — fica fora dos totais.")
        if refazer > 0 and prev > 0 and not dem:
            avisos.append(
                f"Serviço {item}: há quantidade a refazer sem composição de demolição/remoção. "
                "Se a remoção for necessária, informe o bloco 'demolicao' ou lance-a como serviço próprio."
            )
        if dem and _num(dem.get("preco_unitario")) is None:
            avisos.append(f"Serviço {item}: demolição sem preço unitário.")
        l = {
            "item": item,
            "etapa": s.get("etapa") or "Geral",
            "fonte": s.get("fonte") or base.get("fonte") or "",
            "codigo": str(s.get("codigo") or ""),
            "descricao": s.get("descricao") or "",
            "unidade": s.get("unidade") or "",
            "prev": prev,
            "aceita": aceita,
            "refazer": refazer,
            "nao_exec": nao_exec,
            "pu": pu,
            "pu_dem": pu_dem if dem else None,
            "demolicao": dem,
            "observacao": s.get("observacao") or "",
        }
        if pu is not None:
            pub = pu * (1 + bdi)
            l.update(
                pu_bdi=pub,
                v_prev=prev * pub,
                v_aceito=aceita * pub,
                v_bruto=(aceita + refazer) * pub,
                c_refazer=refazer * (pu + pu_dem) * (1 + bdi),
                c_executar=nao_exec * pub,
            )
            l["c_concluir"] = l["c_refazer"] + l["c_executar"]
        else:
            for k in ("pu_bdi", "v_prev", "v_aceito", "v_bruto", "c_refazer", "c_executar", "c_concluir"):
                l[k] = None
        linhas.append(l)

    def soma(k):
        return sum(l[k] for l in linhas if l[k] is not None)

    tot = {k: soma(k) for k in ("v_prev", "v_aceito", "v_bruto", "c_refazer", "c_executar", "c_concluir")}
    tot["pct_aceito"] = tot["v_aceito"] / tot["v_prev"] if tot["v_prev"] else None
    tot["pct_bruto"] = tot["v_bruto"] / tot["v_prev"] if tot["v_prev"] else None
    tot["sem_preco"] = sum(1 for l in linhas if l["pu"] is None)
    if tot["pct_aceito"] is not None and tot["pct_aceito"] > 1.0001:
        avisos.append("Percentual executado acima de 100% — há quantidade lançada errada.")

    # por etapa (ordem de aparição)
    etapas_orc = []
    for l in linhas:
        if l["etapa"] not in etapas_orc:
            etapas_orc.append(l["etapa"])
    por_etapa = []
    for e in etapas_orc:
        ls = [l for l in linhas if l["etapa"] == e and l["pu"] is not None]
        d = {k: sum(l[k] for l in ls) for k in ("v_prev", "v_aceito", "c_refazer", "c_executar", "c_concluir")}
        d["etapa"] = e
        d["pct_aceito"] = d["v_aceito"] / d["v_prev"] if d["v_prev"] else None
        por_etapa.append(d)

    # método B
    etapas_b = None
    eb = dados.get("etapas")
    modelo = (eb or {}).get("modelo")
    tabela_modelo = PESOS_MODELOS.get(modelo) if modelo else None
    if modelo and not tabela_modelo:
        avisos.append(f"Modelo de pesos '{modelo}' desconhecido; use um de {list(PESOS_MODELOS)}.")
    if eb and tabela_modelo and not eb.get("itens"):
        eb = dict(eb, itens=[{"etapa": n} for n in tabela_modelo if not n.startswith("_")])
        avisos.append("Etapas geradas a partir do modelo sem percentual executado — informe o % de cada etapa.")
    if eb and tabela_modelo and eb.get("itens"):
        informadas = [it.get("etapa") for it in eb["itens"]]
        faltantes = [n for n in tabela_modelo if not n.startswith("_")
                     and not any(_peso_modelo({n: 1}, x) for x in informadas)]
        if faltantes:
            eb = dict(eb, itens=list(eb["itens"]) + [
                {"etapa": n, "percentual_executado": 0, "observacao": "não informada — considerada não executada"} for n in faltantes])
            avisos.append(f"Etapas do modelo não informadas, consideradas 0% executadas: {', '.join(faltantes)}.")
    if eb and eb.get("itens"):
        cub = eb.get("cub") or {}
        valor_cub = _num(cub.get("valor"))
        area = _num(eb.get("area_equivalente"))
        contrato = _num(eb.get("valor_contrato"))
        adicional = _num(eb.get("valor_global_adicional")) or 0.0
        base_vg = eb.get("valor_global_base") or ("contrato" if contrato else "cub")
        if base_vg == "contrato":
            vg = (contrato or 0.0) + adicional if contrato is not None else None
        else:
            vg = valor_cub * area + adicional if (valor_cub is not None and area is not None) else None
        if vg is None:
            avisos.append("Método por etapas: valor global indefinido (falta CUB × área equivalente ou valor de contrato).")
        itens = []
        soma_peso = 0.0
        pct_global = 0.0
        for it in eb["itens"]:
            peso = _num(it.get("peso"))
            if peso is None and tabela_modelo:
                peso = _peso_modelo(tabela_modelo, it.get("etapa"))
                if peso is None:
                    avisos.append(f"Etapa '{it.get('etapa')}' não encontrada no modelo '{modelo}' — informe o peso.")
            peso = peso or 0.0
            pct = _num(it.get("percentual_executado"))
            if peso > 1:
                peso /= 100.0
            if pct is not None and pct > 1:
                pct /= 100.0
            soma_peso += peso
            contrib = peso * (pct or 0.0)
            pct_global += contrib
            v_etapa = vg * peso if vg is not None else None
            v_exec = v_etapa * (pct or 0.0) if v_etapa is not None else None
            itens.append(
                dict(
                    etapa=it.get("etapa", ""),
                    peso=peso,
                    pct=pct,
                    contrib=contrib,
                    v_etapa=v_etapa,
                    v_exec=v_exec,
                    v_rest=(v_etapa - v_exec) if v_etapa is not None else None,
                    observacao=it.get("observacao", ""),
                )
            )
            if pct is None:
                avisos.append(f"Etapa '{it.get('etapa')}': sem percentual executado (considerado 0%).")
        if abs(soma_peso - 1.0) > 0.001:
            avisos.append(f"Método por etapas: a soma dos pesos é {soma_peso*100:.2f}% (deveria ser 100%).")
        etapas_b = dict(
            base=base_vg,
            cub=cub,
            area=area,
            contrato=contrato,
            adicional=adicional,
            valor_global=vg,
            itens=itens,
            soma_peso=soma_peso,
            pct_global=pct_global,
            v_exec=vg * pct_global if vg is not None else None,
            v_rest=vg * (1 - pct_global) if vg is not None else None,
            pesos_origem=eb.get("pesos_origem") or (tabela_modelo or {}).get("_origem", ""),
        )

    # grau de risco por anomalia e coerência do global
    pior = None
    for a in dados.get("anomalias") or []:
        g = a.get("grau_risco") or PRIORIDADE_PARA_GRAU.get(a.get("prioridade"))
        a["_grau"] = g
        if g and (pior is None or ORDEM_GRAU.get(g, 0) > ORDEM_GRAU.get(pior, 0)):
            pior = g
        if a.get("grau_risco") and a.get("prioridade") and PRIORIDADE_PARA_GRAU.get(a["prioridade"]) != a["grau_risco"]:
            avisos.append(f"Anomalia {a.get('id')}: prioridade {a['prioridade']} e grau '{a['grau_risco']}' não correspondem.")
    glob = dados.get("grau_risco_global")
    if glob and pior and ORDEM_GRAU.get(glob, 0) < ORDEM_GRAU.get(pior, 0):
        avisos.append(
            f"INCOERÊNCIA: grau de risco global '{glob}' é mais brando que a pior anomalia ('{pior}'). "
            "Revise a conclusão ou justifique por que a anomalia é localizada e controlada."
        )
    for a in dados.get("anomalias") or []:
        sistema = _norm(a.get("sistema"))
        if any(k in sistema for k in ("estrutur", "fundac")) and a.get("natureza") in ("nao_conformidade", "defeito", "nao_executado") \
                and (a.get("prioridade") or 9) > 1:
            avisos.append(
                f"Anomalia {a.get('id')} é estrutural ({a.get('natureza')}) com prioridade {a.get('prioridade')} — "
                "elemento estrutural em desacordo/ausente pede verificação por projetista e, em regra, prioridade 1."
            )

    # custo por anomalia (serviços relacionados)
    por_item = {l["item"]: l for l in linhas}
    custo_anom = {}
    for a in dados.get("anomalias") or []:
        refs = [str(x) for x in (a.get("servicos") or [])]
        faltando = [r for r in refs if r not in por_item]
        if faltando:
            avisos.append(f"Anomalia {a.get('id')}: serviços {faltando} não existem na lista de serviços.")
        vals = [por_item[r]["c_concluir"] for r in refs if r in por_item and por_item[r]["c_concluir"] is not None]
        custo_anom[a.get("id")] = sum(vals) if vals else None

    # materiais não incorporados
    mats = []
    for m in dados.get("materiais_nao_incorporados") or []:
        q = _num(m.get("quantidade")) or 0.0
        vu = _num(m.get("valor_unitario"))
        mats.append(dict(m, quantidade=q, valor_unitario=vu, total=(q * vu if vu is not None else None)))

    return dict(
        bdi=bdi,
        linhas=linhas,
        totais=tot,
        por_etapa=por_etapa,
        etapas_b=etapas_b,
        custo_anomalia=custo_anom,
        grau_pior=pior,
        materiais=mats,
        avisos=avisos,
    )
