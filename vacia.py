def encontrar_ficha_vacia(images):
    for i, image in enumerate(images):
        if image is None:
            return i
    return -1

def mover_ficha_vacia(images, direccion):
    fila, col = encontrar_ficha_vacia(images) // 3, encontrar_ficha_vacia(images) % 3
    nueva_posicion = -1
    if direccion == "up" and fila > 0:
        nueva_posicion = encontrar_ficha_vacia(images) - 3
    elif direccion == "down" and fila < 2:
        nueva_posicion = encontrar_ficha_vacia(images) + 3
    elif direccion == "left" and col > 0:
        nueva_posicion = encontrar_ficha_vacia(images) - 1
    elif direccion == "right" and col < 2:
        nueva_posicion = encontrar_ficha_vacia(images) + 1
    
    if nueva_posicion != -1:
        images[encontrar_ficha_vacia(images)], images[nueva_posicion] = images[nueva_posicion], images[encontrar_ficha_vacia(images)]
