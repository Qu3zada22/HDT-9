from sistema_viajes import SistemaViajes

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
