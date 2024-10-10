
class Alumno:
    #Crear una funcion conturctor con atributos vacios
    def __init__(self):
        # Atributos privados
        self.__nombre = ""
        self.__apellido_paterno = ""
        self.__apellido_materno = ""
        self.__no_control = ""
        self.__semestre = ""

    # Métodos para establecer los valores (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener los valores (getters)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre
    def get_nombrecom(self):
        return self.__nombre + " " + self.__apellido_paterno + " " + self.__apellido_materno

registro_alumnos = {}

#Capturar 3 registros
for i in range(3):
    alumno1 = Alumno()
    alumno1.set_nombre(input(f"Ingrese el nombre del alumno {i+1}: "))
    alumno1.set_apellido_paterno(input(f"Ingrese el apellido paterno del alumno {i+1}: "))
    alumno1.set_apellido_materno(input(f"Ingrese el apellido materno del alumno {i+1}: "))
    alumno1.set_no_control(input(f"Ingrese el número de control del alumno {i+1}: "))
    alumno1.set_semestre(input(f"Ingrese el semestre del alumno {i+1}: "))
    print()

    registro_alumnos[f"alumno1_{i + 1}"] = alumno1

#Mostrar los nombres de los registros
for i in range(3):
    alumno1 = registro_alumnos[f"alumno1_{i + 1}"]
    print(f"Alumno {i + 1}: ")
    print(f"Nombre Completo: {alumno1.get_nombrecom()}")




# Crear instancia de alumno
#Una instancia es la creacion de un objeto a partir de una clase
#alumno1 = Alumno("David", "Jahuey", "Hernandez", "12345678", 5)

# Obtener los valores
#print("Nombre: " + alumno1.get_nombre())             # Juan
#print("Apellido Paterno: " + alumno1.get_apellido_paterno())   # Pérez
#print("Apellido Materno: " + alumno1.get_apellido_materno())   # Gómez
#print("No. de Control:" + alumno1.get_no_control())         # 12345678
#print(alumno1.get_semestre())           # 5

#print("Nombre Completo: " + alumno1.get_nombrecom())