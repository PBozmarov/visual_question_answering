from flask import Flask, request, jsonify
from model_normal import generate_detailed_description 
from model_fast import generate_fast_description

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aoisdfj12peiq0wi-d0-a0sd-1'

@app.route('/generate_description', methods=['POST'])
def generate_description():
    
    data = request.get_json() 
    if 'image_path' not in data:
        return jsonify({'error': 'No image path provided!'}), 400

    image_path = data['image_path']
    model = data['model']
    try:
        if model == 'fast':
            fast_description = generate_fast_description(image_path)
            return jsonify({'description': fast_description}), 200
        elif model == 'normal':
            detailed_description = generate_detailed_description(image_path)
            return jsonify({'description': detailed_description}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,port=5000)


