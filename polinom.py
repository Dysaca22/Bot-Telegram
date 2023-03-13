import numpy as np
import sympy as sp
from fractions import Fraction as frac


def mainPolinomio(coeficientes, iniciales):
    n = sp.Symbol('n')
    c = sp.Symbol('c')
    sol = ""

    coef = np.array(coeficientes)
    R = np.roots(coef).real

    text = ""
    cont = 0
    for i in range(len(R)):
        if i >= 1:
            if R[i] == R[i - 1]:
                cont += 1
            else:
                cont = 0
        fracPar = str(frac(R[i]).limit_denominator()).split("/")
        if len(fracPar) == 2:
            fracc = "\\frac{" + str(fracPar[0]) + "}{" + str(fracPar[1]) + "}"
        else:
            fracc = str(round(R[i], 3))
        text += str(c * (n**cont)) + "*(" + fracc + ")**n"
        if i < len(R) - 1:
            text += "+"
    resp = ""
    cont = 1
    for i in range(len(text) - 1):
        if text[i:i + 1] == 'c' and not text[i - 1:i] == 'a':
            resp += text[i:i + 1] + "_" + str(cont)
            cont += 1
        else:
            resp += text[i:i + 1]
    resp += text[-1]
    formula = resp.replace("\\frac{", "").replace("}{", "/").replace("}", "")
    f = []
    for i in range(len(iniciales)):
        s = formula.replace("n", str(i))
        par = s.split("+")

        a = []
        for j in range(len(par)):
            index = par[j].index('*')
            t = par[j][index + 1: len(par[j])].strip()
            a.append(eval(t))
        f.append(a)

    val1 = np.array(f)
    val2 = np.array(iniciales)
    constantes = np.linalg.solve(val1, val2).real
    cons = []
    for i in range(len(constantes)):
        cons.append(str(frac(constantes[i]).limit_denominator()))
    respuesta = ""
    cont = 0
    text = text.replace("\\frac{", "").replace("}{", "/").replace("}", "")
    for i in range(len(text) - 1):
        if text[i:i + 1] == 'c':
            respuesta += str(cons[cont])
            cont += 1
        else:
            respuesta += str(text[i])
    respuesta += text[-1]
    respuesta = eval(respuesta)
    partesResp = str(respuesta).replace("**", "^").split("^n")

    try:
        partesResp.remove("")
    except Exception as e:
        print("No se elimini algun espacio")

    pr = ""
    for p in range(len(partesResp)):
        partes = str(partesResp[p]).strip().split("*")
        r = []
        if partesResp[p] == "":
            continue
        if len(partes) == 2 and partes[1] == "n":
            pr += " \\cdot " + partes[1]
            if p != len(partesResp) - 1:
                pr += "+"
            continue
        for i in range(len(partes)):
            t = partes[i].replace("(","").replace(")","")
            r.append("(" + str(frac(eval(t)).limit_denominator()) + ")")
        respuesta = ""
        for i in range(len(r)):
            if not i == len(r) - 1:
                respuesta += r[i] + " \\cdot "
            else:
                respuesta += r[i]
        if p != len(partesResp) - 1:
            if partesResp[p + 1][0:2] != "*n":
                pr += respuesta + "^n +"
            else:
                pr += respuesta + "^n"
        else:
            pr += respuesta + "^n"

    parParenFracA = pr.split("(")
    for i in parParenFracA:
        parParenFracD = i.split(")")
        for j in range(len(parParenFracD)):
            if parParenFracD[j].find("/") >= 0:
                index =  parParenFracD[j].find("/")
                parParenFracD[j] = "\\frac{" + str(parParenFracD[j][0: index]) + "}{" + str(parParenFracD[j][index + 1:len(parParenFracD[j])]) + "}"
                sol += "\\left(" + parParenFracD[j] +"\\right)"
            else:
                sol += parParenFracD[j]
    return resp.replace("**", "^").replace("*", " \\cdot ").replace("(", "\\left(").replace(")", "\\right)"), sol