from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        if asignaturas is None:
            asignaturas = []
        if estudiantes is None:
            estudiantes = []
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, *args):
        for x in args:
            self._asignaturas.append(Asignatura(x, "Remoto"))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    @classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @classmethod
    def asignarNombre(cls, nombre="Grado 12"):
        cls.grado = nombre

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}\nGrado {self.grado}\n{self.listadoAlumnos}"

