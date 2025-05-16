# Image Description Generator

This project generates detailed descriptions for images using a pre-trained model. It provides a REST API and a CLI for interacting with the model.

## Readme Usage

To view the README.md file in a more readable format:

**cmd+shift+v** - Mac

**ctrl+shift+v** - Windows

# Repository Structure

```
.
├── Siteground
├── images # folder with sample images and predictions/
│   ├── fast_predictions/... # generated captions using the fast model
│   ├── normal_predictions/... # generated descriptions using the normal model
│   ├── bridge.jpeg
│   ├── chess.jpeg
│   ├── football.jpeg
│   └── ...
├── temp_images # folder necessary for the streamlit application
├── flask_app.py # the flask application
├── test.py # the file for making inferences
├── streamlit_app.py # the streamlit application
└── ...
```

## Installation

First, go to the Siteground folder using **cd**. Then, Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

You can also directly install the environment and the packages using the following command:

```bash
  conda env create -f environment.yaml --name <myenv>
  activate <myenv>
```

Replace `<myenv>` with your desired environment name.

## Usage

Please do keep in mind that when initially running the inference code, it may take a while to download the model weights.

### Flask Application

To make inference using the Flask application, run the following command:

```bash
python flask_app.py
```

Then, open another terminal window and run the following command:

(Don't forget to activate the environment in the new terminal window)

```bash
python test.py --image_path <path to image> --model [normal,fast]
```

Example:

```bash
python test.py --image_path images/bridge.jpeg --model normal
```

- model: normal or fast, default is normal.
  - normal: uses **TinyLLaVA-OpenELM**
  - fast: uses **Blip-image-captioning-large**
- image_path: path to the image.

### Streamlit Application

To run the streamlit application, run the following command:

```bash
streamlit run streamlit_app.py
```

Then, open the browser and go to the address shown in the terminal. There you will be able to upload images and see the generated descriptions.
