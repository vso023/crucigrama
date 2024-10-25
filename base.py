import random

def crear_matriz(N):
    """Crear una matriz"""
    return [['.' for _ in range(N)] for _ in range(N)]

def se_puede_colocar(matriz, palabra, fila, col, orientacion):
    """Verifica si la palabra cabe"""
    longitud = len(palabra)

    if orientacion == 'H':
        if col + longitud > len(matriz[0]):
            return False    
        if col > 0 and matriz[fila][col - 1] != ' ':
            return False
        if col + longitud < len(matriz[0]) and matriz[fila][col + longitud] != ' ':
            return False

        return all(matriz[fila][col + i] in ['.', palabra[i]] for i in range(longitud))

    elif orientacion == 'V':
        if fila + longitud > len(matriz):
            return False
        if fila > 0 and matriz[fila - 1][col] != ' ':
            return False
        if fila + longitud < len(matriz) and matriz[fila + longitud][col] != ' ':
            return False

        return all(matriz[fila + i][col] in ['.', palabra[i]] for i in range(longitud))

def colocar_palabra_en_posicion(matriz, palabra, fila, col, orientacion):
    """Coloca la palabra en la matriz."""
    for i in range(len(palabra)):
        if orientacion == 'H':
            matriz[fila][col + i] = palabra[i]
        elif orientacion == 'V':
            matriz[fila + i][col] = palabra[i]

def encontrar_posiciones_conectadas(matriz, palabra):
    """Busca posiciones donde la palabra pueda conectarse sin conflictos."""
    N = len(matriz)
    posiciones_validas = []

    for i in range(N):
        for j in range(N):
            if matriz[i][j] in palabra:
                letra = matriz[i][j]
                indices = [pos for pos, char in enumerate(palabra) if char == letra]

                for idx in indices:
                    if se_puede_colocar(matriz, palabra, i - idx, j, 'V'):
                        posiciones_validas.append((i - idx, j, 'V'))
                    if se_puede_colocar(matriz, palabra, i, j - idx, 'H'):
                        posiciones_validas.append((i, j - idx, 'H'))

    return posiciones_validas

def colocar_palabra_conectada(matriz, palabra):
    """Intenta colocar la palabra conectada con otra ya existente."""
    posiciones = encontrar_posiciones_conectadas(matriz, palabra)
    if posiciones:
        fila, col, orientacion = random.choice(posiciones)
        colocar_palabra_en_posicion(matriz, palabra, fila, col, orientacion)
        return True
    return False

def generar_crucigrama(matriz, palabras):
    """Genera el crucigrama colocando todas las palabras."""
    primera_palabra = palabras.pop(0)
    fila_central = len(matriz) // 2
    col_central = len(matriz[0]) // 2 - len(primera_palabra) // 2
    colocar_palabra_en_posicion(matriz, primera_palabra, fila_central, col_central, 'H')

    for palabra in palabras:
        intentos = 3
        while intentos > 0 and not colocar_palabra_conectada(matriz, palabra):
            intentos -= 1
        if intentos == 0:
            print(f"No se pudo colocar la palabra: {palabra}")

    print("\nCrucigrama generado:")
    imprimir_crucigrama(matriz)

def imprimir_crucigrama(matriz):
    """Muestra la matriz de forma organizada."""
    borde_superior = "+" + "-" * (2 * len(matriz[0]) - 1) + "+"
    print(borde_superior)    
    
    for fila in matriz:
        print("| " + " ".join(fila) + " |")
    print(borde_superior)

def read_dict_from_txt(file_path):
    """Lee un archivo de texto y devuelve un diccionario."""
    dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if ':' in line:
                key, value = line.split(':', 1)
                dictionary[key.strip().lower()] = value.strip()
    return dictionary

def select_random_words(dictionary, amount):
    """Selecciona palabras aleatorias del diccionario."""
    word_list = list(dictionary.items())
    selected = random.sample(word_list, amount)
    return selected  

def mostrar_significados(palabras_seleccionadas):
    """Muestra los significados de las palabras seleccionadas."""
    print("\nSignificados de las palabras:\n")
    for palabra, significado in palabras_seleccionadas:
        print(f"{palabra}: {significado}")

if __name__ == "__main__":
    file_path = 'crucigrama.txt'
    dictionary = read_dict_from_txt(file_path)

    word_count = 10
    selected_words = select_random_words(dictionary, word_count)

    # Extraemos solo las palabras para el crucigrama.
    palabras_para_crucigrama = [word for word, _ in selected_words]

    max_length = max(len(word) for word in palabras_para_crucigrama)
    N = max(20, max_length + 5)
    matriz = crear_matriz(N)

    generar_crucigrama(matriz, palabras_para_crucigrama)

    # Mostramos los significados después de generar el crucigrama.
    mostrar_significados(selected_words)
