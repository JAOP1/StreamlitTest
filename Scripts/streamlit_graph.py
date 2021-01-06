import streamlit as st
import graphviz as gv
import numpy as np

#n = number of nodes.
def RandomTree(n):
    random_tree = gv.Graph()

    if n < 2:
        return random_tree

    random_tree.edge('0','1')

    for v in range(2,n):
        u = np.random.randint(0,v)
        random_tree.edge(str(u),str(v))

    return random_tree

def Complete(n):
    complete_graph = gv.Graph()    

    for v in range(n):
        for u in range(v+1,n):
            complete_graph.edge(str(v),str(u))
    return complete_graph


#P is the probability.
def random(n, p=0.25):
    random_graph = gv.Graph()

    for v  in range(n):
        for u in range(v+1,n):
            if np.random.rand() <= p:
                random_graph.edge(str(v),str(u))
    return random_graph

def square_grid(n):
    raise NotImplementedError

def cycle_graph(n):
    raise NotImplementedError


graph_representation = ["Árbol aleatorio", "Completo","Aleatorio"]

def get_graph(graph_type,num_nodes):
    if graph_type =="Árbol aleatorio": 
        return RandomTree(num_nodes)

    elif graph_type == 'Completo':
        return Complete(num_nodes)

    elif graph_type == 'Aleatorio':
        return random(num_nodes)

    return gv.Graph()
    
def graph_generator():
    left_col , right_col = st.beta_columns(2)

    with left_col:
        graph_type = st.radio(
            "Generador de grafos:",
            graph_representation
        )

    with right_col:
        num_nodes= st.number_input(
            "Número de nodos:",
            min_value=5,
            max_value=15,
            step=1
        )
        pressed = st.button("¡Generar!")

    if pressed:
        Graph = get_graph(graph_type, num_nodes)
        st.graphviz_chart(Graph)
