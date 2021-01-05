import streamlit as st
from Scripts.streamlit_graph import graph_generator
from Scripts.streamlit_covid import show_map
import pandas as pd
from pathlib import Path

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

def load_data(Path):
    return pd.read_csv(Path)

if __name__ == "__main__":
    main_markdown = read_markdown_file("README.md")
    st.markdown(main_markdown, unsafe_allow_html=True)
