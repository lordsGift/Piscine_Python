# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmarinel <mmarinel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 22:58:10 by mmarinel          #+#    #+#              #
#    Updated: 2022/05/19 14:23:48 by mmarinel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from functools import reduce

def	as_reversed(couple):
	return (tuple(reversed(couple)))

states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
}
capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
}
# if len(sys.argv) != 2:
# 	sys.stderr.write("Error: Wrong Number of arguments" + "\n")
states_inverted = dict(reversed(sorted(states.items())))
print (states_inverted)

# elif not sys.argv[1] in capital_cities.keys() or not capital_cities[sys.argv[1]] in states.keys():
# 	sys.stdout.write("Unknown state" + "\n")
# else:
# 	sys.stdout.write(capital_cities[states[sys.argv[1]]] + "\n")
