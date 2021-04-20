from flask import Flask , render_template ,request, redirect,url_for
import pymysql

app = Flask(__name__)

#Path เว็บ
@app.route('/')
def Home():
    #เชื่อม Database MySQL
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='usersdb'
    )
    PyText = "Python"
    FlText = "Flask"
    
    with conn:
        #Cursorลูกศรในการดึงข้อมูล
        cur = conn.cursor()
        cur.execute("SELECT * FROM `user`")
        rows = cur.fetchall()
    return render_template('index.html',datas = rows,data1 = PyText,data2 =FlText)

@app.route('/register')
def register():
    return render_template('reg.html')


#เพิ่มข้อมูล ยิง API
@app.route('/insert',methods=['POST'])
def insert():
    #เชื่อม Database MySQL
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='usersdb'
    )
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        phone = request.form['phone']
        with conn.cursor() as curson:
            sql = "INSERT INTO `user`(`fname`, `lname`, `age`, `phone`) VALUES (%s,%s,%s,%s)"
            curson.execute(sql,(fname,lname,age,phone))
            #สั่งเปลี่ยนแปลง
            conn.commit()
        return redirect(url_for('Home'))

#ลบข้อมูล ยิง API
@app.route('/delete/<string:id_data>',methods=['GET'])
def delete(id_data):
    #เชื่อม Database MySQL
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='usersdb'
    )
    with conn:
        #Cursorลูกศรในการดึงข้อมูล
        cur = conn.cursor()
        cur.execute("DELETE FROM `user` WHERE id=%s",(id_data))
        conn.commit()
    return redirect(url_for('Home'))

#Updateข้อมูล ยิง API
@app.route('/update',methods=['POST'])
def Update():
    #เชื่อม Database MySQL
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='usersdb'
    )
    if request.method == "POST":
        id = request.form['id']
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        phone = request.form['phone']
        with conn.cursor() as curson:
            sql = "UPDATE `user` SET `fname`=%s,`lname`=%s,`age`=%s,`phone`=%s WHERE `id`=%s"
            curson.execute(sql,(fname,lname,age,phone,id))
            #สั่งเปลี่ยนแปลง
            conn.commit()
        return redirect(url_for('Home'))


if __name__ == "__main__":
    app.run(debug=True)