def sol1():
    with open('input', 'r') as f:
        lineas = f.readlines()
    horizontal = 0
    vertical = 0
    for linea in lineas:
        movimiento = linea.split(' ')[0]
        cantidad = int(linea.split(' ')[1])
        if movimiento == 'forward':
            horizontal += cantidad
        if movimiento == 'up':
            vertical -= cantidad
        if movimiento == 'down':
            vertical += cantidad
    print(horizontal * vertical)


def sol2():
    with open('input', 'r') as f:
        lineas = f.readlines()
    horizontal = 0
    vertical = 0
    aim = 0
    for linea in lineas:
        movimiento = linea.split(' ')[0]
        cantidad = int(linea.split(' ')[1])
        if movimiento == 'forward':
            horizontal += cantidad
            vertical += (aim * cantidad)
        if movimiento == 'up':
            #vertical -= cantidad
            aim -= cantidad
        if movimiento == 'down':
            #vertical += cantidad
            aim += cantidad
    print(horizontal * vertical)


if __name__ == "__main__":
    sol1()
    sol2()
