from flask import Flask,render_template,request,session,url_for,flash,redirect,jsonify
from flaskext.mysql import MySQL
import json

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'thususu3115'
app.config['MYSQL_DATABASE_PASSWORD'] = 'thelove123'
app.config['MYSQL_DATABASE_DB'] = 'thususu3115'
app.config['MYSQL_DATABASE_HOST'] = '115.84.183.142'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
mysql.init_app(app)

@app.route('/check')
def check():
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT * FROM users")
	data = cursor.fetchone()
	return str(data[3])

@app.route('/')
def index():
	return render_template('home/index.html')

@app.route('/login')
def login():
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