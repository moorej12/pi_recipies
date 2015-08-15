import cmd
import User

class CmdPrompt(cmd.Cmd):
	"""Simple command processor"""

	def do_register(self, line):
		newUser = User.User.createUser()
		newUser.run()

	def do_login(self, line):
		print("logging in")

	def do_load(self, line):
		print("loading file")

	def do_storage(self, line):
		print("setting storage file")

	def do_exit(self, line):
		return True

class CmdPrompt2(cmd.Cmd):

	def do_exit(self, line):
		return True

	def do_print(self, line):
		print("hi from 2")

if __name__ == '__main__':
	CmdPrompt().cmdloop()