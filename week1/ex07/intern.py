# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    intern.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmarinel <mmarinel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/19 18:21:22 by mmarinel          #+#    #+#              #
#    Updated: 2022/05/21 16:34:59 by mmarinel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class	Intern:
	def	__init__(self, name = "My name? I’m nobody, an \
intern, I have no name."):
		self.Name = name
	def	__str__(self):
		return (self.Name)
	class	Coffee:
		def	__str__(self):
			return ("This is the worst coffee you ever tasted.")
	def	work(self):
		raise Exception("I'm just an intern, I can't do that...")
	def	make_coffee(self):
		return (self.Coffee())

intern_john_doe = Intern()
intern_mark = Intern("Mark")

print (intern_john_doe)
print (intern_mark)

print (intern_mark.make_coffee())
try:
	print (intern_john_doe.work())
except Exception as exc:
	print(f"exception: {(exc)}")