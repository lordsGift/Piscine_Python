# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_secs.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: earendil <earendil@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 22:58:10 by mmarinel          #+#    #+#              #
#    Updated: 2022/05/21 10:35:03 by earendil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from functools import reduce
from tokenize import String

class	WrongInputException(Exception):
	def __init__(self, msg: String) -> None:
		super().__init__("WrongInputException: " + msg)

def to_secs(time):
	index, t = time
	return (pow(60, index) * t)

def sum(n, m):
	return (n + m)

def as_int(n):
	if (not n.isdigit()):
		raise WrongInputException("alphanumerical argument found")
	return (int(n))

try:
	if len(sys.argv) != 4:
		raise WrongInputException("Wrong number of arguments (3 expected)")
	else:
		print(reduce(sum, map(to_secs, list(enumerate(map(as_int, sys.argv[1:])))), 0))
except WrongInputException as e:
	print(e)