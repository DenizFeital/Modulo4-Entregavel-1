# app.py
import streamlit as st
st.set_page_config(
    page_title='Análise Agrícola',
    page_icon=':farmer:',
    layout='wide'
)
st.title('FarmTech Solutions :farmer:')
st.write('Bem-vindo ao nosso controle de análise de dados agrícolas.')
st.markdown("""
Este aplicativo permite explorar um dataset simulado de produção agrícola,
realizar análises exploratórias e aplicar modelos preditivos.
Utilize o menu à esquerda para navegar entre as páginas.
""")