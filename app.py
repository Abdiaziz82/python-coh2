from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World !"

@app.route('/about')
def about():
    return "this is is the about page"

@app.route('/contact')
def contact():
    return "this is is the contact page"

@app.route('/user/<user_name>')
def show_profile(user_name):
    return f"welcome: {user_name}"

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