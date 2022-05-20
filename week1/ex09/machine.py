# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    machine.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: earendil <earendil@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/20 11:11:03 by earendil          #+#    #+#              #
#    Updated: 2022/05/20 13:49:50 by earendil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

BEV_SERVED_BEFORE_FAILURE = 3

import os
import random
from time import sleep
from typing import Type, TypeVar
from beverages import *

class	CoffeeMachine:
	def	__init__(self) -> None:
		random.seed()
		self.__drinks_served = 0;
	
	class	EmptyCup(HotBeverage):
		name = "empty cup"
		price = 0.90

		def	description(self):
			return ("An empty cup?! Gimme my money back!")

	class	BrokenMachineException(Exception):
		def	__init__(self, *args: object) -> None:
			super().__init__("This coffee machine has to be repaired.")

	def	repair(self):
		self.__drinks_served = 0

	def	serve(self, beverage : TypeVar('T', bound=HotBeverage)):
		if self.__drinks_served == BEV_SERVED_BEFORE_FAILURE:
			raise self.BrokenMachineException()
		self.__drinks_served += 1
		if random.randrange(1, 3) == 1:
			return (self.EmptyCup())
		else:
			return (beverage())

cheap_machine = CoffeeMachine()

while True:
	while True:
		os.system("clear")
		action = input("Are we going back to work? (yes/no)\n")
		if action == "yes" or action == "no":
			break
		print("please enter a valid choice : yes/no\n")
		sleep(1)

	if action == "yes":
		print("See you later pal!\n")
		sleep(0.5)
		break
	
	while True:
		print ("\nMenu:")
		print("\n")
		print(hot_beverage)
		print("\n")
		print(coffee)
		print("\n")
		print(tea)
		print("\n")
		print(chocolate)
		print("\n")
		print(cappuccino)
		print("\n")
		
		sleep(0.5)
		beverage = input("\nChoose a beverage\n")
		try:
			if (beverage == "hot beverage"):
				print("Here you are: " +  cheap_machine.serve(HotBeverage).description())
				print("\n")
				input("press any key to continue...")
			elif (beverage == "coffee"):
				print("Here you are: " + cheap_machine.serve(Coffee).description())
				print("\n")
				input("press any key to continue...")
			elif (beverage == "tea"):
				print("Here you are: " + cheap_machine.serve(Tea).description())
				print("\n")
				input("press any key to continue...")
			elif (beverage == "chocolate"):
				print("Here you are: " + cheap_machine.serve(Chocolate).description())
				print("\n")
				input("press any key to continue...")
			elif (beverage == "cappuccino"):
				print("Here you are: " + cheap_machine.serve(Cappuccino).description())
				print("\n")
				input("press any key to continue...")
			else:
				print("please, choose a correct beverage\n")
				input("press any key to continue...")
		except CoffeeMachine.BrokenMachineException as bme:
			print(bme)
			print("Waiting for the guy...")
			sleep(2)
			print("repairing...")
			cheap_machine.repair()
			sleep(3)
			print("repaired!\n\n")
			input("press any key to continue...")
		finally:
			break
