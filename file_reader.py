class FileReader():
    def __init__(self, file_path):
        self.file_path = file_path
        

    def read_dict_from_txt(self):
        """Lee un archivo de texto y devuelve un diccionario."""
        dictionary = {}
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if ':' in line:
                    key, value = line.split(':', 1)
                    dictionary[key.strip().lower()] = value.strip()
        return dictionary