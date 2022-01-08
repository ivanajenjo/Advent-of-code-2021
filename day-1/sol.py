def sol1():
    with open('input', 'r') as f:
        lineas = f.readlines()
    contador = 0
    valor_anterior = float("inf")
    for linea in lineas:
        if int(linea) > valor_anterior:
            contador += 1
        valor_anterior = int(linea)
    print(contador)


def sol2():
    with open('input', 'r') as f:
        lineas = f.readlines()
    contador = 0
    valor_anterior = float("inf")
    for i in range(len(lineas)-2):
        calculo_valor = (int(lineas[i]) + int(lineas[i+1]) + int(lineas[i+2]))
        if calculo_valor > valor_anterior:
            contador += 1
        valor_anterior = calculo_valor
    print(contador)


if __name__ == "__main__":
    sol1()
    sol2()
