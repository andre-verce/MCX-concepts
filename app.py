import streamlit as st
import yaml

# Funzione per caricare i dati dal file YAML
def carica_dati(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

# Carica i dati
dati = carica_dati('dati.yaml')

st.title("Tabella con descrizioni espandibili da YAML")

# Itera sugli elementi e crea un expander per ciascuno
for elemento in dati['elementi']:
    with st.expander(elemento['nome']):

        st.write(elemento['descrizione'])
