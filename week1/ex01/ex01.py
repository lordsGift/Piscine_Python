# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex01.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmarinel <mmarinel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 22:58:10 by mmarinel          #+#    #+#              #
#    Updated: 2022/05/18 23:24:23 by mmarinel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from functools import reduce

def to_secs(time):
	index, t = time;
	return (pow(60, index) * t)

def sum(n, m):
	return (n + m)

def as_int(n):
	if (not n.isdigit()):
		return (0)
	return (int(n))

if len(sys.argv) != 4:
	print ("Error: Wrong number of arguments (3 expected)")
print(reduce(sum, map(to_secs, list(enumerate(map(as_int, sys.argv[1:])))), 0))
