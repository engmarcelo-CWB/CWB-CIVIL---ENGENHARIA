#!/usr/bin/env python3
"""Busca composições/insumos em planilhas de tabelas referenciais (SINAPI, SICRO, SETOP, SMOP, DER, ORSE...).

Exemplos:
    python buscar_precos.py SINAPI.xlsx "alvenaria bloco ceramico 9cm"
    python buscar_precos.py SINAPI.xlsx "janela aluminio correr" --uf PR --limite 20
    python buscar_precos.py SINAPI.xlsx --codigo 87503 --uf PR
    python buscar_precos.py SINAPI.xlsx --diagnostico
    python buscar_precos.py tabela.xlsx "reboco" --aba "Composições" --col-preco "Custo Total"

Funciona com .xlsx/.xlsm e .csv (separador ; ou ,). Para .xls antigo, converta antes:
    soffice --headless --convert-to xlsx arquivo.xls

O script detecta automaticamente, em cada aba, a linha de cabeçalho e as colunas de código,
descrição, unidade e preço. Com --uf, usa como preço a coluna cujo título é a sigla da UF
(formato com várias UFs lado a lado). Use --diagnostico para ver o que foi detectado e as
opções --col-* para corrigir.
"""

import argparse
import csv
import os
import re
import sys
import unicodedata

UFS = "AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO".split()


def norm(s):
    s = "" if s is None else str(s)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", s).strip().lower()


def num(v):
    if v is None or v == "":
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace("R$", "").replace(" ", "")
    if re.fullmatch(r"-?[\d.]+,\d+", s):
        s = s.replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def ler_abas(caminho, aba=None):
    ext = os.path.splitext(caminho)[1].lower()
    if ext == ".csv":
        with open(caminho, encoding="utf-8-sig", errors="replace") as f:
            amostra = f.read(4096)
            f.seek(0)
            sep = ";" if amostra.count(";") > amostra.count(",") else ","
            yield os.path.basename(caminho), list(csv.reader(f, delimiter=sep))
        return
    if ext == ".xls":
        sys.exit("Formato .xls: converta para .xlsx (soffice --headless --convert-to xlsx arquivo.xls).")
    from openpyxl import load_workbook

    wb = load_workbook(caminho, read_only=True, data_only=True)
    for ws in wb.worksheets:
        if aba and norm(ws.title) != norm(aba):
            continue
        yield ws.title, [list(r) for r in ws.iter_rows(values_only=True)]


