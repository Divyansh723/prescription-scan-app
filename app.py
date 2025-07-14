from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from config import Config
from models.nova import invoke_model_api
from urllib.parse import quote as url_quote

app = Flask(__name__)
app.config.from_object(Config)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            
            file.save(filepath)
            image_format = filename.rsplit('.', 1)[1].lower()
            
            prompt_option = request.form.get('prompt_option')
            if prompt_option == 'option1':
                prompt_text = """Extract medicine details from this image of a medicine wrapper. Provide output in strict JSON format without markdown formatting (no ```json). Use the following fields: Medicine, Dosage, Usage, Side Effects, Composition, Warning, Age Preferred, Price, Manufacturing Date, Expiry Date, Storage, Manufacturer. If any field is missing, return it with an empty string remember to only return output only if medicine is present in the image. else return please upload a valid image of a prescription image."""
            else:
                prompt_text = """Extract medicine details from this image of a medicine wrapper. Provide output in strict JSON format without markdown formatting (no ```json). Use the following fields: Medicine, Dosage, Usage, Side Effects, Composition, Warning, Age Preferred, Price, Manufacturing Date, Expiry Date, Storage, Manufacturer. If any field is missing, return it with an empty string remember to only return output only if medicine is present in the image. else return please upload a valid image of a medicine image."""
            print(filepath, image_format, prompt_text)
            extracted_text = invoke_model_api(filepath, image_format, prompt_text)
            print(extracted_text)
            return redirect(url_for('result', filename=filename, text=extracted_text))
    return render_template('index.html')

@app.route('/result')
def result():
    filename = request.args.get('filename')
    text = request.args.get('text')
    return render_template('result.html', filename=filename, text=text)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == '__main__':
    app.run(debug=True)