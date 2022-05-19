# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    beverages.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: earendil <earendil@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/19 22:36:50 by earendil          #+#    #+#              #
#    Updated: 2022/05/19 23:23:47 by earendil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class	HotBeverage:
	
	price = 0.30
	name = "hot beverage"
	
	def	description(self):
		return ("Just some hot water in a cup")
	def	__str__(self):
		return ("name : " + str(self.name) + "\n"
			"price : " + str(round(self.price, 2)) + "\n"
			"description : " + self.description())

class	Coffee(HotBeverage):
	name = "coffee"
	price = 0.40
	
	def	description(self):
		return ("A coffee, to stay awake.")

class	Tea(HotBeverage):
	name = "tea"
	price = 0.30

	def	description(self):
		return ("Just some hot water in a cup.")

class	Chocolate(HotBeverage):
	name = "chocolate"
	price = 0.50

	def	description(self):
		return ("Chocolate, sweet chocolate...")

class	Cappuccino(HotBeverage):
	name = "cappuccino"
	price = 0.45

	def	description(self):
		return ("Un po' di Italia nella sua tazza!")

hot_beverage = HotBeverage()
coffee = Coffee()
tea = Tea()
chocolate = Chocolate()
cappuccino = Cappuccino()

print(hot_beverage)
print(coffee)
print(tea)
print(chocolate)
print(cappuccino)
