# Image-Denoising-AutoEncoder

## Introduction 🚨

One of the fundamental challenge in signal processing is the presence of noise. Random nature of noise makes it difficult to process the data and distructively affects the quality of data collected. The field of computer vision is growing large with its vast applications accross different fields. Advancements in computer vision demands high quality image data for building robust state of the art models. 

This project aims at exploring autoencoder architecture for image denoising. AutoEncoder arcitecture is a neural netwoek architecture widely used for denoising and reconstruction of images and video files.

check out [AutoEncoders](https://en.wikipedia.org/wiki/Autoencoder)
learn more about [Image-Noise](https://en.wikipedia.org/wiki/Image_noise#:~:text=Image%20noise%20is%20random%20variation,of%20an%20ideal%20photon%20detector.)
GitHub link [Project-Repo](https://github.com/ananthapadmanabhan-o/Image-Denoising-AutoEncoder)
Data set linke [link](https://www.kaggle.com/datasets/huaiyingu/bsd100)
## 🚀 Installation and Setup 🔥

### STEP 01
#### 💻Clone the repository
```bash 
git clone https://github.com/ananthapadmanabhan-o/Image-Denoising-AutoEncoder.git
```

### STEP 02
#### Create a virtual environment after opening the repository
```bash 
cd Image-Denoising-AutoEncoder
```

```bash
python3 -m venv venv
```


### STEP 03
#### Activate the virtual environment

```bash
source venv/bin/activate
```


### STEP 04
#### Install the requirements 🔧
```bash 
pip install -r requirements.txt
```


### STEP 05
#### Model parameters setup ⚙️. 
- Model parameters like epochs, batch size etc can be modified in the params.yaml file before training

### STEP 06
#### Run this command
```bash
python3 main.py
```

### Pipelines🤖

#### Running main.py  will start the pipelines.
- 📥 **Data ingestion pipeline** downloads the data and stores it in artifacts folder🛢️.

- **Data transformation pipeline**  preproccess the stored data and splits it into input feature and output targets. Then
transformed data is saved as pickle file in artifacts.

- **Base model pipeline** creates and initializes the deep learning model. The model follows autoencoder architecture. Tensorflow
Keras is used for building the model. After building, the model is saved as pickle file even before training(model.fit()) method is
not called.

- **Training pipeline**  loads the untrained model from Base model pipeline and loads the data which was pickled earlier. Training
pipeling collects the confgurations and parameter for the model from config.yaml and params.yaml files. Training pipeline is
configured to train the model in GPU if GPUs are available in the machine.

### For Running Streamlit UI
#### Run Home.py
```bash 
streamlit run Home.py
```
