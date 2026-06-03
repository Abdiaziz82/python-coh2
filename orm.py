import sqlite3
CONN = sqlite3.connect("my_database.db")
CURSOR = CONN.cursor()

class User:
    def __init__(self,name,email,number):
        self.id = None
        self.name = name
        self.email = email
        self.number = number
    
    @classmethod
    def create_table(cls):
        sql = """  

        CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY,  
        name TEXT,
        email TEXT,
        number TEXT
        )

           """
        
        CURSOR.execute(sql)
        CONN.commit()

    def save_to_db(self):
        sql = """
        
        INSERT INTO users(name,email,number) 
        VALUES (?,?,?)
        
        """
        CURSOR.execute(sql, (self.name,self.email,self.number))
        CONN.commit()
        self.id = CURSOR.lastrowid
        

user1 = User("Ahmed", "ahmed@gmail.com", "072415681")
user2 = User("marcelo", "marcelo@gmail.com", "012415681")
user3 = User("halima", "halima@gmail.com", "+26427789765")
user4 = User("anab", "anab@gmail.com", "+26427789765")
User.create_table()
# user1.save_to_db()
# user3.save_to_db()
user4.save_to_db()
print (user4.id)
        