def detectar(linhas, uf=None, forc=None):
    """Retorna (linha_cab, {codigo, descricao, unidade, preco}) ou None."""
    forc = forc or {}
    melhor = None
    for i, row in enumerate(linhas[:40]):
        cab = [norm(c) for c in row]
        cols = {}
        for j, h in enumerate(cab):
            if not h:
                continue
            if "codigo" not in cols and (h.startswith("codigo") or h in ("cod", "cod.", "item") or h.startswith("cod ")):
                cols["codigo"] = j
            elif "descricao" not in cols and h.startswith("descri"):
                cols["descricao"] = j
            elif "unidade" not in cols and (h.startswith("unid") or h in ("un", "un.", "und")):
                cols["unidade"] = j
        # preço
        if uf:
            for j, h in enumerate(cab):
                if h == uf.lower() or h.endswith(f" {uf.lower()}") or h.startswith(f"{uf.lower()} "):
                    cols["preco"] = j
                    break
        if "preco" not in cols:
            prefer = ["custo total", "preco unitario", "custo unitario", "preco total", "valor unitario", "preco", "custo", "valor", "total"]
            for p in prefer:
                for j, h in enumerate(cab):
                    if h.startswith(p) and j not in cols.values():
                        cols["preco"] = j
                        break
                if "preco" in cols:
                    break
        for k, nome in forc.items():
            if nome is None:
                continue
            for j, h in enumerate(cab):
                if h == norm(nome):
                    cols[k] = j
        score = len([k for k in ("codigo", "descricao", "unidade", "preco") if k in cols])
        if "descricao" in cols and score >= 3 and (melhor is None or score > melhor[2]):
            melhor = (i, cols, score)
    if not melhor:
        # formato com UFs numa linha de sub-cabeçalho: procura a sigla da UF nas linhas próximas
        return None
    i, cols, _ = melhor
    if uf and "preco" in cols and norm(linhas[i][cols["preco"]]) != uf.lower():
        # tenta sub-cabeçalho logo abaixo/acima com as siglas
        for k in (i + 1, i - 1, i + 2):
            if 0 <= k < len(linhas):
                sub = [norm(c) for c in linhas[k]]
                if uf.lower() in sub:
                    cols["preco"] = sub.index(uf.lower())
                    break
    return i, cols


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivo")
    ap.add_argument("termos", nargs="?", default="", help="palavras que devem aparecer na descrição")
    ap.add_argument("--codigo")
    ap.add_argument("--uf")
    ap.add_argument("--aba")
    ap.add_argument("--limite", type=int, default=15)
    ap.add_argument("--diagnostico", action="store_true")
    ap.add_argument("--col-codigo")
    ap.add_argument("--col-descricao")
    ap.add_argument("--col-unidade")
    ap.add_argument("--col-preco")
    a = ap.parse_args()
    if a.uf and a.uf.upper() not in UFS:
        sys.exit(f"UF inválida: {a.uf}")
    forc = {"codigo": a.col_codigo, "descricao": a.col_descricao, "unidade": a.col_unidade, "preco": a.col_preco}
    termos = [norm(t) for t in a.termos.split() if t.strip()]
    if not termos and not a.codigo and not a.diagnostico:
        sys.exit("Informe termos de busca, --codigo ou --diagnostico.")

    achados = []
    aviso_uf = False
    for nome, linhas in ler_abas(a.arquivo, a.aba):
        det = detectar(linhas, a.uf, forc)
        if det and not a.uf and "preco" not in det[1]:
            cab = {norm(c).upper() for c in linhas[det[0]] if c}
            if cab & set(UFS):
                aviso_uf = True
        if a.diagnostico:
            print(f"\n[Aba] {nome} — {len(linhas)} linhas")
            if not det:
                print("  cabeçalho não detectado. Primeiras linhas:")
                for r in linhas[:8]:
                    print("   ", [c for c in r if c not in (None, "")][:10])
                continue
            i, cols = det
            print(f"  cabeçalho na linha {i + 1}:")
            for k, j in cols.items():
                print(f"    {k:<10} -> coluna {j + 1}: {linhas[i][j]!r}")
            for r in linhas[i + 1:i + 4]:
                print("    ex.:", [r[j] if j < len(r) else None for j in cols.values()])
            continue
        if not det:
            continue
        i, cols = det
        jc, jd, ju, jp = (cols.get(k) for k in ("codigo", "descricao", "unidade", "preco"))
        for r in linhas[i + 1:]:
            if jd is None or jd >= len(r) or not r[jd]:
                continue
            desc = str(r[jd])
            cod = str(r[jc]).strip() if jc is not None and jc < len(r) and r[jc] is not None else ""
            if cod.endswith(".0"):
                cod = cod[:-2]
            if a.codigo:
                if cod != str(a.codigo).strip():
                    continue
            else:
                nd = norm(desc)
                if not all(t in nd for t in termos):
                    continue
            un = r[ju] if ju is not None and ju < len(r) else ""
            pr = num(r[jp]) if jp is not None and jp < len(r) else None
            achados.append((nome, cod, desc, un or "", pr))
    if aviso_uf:
        print("Atenção: a tabela tem preços em colunas por UF — repita a busca com --uf <sigla> para ver os preços.\n")
    if a.diagnostico:
        return
    if not achados:
        print("Nenhum resultado. Tente menos palavras, sinônimos (ex.: 'bloco ceramico' / 'tijolo'), ou --diagnostico.")
        return
    achados.sort(key=lambda x: len(x[2]))
    print(f"{len(achados)} resultado(s){' — mostrando ' + str(a.limite) if len(achados) > a.limite else ''}\n")
    for nome, cod, desc, un, pr in achados[: a.limite]:
        ps = "sem preço" if pr is None else f"R$ {pr:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"[{nome}] {cod} | {un} | {ps}\n    {desc}\n")


if __name__ == "__main__":
    main()
