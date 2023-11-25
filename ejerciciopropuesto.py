# class Biblioteca:
#     def __init__(self):
#         self.pila_libros = []

#     def prestar_libro(self, libro):
#         self.pila_libros.append(libro)
#         print(f"Libro prestado: {libro}")

#     def devolver_libro(self):
#         if self.pila_libros:
#             libro_devuelto = self.pila_libros.pop()
#             print(f"Libro devuelto: {libro_devuelto}")
#         else:
#             print("No hay libros para devolver.")

#     def mostrar_estado(self):
#         if self.pila_libros:
#             print("Libros prestados: ", self.pila_libros)
#         else:
#             print("La pila de libros está vacía.")

class Banco:
    def __init__(self):
        self.cola_clientes = []

    def llegar_cliente(self, cliente):
        self.cola_clientes.append(cliente)
        print(f"Cliente llegó: {cliente}")

    def atender_cliente(self):
        if self.cola_clientes:
            cliente_atendido = self.cola_clientes.pop(0)
            print(f"Atendiendo a: {cliente_atendido}")
        else:
            print("No hay clientes en la cola.")

    def mostrar_estado(self):
        if self.cola_clientes:
            print("Cola de clientes: ", self.cola_clientes)
        else:
            print("La cola de clientes está vacía.")

