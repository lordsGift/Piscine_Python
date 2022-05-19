# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmarinel <mmarinel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 22:58:10 by mmarinel          #+#    #+#              #
#    Updated: 2022/05/19 10:43:25 by mmarinel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from functools import reduce

def as_type(acc, n):
	return (str(acc) + str(n) + " has a type " + str(type(n)) + '\n')

def	my_var():
	l = [
		42,
		"42",
		"quarante-deux",
		42.0,
		True,
		[42],
		{42: 42},
		(42,),
		set()
	]
	print(reduce(as_type, l, "")[:-1])

my_var()
