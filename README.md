# Image-Denoising-AutoEncoder

## How to Run?

### STEP 01
#### Clone the repository
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
#### Install the requirements
```bash 
pip install -r requirements.txt
```
### STEP 05
#### Model parameters setup
- Model parameters like epochs, batch size etc can be modified in the params.yaml file before training

### STEP 06
#### Run this command
```bash
python3 main.py
```

### Pipelines

Running main.py  will start the pipelines.
    - Data ingestion pipeline downloads the data and stores it in artifacts folder
    - Data transformation pipeline preproccess the stored data and splits it into input feature and output targets. Then transformed data is saved as pickle file in artifacts
    - Base model pipeline creates and initializes the deep learning model. The model follows autoencoder architecture. Tensorflow Keras is used for building the model. After building, the model is saved as pickle file even before training(model.fit() method is not called.)
    - Training pipeline loads the untrained model from Base model pipeline and loads the data which was pickled earlier. Training pipeling collects the confgurations and parameter for the model from config.yaml and params.yaml files. Training pipeline is configured to train the model in GPU if GPUs are available in the machine.