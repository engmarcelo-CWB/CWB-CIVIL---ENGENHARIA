#!/usr/bin/env python3
"""Gera o laudo (.docx) e a planilha (.xlsx) a partir de laudo.json.

Uso:
    python gerar_documentos.py laudo.json [--saida pasta] [--so-planilha | --so-laudo]

O formato do JSON está em references/formato-dados.md e há um exemplo em assets/exemplo_laudo.json.
Caminhos de fotos podem ser absolutos ou relativos à pasta do JSON.
"""

import argparse
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

from calculos import calcular  # noqa: E402
from laudo import Laudo, moeda, pct  # noqa: E402
from planilha import gerar_planilha  # noqa: E402
from textos_padrao import TIPOS  # noqa: E402

PERITO_PADRAO = os.path.join(AQUI, "..", "assets", "perito_padrao.json")


def carregar_perito(dados):
    perito = {}
    if os.path.exists(PERITO_PADRAO):
        with open(PERITO_PADRAO, encoding="utf-8") as f:
            perito = json.load(f)
        if perito.get("logo") and not os.path.isabs(perito["logo"]):
            perito["logo"] = os.path.join(AQUI, "..", "assets", perito["logo"])
    over = dados.get("perito") or {}
    for k, v in over.items():
        if k == "empresa" and isinstance(v, dict):
            perito["empresa"] = {**perito.get("empresa", {}), **v}
        elif v not in (None, ""):
            perito[k] = v
    return perito


