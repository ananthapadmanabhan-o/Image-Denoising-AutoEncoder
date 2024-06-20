import streamlit as st
from denoisingEncoder.pipeline.prediction import PredictionPipeline
from skimage.transform import resize
from skimage.io import imread

st.set_page_config(
    page_title='Demo',
    layout='centered',
    page_icon='🎯',
    initial_sidebar_state="expanded"
)

st.header("Image Denoising AutoEncoder", divider='rainbow')

uploaded_image = st.file_uploader("", type=["png","jpg","bmp","jpeg"])



if uploaded_image is not None:
    image = imread(uploaded_image)
    image = resize(image,(256,256))
    
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
            st.image(image='assets/output/output.png',use_column_width=True)
            img_exist_flag = True

    if img_exist_flag:
        st.download_button(
                            label='Download Image',
                            data= open('assets/output/output.png', 'rb').read(),
                            file_name='denoised_image.png',
                            mime='image/png',
                            type='primary',
                            use_container_width=True
                        )
