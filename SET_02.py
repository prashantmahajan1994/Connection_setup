from flask import Flask, request, jsonify
import mysql.connector as conn

app=Flask(__name__)
mydb=conn.connect(host="localhost", user="root", passwd="India@2022")
cursor=mydb.cursor()
cursor.execute(" create database if not exists Rajveer ")
cursor.execute(" create table if not exists Rajveer.table1(name varchar(30), mob_no int) ")

@app.route('/insert',methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        mob_no = request.json['mob_no']
        cursor.execute(" insert into Rajveer.table1 values(%s,  %s)" ,(name,mob_no))
        mydb.commit()
        return jsonify(str('succes'))

if __name__== '__main__':
    app.run()