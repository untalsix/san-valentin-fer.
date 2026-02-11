import streamlit as st

st.set_page_config(page_title="Para Fer López ❤️", page_icon="🌹")

st.markdown("""
    <style>
    .main {
        background-color: #fff0f3;
    }
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3.5em;
        background-color: #ff4b6b;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border: none;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    h1 {
        color: #ff4b6b;
        text-align: center;
        font-family: 'Helvetica';
    }
    p {
        text-align: center;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💌 Una pregunta especial...")

# Intenta cargar la foto de ustedes
try:
    st.image("IMG_0159.jpeg", use_container_width=True)
except:
    st.warning('IMG_0159.jpeg')

st.write("### Holaaa, mi vida preciosa")
st.write("Hay algo que he querido preguntarte hace tiempo...")

st.markdown("## **¿Quieres ser mi San Valentín? ❤️**")

col1, col2 = st.columns(2)

with col1:
    if st.button("¡SÍ! 😍"):
        st.balloons()
        st.success("¡Me acabas de hacer la persona más feliz del mundo! 🌹✨")
        st.snow()

with col2:
    if st.button("No... 🥺"):
        st.error("¡Ijoleeeee esa opción ahorita no anda funcionando. Intenta de nuevo 🤣")
