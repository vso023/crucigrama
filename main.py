from file_reader import FileReader
from utilidades import Utilidades
from matriz import Matriz
from crucigrama import Crucigrama

file_path = 'crucigrama.txt'
dictionary = FileReader(file_path).read_dict_from_txt()

word_count = 10
selected_words = Utilidades.select_random_words(dictionary, word_count)


palabras_para_crucigrama = [word for word, _ in selected_words]

max_length = max(len(word) for word in palabras_para_crucigrama)
N = max(20, max_length + 5)


matriz = Matriz(N)

crucigrama = Crucigrama(N)


crucigrama.generar(palabras_para_crucigrama)


Utilidades.mostrar_significados(selected_words)
