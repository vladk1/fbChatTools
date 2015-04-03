from flask import Flask
from flask import request, redirect, url_for
from flask import jsonify, send_from_directory
from werkzeug import secure_filename

import subprocess
import os
import codecs

from api import search_people
from api import search_tags

UPLOAD_FOLDER = 'src/files/fbmessages/'
JSONS_FOLDER = 'src/files/tfidf/jsons/'

ALLOWED_EXTENSIONS = set(['htm'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/src/files/<path:path>')
def send_js(path):
    return send_from_directory('src/files', path)




@app.route('/matrix')
def matrixa():
    return app.send_static_file('matrix.html')



@app.route('/')
def index_page():
    return """hello. <a href='upload'>upload messages</a></br></br>
              <a href='search_people'>search people</a>
              <a href='search_tags'>search tags</a>"""


@app.route('/run')
def run():
    ret = subprocess.Popen('java -jar fbchat.jar',
                           shell=True, stdout=subprocess.PIPE).stdout.read()

    return 'parsing done! the files have been created!'


def allowed_file(filename):
    return '.' in filename and \
      filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/search_people', methods=['POST', 'GET'])
def search_people_page():
    if request.method == 'POST':
        keyword = request.form['keyword']

        return search_people(JSONS_FOLDER, keyword)

    elif request.method == 'GET':
        return app.send_static_file('search_people.html')


@app.route('/search_tags', methods=['POST', 'GET'])
def search_tags_page():
    if request.method == 'POST':
        keyword = request.form['keyword']

        return search_tags(JSONS_FOLDER, keyword)

    elif request.method == 'GET':
        return app.send_static_file('search_tags.html')

@app.route('/shutterstock', methods=['POST', 'GET'])
def shutterstock():
    if request.method == 'POST':
        keyword = request.form['keyword']

        return search_tags(JSONS_FOLDER, keyword)

    elif request.method == 'GET':
      return app.send_static_file('shutterstock.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file_page():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return redirect(url_for('run'))
    return '''<!doctype html>
              <title>Upload Messages</title>
              <h1>Upload your Facebook Messages .htm file</h1>
              <form action="" method=post enctype=multipart/form-data>
                <p><input type=file name=file>
                   <input type=submit value=Upload>
              </form>
            '''

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0')
