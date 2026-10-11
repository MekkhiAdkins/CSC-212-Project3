
"""
Author: Mekkhi Adkins
Course Number and Name: CSC 212 - Data Structures
Programming Assignment: Project 3 - Classes and objects
Program Description: This program uses classes and objects
to create a class called pet, reads the data from a text file
and populates the data attributes and outputs the fields using the class's mutator and __str__ methods
"""

from pet import Pet

pet_list = []
pet_file = open('petdata.txt', 'r')

for line in pet_file:
    pet_data = line.split()
    new_pet = Pet(pet_data[0],pet_data[1], pet_data[2], pet_data[3])
    pet_list.append(new_pet)
          
pet_file.close()

print("List of pets:")
print()

for pet in pet_list:
    print(pet)
    print()

print("********** Owners with snake family pets: ****************")

for pet in pet_list:
    if pet.get_Family_Type() == "snake":
        print("Owner:", pet.get_owner())
        print("Pet:", pet.get_Name())
        print()

