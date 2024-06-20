from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

words = ["Lucky", "Golden", "Dragon", "Palace", "Garden", "Jade", 
         "Lotus", "Joy", "Wok", "Chef", "Dynasty", "House"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    num_words = int(request.form['option'])
    
    if num_words > len(words):
        return jsonify(error='Not enough words to generate the name')

    # Ensure no duplicate words in the generated name
    selected_words = random.sample(words, num_words)
    restaurant_name = ' '.join(selected_words)
    
    return jsonify(name=restaurant_name)

if __name__ == '__main__':
    app.run(debug=True)