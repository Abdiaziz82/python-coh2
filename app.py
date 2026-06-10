from flask import Flask, request ,render_template ,jsonify
from model import db ,Student

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/students' ,methods= ["GET"])
def get_students():
    students  = Student.query.all()

    students_list = [student.to_dict() for student in students]
    return jsonify(students_list),200

@app.route('/students' , methods = ["POST"])
def register_student():
    data = request.get_json()
    
    existing = Student.query.filter_by(email=data["email"]).first()
    if existing:
        return jsonify({"error":"email is already taken"}),409
    
    new_student = Student(
        name = data.get("name"),
        email = data.get("email"),
        course = data.get("course"),
        department = data.get("department")
    )

    db.session.add(new_student)
    db.session.commit()

    return jsonify(new_student.to_dict()),201














# with app.app_context():
#     db.create_all()

#     student_1 = Student(
#         name = "Abdi",
#         email = "abdi1@gmail.com",
#         course = "Computer Science",
#         department = "Computer"
#     )

#     student_2 = Student(
#         name = "Hibo",
#         email = "hibo2@gmail.com",
#         course = "Computer Science",
#         department = "Computer"
#     )
#     db.session.add(student_1)
#     db.session.add(student_2)

#     #save to the db
#     db.session.commit()



# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/contact')
# def contact():
#     return "this is is the contact page"

# @app.route('/<user_name>')
# def show_profile(user_name):
#     return f"welcome: {user_name}"

# @app.route('/courses/<string:course_name>/<int:course_id>')
# def display_course(course_name , course_id):
#     return f"welcome to {course_name} course with id: {course_id}"

# @app.route('/test_request')
# def test_request():
    
#     request_url = request.url
#     request_method = request.method
    
#     return f"""
# <h1>Request url:{request_url}</h1>
# <h1>Request method:{request_method}</h1>

# """









if __name__ == "__main__":
    app.run(debug=True,port=5001)