from colorama import init, Fore,Style

class Carrera:
    _carrera = ""
    def __init__(self, nombre):
        self.carrera = nombre
        Carrera._carrera = self.carrera

    def mostrarCarrera(self):
        return "Carrera: {}".format(self.carrera)


class Curso:
    def __init__(self, paralelo, seccion):
        self.paralelo = paralelo
        self.seccion = seccion

    def mostrarCurso(self):
        return "Paralelo: {}\nSección: {}".format(self.paralelo, self.seccion)
        
class Semestre(Carrera):
    _semestre = " "
    def __init__(self, carrera, nivel):
        super().__init__(carrera)
        self.nivel_semestre = nivel
        Semestre._semestre = self.nivel_semestre
        
    def mostrarSemestre(self):
        return "Carrera: {}\nSemestre: {}".format(self.carrera, self.nivel_semestre)


class Estudiante:
    def __init__(self, nombres, apellidos, cedula, matricula, asistencias):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.matricula = matricula 
        self.asistencias = asistencias
    
    def mostrarEstudiante(self):
        print("           Nombre                      Cedula              Matricula      Asistencia")
        return " {} {}      {}             {}          {}%".format(self.nombres, self.apellidos, self.cedula, "Activa" if self.matricula else "Pendiente", self.asistencias)


class Profesor:
    def __init__(self, nombres, apellidos):
        self.nombres = nombres
        self.apellidos = apellidos
        
    def mostrarProfesor(self):
        return "Profesor: {} {}".format(self.nombres, self.apellidos)
        
class Asignatura:
    def __init__(self, nombre, inicio, fin):
        self.nombre_asignatura = nombre
        self.fecha_inicio = inicio
        self.fecha_fin = fin
    
    def mostrarAsignatura(self):
        return "Asignatura: {}\nFecha inicio: {}\nFecha fin: {}".format(self.nombre_asignatura, self.fecha_fin, self.fecha_fin)
        
class Calificaciones:
    def __init__(self, n1, n2, ex1, n3, n4, ex2, re, estudiante):
        self.n1 = n1
        self.n2 = n2
        self.ex1 = ex1
        self.n3 = n3
        self.n4 = n4
        self.ex2 = ex2
        self.recuperacion = re
        self.estudiante = estudiante
        
        
    def calcularCalificaciones(self):
        if self.recuperacion == 0:
            nota_total = self.n1 + self.n2 + self.n3 + self.n4 + self.ex1 + self.ex2
        else:
            nota_total = round( ((self.n1 + self.n2 + self.n3 + self.n4 + self.ex1 + self.ex2 + self.recuperacion) / 2), 2)

        return nota_total
    init()
    def actaCalificaciones(self):
        
        nota_final = Calificaciones.calcularCalificaciones(self)
        
        if nota_final >= 70 and self.estudiante.asistencias >= 70 and self.estudiante.matricula:
            estado =   "Aprobado"
            color_estado = Fore.GREEN +  estado
            print(Style.RESET_ALL)
        else:
            estado = "Reprobado"
            color_estado = Fore.RED + estado
            print(Style.RESET_ALL)

        print("*" * 100)
        print("                                      Estudiante")
        print(" ")
        print(" ")
        print(self.estudiante.mostrarEstudiante())
        print(" ")
        print(" ")
        print("                                     Calificaciones")
        print(" ")
        print(" ")
        print("_" * 100)
        print("N1: {:5} | N2: {:5} | EX1: {:5} | N3: {:5} | N4: {:5} | EX2: {:5} | RE: {:5} | TOTAL: {:5}".format(self.n1, self.n2, self.ex1, self.n3, self.n4, self.ex2, self.recuperacion, nota_final))
        print(" " * 100)

        print("Estado: ", color_estado)
        print(Style.RESET_ALL)
        print("*" * 100)


class detalleCalificaciones:
        def __init__(self, profesor, curso, asignatura):
            self.profesor = profesor
            self.curso = curso
            self.asignatura = asignatura

        def cabeceraCalificaciones(self):
            print("*"*100)
            print("Carrera: {}".format(Carrera._carrera))
            print("Semestre: {}".format(Semestre._semestre))
            print(self.profesor.mostrarProfesor())
            print(self.curso.mostrarCurso())
            print(self.asignatura.mostrarAsignatura())
            print("*"*100)


if __name__ == "__main__":
    
    carr = Carrera("Ingeneria en Software")
    se = Semestre(carr.carrera, "1er nivel")
    prof = Profesor("Daniel", "Vera")
    asig = Asignatura("Algoritmo y programación", "12/12/12", "12/12/12")
    cur = Curso("A1", "Vespertino")
    cab = detalleCalificaciones(prof, cur, asig)
    cab.cabeceraCalificaciones()
    
    est = Estudiante("Willian Alexander", "Macias Almeida", "0941498941", True, 80)
    calif = Calificaciones(15, 15, 20, 15, 15, 20, 0, est)
    calif.actaCalificaciones()
    
    est = Estudiante("Wilmer Samuel", "Briones Garrido", "0941498941", True, 70)
    calif = Calificaciones(15, 15, 20, 15, 15, 19, 0, est)
    calif.actaCalificaciones()
    
    est = Estudiante("Fiorella Nicole", "Franco Alvarez", "0941498941", False, 100)
    calif = Calificaciones(15, 15, 10, 15, 15, 10, 0, est)
    calif.actaCalificaciones()