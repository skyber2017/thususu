from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")
@app.route('/login')
def login():
	return render_template("login/index.html")

@app.route("/login",methods=["POST"])
def check_login():
	if request.method == "POST":
		user = request.form['email']
		password = request.form['password']
		
		return "True"
	return "False"
if __name__=='__main__':
	app.run(debug=True)