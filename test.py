import requests
import argparse
import time

# This route should match the Flask route
url = 'http://127.0.0.1:5000/generate_description'

desc = "Generate Image Description."
parser = argparse.ArgumentParser(description=desc)

parser.add_argument(
    "--image_path",
    default='images/zebra.jpeg',
    type=str,
    help="Absolute or relative path to the image file.",
)

parser.add_argument(
    "--model",
    default='normal',
    type=str,
    choices=['fast', 'normal'],
    help="Choose between 'fast' and 'normal' models. 'normal' provides a detailed image description, while 'fast' provides a simple caption.",
)

args = parser.parse_args()
image_path = args.image_path
model_choice = args.model

data = {
    'image_path': image_path,
    'model': model_choice
}

# Start the timer
start = time.time()

print('Running Inference...\n')
response = requests.post(url, json=data)
if response.status_code == 200:
    description = response.json()['description']
    print(description)
    end = time.time() - start
    print(f"Total time taken: {end} seconds")
elif response.status_code in [400,500]:
    error = response.json()['error']
    print(error)
