from flask import Flask,request,jsonify
import mysql.connector

app=Flask(__name__)
db=mysql.connector.connect(host='localhost',user='root',password='',database='tasks')
cursor=db.cursor(dictionary=True)

@app.route('/tasks',methods=['GET'])
def get_tasks():
    cursor.execute('SELECT * FROM tasks')
    return jsonify(cursor.fetchall())

@app.route('/tasks',methods=['POST'])
def add_task():
    data=request.json
    cursor.execute('INSERT INTO tasks(title,description,status) VALUES(%s,%s,%s)',(data['title'],data['description'],data['status']))
    db.commit()
    return jsonify({'message':'Task added'})

app.run(debug=True)