# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex00.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmarinel <mmarinel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 22:58:17 by mmarinel          #+#    #+#              #
#    Updated: 2022/05/19 18:13:23 by mmarinel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from functools import reduce

def sum(acc, m):
	return (acc + m)

def as_int(n):
	if (not n.isdigit()):
		return (0)
	return (int(n))

if len(sys.argv) != 3:
	print ("Error: Wrong number of arguments (3 expected)")
else:
	print(reduce(sum, map(as_int, sys.argv), 0))