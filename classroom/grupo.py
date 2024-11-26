from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"


    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        if asignaturas is None:
            asignaturas = []
        if estudiantes is None:
            estudiantes = []
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        self._imprimir_grado = False

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x, "remoto"))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        if self._imprimir_grado:
            return f"Grupo de estudiantes: {self._grupo}\nGrado {self.grado}"
        else:
            return f"Grupo de estudiantes: {self._grupo}"