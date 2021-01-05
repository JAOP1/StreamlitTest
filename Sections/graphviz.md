# Graphviz
 
Graphviz es una librería de visualización de información, donde, nos permite mostrar la información en una representación de red (grafo).
 
Para la creación de grafos,Graphviz proporciona dos clases:  `Digraph` (grafo dirigido) o `Graph` (grafo no dirigido).
 
Es importante resaltar, que no es necesario crear los nodos, sino que se puede realizar durante la creación de las aristas.
 
```python
import graphviz
 
G = graphviz.Digraph(format='png')
 
G.edge('Abuelo','Padre')
G.edge('Padre','Hijo')
 
G.render(view=True)
```
En el ejemplo muestra cómo se crea un grafo dirigido, donde, podemos mencionar en ese momento en que formato será guardado el resultado. Después, anexa las aristas y finalmente, lo generamos (el parámetro view es para desplegar el resultado).
 
Si quieres consultar la documentación, la puedes encontrar [aquí](https://graphviz.readthedocs.io/en/stable/manual.html)
 
 
## Graphviz y Streamlit
En este trabajo hemos creado un generador de grafos. Vamos a explicar cómo incluir funciones generadoras al proyecto.
 
El proyecto está dividido en:
* Scripts/
* Sections/
* main.py
 
En *Scripts* se encuentra el archivo **streamlit_graph.py** donde contendrá todas nuestras funciones que toman como parámetro de entrada el número de nodos y regresa un objeto del tipo **graphviz.Graph**.
 
```python
#Función en graph.py
def path(n):
   path_graph = graphviz.Graph()
 
   for i in range(n):
       path_graph.edge(str(i), str(i+1))
   return path_graph
```
Como en el apartado anterior, definimos nuestro grafo, es importante notar que cada nodo está representado con una cadena de texto y para añadir aristas es *grafo.edge(u,v)*.
 
Ahora tenemos que hacer visible nuestra función  en el conjunto opciones. 
 
```python
#Esta función se encuentra en streamlit_graph.py
graph_representation.append('path')
def get_graph(graph_type, num_nodes):
 
   #Incluir este 'elif'
   elif graph_type == "path":
       graph_ = graph.path(num_nodes)
 
   return graph_
```


