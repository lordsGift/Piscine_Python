# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_sum.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmarinel <mmarinel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 22:58:17 by mmarinel          #+#    #+#              #
#    Updated: 2022/05/21 16:34:24 by mmarinel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from functools import reduce
from tokenize import String

class	WrongInputException(Exception):
	def __init__(self, msg: String) -> None:
		super().__init__("WrongInputException: " + msg)

def sum(acc, m):
	return (acc + m)

def as_int(n):
	if (not n.isdigit()):
		raise WrongInputException("alphanumerical argument found")
	return (int(n))

try:
	if len(sys.argv) != 3:
		raise WrongInputException("too many / to few arguments found (2 expected)")
	else:
		print(reduce(sum, map(as_int, sys.argv[1:]), 0))
except WrongInputException as e:
		print(e)