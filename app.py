from flask import Flask,render_template,request,session,url_for,flash,redirect,jsonify,json
from flaskext.mysql import MySQL
from datetime import datetime

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'thususu3115'
app.config['MYSQL_DATABASE_PASSWORD'] = 'thelove123'
app.config['MYSQL_DATABASE_DB'] = 'thususu3115'
app.config['MYSQL_DATABASE_HOST'] = '115.84.183.142'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
mysql.init_app(app)

@app.route('/delete',methods=["POST"])
def delete():
	try:
		if request.method == "POST":
			id = request.form['id']
			user = request.form['user']
			if user == session.get('user') or session.get("is_admin") == 1:
				conn = mysql.connect()
				cursor = conn.cursor()
				cursor.execute("SELECT * FROM job WHERE id='"+id+"'")
				data = cursor.fetchone()
				if data is None:
					return jsonify(status=1,message="Cái bạn định xóa không tồn tại hoặc đã bị xóa!")
				else:
					cursor.execute("DELETE FROM job WHERE id='"+id+"'")
					conn.commit()
					return jsonify(status=0,message="Đã xóa thành công!")
			else:
				return jsonify(status=1,message="Bạn không đủ quyền truy cập!")

	except:
		return jsonify(status=1,message="Lỗi không xác định!")
@app.route('/info',methods=["POST"])
def info():
	try:
		if request.method=="POST":
			if session.get('user') and session.get('user') == str(request.form['user']) or session.get('is_admin') == 1:
				with mysql.connect().cursor() as cursor:
					cursor.execute("SELECT content FROM job WHERE id='"+str(request.form['id'])+"'")
					data = cursor.fetchone()
					return jsonify(status=0,content=data[0])
			else:
				return jsonify(status=1,message="Bạn không đủ quyền để xem!")
	except:
		return jsonify(status=1,message="Lỗi không xác định!")
@app.route('/add',methods=["POST"])
def add():
	try:
		
		return jsonify(status=0,message="Chúc mừng! Đã thêm thành công!")
	except:
		return jsonify(status=1,message="Lỗi không xác định!")


@app.route('/check')
def check():
	with mysql.connect().cursor() as cursor:
		cursor.execute("SELECT * FROM job WHERE user='"+session.get('user')+"'")
		data = cursor.fetchall()
		return jsonify(data)

@app.route('/')
def index():
	if session.get('user'):
		with mysql.connect().cursor() as cursor:
			cursor.execute("SELECT * FROM job WHERE user='"+session.get('user')+"' ORDER BY id DESC")
			data = cursor.fetchall()
		return render_template("home/index.html",data=data)
	else:
		return render_template("login/index.html")

@app.route('/login')
def login():
	if session.get('user'):
		return redirect('')
	return render_template('/login/index.html')

@app.route("/login",methods=["POST"])
def check_login():
	try:
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
	except:
		return jsonify(mess="Lỗi không xác định!")

@app.route('/logout')
def logout():
	if session.get('user'):
		session['user'] = ""
		session['is_admin'] = 0
	return redirect("/")
if __name__=='__main__':

	app.run(debug=True)