from flask_sqlalchemy import SQLAlchemy

#initialize sqlALchemy instance
db = SQLAlchemy()

class Student(db.Model):

    __tablename__ = "students"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30),nullable = False)
    email = db.Column(db.String(100),nullable = False,unique = True)
    course = db.Column(db.String(120),nullable =True)
    department = db.Column(db.String(80),nullable =True)


    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "course":self.course,
            "department":self.department
        }