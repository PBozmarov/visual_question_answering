from transformers import AutoTokenizer, AutoModelForCausalLM
from tqdm import tqdm
import time
import os
import warnings
warnings.filterwarnings("ignore")


# Load model and tokenizer
hf_path = 'jiajunlong/TinyLLaVA-OpenELM-450M-SigLIP-0.89B'
model = AutoModelForCausalLM.from_pretrained(hf_path, trust_remote_code=True)
config = model.config
tokenizer = AutoTokenizer.from_pretrained(hf_path, use_fast=False, model_max_length=config.tokenizer_model_max_length, padding_side=config.tokenizer_padding_side)

def generate_main_description(image_path: str) -> str:

    '''
    Function to generate a detailed description for an image using the model.
    Args:
        image_path (str): Path to the image file.
    Returns:
        str: The generated detailed description for the image.
    '''

    # Get the description from the model
    output_text, _ = model.chat(prompt="Describe the image in details within 1 paragraph.", image=image_path, tokenizer=tokenizer, temperature=0.85)
    
    # Format the output
    formatted_output = f"Image description:\n{output_text}"
    
    return formatted_output


def generate_main_colors(image_path: str) -> str:

    ''' 
    Function to generate the main colors in an image using the model.
    Args:
        image_path (str): Path to the image file.
    Returns:
        str: The main colors in the image.
    '''
    
    # Get the colors from the model
    output_text, _ = model.chat(prompt="List the main colors in the image and seperate them with commas.", image=image_path, tokenizer=tokenizer, temperature=0.75)
    
    # Format the output
    formatted_output = f"Main colors:\n{output_text}"
    return formatted_output


def generate_tags():
    pass # Skeleton for generating tags


def generate_detailed_description(image_path: str) -> str:
    '''
    Function to generate a detailed description for an image using the model.
    Args:
        image_path (str): Path to the image file.
    Returns:
        str: The generated detailed description for the image.
    '''

    # Generate the main description and add colors
    main_desc = generate_main_description(image_path)
    colors = generate_main_colors(image_path)

    # Combine the main description and colors
    detailed_description = f"{main_desc}\n\n{colors}"
    return detailed_description


def generate_detailed_description_folder(image_folder_path: str) -> None:
    '''
    Function to generate detailed descriptions for all images in a folder.
    Args:
        image_folder_path (str): Path to the image folder.
    Returns:
        None
    '''

    # Create the predictions folder
    predictions_folder_path = os.path.join(image_folder_path, 'normal_predictions')
    os.makedirs(predictions_folder_path, exist_ok=True)
    
    valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp'}

    for image_filename in tqdm(os.listdir(image_folder_path),desc='Generating Descriptions...'):
        image_path = os.path.join(image_folder_path, image_filename)
        
        # Check if the path is a file and has a valid image extension
        if os.path.isfile(image_path) and os.path.splitext(image_filename)[1].lower() in valid_extensions:
            detailed_description = generate_detailed_description(image_path)
            
            prediction_filename = f"{os.path.splitext(image_filename)[0]}.txt"
            prediction_path = os.path.join(predictions_folder_path, prediction_filename)
            
            # Write the detailed description to the text file
            with open(prediction_path, 'w') as f:
                f.write(detailed_description)


if __name__=="__main__":

    start = time.time()
    # Load and preprocess the image
    image_path = 'images/zebra.jpeg'

    # Generate the detailed description
    detailed_description = generate_detailed_description(image_path)
    end = time.time() - start
    print(detailed_description)
    print(f"Total time taken: {end} seconds")


    # To test the model on an image folder, uncomment the following lines
    # image_folder_path = 'images'
    # generate_detailed_description_folder(image_folder_path = image_folder_path)




