class Biblioteca:
    def __init__(self):  
        self.libros = {}
        self.lecturas_usuario = {}

    def agregar_libro(self, titulo, autor, cantidad, tematica): #Agregar libros con título, autor, cantidad disponible y temática
        self.libros[titulo] = {"autor": autor, "cantidad": cantidad, "tematica": tematica}

    def prestar_libro(self, usuario, titulo):  #Prestar un libro a un usuario reduciendo su cantidad disponible
        if titulo in self.libros and self.libros[titulo]["cantidad"] > 0: #Comprueba si el libro está disponible
            self.libros[titulo]["cantidad"] -= 1
            self.lecturas_usuario.setdefault(usuario, []).append(titulo)
            print(f"Libro '{titulo}' prestado a {usuario}.")
        else:
            print(f"Lo siento, el libro '{titulo}' no está disponible.")

    def devolver_libro(self, usuario, titulo): #Usuario devuelve un libro aumentando su disponibilidad
        if titulo in self.libros:
            self.libros[titulo]["cantidad"] += 1
            print(f"Libro '{titulo}' devuelto por {usuario}.")
        else:
            print(f"El libro '{titulo}' no pertenece a esta biblioteca.")

    def sugerir_libro(self, usuario): #Suigiere libros al usuario en función de las temáticas leidas previamente
        if usuario in self.lecturas_usuario and self.lecturas_usuario[usuario]:
            ultima_lectura = self.lecturas_usuario[usuario][-1]
            tematica = self.libros.get(ultima_lectura, {}).get("tematica")
            if tematica:
                for libro, detalles in self.libros.items():
                    if detalles["tematica"] == tematica and libro not in self.lecturas_usuario[usuario]:
                        return f"Sugerencia para {usuario}: '{libro}' de {detalles['autor']}"
        return "No hay sugerencias disponibles en este momento."

    def organizar_por_tematica(self):   #Crea un diccionario con los libros organizados por temática
        tematicas = {}
        for titulo, detalles in self.libros.items():
            tematica = detalles["tematica"]
            tematicas.setdefault(tematica, []).append(titulo)
        return tematicas

