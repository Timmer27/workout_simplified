import flask
from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
from datetime import datetime
from collections import defaultdict
import os
import re
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def getMountedInfo():
    # DB정보 받아서 화면 출력
    conn = pymysql.connect(host='54.180.119.9', user='root1', password='1234', db='workout', charset='utf8')

    # sql = 'SELECT * FROM user_info'
    sql_workoutCnt = 'SELECT name, COUNT(*) FROM user_info WHERE month(uploaddate) = DATE_FORMAT(NOW(), "%m") GROUP BY NAME'

    res_dict = defaultdict(dict)
    result_cnt = defaultdict(int)
    result_todayPic = defaultdict(list)
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql_workoutCnt)
            result = cur.fetchall()
            for data in result:
                result_cnt[data[0]] = data[-1]
    result_cnt_sorted = sorted(result_cnt.items(), key=lambda x : x[1], reverse=True)
    
    conn = pymysql.connect(host='54.180.119.9', user='root1', password='1234', db='workout', charset='utf8')

    sql_workoutToday = "SELECT name, file_name FROM user_info WHERE uploaddate = DATE_FORMAT(NOW(), '%y-%m-%d')"
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql_workoutToday)
            result = cur.fetchall()
            for num, data in enumerate(result):
                result_todayPic[num] = [data[0], data[1]]

    result_cnt_sorted = sorted(result_cnt.items(), key=lambda x : x[1], reverse=True)

    res_dict['result_cnt'] = result_cnt_sorted
    res_dict['result_todayPic'] = result_todayPic

    return res_dict


@app.route('/uploadFile', methods=['POST'])
def uploadFile():
    saved_path = './assets/images/'
    milisec = str(time.time()).replace('.', '')
    name = request.form.get('name')
    file = request.files.get('file')
    
    extension = '.' + file.filename[-4:].split('.')[-1]
    fileName_origin = file.filename[:-4]

    fileName_adj = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", fileName_origin).replace(' ', '')
    file_name = fileName_adj + milisec + extension

    conn = pymysql.connect(host='54.180.119.9', user='root1', password='1234', db='workout', charset='utf8')
    cur = conn.cursor()

    # 하루 여러장 업로드 시
    sql_reg = f"SELECT COUNT(1) FROM user_info where uploaddate = DATE_FORMAT(NOW(), '%y-%m-%d') AND name = '{name}' GROUP BY name, uploaddate"
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql_reg)
            result = cur.fetchall()
            
            if len(result) >= 1:
                return '하루 2연속 업로드 안됨 ㄴㄴ'

    curr_date = datetime.now().strftime('%Y-%m-%d')

    sql = 'INSERT INTO user_info (name, File_name, uploaddate) VALUES(%s, %s, %s)'
    vals = (name, file_name, curr_date)
    cur.execute(sql, vals)

    conn.commit()
    conn.close()

    os.makedirs(saved_path, exist_ok=True)
    file.save(saved_path + file_name)
    # file.save(os.path.join(saved_path, file_name))
    
    return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)