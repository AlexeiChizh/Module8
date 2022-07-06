

from peewee import *

conn = SqliteDatabase('ORM.sqlite')

class Student(Model):
	id = PrimaryKeyField(column_name='student_id', unique = True)
	name = CharField(column_name = 'lastname')
	surname = CharField(column_name = 'surname')
	age = IntegerField(column_name = 'age')
	city = CharField(column_name = 'city')
	class Meta:
		database = conn
		
class Course(Model):
	id = PrimaryKeyField(column_name = 'course_id', unique = True)
	course_name = CharField(column_name = 'course_name')
	time_start = CharField(column_name = 'time_start')
	time_end = IntegerField(column_name = 'time_end')
	
	class Meta:
		database = conn

class Student_course(Model):
	student_id = ForeignKeyField(Student)
	course_id = ForeignKeyField(Course)
	
	class Meta:
		database = conn

Student.create_table()
Course.create_table()
Student_course.create_table()

Students = [
{ 'id': 1, 'name':'Max', 'surname':'Brooks', 'age': 24, 'city':'Spb'},
 {'id': 2, 'name':'John', 'surname':'Stones', 'age': 15, 'city':'Spb'},
 {'id': 3, 'name':'Andy', 'surname':'Wings', 'age': 45, 'city':'Manchester'},
 {'id': 4, 'name':'Kate', 'surname':'Brooks', 'age': 34, 'city':'Spb'}
]

Student.insert_many(Students).execute()

Courses = [
{'id':1, 'course_name':'python', 'time_start':'21.07.21', 'time_end':'21.08.21'},
{'id':2, 'course_name':'java', 'time_start':'13.07.21', 'time_end':'16.08.21'}
]

Course.insert_many(Courses).execute()

s = Student.select()
c = Course.select()

Student_courses = [
{ 'student_id': s[0], 'course_id': c[0]},
{ 'student_id': s[1], 'course_id': c[0]},
{ 'student_id': s[2], 'course_id': c[0]},
{ 'student_id': s[3], 'course_id': c[1]}
]

Student_course.insert_many(Student_courses).execute()

Student_30 = (Student.select().where(Student.age > 30))

print(f'Студенты старше 30 лет:')
for a in Student_30:
	print(a.name, a.surname)

Student_python = (Student.select().join(Student_course).where(Student_course.course_id == 1))

print(f'Студенты курса Python:')
for b in Student_python:
	print (b.name, b.surname)

Student_python_spb = Student.select().join(Student_course).where(Student_course.course_id == 1, Student.city == 'Spb')

print('Студенты курса Python из СПб:')
for c in Student_python_spb:
	print (c.name, c.surname)


conn.close()