def validar(dados):
    erros, avisos = [], []
    if dados.get("tipo") not in TIPOS:
        erros.append(f"'tipo' deve ser um de {list(TIPOS)} (recebido: {dados.get('tipo')!r}).")
    for campo in ("numero_laudo", "data_emissao"):
        if not dados.get(campo):
            erros.append(f"Campo obrigatório ausente: '{campo}'.")
    if not (dados.get("imovel") or {}).get("endereco"):
        erros.append("Campo obrigatório ausente: 'imovel.endereco'.")
    if not (dados.get("solicitante") or {}).get("nome"):
        avisos.append("Solicitante sem nome.")
    if not (dados.get("vistoria") or {}).get("datas"):
        avisos.append("Sem data de vistoria (vistoria.datas).")
    if dados.get("servicos") and not dados.get("base_custos"):
        avisos.append("Há serviços mas não há 'base_custos' (fonte, UF, mês, regime, BDI).")
    ids = [a.get("id") for a in dados.get("anomalias") or []]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        erros.append(f"IDs de anomalia repetidos: {sorted(dup)}.")
    for a in dados.get("anomalias") or []:
        if a.get("prioridade") not in (1, 2, 3, None):
            avisos.append(f"Anomalia {a.get('id')}: prioridade deve ser 1, 2 ou 3.")
        if not a.get("descricao"):
            avisos.append(f"Anomalia {a.get('id')}: sem descrição.")
    itens = [str(s.get("item")) for s in dados.get("servicos") or []]
    dup = {i for i in itens if itens.count(i) > 1}
    if dup:
        erros.append(f"Itens de serviço repetidos: {sorted(dup)}.")
    from textos_padrao import GRAU_RISCO, SISTEMAS, SITUACAO_SISTEMA

    if dados.get("grau_risco_global") and dados["grau_risco_global"] not in GRAU_RISCO:
        erros.append(f"'grau_risco_global' deve ser um de {list(GRAU_RISCO)}.")
    st = (dados.get("imovel") or {}).get("sistema_construtivo_tipo")
    if st and st not in SISTEMAS:
        avisos.append(f"'imovel.sistema_construtivo_tipo' desconhecido ({st}); use um de {list(SISTEMAS)}.")
    if not st:
        avisos.append("Sem 'imovel.sistema_construtivo_tipo' — informe para incluir as normas do sistema.")
    for s_ in dados.get("situacao_sistemas") or []:
        if s_.get("situacao") not in SITUACAO_SISTEMA:
            avisos.append(f"situacao_sistemas '{s_.get('sistema')}': situação deve ser um de {list(SITUACAO_SISTEMA)}.")
    for a in dados.get("anomalias") or []:
        if not a.get("fotos"):
            avisos.append(f"Anomalia {a.get('id')}: sem foto (todo registro deve ter evidência fotográfica).")
        if a.get("natureza") == "nao_conformidade" and not (a.get("especificado") and a.get("executado")):
            avisos.append(f"Anomalia {a.get('id')}: não conformidade sem 'especificado' × 'executado'.")
    if dados.get("anomalias") and not dados.get("grau_risco_global") and dados.get("tipo") in ("obra_inacabada", "inspecao_predial"):
        avisos.append("Sem 'grau_risco_global' — os laudos de obra pública/inspeção costumam exigir a classificação global.")
    if dados.get("tipo") == "inspecao_predial":
        for c in ("avaliacao_manutencao", "avaliacao_uso"):
            if not dados.get(c):
                avisos.append(f"Inspeção predial sem '{c}' (conteúdo mínimo da norma).")
    return erros, avisos


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("json")
    ap.add_argument("--saida", default=".")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--so-planilha", action="store_true")
    g.add_argument("--so-laudo", action="store_true")
    a = ap.parse_args()

    with open(a.json, encoding="utf-8") as f:
        dados = json.load(f)
    base_dir = os.path.dirname(os.path.abspath(a.json))

    erros, avisos = validar(dados)
    if erros:
        print("ERROS — corrija o JSON:")
        for e in erros:
            print("  -", e)
        sys.exit(1)

    perito = carregar_perito(dados)
    calc = calcular(dados)
    avisos += calc["avisos"]
    os.makedirs(a.saida, exist_ok=True)
    num = re.sub(r"[^\w\-]+", "_", str(dados["numero_laudo"]))
    arq_xlsx = os.path.join(a.saida, f"Planilha_{num}.xlsx")
    arq_docx = os.path.join(a.saida, f"Laudo_{num}.docx")

    gerou = []
    if not a.so_laudo and (calc["linhas"] or calc["etapas_b"] or dados.get("anomalias")):
        gerar_planilha(dados, calc, arq_xlsx)
        gerou.append(arq_xlsx)
    if not a.so_planilha:
        avisos += Laudo(dados, calc, base_dir, perito).gerar(arq_docx)
        gerou.append(arq_docx)

    t = calc["totais"]
    print("=== RESUMO ===")
    print(f"Tipo: {TIPOS[dados['tipo']]['titulo']}")
    anom = dados.get("anomalias") or []
    if anom:
        cont = {p: sum(1 for x in anom if x.get("prioridade") == p) for p in (1, 2, 3)}
        print(f"Anomalias: {len(anom)} (P1={cont[1]}, P2={cont[2]}, P3={cont[3]})")
    if calc["linhas"]:
        print(f"Serviços: {len(calc['linhas'])} ({t['sem_preco']} sem preço)")
        print(f"Valor previsto:        {moeda(t['v_prev'])}")
        print(f"Executado aceito:      {moeda(t['v_aceito'])}  ({pct(t['pct_aceito'])})")
        print(f"Executado bruto:       {pct(t['pct_bruto'])}")
        print(f"Custo de refazer:      {moeda(t['c_refazer'])}")
        print(f"Custo a executar:      {moeda(t['c_executar'])}")
        print(f"Custo para concluir:   {moeda(t['c_concluir'])}")
    eb = calc["etapas_b"]
    if eb:
        print(f"Método por etapas: valor global {moeda(eb['valor_global'])}; executado {pct(eb['pct_global'])} = {moeda(eb['v_exec'])}")
    if not perito.get("art"):
        avisos.append("ART do laudo não informada (perito.art).")
    if avisos:
        print("\n=== AVISOS ===")
        for x in avisos:
            print("  -", x)
    print("\nArquivos gerados:")
    for g_ in gerou:
        print("  ", os.path.abspath(g_))


if __name__ == "__main__":
    main()
