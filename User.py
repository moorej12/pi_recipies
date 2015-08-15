import AuthorUser
import ConsumerUser

class User():

	def __init__(self):
		self._name = ""
		self._pass = ""
		self._cmd = None
		self._recipies = []

	@staticmethod
	def createUser():
		type = input("Would you like to be an author (a) or a consumer (c)? ")
		newUser = None
		if(type == "a"):
			newUser = AuthorUser()
		else:
			newUser = ConsumerUser()
		newUser._name = input("Please enter a username: ")
		newUser._password = input("Please enter a password: ")
		return newUser

	def checkLogin(self, name, password):
		if(self._name == name):
			if(self._pass == password):
				return True
			else:
				return False
		else:
			return False

	def run(self):
		return True