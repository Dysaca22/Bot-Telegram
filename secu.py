def Sec(secuencia,sec_t):
  i = 0
  j = i + 1
  k = 2
  while i < (len(secuencia)-1):
    sw = False
    valor = secuencia[i] + secuencia[j]
    k = j+1
    while k < len(secuencia):
      if valor == secuencia[k]:
        if i == 0:
          sec_t.append(secuencia[i])
          sec_t.append(secuencia[j])
        sec_t.append(secuencia[k])
        i = j;j = k
        sw = True
        break
      k = k+1
    if sw == False:
      break
  return sec_t

def mainSecuancia(secu):
    tam = 0
    resp = []
    while (not secu == 0) and tam < len(secu):
      sec_t = []
      sec_t = Sec(secu, sec_t)
      if tam < len(sec_t):
        tam = len(sec_t)
        resp = sec_t
      secu.pop(0)
    return resp