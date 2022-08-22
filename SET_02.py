@app.route('/inserts',methods = ['POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into connection001.tasktable  values(%s , %s)",(name ,number))
        mydb.commit()
        return jsonify(str('succesfully inserted'))
