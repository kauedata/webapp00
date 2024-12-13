# MEU PRIMEIRO WEB APP
import streamlit as st

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Primeiro site teste Streamlit")

a = float(st.text_input("Digite valor a: "))
b = float(st.text_input("Digite valor b: "))
media = (a+b)/2
if media>5:
  st.write("Aprovado(a)!")
  st.write(media)
else:
  st.write("REC! :(")
  st.write(media)

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("SENAI Roberto Mange")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Kauê Gonçalves de Carvalho")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

