import random
from matriz import Matriz

class Crucigrama:
    """Clase que gestiona la generación del crucigrama."""

    def __init__(self, N):
        self.matriz = Matriz(N)

    def encontrar_posiciones_conectadas(self, palabra):
        """Busca posiciones donde la palabra pueda conectarse sin conflictos."""
        N = len(self.matriz.matriz)
        posiciones_validas = []

        for i in range(N):
            for j in range(N):
                if self.matriz.matriz[i][j] in palabra:
                    letra = self.matriz.matriz[i][j]
                    indices = [pos for pos, char in enumerate(palabra) if char == letra]

                    for idx in indices:
                        if self.matriz.se_puede_colocar(palabra, i - idx, j, 'V'):
                            posiciones_validas.append((i - idx, j, 'V'))
                        if self.matriz.se_puede_colocar(palabra, i, j - idx, 'H'):
                            posiciones_validas.append((i, j - idx, 'H'))

        return posiciones_validas

    def colocar_palabra_conectada(self, palabra):
        """Intenta colocar la palabra conectada con otra ya existente."""
        posiciones = self.encontrar_posiciones_conectadas(palabra)
        if posiciones:
            fila, col, orientacion = random.choice(posiciones)
            self.matriz.colocar_palabra(palabra, fila, col, orientacion)
            return True
        return False

    def generar(self, palabras):
        """Genera el crucigrama colocando todas las palabras."""
        primera_palabra = palabras.pop(0)
        fila_central = len(self.matriz.matriz) // 2
        col_central = len(self.matriz.matriz[0]) // 2 - len(primera_palabra) // 2
        self.matriz.colocar_palabra(primera_palabra, fila_central, col_central, 'H')

        for palabra in palabras:
            intentos = 3
            while intentos > 0 and not self.colocar_palabra_conectada(palabra):
                intentos -= 1
            if intentos == 0:
                print(f"No se pudo colocar la palabra: {palabra}")

        print("\nCrucigrama generado:")
        self.matriz.imprimir()
