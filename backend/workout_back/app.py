import flask
from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/uploadFile', methods=['POST'])
def uploadFile():
    name = request.form.get('name')
    file = request.files.get('file')

    conn = pymysql.connect(host='54.180.119.9', user='root1', password='1234', db='workout', charset='utf8')
    cur = conn.cursor()
    curr_date = datetime.now().strftime('%Y-%m-%d')

    sql = 'INSERT INTO user_info (name, File_name, uploaddate) VALUES(%s, %s, %s)'
    # vals = ('이종ㅎ', 'test_image.jpg', curr_date)
    vals = (name, file.filename, curr_date)
    cur.execute(sql, vals)

    conn.commit()
    conn.close()
    
    return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)