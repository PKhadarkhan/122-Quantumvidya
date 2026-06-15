import math
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, render_template, request, jsonify, session,redirect,url_for,Response,flash
import os
import sqlite3
import json
import io
import numpy as np
from enum import Enum
import warnings
import threading
import utils
import random
import time
import cv2
import keyboard

#variables
studentInfo=None
camera=None
profileName=None

#Flak's Application Confguration
warnings.filterwarnings("ignore")
app = Flask(__name__, template_folder='../../Frontend/ExamTemplates', static_folder='../../Frontend/ExamStatic')
app.secret_key = 'xyz'
# app.config["MONGO_URI"] = "mongodb://localhost:27017/"
os.path.dirname("../templates")

#Flak's Database Configuration
def get_db_connection():
    conn = sqlite3.connect('database.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Email TEXT NOT NULL,
            Password TEXT NOT NULL,
            Role TEXT NOT NULL,
            Department TEXT
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Timer INTEGER NOT NULL,
            Department TEXT NOT NULL DEFAULT 'Computer'
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Subject_ID INTEGER NOT NULL,
            Title TEXT NOT NULL,
            Choice1 TEXT NOT NULL,
            Choice2 TEXT NOT NULL,
            Choice3 TEXT NOT NULL,
            Choice4 TEXT NOT NULL,
            Answer TEXT NOT NULL,
            FOREIGN KEY(Subject_ID) REFERENCES subjects(ID) ON DELETE CASCADE
        )
    ''')
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM students")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO students (Name, Email, Password, Role) VALUES ('Admin', 'admin@admin.com', 'admin', 'ADMIN')")
        cur.execute("INSERT INTO students (Name, Email, Password, Role) VALUES ('Student', 'student@student.com', 'student', 'STUDENT')")
    conn.commit()
    conn.close()

init_db()

executor = ThreadPoolExecutor(max_workers=4)  # Adjust the number of workers as needed

#Function to show face detection's Rectangle in Face Input Page
def capture_by_frames():
    global camera
    utils.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        success, frame = utils.cap.read()  # read the camera frame
        detector=cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
        faces=detector.detectMultiScale(frame,1.2,6)
         #Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#Function to run Cheat Detection when we start run the Application
@app.before_request
def start_loop():
    task1 = executor.submit(utils.cheat_Detection2)
    task2 = executor.submit(utils.cheat_Detection1)
    task3 = executor.submit(utils.fr.run_recognition)
    task4 = executor.submit(utils.a.record)


#Login Related
@app.route('/')
def main():
    return render_template('login.html')

@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        department = request.form.get('department')
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM students WHERE Email=?", (email,))
        if cur.fetchone() is not None:
            conn.close()
            flash('Email is already registered. Please login.', category='error')
            return redirect(url_for('signup'))
            
        cur.execute("INSERT INTO students (Name, Email, Password, Role, Department) VALUES (?, ?, ?, ?, ?)", (name, email, password, role, department))
        conn.commit()
        conn.close()
        
        flash('Registration successful! Please login.', category='success')
        if role == 'ADMIN':
            return redirect(url_for('admin_login'))
        else:
            return redirect(url_for('main'))
            
    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def login():
    global studentInfo
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students where Email=? and Password=?", (username, password))
        data = cur.fetchone()
        conn.close()
        if data is None:
            flash('Your Email or Password is incorrect, try again.', category='error')
            return redirect(url_for('main'))
        else:
            studentInfo={ "Id": data['ID'], "Name": data['Name'], "Email": data['Email'], "Password": data['Password']}
            role = data['Role']
            if role == 'STUDENT':
                utils.Student_Name = data['Name']
                session['department'] = data['Department']
                return redirect(url_for('rules'))
            else:
                return redirect(url_for('adminStudents'))

@app.route('/logout')
def logout():
    return render_template('login.html')

#Student Related
@app.route('/rules')
def rules():
    conn = get_db_connection()
    department = session.get('department', 'Computer')
    subjects = conn.execute('SELECT * FROM subjects WHERE Department = ?', (department,)).fetchall()
    conn.close()
    return render_template('ExamRules.html', subjects=subjects)

@app.route('/setSubject', methods=['POST'])
def setSubject():
    session['subject_id'] = request.form.get('subject_id')
    return redirect(url_for('faceInput'))

@app.route('/faceInput')
def faceInput():
    return render_template('ExamFaceInput.html')

@app.route('/video_capture')
def video_capture():
    return Response(capture_by_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/saveFaceInput')
def saveFaceInput():
    global profileName
    if utils.cap.isOpened():
        utils.cap.release()
    cam = cv2.VideoCapture(0)
    success, frame = cam.read()  # read the camera frame
    profileName=f"{studentInfo['Name']}_{utils.get_resultId():03}" + "Profile.jpg"
    cv2.imwrite(profileName,frame)
    utils.move_file_to_output_folder(profileName,'Profiles')
    cam.release()
    return redirect(url_for('confirmFaceInput'))

@app.route('/confirmFaceInput')
def confirmFaceInput():
    profile = profileName
    utils.fr.encode_faces()
    return render_template('ExamConfirmFaceInput.html', profile = profile)

@app.route('/systemCheck')
def systemCheck():
    return render_template('ExamSystemCheck.html')

@app.route('/systemCheck', methods=["POST"])
def systemCheckRoute():
    if request.method == 'POST':
        examData = request.json
        output = 'exam'
        if 'Not available' in examData['input'].split(';'): output = 'systemCheckError'
    return jsonify({"output": output})

@app.route('/systemCheckError')
def systemCheckError():
    return render_template('ExamSystemCheckError.html')

@app.route('/exam')
def exam():
    utils.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    keyboard.hook(utils.shortcut_handler)
    return render_template('Exam.html')

@app.route('/exam', methods=["POST"])
def examAction():
    link = ''
    if request.method == 'POST':
        examData = request.json
        if(examData['input']!=''):
            utils.Globalflag= False
            utils.cap.release()
            utils.write_json({
                "Name": ('Prohibited Shorcuts (' + ','.join(list(dict.fromkeys(utils.shorcuts))) + ') are detected.'),
                "Time": (str(len(utils.shorcuts)) + " Counts"),
                "Duration": '',
                "Mark": (1.5 * len(utils.shorcuts)),
                "Link": '',
                "RId": utils.get_resultId()
            })
            utils.shorcuts=[]
            trustScore= utils.get_TrustScore(utils.get_resultId())
            totalMark=  math.floor(float(examData['input'])* 6.6667)
            if trustScore >=30:
                status="Fail(Cheating)"
                link = 'showResultFail'
            else:
                if totalMark < 50:
                    status="Fail"
                    link = 'showResultFail'
                else:
                    status="Pass"
                    link = 'showResultPass'
            utils.write_json({
                "Id": utils.get_resultId(),
                "Name": studentInfo['Name'],
                "TotalMark": totalMark,
                "TrustScore": max(100-trustScore, 0),
                "Status": status,
                "Date": time.strftime("%Y-%m-%d", time.localtime(time.time())),
                "StId": studentInfo['Id'],
                "Link" : profileName
            },"result.json")
            resultStatus= studentInfo['Name']+';'+str(totalMark)+';'+status+';'+time.strftime("%Y-%m-%d", time.localtime(time.time()))
        else:
            utils.Globalflag = True
            resultStatus=''
    return jsonify({"output": resultStatus, "link": link})

@app.route('/showResultPass/<result_status>')
def showResultPass(result_status):
    return render_template('ExamResultPass.html',result_status=result_status)

@app.route('/showResultFail/<result_status>')
def showResultFail(result_status):
    return render_template('ExamResultFail.html',result_status=result_status)

#Admin Related
@app.route('/adminResults')
def adminResults():
    results = utils.getResults()
    return render_template('Results.html', results=results)

@app.route('/adminResultDetails/<resultId>')
def adminResultDetails(resultId):
    result_Details = utils.getResultDetails(resultId)
    return render_template('ResultDetails.html', resultDetials=result_Details)

@app.route('/adminResultDetailsVideo/<videoInfo>')
def adminResultDetailsVideo(videoInfo):
    return render_template('ResultDetailsVideo.html', videoInfo= videoInfo)

@app.route('/adminStudents')
def adminStudents():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students where Role='STUDENT'")
    data = cur.fetchall()
    conn.close()
    return render_template('Students.html', students=data)

@app.route('/insertStudent', methods=['POST'])
def insertStudent():
    if request.method == "POST":
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO students (Name, Email, Password, Role) VALUES (?, ?, ?, ?)", (name, email, password,'STUDENT'))
        conn.commit()
        conn.close()
        return redirect(url_for('adminStudents'))

@app.route('/deleteStudent/<string:stdId>', methods=['GET'])
def deleteStudent(stdId):
    flash("Record Has Been Deleted Successfully")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE ID=?", (stdId,))
    conn.commit()
    conn.close()
    return redirect(url_for('adminStudents'))

@app.route('/updateStudent', methods=['POST', 'GET'])
def updateStudent():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
               UPDATE students
               SET Name=?, Email=?, Password=?
               WHERE ID=?
            """, (name, email, password, id_data))
        conn.commit()
        conn.close()
        return redirect(url_for('adminStudents'))

# Admin Subjects
@app.route('/adminSubjects')
def adminSubjects():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM subjects")
    data = cur.fetchall()
    conn.close()
    return render_template('Subjects.html', subjects=data)

@app.route('/insertSubject', methods=['POST'])
def insertSubject():
    if request.method == "POST":
        name = request.form['name']
        timer = request.form['timer']
        department = request.form['department']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO subjects (Name, Timer, Department) VALUES (?, ?, ?)", (name, timer, department))
        conn.commit()
        conn.close()
        return redirect(url_for('adminSubjects'))

@app.route('/deleteSubject/<string:subId>', methods=['GET'])
def deleteSubject(subId):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM subjects WHERE ID=?", (subId,))
    conn.commit()
    conn.close()
    return redirect(url_for('adminSubjects'))

@app.route('/updateSubject', methods=['POST', 'GET'])
def updateSubject():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        timer = request.form['timer']
        department = request.form['department']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
           UPDATE subjects
           SET Name=?, Timer=?, Department=?
           WHERE ID=?
        """, (name, timer, department, id_data))
        conn.commit()
        conn.close()
        return redirect(url_for('adminSubjects'))

# Admin Questions
@app.route('/adminQuestions')
def adminQuestions():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT q.*, s.Name as SubjectName FROM questions q JOIN subjects s ON q.Subject_ID = s.ID")
    data = cur.fetchall()
    cur.execute("SELECT * FROM subjects")
    subjects = cur.fetchall()
    conn.close()
    return render_template('Questions.html', questions=data, subjects=subjects)

@app.route('/insertQuestion', methods=['POST'])
def insertQuestion():
    if request.method == "POST":
        sub_id = request.form['subject_id']
        title = request.form['title']
        c1 = request.form['choice1']
        c2 = request.form['choice2']
        c3 = request.form['choice3']
        c4 = request.form['choice4']
        ans = request.form['answer']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO questions (Subject_ID, Title, Choice1, Choice2, Choice3, Choice4, Answer) VALUES (?, ?, ?, ?, ?, ?, ?)", (sub_id, title, c1, c2, c3, c4, ans))
        conn.commit()
        conn.close()
        return redirect(url_for('adminQuestions'))

@app.route('/deleteQuestion/<string:qId>', methods=['GET'])
def deleteQuestion(qId):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM questions WHERE ID=?", (qId,))
    conn.commit()
    conn.close()
    return redirect(url_for('adminQuestions'))

@app.route('/updateQuestion', methods=['POST'])
def updateQuestion():
    if request.method == 'POST':
        id_data = request.form['id']
        sub_id = request.form['subject_id']
        title = request.form['title']
        c1 = request.form['choice1']
        c2 = request.form['choice2']
        c3 = request.form['choice3']
        c4 = request.form['choice4']
        ans = request.form['answer']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE questions SET Subject_ID=?, Title=?, Choice1=?, Choice2=?, Choice3=?, Choice4=?, Answer=? WHERE ID=?", (sub_id, title, c1, c2, c3, c4, ans, id_data))
        conn.commit()
        conn.close()
        return redirect(url_for('adminQuestions'))

@app.route('/api/getExamData')
def getExamData():
    subject_id = session.get('subject_id')
    if not subject_id:
        return jsonify({"error": "No subject selected"}), 400
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM subjects WHERE ID=?", (subject_id,))
    subject = cur.fetchone()
    cur.execute("SELECT * FROM questions WHERE Subject_ID=?", (subject_id,))
    questions = cur.fetchall()
    conn.close()
    if not subject:
        return jsonify({"error": "Subject not found"}), 404
    
    questions_list = []
    for q in questions:
        questions_list.append({
            "id": q["ID"],
            "title": q["Title"],
            "choices": [q["Choice1"], q["Choice2"], q["Choice3"], q["Choice4"]],
            "answer": q["Answer"]
        })
    
    return jsonify({
        "subject_name": subject["Name"],
        "timer": subject["Timer"],
        "questions": questions_list
    })

if __name__ == '__main__':
    app.run(debug=True)