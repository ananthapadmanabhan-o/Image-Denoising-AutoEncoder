import streamlit as st 
from denoisingEncoder.pipeline.prediction import PredictionPipeline

st.title("Image Denoising AutoEncoder")
st.image('assets/head_image.png')
uploaded_image = st.file_uploader("Upload Image 🚀", type=["png","jpg","bmp","jpeg"])

st.image(uploaded_image)

if st.button('Denoise Image'):
    with st.spinner('Wait for it...'):
        prediction = PredictionPipeline(uploaded_image)
        output_img = prediction.predict()
        st.image(output_img)
        st.success('Done!') 


with open('artifacts/output/output.png','rb') as file:
    st.download_button(
            label='download image',
            data=file,
            file_name='image.png',
            mime='image/png',

        )