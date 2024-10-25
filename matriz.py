class Matriz:
    """Clase para gestionar la creación y manipulación de la matriz del crucigrama."""

    def __init__(self, N):
        self.matriz = [['.' for _ in range(N)] for _ in range(N)]

    def imprimir(self):
        """Muestra la matriz de forma organizada."""
        borde_superior = "+" + "-" * (2 * len(self.matriz[0]) - 1) + "+"
        print(borde_superior)

        for fila in self.matriz:
            print("| " + " ".join(fila) + " |")
        print(borde_superior)

    def colocar_palabra(self, palabra, fila, col, orientacion):
        """Coloca una palabra en la matriz."""
        for i in range(len(palabra)):
            if orientacion == 'H':
                self.matriz[fila][col + i] = palabra[i]
            elif orientacion == 'V':
                self.matriz[fila + i][col] = palabra[i]

    def se_puede_colocar(self, palabra, fila, col, orientacion):
        """Verifica si se puede colocar una palabra en una posición específica."""
        longitud = len(palabra)

        if orientacion == 'H':
            if col + longitud > len(self.matriz[0]):
                return False
            if col > 0 and self.matriz[fila][col - 1] != '.':
                return False
            if col + longitud < len(self.matriz[0]) and self.matriz[fila][col + longitud] != '.':
                return False

            return all(self.matriz[fila][col + i] in ['.', palabra[i]] for i in range(longitud))

        elif orientacion == 'V':
            if fila + longitud > len(self.matriz):
                return False
            if fila > 0 and self.matriz[fila - 1][col] != '.':
                return False
            if fila + longitud < len(self.matriz) and self.matriz[fila + longitud][col] != '.':
                return False

            return all(self.matriz[fila + i][col] in ['.', palabra[i]] for i in range(longitud))
