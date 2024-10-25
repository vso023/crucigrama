import random

class Utilidades:

    @staticmethod
    def select_random_words(dictionary, amount):
        """Selecciona palabras aleatorias del diccionario."""
        word_list = list(dictionary.items())
        return random.sample(word_list, amount)

    @staticmethod
    def mostrar_significados(palabras_seleccionadas):
        """Muestra los significados de las palabras seleccionadas."""
        print("\nSignificados de las palabras:\n")
        for palabra, significado in palabras_seleccionadas:
            print(f"{palabra}: {significado}")
