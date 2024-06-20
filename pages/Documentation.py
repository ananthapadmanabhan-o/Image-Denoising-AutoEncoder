import streamlit as st

st.set_page_config(
    page_title="Documentation",
    page_icon="📄",
)

st.write("# Welcome to Documentation! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Image Denoising AutoEncoder is an open-source project to explore the power of autoencoder architecture for
    image denoising.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [Github Repo](https://github.com/ananthapadmanabhan-o/Image-Denoising-AutoEncoder)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### How to Run?
    - #### Step 1:
    ```bash
    https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
    ```
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)