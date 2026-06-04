from flask import Flask, request ,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return "this is is the contact page"

@app.route('/<user_name>')
def show_profile(user_name):
    return f"welcome: {user_name}"

@app.route('/courses/<string:course_name>/<int:course_id>')
def display_course(course_name , course_id):
    return f"welcome to {course_name} course with id: {course_id}"

@app.route('/test_request')
def test_request():
    
    request_url = request.url
    request_method = request.method
    
    return f"""
<h1>Request url:{request_url}</h1>
<h1>Request method:{request_method}</h1>

"""









if __name__ == "__main__":
    app.run(debug=True,port=5001)