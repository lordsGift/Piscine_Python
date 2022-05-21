# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var_to_dict.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: earendil <earendil@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 22:58:10 by mmarinel          #+#    #+#              #
#    Updated: 2022/05/21 10:39:57 by earendil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from collections import defaultdict
from functools import reduce

def	as_reversed(couple):
	return (tuple(reversed(couple)))

def	to_string(acc, el):
	return (str(acc) + str(el) + " ")

def	create_and_print_dict():
	d = [
		('Hendrix' , '1942'),
		('Allman' , '1946'),
		('King' , '1925'),
		('Clapton' , '1945'),
		('Johnson' , '1911'), 
		('Berry' , '1926'),
		('Vaughan' , '1954'),
		('Cooder' , '1947'),
		('Page' , '1944'),
		('Richards' , '1943'),
		('Hammett' , '1962'),
		('Cobain' , '1967'),
		('Garcia' , '1942'),
		('Beck' , '1944'),
		('Santana' , '1947'),
		('Ramone' , '1948'),
		('White' , '1975'),
		('Frusciante', '1970'),
		('Thompson' , '1949'),
		('Burton' , '1939')
	]
	musicians = map(as_reversed, d)
	my_dict = defaultdict(list)
	for k, v in musicians:
		my_dict[k].append(v)
	my_dict = dict(reversed(sorted(my_dict.items())))
	for k in my_dict:
		print(str(k) + " : " + str(reduce(to_string, my_dict[k], "")[:-1]))

create_and_print_dict()
