import tkinter as tk
from tkinter import messagebox, filedialog
from file_reader import FileReader
from utilidades import Utilidades
from matriz import Matriz
from crucigrama import Crucigrama


class Interfaz:
    """Clase que gestiona la interfaz gráfica del crucigrama."""

    def __init__(self, master):
        self.master = master
        self.master.title("Generador de Crucigramas")
        self.master.geometry("600x600")

        self.load_button = tk.Button(master, text="Subir archivo", command=self.cargar_diccionario)
        self.load_button.pack(pady=10)

        self.generate_button = tk.Button(master, text="Generar Crucigrama", command=self.generar_crucigrama, state=tk.DISABLED)
        self.generate_button.pack(pady=10)

        self.text_area = tk.Text(master, wrap=tk.WORD, width=50, height=35)
        self.text_area.pack(pady=10)

        self.meaning_area = tk.Text(master, wrap=tk.WORD, width=50, height=35)
        self.meaning_area.pack(pady=10)

        self.file_path = ''
        self.selected_words = []

    def cargar_diccionario(self):
        self.file_path = filedialog.askopenfilename(title="Seleccionar archivo de diccionario",
                                                     filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
        if self.file_path:
            self.generate_button.config(state=tk.NORMAL)
            messagebox.showinfo("Éxito", "Se subio el archivo")

    def generar_crucigrama(self):
        dictionary = FileReader(self.file_path).read_dict_from_txt()
        word_count = 10
        self.selected_words = Utilidades.select_random_words(dictionary, word_count)

        palabras_para_crucigrama = [word for word, _ in self.selected_words]

        max_length = max(len(word) for word in palabras_para_crucigrama)
        N = max(20, max_length + 5)

        crucigrama = Crucigrama(N)
        crucigrama.generar(palabras_para_crucigrama)

        self.mostrar_crucigrama(crucigrama)
        self.mostrar_significados()

    def mostrar_crucigrama(self, crucigrama):
        self.text_area.delete(1.0, tk.END)  
        self.text_area.insert(tk.END, "\n".join(" ".join(fila) for fila in crucigrama.matriz.matriz))

    def mostrar_significados(self):
        self.meaning_area.delete(1.0, tk.END)  
        for palabra, significado in self.selected_words:
            self.meaning_area.insert(tk.END, f"{palabra}: {significado}\n") 


if __name__ == "__main__":
    root = tk.Tk()
    gui = Interfaz(root)
    root.mainloop()
