class Bebida:
    def __init__(self, id, nombre, clasificacion, marca, precio):
        self.id = id
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.marca = marca
        self.precio = precio

class AlmacenBebidas:
    def __init__(self):
        self.bebidas = []

    def alta_bebida(self, id, nombre, clasificacion, marca, precio):
        bebida = Bebida(id, nombre, clasificacion, marca, precio)
        self.bebidas.append(bebida)
        print("Bebida agregada con éxito.")

    def baja_bebida(self, id):
        for bebida in self.bebidas:
            if bebida.id == id:
                self.bebidas.remove(bebida)
                print("Bebida eliminada con éxito.")
                return
        print("No se encontró una bebida con el ID especificado.")

    def actualizar_bebida(self, id, nombre, clasificacion, marca, precio):
        for bebida in self.bebidas:
            if bebida.id == id:
                bebida.nombre = nombre
                bebida.clasificacion = clasificacion
                bebida.marca = marca
                bebida.precio = precio
                print("Bebida actualizada con éxito.")
                return
        print("No se encontró una bebida con el ID especificado.")

    def mostrar_bebidas(self):
        if len(self.bebidas) > 0:
            print("Bebidas en el almacén:")
            for bebida in self.bebidas:
                print(f"Id: {bebida.id}")
                print(f"Nombre: {bebida.nombre}")
                print(f"Clasificación: {bebida.clasificacion}")
                print(f"Marca: {bebida.marca}")
                print(f"Precio: {bebida.precio}")
                print("-------------------")
            
        else:
            print("No hay bebidas en el almacén.")

    def calcular_precio_promedio(self):
        if len(self.bebidas) == 0:
            print("No hay bebidas en el almacén.")
        else:
            total_precios = sum(bebida.precio for bebida in self.bebidas)
            promedio = total_precios / len(self.bebidas)
            print(f"El precio promedio de las bebidas es: {promedio}")

    def cantidad_bebidas(self, marca):
        cantidad = sum(1 for bebida in self.bebidas if bebida.marca == marca)
        print(f"La cantidad de bebidas de la marca {marca} es: {cantidad}")

    def cantidad_bebidas_clasificacion(self, clasificacion):
        cantidad = sum(1 for bebida in self.bebidas if bebida.clasificacion == clasificacion)
        print(f"La cantidad de bebidas de la clasificación {clasificacion} es: {cantidad}")




almacen = AlmacenBebidas()

# Alta de bebidas
almacen.alta_bebida(1, "Agua Ciel", "Agua", "CocaCola", 15.0)
almacen.alta_bebida(2, "Agua Bonafont", "Agua", "Grupo Danone", 17.50)
almacen.alta_bebida(3, "Agua Epura", "Agua", "PEPSI", 14.50)
almacen.alta_bebida(4, "Coca Cola", "Refresco", "CocaCola", 20.0)
almacen.alta_bebida(5, "Pepsi", "Refresco", "PEPSI", 16.0)
almacen.alta_bebida(6, "Fresca", "Refresco", "CocaCola", 17.0)
almacen.alta_bebida(7, "Gatorade", "Energetico", "Quaker", 25.0)
almacen.alta_bebida(8, "Powerade", "Energetico", "CocaCola", 25.0)

# Baja de bebidas
almacen.baja_bebida(7)

# Actualizar babidas
almacen.actualizar_bebida(5, "GatoradeX", "Energetico", "Quaker", 28.0)


# Mostrar todas las bebidas
almacen.mostrar_bebidas()

# Calcular precio promedio de bebidas
almacen.calcular_precio_promedio()

# Cantidad de bebidas de una marca
almacen.cantidad_bebidas("CocaCola")

# Cantidad por clasificación
almacen.cantidad_bebidas_clasificacion("Agua")
