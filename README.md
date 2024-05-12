# Sistema de Viajes

Este programa implementa un sistema de viajes entre estaciones utilizando un grafo dirigido para representar las conexiones entre las estaciones y el algoritmo de Dijkstra para encontrar las distancias más cortas entre ellas.

## Funcionalidades

El programa ofrece las siguientes funcionalidades:

1. **Ver posibles destinos desde una estación**: Permite al usuario ingresar el nombre de una estación y muestra los destinos posibles desde esa estación junto con el costo asociado a cada destino.

2. **Calcular las distancias más cortas usando Dijkstra**: Permite al usuario ingresar el nombre de una estación como punto de partida y calcula las distancias más cortas desde esa estación a todas las demás estaciones utilizando el algoritmo de Dijkstra.

3. **Mostrar grafo**: Muestra visualmente el grafo de estaciones utilizando la librería NetworkX y Matplotlib.

4. **Salir**: Permite al usuario salir del programa.

## Uso

Para ejecutar el programa, simplemente ejecuta el archivo `main.py`. Se mostrará un menú con las opciones disponibles, y puedes seleccionar una opción ingresando el número correspondiente.

## Archivo de Datos

El programa lee los datos de un archivo de texto que contiene las conexiones entre estaciones y los costos asociados. El formato del archivo debe ser el siguiente:

```
"Estación de Origen","Estación de Destino",Costo
```

Por ejemplo:

```
"A","B",10
"B","C",15
"C","D",20
```

## Requisitos

El programa requiere Python 3.x y las siguientes librerías:

- NetworkX
- Matplotlib

Puedes instalar estas dependencias usando `pip`:

```
pip install networkx matplotlib
```

## Repocitorio
https://github.com/Qu3zada22/HDT-9.git