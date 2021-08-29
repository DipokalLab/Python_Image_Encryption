from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
upload_dir = './uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename(upload_dir+file.filename))
        return jsonify(
            status= 1,
            filename= file.filename
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8823) 