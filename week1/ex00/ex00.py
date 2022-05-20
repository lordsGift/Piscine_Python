# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex00.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: earendil <earendil@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 22:58:17 by mmarinel          #+#    #+#              #
#    Updated: 2022/05/20 23:03:04 by earendil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from functools import reduce
from tokenize import String

class	IllegalArgumentException(Exception):
	def __init__(self, msg: String) -> None:
		super().__init__("IllegalArgumentException: " + msg)

class	OutofBoundException(Exception):
	def __init__(self, msg: String) -> None:
		super().__init__("OutofBoundException: " + msg)

def sum(acc, m):
	return (acc + m)

def as_int(n):
	if (not n.isdigit()):
		raise IllegalArgumentException("alphabetical argument found")
	return (int(n))

try:
	if len(sys.argv) != 3:
		raise OutofBoundException("too many / to few arguments found (3 expected)")
	else:
		print(reduce(sum, map(as_int, sys.argv[1:]), 0))
except (IllegalArgumentException, OutofBoundException) as e:
		print(e)