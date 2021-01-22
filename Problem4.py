maiorMultContrario = 0
for num1 in range(999, 100, -1):
    for num2 in range(999,100, -1):
        mult = str(num1 * num2)
        multAoContrario = ''
        for i in range(len(mult)-1, -1, -1):
            multAoContrario += mult[i]
        if mult == multAoContrario:
            mult = int(mult)
            if  mult> maiorMultContrario:
                maiorMultContrario = mult

print(maiorMultContrario)
