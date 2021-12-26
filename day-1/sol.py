def sol1():
    with open('input', 'r') as f:
        lineas = f.readlines()
    contador = 0
    valor_anterior = 10000
    for linea in lineas:
        if int(linea) > valor_anterior:
            contador += 1
        valor_anterior = int(linea)
    print(contador)


if __name__ == "__main__":
    sol1()