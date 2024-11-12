import streamlit as st
st.title("App de prueba")
nombre = st.text_input("Nombre:")
st.write("hola como estas ", nombre)
edad = st.number_input("Edad:",step=1)
if edad > 18:
    st.write(nombre, " es mayor de edad")
else:
    st.write(nombre, " es menor de edad")

if st.button('Haz clic aquí'):
    st.write("¡Botón presionado!")
    