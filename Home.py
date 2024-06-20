import streamlit as st

st.set_page_config(
    page_title="Home",
    layout='centered',
    page_icon="🏠︎",
    initial_sidebar_state="expanded",
)


st.header("Image Denoising AutoEncoder", divider='rainbow',)

st.image('assets/head_image.png',use_column_width=True)
st.markdown(
    '''## An introduction to Auto-Encoder architecture

'''
)
st.image('assets/autoencoder.png',use_column_width=True)



body = '''
An **autoencoder** is a type of artificial neural network used in 
unsupervised learning for data compression and feature learning. 

- ### **Basic Structure:**


    - **Encoder:** The encoder compresses the input data into a lower-dimensional representation, known as the latent space or code. This is done by mapping the input data to this compact, feature-rich space.
    - **Decoder:** The decoder reconstructs the original input data from the compressed representation. The goal is to make the reconstructed data as close to the original input as possible.

- ### **Key Concepts:**
    - **Compression:** The encoder reduces the dimensionality of the input, capturing essential features while discarding noise and redundant information.
    - **Reconstruction:** The decoder tries to reconstruct the input data from the compressed representation, ensuring that important features are preserved.
    - **Loss Function:** The autoencoder is trained to minimize the difference between the input and the reconstructed output, typically using mean squared error or another appropriate loss function.
- ### Applications:
    - **Data Denoising:** Removing noise from data by learning to reconstruct clean data from noisy input.
    - **Dimensionality Reduction:** Reducing the number of features while preserving important information, similar to Principal Component Analysis (PCA).
    - **Anomaly Detection:** Identifying unusual data points by measuring reconstruction error; high error indicates a potential anomaly.
 '''

st.markdown(body)