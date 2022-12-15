from flask import Flask, request, Response
from db import db_init, db
from werkzeug.utils import secure_filename
from models import Img
app = Flask(__name__)

app.config['SQLALCHEMY_DATABSE_URL'] = 'sqlite:///img.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_init(app)


@app.route('/')
def home():
    return 'Hello world'


@app.route('/upload', methods=['POST'])
def upload():
    pic = request.files['pic']
    if not pic:
        return 'No image uploaded', 400
    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype

    img = Img(img=pic.read(), mimetype=mimetype, name=filename)
    db.session.add(img)
    db.session.commit

    return 'Image has been uploaded!', 200


@app.route('/get-gif', methods=['GET'])
def get_image():
    final_output = []
    args = request.args
    text = args.get('text', default='', type=str)
    if text == '':
        jsonify({'error': 'Enter a text Input'})
    text_list = text.split()
    for word in text_list:
        img = Img.query.filter_by(name=word).first()
        if not img:
            for char in word:
                temp = Img.query.filter_by(name=char).first()
                final_output.append(temp.img, mimetype=temp.mimetype)
        else:
            final_output.append(img.img, mimetype=img.mimetype)
