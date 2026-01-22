import streamlit as st
import pandas as pd

# Use wide layout so the table can occupy more horizontal space
st.set_page_config(layout="wide")

# Mobile responsive tweaks: increase font on small screens and enable horizontal scroll
st.markdown(
        """
        <style>
        /* Basic responsive rules for mobile browsers */
        @media (max-width: 700px) {
            table {font-size: 14px !important;}
            select {font-size: 14px !important; height: 36px !important;}
            /* Allow horizontal scroll for wide tables */
            .stDataEditor, .dataframe, table {max-width: 100%; overflow-x: auto;}
            /* Reduce default padding to fit mobile */
            .main > div {padding-left: 8px; padding-right: 8px;}
        }
        </style>
        """,
        unsafe_allow_html=True,
)

df = pd.DataFrame({
    "Pacote": ["1. Verificar diariamente a necessidade de manter o cateter vesical", "2. Executar a técnica correta durante manipulação do sistema de drenagem (desprezar diurese)", "3. Realizar a higiene diária do meato uretral", "4. Manter o sistema de drenagem estéril e continuamente fechado (durante coleta de amostra de urina)"],
    "1": ["", "", "", ""],
    "2": ["", "", "", ""],
    "3": ["", "", "", ""],
    "4": ["", "", "", ""],
    "5": ["", "", "", ""],
    "6": ["", "", "", ""],
    "7": ["", "", "", ""],
    "8": ["", "", "", ""],
    "9": ["", "", "", ""],
    "10": ["", "", "", ""],
    "11": ["", "", "", ""],
    "12": ["", "", "", ""],
    "13": ["", "", "", ""],
    "14": ["", "", "", ""],
    "15": ["", "", "", ""],
    "16": ["", "", "", ""],
    "17": ["", "", "", ""],
    "18": ["", "", "", ""],
    "19": ["", "", "", ""],
    "20": ["", "", "", ""],
    "21": ["", "", "", ""],
    "22": ["", "", "", ""],
    "23": ["", "", "", ""],
    "24": ["", "", "", ""],
    "25": ["", "", "", ""],
    "26": ["", "", "", ""],
    "27": ["", "", "", ""],
    "28": ["", "", "", ""],
    "29": ["", "", "", ""],
    "30": ["", "", "", ""],
})

# Garantir exatamente 4 linhas visíveis (evita linhas em branco adicionadas pelo editor)
df = df.head(4).reset_index(drop=True)

st.data_editor(
    df,
    disabled=["Pacote"],
    width='stretch',
    height=600,
    num_rows=4,
    hide_index=True,
    key="kamishibai_editor",
    column_config={
        "1": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "2": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "3": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "4": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "5": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "6": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "7": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "8": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "9": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "10": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "11": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "12": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "13": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "14": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "15": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "16": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "17": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "18": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "19": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "20": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "21": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "22": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "23": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "24": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "25": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "26": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "27": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "28": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "29": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        ),
        "30": st.column_config.SelectboxColumn(
            options=["🟩 Conforme", "🟥 Não conforme"]
        )
    }
)