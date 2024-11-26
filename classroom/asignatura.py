class Asignatura:

    def __init__(self, nombre, salon):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        
        return f"Asignatura: {self._nombre}, Salón: {self._salon}"
