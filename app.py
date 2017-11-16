from flask import Flask,render_template,request,session,url_for,flash,redirect,jsonify
from flaskext.mysql import MySQL
from datetime import datetime
import json
mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'thususu3115'
app.config['MYSQL_DATABASE_PASSWORD'] = 'thelove123'
app.config['MYSQL_DATABASE_DB'] = 'thususu3115'
app.config['MYSQL_DATABASE_HOST'] = '115.84.183.142'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
mysql.init_app(app)

@app.route('/add',methods=["POST"])
def add():
	if request.method == "POST":
		data = request.json
		user = data['user']
		title= data['title']
		deadline = data['deadline']
		content = data['content']
		init = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		#json = json.dumps({title:content})
		if title:
			cursor = mysql.connect().cursor()
			#cursor.execute("INSERT INTO job VALUES('','%s','%s','%s','%s')"%(user,init,deadline,init,json))
			#mysql.connect().commit()
			return jsonify(status=0,message="Đã thêm thành công!")
			#return jsonify(status=0,message="INSERT INTO job VALUES('','%s','%s','%s','%s')"%(user,init,deadline,init,json))
		else:
			return jsonify(status=1,message="Tiêu đề không được bỏ trống!")



@app.route('/check')
def check():
	return render_template('check.html')

@app.route('/')
def index():
	return render_template('home/index.html')

@app.route('/login')
def login():
	if session.get('user'):
		return redirect('')
	return render_template('/login/index.html')

@app.route("/login",methods=["POST"])
def check_login():
	if request.method == "POST":
		user = request.form['email']
		password = request.form['password']
		if user and password:
			cursor = mysql.connect().cursor()
			cursor.execute("SELECT * FROM users WHERE username='%s' AND password='%s'"%(user,password))
			data = cursor.fetchone()
			if data is not None:
				session['user'] = user
				if str(data[3]):
					session['is_admin'] = 1
				else:
					session['is_admin'] = 0

				return jsonify(mess="Đăng nhập thành công!",result=1)
			else:
				return jsonify(mess="Đăng nhập thất bại!")
		return	jsonify(mess="Không được bỏ trống!")

@app.route('/logout')
def logout():
	if session.get('user'):
		session['user'] = ""
		session['is_admin'] = 0
	return redirect("/")
if __name__=='__main__':

	app.run(debug=True)