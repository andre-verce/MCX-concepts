import streamlit as st
import plotly.express as px
import pandas as pd

# Configurazione pagina
st.set_page_config(page_title="App Grafica Avanzata", layout="wide")

# Titolo e sottotitolo
st.title("🚀 App Grafica Avanzata")
st.subheader("Un'interfaccia più gradevole e completa")

# Layout con colonne
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("### Sezione principale")
    st.write("Qui puoi visualizzare i dati, grafici e controlli interattivi.")
    
    # Caricamento dati di esempio
    df = px.data.iris()

    # Selezione del grafico
    chart_type = st.selectbox(
        "Seleziona il tipo di grafico",
        ["Scatter", "Bar", "Line"]
    )

    # Selezioni per il grafico
    x_axis = st.selectbox("Asse X", df.columns[:-1])
    y_axis = st.selectbox("Asse Y", df.columns[:-1])
    color = st.selectbox("Color", [None] + list(df.columns[:-1]))

    # Creazione del grafico
    if chart_type == "Scatter":
        fig = px.scatter(df, x=x_axis, y=y_axis, color=color)
    elif chart_type == "Bar":
        fig = px.bar(df, x=x_axis, y=y_axis, color=color)
    else:  # Line
        fig = px.line(df, x=x_axis, y=y_axis, color=color)

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("### Opzioni e Info")
    st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb", caption="Nature Image", use_column_width=True)
    st.write("Puoi usare questa sidebar per controllare diverse parti dell'app.")

    # Sidebar con controlli
    st.sidebar.header("Configurazioni")
    dataset_option = st.sidebar.selectbox("Seleziona il dataset", ["Iris", "Tips", "Titanic"])
    show_data = st.sidebar.checkbox("Mostra i dati")

    # Mostrare i dati selezionati
    if show_data:
        if dataset_option == "Iris":
            df_display = px.data.iris()
        elif dataset_option == "Tips":
            df_display = px.data.tips()
        else:
            df_display = px.data.titanic()

        st.subheader(f"Dataset: {dataset_option}")
        st.dataframe(df_display)

# Footer
st.markdown("---")
st.write("App sviluppata per dimostrazione di layout avanzato e interattività.")