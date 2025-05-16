import streamlit as st
from PIL import Image
import warnings
import os

# Suppress warnings
warnings.filterwarnings("ignore")

# Title
st.title("🎰 Image Description Generator")
st.markdown("***")

# Display a spinner while loading the models
with st.spinner("Loading the models. Please wait..."):
    from model_normal import generate_detailed_description
    from model_fast import generate_fast_description

def generate_description(image_path, model_type):
    if model_type == "Normal":
        return generate_detailed_description(image_path)
    else:
        return generate_fast_description(image_path)

# Image uploader
st.markdown("<h2>Choose an image...</h2>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "bmp"],label_visibility='collapsed')

if uploaded_file is not None:
    # Save the uploaded file to a temporary directory
    temp_dir = "temp_images"
    os.makedirs(temp_dir, exist_ok=True)
    image_path = os.path.join(temp_dir, uploaded_file.name)
    
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display the image
    image = Image.open(image_path)
    st.image(image, use_column_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Select model
    st.markdown("<h2>Choose a model...</h2>", unsafe_allow_html=True)
    model_type = st.selectbox("Choose a model...", ["Fast", "Normal"],label_visibility='collapsed')

    # Generate description
    if st.button("Generate Description"):
            description = generate_description(image_path, model_type)
            st.write(description)



