""" 
File: jayawant_gasoline.py 
Author: Pallavi Jayawant 
Description: 
 Prints the pounds of carbon dioxide produced by a given number of 
 gallons of gasoline
 Prints the amount of crude oil required to produce given number of gallons of gasoline
 Prints the price of gallons of gasoline
""" 
 
#ask user to input number of gallons of gasoline 
gas_gallons = float(raw_input('Please enter the number of gallons of gasoline: ')) 
 
#1 gallon of gasoline produces approximately 19.64 pounds of carbon dioxide 
carbon_dioxide_pounds = gas_gallons*19.64 
 #output the pounds of carbon dioxide produced 
print gas_gallons,'gallons of gasoline produces approximately',carbon_dioxide_pounds,'pounds of carbon dioxide.'

#1 barrel of crude oil produces 19 gallons of gasoline
crude_oil_barrel = gas_gallons/19
 #output the barrels of crude oil produced
print crude_oil_barrel, 'barrels of crude oil produces approximately', gas_gallons, 'gallons of gasoline.'

#1 gallon of gasoline costs approximately $2.580
Dollar_gas_gallons = gas_gallons/2.580 
 #output the dollars of gallon of gasoline
print Dollar_gas_gallons,'dollars produces approximately',gas_gallons,'gallons of gasoline.'



