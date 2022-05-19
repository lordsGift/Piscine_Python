# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmarinel <mmarinel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 22:58:10 by mmarinel          #+#    #+#              #
#    Updated: 2022/05/19 14:48:57 by mmarinel         ###   ########.fr        #
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

states_inverted = dict(map(as_reversed, list(states.items())))
capital_cities_inverted = dict(map(as_reversed, list(capital_cities.items())))

if len(sys.argv) != 2:
	exit()
elif not sys.argv[1] in capital_cities_inverted.keys() or not capital_cities_inverted[sys.argv[1]] in states_inverted.keys():
	sys.stdout.write("Unknown state" + "\n")
else:
	sys.stdout.write(states_inverted[capital_cities_inverted[sys.argv[1]]] + "\n")
