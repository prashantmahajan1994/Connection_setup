import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user = 'root' , passwd = "India@2022")
cursor = mydb.cursor()
cursor.execute("create database if not exists connection001")
cursor.execute("create table if not exists connection001.tasktable (name varchar(30) , number int)")

from flask import Flask ,request,jsonify

app = Flask(__name__)
@app.route('/inserts',methods = ['POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into connection001.tasktable  values(%s , %s)",(name ,number))
        mydb.commit()
        return jsonify(str('succesfully inserted'))

if __name__ == '__main__':
    app.run()

    VDFGD