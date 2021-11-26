#This module would allow us to print our dictionary in a more readable format, instead of the normal print which prints in a straight line
import pprint

#Here we have a nested dictionary with key as the name of the cars and value as another dictionary with the attribbute of the car
car_rental_initial= {'Audi':{'model': 'A5','year_released': '2018', 'year_acquire' : '2020' , 'money_made': '$250', 'plate_no': '8CME776', 'no_rent': 9  },
					 'Honda':{'model': 'Accord','year_released': '2019', 'year_acquire' : '2021' , 'money_made': '$400', 'plate_no': '91504CH', 'no_rent': 9 },
					 'Nissan':{'model': 'Ariya','year_released': '2012', 'year_acquire' : '2019' , 'money_made': '$120', 'plate_no': 'HIMK82', 'no_rent': 16 },
					 'Toyota': {'model': 'Avalon','year_released': '2016', 'year_acquire' : '2020' , 'money_made': '$100', 'plate_no': '7RDJ356', 'no_rent': 12 },
					 'Ford': {'model': 'Bronco','year_released': '2006', 'year_acquire' : '2018' , 'money_made': '$200', 'plate_no': '845KPU', 'no_rent': 25 }}

print('Hey there Omondi congrats on your new business I hear you are looking into expansion. Great! below are the cars in your collection')

#As the module, we would have our nested dictionary printed in a readable vertical format instead of just the normal straight line function, we have the sort_dicts as false so it displays the dict in insertion order instead of rearraging it by ascending.  
pprint.pprint(car_rental_initial, sort_dicts=False)

#List of operation Omondi can perform with their respective number to pick from 
print("This program allows you to perform few operations on your collection \nBelow are the listed operations to perform: \n \n1. Add new cars to your collection \n2. Update the attributes of cars in your collection \n3. Remove Cars from your collection. \n4. Rent cars and track the number of times each car has been rented with money earned from each car.")

#This would be the function we would call to show a list of operation Omondi can pick from whenever he finishes a particular operation and he wants to do another one. 
def operations_to_perform():
	omondi_input = int(input('What operation do you want to perform (1/2/3/4): '))
	if omondi_input == 1:
		add_car()  # Would call the function respective to the description in the print statement, in this case 1 is to add a car. So same for the others
	elif omondi_input ==2:
		update_collection()
	elif omondi_input ==3:
		remove_car_collection()
	elif omondi_input ==4:
		car_rental()
	else:
		print("\nPlease enter the right value, try again")
		operations_to_perform() #Call the function again if the value entered is wrong



#Function to add new cars in the collection
def add_car():
  	#This code is use to clarify that the user picked the right input for operation to perform and also to inform them that we would need some information.If the user says no then we call the function operation to perform so they can pick the right one or clarify again. 
		resp_add = input("We would now ask a few question to store your new car in your collection,  Can we Proceed (yes/no): ")
		if resp_add in ["y", "yes", "yeah"]:
			print("\n")  # To print a new line so the output of our code is not packed together. 
      
			#This code would enable the program to collect information of the car Omondi wants to add.
			car_name = input("Enter the name of the new car:")
			model_value = input("Enter the Model of the car:")
			year_release = input("Enter the year the car was released:")
			year_acq = input("What year did you acquire the car:")
			money_made = input("How much have you made from the car so far (in $)")
			plate_num = input("Can you provide us the plate number of the car:")
			num_rent = int(input("Finally, how long has this car been in business, (rent):"))
      
			#Code to insert the new car from the collected information into the car collection 
			car_rental_initial[car_name]= {'model': model_value,'year_released': year_release, 'year_acquire' : year_acq , 'money_made': money_made, 'plate_no': plate_num, 'no_rent': num_rent }
			pprint.pprint(car_rental_initial, sort_dicts=False)  #prints the the new collection of cars  out
			print ( "\nWith the data given, your new car has just been added to the collection view above" )
      
			#This code asks the user if they want to perform another operation if yes then it calls the function of operation to perform, if no it ends the program
			another_operation = input("Would you like to perform a new operation: (yes/no)")
			if another_operation in ["y", "yes", "yeah"]:
				operations_to_perform()
			else:
				exit()
		else:
			operations_to_perform () #Calls the function of that allows the user to pick from a list of option when the user is not sure they picked the right operation number


#Function to update a particular car attribute in the collection
def update_collection():
	#This code is use to clarify that the user picked the right input for operation to perform and also to inform them that we would need some information. If the user says no then we call the function operation to perform so they can pick the right one or clarify again. 
	resp_update = input('We would now ask a few question to update the cars in your dictionary, Can we Proceed (yes/no):')
	if resp_update in ["y", "yes", "yeah"]:
  		
		#This code would enable the program to collect the information of the car Omondi wants to update
		car_upd = input("\nWhat car in your collection would you like to update: ")
		if car_upd in car_rental_initial:
			car_key = input("What attribute in that car do you want to update")
			upd_value = input("What do you want to update it as: ")
      
			#code to update the car the user wants to change from the collected information(user input)
			car_rental_initial[car_upd][car_key]=upd_value
			pprint.pprint(car_rental_initial, sort_dicts=False) #prints the new updated car collection
			print ( "\n View above your updated Car collection" )

			#This code asks the user if they want to perform another operation if yes then it calls the function of operation to perform, if no it ends the program
			print("\n")
			another_operation = input ( "Would you like to perform a new operation: (yes/no):" )
			if another_operation in ["y", "yes", "yeah"]:
				operations_to_perform ()
			else:
				exit ()
	else:
		operations_to_perform() #Calls the function of that allows the user to pick from a list of option when the user is not sure they picked the right operation number


