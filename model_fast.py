import time
import os
from tqdm import tqdm
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import warnings
warnings.filterwarnings("ignore")

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")


def generate_caption(image_path: str) -> str:

    '''
    Function to generate a caption for an image using the model.
    Args:
        image_path (str): Path to the image file.
    Returns:
        str: The generated caption for the image.
    '''

    # Load the images
    image = Image.open(image_path).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    
    # Get the caption from the model
    output = model.generate(**inputs, max_length=100, temperature=1,do_sample=True)
    output_text = processor.decode(output[0], skip_special_tokens=True)

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

    # Load the image
    image = Image.open(image_path).convert("RGB")
    text = "The main colors of the image are"
    inputs = processor(image, text, return_tensors="pt")
    
    # Get the colors from the model
    output = model.generate(**inputs, max_length=40, num_beams=2, temperature=0.75,do_sample=True)
    output_text = processor.decode(output[0], skip_special_tokens=True)
    
    formatted_output = f"Main colors:\n{output_text}"
    return formatted_output


def generate_tags():
    pass # Skeleton for generating tags

def generate_fast_description(image_path: str) -> str:

    '''
    Function to generate a caption and color information for an image.
    Args:
        image_path (str): Path to the image file.
    Returns:
        str: The generated caption and color information for the image.
    '''
    
    # Generate the main description and add colors
    caption = generate_caption(image_path)
    colors = generate_main_colors(image_path)

    # Combine the main description and colors
    fast_description = f"{caption}\n\n{colors}"
    return fast_description


def generate_fast_description_folder(image_folder_path: str)-> None:

    '''
    Function to generate captions and color information for all images in a folder.
    It creates a new folder 'fast_predictions' inside the given image folder path and 
    saves the predictions as text files.
    Args:
        image_folder_path (str): Path to the folder containing the images.
    Returns:
        None

    '''
    
    # Create the predictions folder
    predictions_folder_path = os.path.join(image_folder_path, 'fast_predictions')
    os.makedirs(predictions_folder_path, exist_ok=True)

    valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp'}
    
    for image_filename in tqdm(os.listdir(image_folder_path),desc='Generating Descriptions...'):
        image_path = os.path.join(image_folder_path, image_filename)
        
        # Check if the path is a file and has a valid image extension
        if os.path.isfile(image_path) and os.path.splitext(image_filename)[1].lower() in valid_extensions:
            fast_description = generate_fast_description(image_path)

            prediction_filename = f"{os.path.splitext(image_filename)[0]}.txt"
            prediction_path = os.path.join(predictions_folder_path, prediction_filename)
            
            # Write the fast description to the text file
            with open(prediction_path, 'w') as f:
                f.write(fast_description)


if __name__=="__main__":

    start = time.time()

    # Load and preprocess the image
    image_path = 'images/winter_playground.jpeg'

    # Generate the detailed description
    detailed_description = generate_fast_description(image_path)
    end = time.time() - start
    print(detailed_description)
    print(f"Total time taken: {end} seconds")

    # To test the model on an image folder, uncomment the following lines
    # image_folder_path = 'images'
    # generate_fast_description_folder(image_folder_path = image_folder_path)