# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmarinel <mmarinel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 22:58:10 by mmarinel          #+#    #+#              #
#    Updated: 2022/05/19 14:02:11 by mmarinel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

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
if len(sys.argv) != 2:
	sys.stderr.write("Error: Wrong Number of arguments" + "\n")
elif not sys.argv[1] in states.keys() or not states[sys.argv[1]] in capital_cities.keys():
	sys.stdout.write("Unknown state" + "\n")
else:
	sys.stdout.write(capital_cities[states[sys.argv[1]]] + "\n")
