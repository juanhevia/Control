#El código permite agregar libros con autor, temática, cantidad disponible y temática del libro. 
#Que un usuario haga un préstamo o que devuelva un libro, aumentando y disminuyendo su cantidad disponible.
#Devuelve una sugerencia para la próxima lectura del usuario en función de su historial de préstamos.
#Organiza los libros agregados en función de su temática y de ahí toma las sugerencias.

#Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.agregar_libro("Dune", "Frank Herbert", 3, "ciencia-ficción")
biblioteca.agregar_libro("It", "Stephen King", 2, "terror")
biblioteca.agregar_libro("El Hobbit", "J.R.R. Tolkien", 4, "fantasía")
biblioteca.agregar_libro("1984", "George Orwell", 5, "ciencia-ficción")
biblioteca.agregar_libro("Drácula", "Bram Stoker", 3, "terror")
biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez", 4, "realismo mágico")
biblioteca.agregar_libro("Fundación", "Isaac Asimov", 6, "ciencia-ficción")
biblioteca.agregar_libro("Frankenstein", "Mary Shelley", 2, "terror")
biblioteca.agregar_libro("Los miserables", "Victor Hugo", 3, "drama")
biblioteca.agregar_libro("El nombre del viento", "Patrick Rothfuss", 5, "fantasía")

biblioteca.prestar_libro("Juan", "Dune")
biblioteca.prestar_libro("Juan", "It")
print(biblioteca.sugerir_libro("Juan"))

print(biblioteca.organizar_por_tematica())
