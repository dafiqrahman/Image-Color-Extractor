import streamlit as st
from PIL import Image
from script import main

st.markdown(
    """<style>.css-zt5igj svg{display:none}</style>""", unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center;'>Image Color Extraction App</h1>",
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Extract the dominant colors of your image</h3>",
            unsafe_allow_html=True)


image_file = st.file_uploader(
    "Upload an image", type=['jpg', 'png', 'jpeg'])
n_colors = st.slider("Number of colors to be extracted", 1, 20, 6)
col1, col2 = st.columns(2)
col1.header("Input Image")
if image_file is not None:
    col1.image(image_file, width=300)
    col2.header("Color Palette")
    # uploaded file to array
    image = Image.open(image_file)
    image = image.convert('RGB')
    with col2:
        fig, axs = main(image, n_colors)
        st.pyplot(fig)
