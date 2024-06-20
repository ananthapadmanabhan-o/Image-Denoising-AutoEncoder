import streamlit as st 
from denoisingEncoder.pipeline.prediction import PredictionPipeline


st.set_page_config(
    layout='centered',
)




st.title("Image Denoising AutoEncoder")


uploaded_image = st.file_uploader("", type=["png","jpg","bmp","jpeg"])



if uploaded_image is not None:
    image = uploaded_image
    
    img_exist_flag = False


    if st.button('Denoise',type='primary',use_container_width=True,key=1):
        with st.spinner('Denoising....'):
            prediction = PredictionPipeline(uploaded_image)
            output_img = prediction.predict()
            img_exist_flag = True          
        st.success('Done!')
    


    left_container, right_container = st.columns(2)
    

    if left_container.button('Original',use_container_width=True,key=2):
        st.image(image=image,use_column_width=True)

    if right_container.button('Denoised image',use_container_width=True,key=3):
            st.image(image='artifacts/output/output.png',use_column_width=True)
            img_exist_flag = True

    if img_exist_flag:
        st.download_button(
                            label='Download Image',
                            data= open('artifacts/output/output.png', 'rb').read(),
                            file_name='denoised_image.png',
                            mime='image/png',
                            type='primary',
                            use_container_width=True
                        )
