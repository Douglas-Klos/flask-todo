from datetime import datetime
from model import db, User, Task
from passlib.hash import pbkdf2_sha256

db.connect()
db.drop_tables([User, Task])
db.create_tables([User, Task])

User(name="admin", password=pbkdf2_sha256.hash("password")).save()
User(name="doug", password=pbkdf2_sha256.hash("doug")).save()

Task(name="Do the laundry.").save()
Task(name="Do the dishes.").save()
Task(name="Finish Activity 1.").save()
Task(name="Finish Assignment 1.").save()
