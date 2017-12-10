from datetime import date
class person:
	name=""
	gender = 0
	birthdate = date.today
	def __init__(self, name, gender, birthdate):
		self.name = name
		self.gender = gender
		self.birthdate = birthdate
	def __str__(self):
		return '姓名是%s，性别是%s，出生日期是%s' % (self.name, self.get_gender(), self.birthdate)
	def get_gender(self):
		return '男' if self.gender else '女'

class student(person):
	classname=""
	def __init__(self, name, gender, birthdate, classname):
		self.classname = classname
		return super().__init__(name, gender, birthdate)
	def __str__(self):
		return super().__str__() + '班级是%s' % self.classname