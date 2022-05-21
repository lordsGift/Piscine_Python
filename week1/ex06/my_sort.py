# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_sort.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: earendil <earendil@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/18 22:58:10 by mmarinel          #+#    #+#              #
#    Updated: 2022/05/21 10:53:11 by earendil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Come abbiamo inteso l'esercizio:
#
#	1). ordinare secondo l'anno di nascita
#	2). quando l'anno coincide, adottare l'ordinamento alfabetico sul nome
#
#	3). alla fine printare la lista risultante.

from functools import reduce

def	as_reversed(couple):
	return (tuple(reversed(couple)))

def	musicians_to_string(acc, el):
	return (str(acc) + str(el[1]) + "\n")

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
musicians = list(map(as_reversed, d))
musicians.sort(key=lambda el: (el[0], el[1]), reverse=False)
print(str(reduce(musicians_to_string, musicians, "")[:-1]))
