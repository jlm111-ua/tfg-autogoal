import streamlit as st

import streamlit as st

# Encabezado de la página con nombre y logo
st.markdown(
    """
    <div style="display: flex; align-items: left; flex-direction: column;">
        <div style="display: flex; align-items: center;">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTq7pgyrE20SlvFMPsHAwRteA52lhRPQ6K9DYKprqVjmHpndFbWdiVCqjyv6N8NE8_HMr0&usqp=CAU" alt="Logo" style="width: 50px; height: 50px; margin-right: 10px;">
            <h1 style="color:#FF8C00; margin: 0;">AutoGOAL</h1>
        </div>
        <p style="font-size: 14px; color:#FF8C00; margin: 0;">Automatic Generation, Optimization & Artificial Learning</p>
    </div>
    """,
    unsafe_allow_html=True
)


# Contenido de la página
st.write("Bienvenido a mi página en Streamlit. Este es un ejemplo simple.")