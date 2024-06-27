import streamlit as st
import streamlit_shadcn_ui as ui

resume_file="assets/Cv.pdf"
resume_file_name="Cv_Marco Espina.pdf"
css_file="styles/main.css"



layout = "centered"
page_title = "Portafolio // Marco"
profile_pic="assets/yo1.png"

#page_icon 
name="Marco Espina"
description= "Marco Espina bla bla bla"
email="marcoantonio.espina5@gmail.com"


social_media = {
    "Instagram": "https://www.instagram.com/asagi_corvinus/",
}

proyectos={
    "asdf": "www.google.cl",
    "aaa":"www.nasa.com",
    "eee":"www.youtube.com",
}

#config de pagina
st.set_page_config(page_title=page_title, layout=layout)

with open(resume_file, "rb") as pdf_file:
    PDFbyte=pdf_file.read()

#carga de css
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


#link redes sociales
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    with cols[index]:
        ui.link_button(text=platform, url=link, key=f"link_btn_{platform}")

#cabecera
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(name)
    st.write(description)
    st.download_button(
        label="Descargar CV",
        data=PDFbyte,
        file_name=resume_file_name,)
    st.write("Mail: ", email)
    
#proyectos---

#st.write("##")
#st.subheader("Proyectos")
#st.write("---")

#for proyect, link in proyectos.items():
#    st.write(f"[{proyect}][{link}]")
 
#habilidades-

st.write("##")
st.subheader("Habilidades y Conocimientos")
st.write("---")
st.write(
    """
-   Programacion: Python, JavaScript.
-   Software: Visual Studio, Office.
"""
)

#Experiencia--

st.write("##")
st.subheader("Experiencia")
st.write("---")

#Trabajo1
st.write("Estudios en programacion:")
st.write("28-08-2017 - Actualidad")
st.write("Cursos:"
    """
-   Analista desarrolador de aplicaciones de software en JavaScript impartido por la fundacion instituto profesional DUOC UC del programa becas laborales de capacitacion para el trabajo.
-   Diferentes cursos de Python a traves de la plataforma Udemy.
-   Formacion autodidacta a traves de los años.
"""
)
st.write("Proyectos:"
    """
-   Diferentes proyectos realizados a traves de el proceso de estudio y aprendizaje.
"""
)





