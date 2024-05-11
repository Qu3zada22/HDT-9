import networkx as nx

class SistemaViajes:
    def __init__(self, nombre_archivo):
        self.grafo = self.leer_archivo(nombre_archivo)
    
    def leer_archivo(self, nombre_archivo):
        grafo = nx.DiGraph()
        with open(nombre_archivo, 'r') as file:
            for linea in file:
                datos = linea.strip().split(',')
                estacion_origen = datos[0].strip()[1:-1]  # Eliminar comillas y espacios
                estacion_destino = datos[1].strip()[1:-1]
                costo = int(datos[2].strip())
                grafo.add_edge(estacion_origen, estacion_destino, weight=costo)
                grafo.add_edge(estacion_destino, estacion_origen, weight=costo)  # Rutas simétricas
        
        return grafo
    
    def mostrar_destinos(self, estacion_salida):
        destinos = list(self.grafo.neighbors(estacion_salida))
        if destinos:
            print(f"Posibles destinos desde {estacion_salida}:")
            for destino in destinos:
                costo = self.grafo[estacion_salida][destino]['weight']
                print(f"- {destino}: Costo = {costo}")
        else:
            print(f"No hay destinos disponibles desde {estacion_salida}")
    
    def dijkstra(self, estacion_origen):
        distancias = {nodo: float('inf') for nodo in self.grafo.nodes}
        distancias[estacion_origen] = 0
        visitados = set()
        
        while len(visitados) < len(self.grafo.nodes):
            nodo_actual = min((nodo for nodo in distancias.items() if nodo[0] not in visitados), key=lambda x: x[1])[0]
            visitados.add(nodo_actual)
            for vecino in self.grafo.neighbors(nodo_actual):
                peso_arista = self.grafo[nodo_actual][vecino]['weight']
                nueva_distancia = distancias[nodo_actual] + peso_arista
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
        
        return distancias
def mostrar_menu():
    print("==== Menú ====")
    print("1. Ver posibles destinos desde una estación")
    print("2. Calcular las distancias más cortas usando Dijkstra")
    print("3. Salir")

if __name__ == "__main__":
    sistema_viajes = SistemaViajes('rutas.txt')

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estacion_salida = input("Ingrese el nombre de la estación de salida: ")
            sistema_viajes.mostrar_destinos(estacion_salida)
        elif opcion == "2":
            estacion_salida = input("Ingrese el nombre de la estación de salida: ")
            distancias_desde_estacion = sistema_viajes.dijkstra(estacion_salida)
            print("Distancias desde", estacion_salida + ":")
            for estacion, distancia in distancias_desde_estacion.items():
                print(f"{estacion}: {distancia}")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
