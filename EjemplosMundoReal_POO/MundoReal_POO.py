# 📚 Ejemplo 1: Sistema de Biblioteca
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

class Miembro:
    def __init__(self, nombre):
        self.nombre = nombre

    def pedir_libro(self, libro):
        libro.prestar()

    def devolver_libro(self, libro):
        libro.devolver()

# Ejecución del Sistema de Biblioteca
libro1 = Libro("El Quijote", "Cervantes")
miembro1 = Miembro("Ana")
miembro1.pedir_libro(libro1)
miembro1.devolver_libro(libro1)

# 🏨 Ejemplo 2: Sistema de Reservas de Hotel
class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.disponible = True

    def ocupar(self):
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} ocupada.")
        else:
            print(f"Habitación {self.numero} ya está ocupada.")

    def liberar(self):
        self.disponible = True
        print(f"Habitación {self.numero} liberada.")

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_reserva(self, habitacion):
        habitacion.ocupar()

    def cancelar_reserva(self, habitacion):
        habitacion.liberar()

# Ejecución del Sistema de Reservas de Hotel
habitacion1 = Habitacion(101, "Doble")
cliente1 = Cliente("Carlos")
cliente1.hacer_reserva(habitacion1)
cliente1.cancelar_reserva(habitacion1)

# 🛒 Ejemplo 3: Tienda en Línea
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.stock = 0

    def agregar_stock(self, cantidad):
        self.stock += cantidad
        print(f"Se agregaron {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")

    def vender(self):
        if self.stock > 0:
            self.stock -= 1
            print(f"Se vendió una unidad de {self.nombre}. Stock restante: {self.stock}")
        else:
            print(f"No hay stock de {self.nombre} disponible.")

# Ejecución de la Tienda en Línea
producto1 = Producto("Laptop", 800)
producto1.agregar_stock(10)
producto1.vender()
producto1.vender()

# 🚗 Ejemplo 4: Sistema de Alquiler de Vehículos
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.disponible = True

    def alquilar(self):
        if self.disponible:
            self.disponible = False
            print(f"El vehículo {self.marca} {self.modelo} ha sido alquilado.")
        else:
            print(f"El vehículo {self.marca} {self.modelo} no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El vehículo {self.marca} {self.modelo} ha sido devuelto.")

# Ejecución del Sistema de Alquiler de Vehículos
vehiculo1 = Vehiculo("Toyota", "Corolla")
vehiculo1.alquilar()
vehiculo1.devolver()

# 🏥 Ejemplo 5: Sistema de Gestión de Pacientes en un Hospital
class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.historial_medico = []

    def agregar_historial(self, nota):
        self.historial_medico.append(nota)
        print(f"Nota agregada al historial de {self.nombre}.")

class Medico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def programar_cita(self, paciente, fecha):
        print(f"Cita programada para {paciente.nombre} con el Dr. {self.nombre} el {fecha}.")

# Ejecución del Sistema de Gestión de Pacientes
paciente1 = Paciente("Lucía", 30)
medico1 = Medico("Dr. Pérez", "Cardiología")
paciente1.agregar_historial("Consulta inicial: Sin complicaciones.")
medico1.programar_cita(paciente1, "12/01/2025")

# 🎮 Ejemplo 6: Sistema de Tienda de Videojuegos
class Juego:
    def __init__(self, titulo, genero, precio):
        self.titulo = titulo
        self.genero = genero
        self.precio = precio

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.biblioteca = []

    def comprar_juego(self, juego):
        self.biblioteca.append(juego)
        print(f"{self.nombre} compró el juego '{juego.titulo}'.")

class Compra:
    def __init__(self, jugador, juego):
        self.jugador = jugador
        self.juego = juego

    def realizar_compra(self):
        self.jugador.comprar_juego(self.juego)

# Ejecución del Sistema de Tienda de Videojuegos
juego1 = Juego("The Legend of Zelda", "Aventura", 60)
jugador1 = Jugador("Mario")
compra1 = Compra(jugador1, juego1)
compra1.realizar_compra()