#Function to remove a car from the collection
def remove_car_collection():
  	#This code collects information of the car which the user would like to be remove and deletes it 
		car_del = input("\nWhat car from your collection would you like to delete")

		if car_del in car_rental_initial: #To verify if the user input of car to be removed is in the car collection
			del car_rental_initial[car_del]  #This code deletes (remove)the car according to the user input
			pprint.pprint(car_rental_initial, sort_dicts=False)  #Prints the updated car collection with the removed car 
			print ( "\n You have successfully deleted that car from your collection view below" )

			#This code asks the user if they want to perform another operation if yes then it calls the function of operation to perform, if no it ends the program
			print ( "\n" )
			another_operation = input ( "Would you like to perform a new operation: (yes/no):" )
			if another_operation in ["y", "yes", "yeah"]:
				operations_to_perform ()
			else:
				exit ()

		else:     #To inform the user that their input of car to be deleted is not in the collection.
			print("\n :( Oh sorry, it appears that your input is not in the collection, try again \n")
			operations_to_perform()  #Calls the program so they try again

#Function to track the number of times a car has been rented and calculate and display the money earned
def car_rental(): 
	#Counter for the respective cars to count the no of times they've been rented 
	Audi_no_rent = 0
	Honda_no_rent = 0
	Nissan_no_rent = 0
	Toyota_no_rent = 0
	Ford_no_rent = 0
#counter to count the total price made from each car when it is rented. 
	Audi_rent_price = 0
	Honda_rent_price = 0
	Nissan_rent_price = 0
	Toyota_rent_price = 0
	Ford_rent_price = 0

	rent_loop = True #creating a while loop so we can keep looping till Omondi doesn't want to rent any car aagin. 
	while rent_loop:
  	#code to collect information of the type of car Omondi wants to rent, and none when he doesn't want to rent again
		omondi_rent_input = input("\nWhat car would you Like to rent (note if none say none):") 
    
		#This conditional statement codes is to check what car omondi wants rent and add to the no of time he has rented it and also add to the money made from each rent. 
		if omondi_rent_input in car_rental_initial and  omondi_rent_input == 'Audi':
			Audi_no_rent += 1
			Audi_rent_price += 50   #50 indicates the fixed amount of price, in $ for rent for the Audi car.

		elif omondi_rent_input in car_rental_initial and omondi_rent_input == 'Honda':
			Honda_no_rent += 1
			Honda_rent_price+= 100   #100 indicates the fixed amount of price, in $ for rent for the Honda car.

		elif omondi_rent_input in car_rental_initial and omondi_rent_input == 'Nissan':
			Nissan_no_rent += 1
			Nissan_rent_price += 120  #120 indicates the fixed amount of price, in $ for rent for the Nissan car.

		elif omondi_rent_input in car_rental_initial and omondi_rent_input == 'Toyota':
			Toyota_no_rent += 1
			Toyota_rent_price += 150 #150 indicates the fixed amount of price, in $ for rent for the Toyota car.

		elif omondi_rent_input in car_rental_initial and omondi_rent_input == 'Ford':
			Ford_no_rent += 1
			Ford_rent_price += 75 #75 indicates the fixed amount of price, in $ for rent for the Ford car.

		else:   #code to show that the user inputed a car car in cases where he had deleted it before, or that he doesn't want to rent again.
			print("It appears that, your last input car is not in the collection or you don't want to rent again,")
			break_response = input("Do you want to rent a car again (yes/no)") #to clarify if Omondi wants to rent again or not 
			if break_response in ["y", "yes", "yeah"]:
				car_rental() #runs the function again if he wants to rent again
			elif break_response not in ["y", "yes", "yeah"] :
  				#prints the number of times Omondi has rented each car and the total money earned in each car
				print ( "\nAnalysis of the car you rented and money made is shown below: \nHonda was rented out ", Honda_no_rent, " times the allocated money was: $", Honda_rent_price, "",'Audi was rented out', Audi_no_rent, 'times the allocated money was: $', Audi_rent_price, "\n",'Nissan was rented out', Nissan_no_rent, 'times the allocated money was: $', Nissan_rent_price, "\n",'Toyota was rented out', Toyota_no_rent, 'times the allocated money was: $', Toyota_rent_price, "\n",'Ford was rented out', Ford_no_rent, 'times the allocated money was: $', Ford_rent_price, "\n")

      #This code asks the user if they want to perform another operation if yes then it calls the function of operation to perform, if no it ends the program
				print ( "\n" )
				another_operation = input ( "Would you like to perform a new operation: (yes/no)" )
				if another_operation in ["y", "yes", "yeah"]:
					operations_to_perform ()
				else:
  					exit ()

# This 1 line of code would all us to execute the function because the file was run directly not imported ,
# The 2nd line is us calling the function, if we don't call the function then none of our code after the first print would be executed.
if __name__ == "__main__": 
	operations_to_perform()



















